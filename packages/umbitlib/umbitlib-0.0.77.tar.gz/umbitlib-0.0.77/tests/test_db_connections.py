import unittest
from unittest.mock import patch, MagicMock, mock_open
import pandas as pd
import sqlalchemy as sa
from sqlalchemy.engine import create_engine
from urllib import parse
from src.umbitlib import db_connections
from src.umbitlib.db_connections import (SecurityHandler, DatabaseEngine, SqlHandler, CredentialProvider, KeyringCredentialProvider,
                                         TNSConfigLoader, YamlTNSConfigLoader, OracleEngineFactory, PostgresEngineFactory,
                                         DatabaseEngineController, SqlManagerFactory, SqlManager)


class TestSecurityHandler(unittest.TestCase):
    def test_valid_service_name(self):
        # Test if initializing with a valid destination doesn't raise an exception
        valid_service_name = 'oracle'
        sec_io = SecurityHandler(valid_service_name)
        self.assertEqual(sec_io.service_name, valid_service_name)

    def test_invalid_service_name(self):
        # Test if initializing with an invalid service_name raises a ValueError
        invalid_service_name = 'invalid_service_name'
        with self.assertRaises(ValueError):
            db_connections.SecurityHandler(invalid_service_name)


class TestDatabaseEngine(unittest.TestCase):
    def testDatabaseEngine(self):
        orc = DatabaseEngine('oracle')
        self.assertIsNotNone(orc)


class TestSqlHandler(unittest.TestCase):
    def testConnectOracle(self):
        oracle = SqlHandler('oracle')
        conn = oracle.connect()
        self.assertIsNotNone(conn)
        conn.close()

    def testConnectPostgres(self):
        pg = SqlHandler('postgres_dev')
        conn = pg.connect()
        self.assertIsNotNone(conn)
        conn.close()

    def testQueryOracle(self):
        query_str = """
                SELECT NAME
                FROM CLARITY_ORG.ZC_STATE
                WHERE ABBR = 'AK'
                """
        oracle = SqlHandler('oracle')
        df = oracle.query(query_str)
        self.assertEqual(df['name'][0], 'Alaska')

    def testQueryPg(self):
        query_str = """
                SELECT * FROM public.pages_glossary where id = 41
                """
        pg = SqlHandler('postgres_dev')
        df = pg.query(query_str)
        self.assertEqual(df['id'][0], 41)

    def testUploadDfTrunc(self):
        # set mock dataset
        data1 = {
            "col1":[1,2,3],
            "col2":['a', 'b', 'c']
        }
        df1 = pd.DataFrame(data1)

        data2 = {
            "col1":[1, 2, 3, 4],
            "col2":['a', 'b', 'c', 'd']
        }
        df2 = pd.DataFrame(data2)

        pg = SqlHandler('postgres_dev')
        pg.upload_df(dataframe=df1, table_name='umbitlib_trunc_test', table_mgmt='replace')
        pgdf = pg.query("select * from public.umbitlib_trunc_test")
        self.assertEqual(len(pgdf), 3)

        pg.upload_df(dataframe=df2, table_name='umbitlib_trunc_test', table_mgmt='truncate')
        pgdf = pg.query("select * from public.umbitlib_trunc_test")
        self.assertEqual(len(pgdf), 4)

    def testUploadDfReplace(self):
        orc = SqlHandler('oracle')
        pg = SqlHandler('postgres_dev')
        df = orc.query('select * from clarity_org.zc_state')
        pg.upload_df(df, 'umbitlib_test_table', 'replace')
        pgdf = pg.query("select * from public.umbitlib_test_table where state_c = '1'")
        self.assertEqual(pgdf['abbr'][0], 'AL')

class TestKeyringCredentialProvider(unittest.TestCase):    
    @patch('keyring.get_credential')
    def test_get_credentials_success(self, mock_get_credential):
        mock_security_obj = MagicMock()
        mock_security_obj.username = "testuser"
        mock_security_obj.password = "testpassword"
        mock_get_credential.return_value = mock_security_obj

        provider = KeyringCredentialProvider()
        credentials = provider.get_credentials("test_service")

        self.assertEqual(credentials, {"username": "testuser", "password": parse.quote_plus("testpassword")})
        mock_get_credential.assert_called_once_with(service_name="test_service", username=None)

    @patch('keyring.get_credential')
    def test_get_credentials_success_with_username(self, mock_get_credential):
        mock_security_obj = MagicMock()
        mock_security_obj.username = "specificuser"
        mock_security_obj.password = "specificpassword"
        mock_get_credential.return_value = mock_security_obj

        provider = KeyringCredentialProvider()
        credentials = provider.get_credentials("another_service", "specific_user")

        self.assertEqual(credentials, {"username": "specificuser", "password": parse.quote_plus("specificpassword")})
        mock_get_credential.assert_called_once_with(service_name="another_service", username="specific_user")

    @patch('keyring.get_credential')
    def test_get_credentials_not_found(self, mock_get_credential):
        mock_get_credential.return_value = None

        provider = KeyringCredentialProvider()
        with self.assertRaisesRegex(ValueError, "No credentials found for service: missing_service, username: None"):
            provider.get_credentials("missing_service")

    @patch('keyring.get_credential')
    def test_get_credentials_not_found_with_username(self, mock_get_credential):
        mock_get_credential.return_value = None

        provider = KeyringCredentialProvider()
        with self.assertRaisesRegex(ValueError, "No credentials found for service: missing_service_user, username: specific_user"):
            provider.get_credentials("missing_service_user", "specific_user")

class TestYamlTNSConfigLoader(unittest.TestCase):

    def test_load_tns_address_success_address_list(self):
        config_data = """
        tns_entries:
            test_entry:
                DESCRIPTION:
                    ADDRESS_LIST:
                        - ADDRESS: {NAME: test_address, HOST: localhost, PORT: 1521}
                        - ADDRESS: {NAME: another_address, HOST: 127.0.0.1, PORT: 1522}
        """
        with patch("builtins.open", mock_open(read_data=config_data)):
            loader = YamlTNSConfigLoader()
            address = loader.load_tns_address("dummy_file.yaml", "test_entry", "test_address")
            self.assertEqual(address, {"NAME": "test_address", "HOST": "localhost", "PORT": 1521})

    def test_load_tns_address_success_single_address(self):
        config_data = """
        tns_entries:
            test_entry:
                DESCRIPTION:
                    ADDRESS: {NAME: test_address, HOST: localhost, PORT: 1521}
        """
        with patch("builtins.open", mock_open(read_data=config_data)):
            loader = YamlTNSConfigLoader()
            address = loader.load_tns_address("dummy_file.yaml", "test_entry", "test_address")
            self.assertEqual(address, {"NAME": "test_address", "HOST": "localhost", "PORT": 1521})

    def test_load_tns_address_file_not_found(self):
        with patch("builtins.open", side_effect=FileNotFoundError):
            loader = YamlTNSConfigLoader()
            with self.assertRaisesRegex(YamlTNSConfigLoader.TNSConfigError, "Config file 'config.yaml' not found."):
                loader.load_tns_address("config.yaml", "test_entry", "test_address")

    def test_load_tns_address_invalid_yaml(self):
        with patch("builtins.open", mock_open(read_data="invalid yaml: {")):
            loader = YamlTNSConfigLoader()
            with self.assertRaisesRegex(YamlTNSConfigLoader.TNSConfigError, "Invalid YAML in 'config.yaml'"):
                loader.load_tns_address("config.yaml", "test_entry", "test_address")

    def test_load_tns_address_missing_tns_entries(self):
        config_data = "{}"
        with patch("builtins.open", mock_open(read_data=config_data)):
            loader = YamlTNSConfigLoader()
            with self.assertRaisesRegex(YamlTNSConfigLoader.TNSConfigError, "Key 'tns_entries' not found in config."):
                loader.load_tns_address("config.yaml", "test_entry", "test_address")

    def test_load_tns_address_missing_tns_entry(self):
        config_data = """{"tns_entries": {None}}"""
        with patch("builtins.open", mock_open(read_data=config_data)):
            loader = YamlTNSConfigLoader()
            with self.assertRaisesRegex(YamlTNSConfigLoader.TNSConfigError, "TNS entry 'missing_entry' not found."):
                loader.load_tns_address("config.yaml", "missing_entry", "test_address")

    def test_load_tns_address_missing_description(self):
        config_data = """{"tns_entries": {"test_entry": {None}}}"""
        with patch("builtins.open", mock_open(read_data=config_data)):
            loader = YamlTNSConfigLoader()
            with self.assertRaisesRegex(YamlTNSConfigLoader.TNSConfigError, "Key 'DESCRIPTION' not found in entry 'test_entry'."):
                loader.load_tns_address("config.yaml", "test_entry", "test_address")

    def test_load_tns_address_missing_address(self):
        config_data = """{"tns_entries": {"test_entry": {"DESCRIPTION": {None}}}}"""
        with patch("builtins.open", mock_open(read_data=config_data)):
            loader = YamlTNSConfigLoader()
            with self.assertRaisesRegex(YamlTNSConfigLoader.TNSConfigError, "Address with name 'test_address' not found in entry 'test_entry'."):
                loader.load_tns_address("config.yaml", "test_entry", "test_address")

    def test_load_tns_address_missing_address_in_list(self):
        config_data = """
        tns_entries:
            test_entry:
                DESCRIPTION:
                    ADDRESS_LIST:
                        - ADDRESS: {NAME: another_address, HOST: 127.0.0.1, PORT: 1522}
        """
        with patch("builtins.open", mock_open(read_data=config_data)):
            loader = YamlTNSConfigLoader()
            with self.assertRaisesRegex(YamlTNSConfigLoader.TNSConfigError, "Address with name 'test_address' not found in entry 'test_entry'."):
                loader.load_tns_address("config.yaml", "test_entry", "test_address")

class TestDatabaseEngineController(unittest.TestCase):

    def test_get_engine_unsupported_service(self):
        mock_credential_provider = MagicMock(spec=CredentialProvider)
        mock_tns_config_loader = MagicMock(spec=TNSConfigLoader)
        controller = DatabaseEngineController("config.yaml", mock_credential_provider, mock_tns_config_loader)
        with self.assertRaisesRegex(ValueError, "Unsupported service name: unknown_service"):
            controller.get_engine("unknown_service")

    def test_get_engine_no_factory(self):
        mock_credential_provider = MagicMock(spec=CredentialProvider)
        mock_tns_config_loader = MagicMock(spec=TNSConfigLoader)
        controller = DatabaseEngineController("config.yaml", mock_credential_provider, mock_tns_config_loader)
        controller.factories = {}  # You need to leave this empty for the test to execute properly!!
        with self.assertRaisesRegex(ValueError, "No factory found for service_name 'oracle'."):
            controller.get_engine("oracle")

class TestSqlManagerFactory(unittest.TestCase):

    def test_slq_manager_create_oracle(self):
        orc = SqlManagerFactory.create_sql_manager(service_name='oracle')
        self.assertIsNotNone(orc)

    def test_slq_manager_create_postgres(self):
        pg = SqlManagerFactory.create_sql_manager(service_name='postgres_dev')
        self.assertIsNotNone(pg)

class TestSqlManager(unittest.TestCase):

    def test_sql_manager_query(self):
        orc = SqlManagerFactory.create_sql_manager(service_name='oracle')
        df = orc.query("select * from clarity_org.zc_state")
        self.assertIsNotNone(df)
    
