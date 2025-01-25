import unittest
from unittest.mock import patch, mock_open, MagicMock
import json
import locale

# telethon_client_wrapper/test_client.py


from telethon_client_wrapper.client import (
    create_client,
    create_default_config,
    get_system_language,
    get_text,
    load_config,
    validate_config,
    DEFAULT_CONFIG,
    TRANSLATIONS
)

class TestCreateClient(unittest.TestCase):
    @patch('telethon_client_wrapper.client.TelegramClient')
    @patch('telethon_client_wrapper.client.load_config')
    @patch('telethon_client_wrapper.client.validate_config')
    def test_create_client(self, mock_validate_config, mock_load_config, mock_telegram_client):
        mock_load_config.return_value = {
            'api_id': '12345',
            'api_hash': 'abcde',
            'device_model': 'Rerowros',
            'system_version': '14.8.1',
            'app_version': '8.4',
            'lang_code': 'en',
            'system_lang_code': 'en-US'
        }
        client = create_client('config.json', 'session_name')
        mock_load_config.assert_called_once_with('config.json')
        mock_validate_config.assert_called_once()
        mock_telegram_client.assert_called_once_with(
            'session_name',
            '12345',
            'abcde',
            device_model='Rerowros',
            system_version='14.8.1',
            app_version='8.4',
            lang_code='en',
            system_lang_code='en-US'
        )

class TestGetText(unittest.TestCase):
    @patch('telethon_client_wrapper.client.get_system_language', return_value='ru')
    def test_get_text_ru(self, mock_get_system_language):
        self.assertEqual(get_text('enter_api_id'), TRANSLATIONS['ru']['enter_api_id'])

    @patch('telethon_client_wrapper.client.get_system_language', return_value='en')
    def test_get_text_en(self, mock_get_system_language):
        self.assertEqual(get_text('enter_api_id'), TRANSLATIONS['en']['enter_api_id'])

class TestLoadConfig(unittest.TestCase):
    @patch('builtins.open', new_callable=mock_open, read_data=json.dumps({'api_id': '12345', 'api_hash': 'abcde'}))
    def test_load_config_valid(self, mock_open):
        config = load_config('config.json')
        self.assertEqual(config['api_id'], '12345')
        self.assertEqual(config['api_hash'], 'abcde')

    @patch('builtins.open', side_effect=FileNotFoundError)
    @patch('telethon_client_wrapper.client.create_default_config')
    def test_load_config_file_not_found(self, mock_create_default_config, mock_open):
        load_config('config.json')
        mock_create_default_config.assert_called_once_with('config.json')

    @patch('builtins.open', new_callable=mock_open, read_data='invalid json')
    @patch('telethon_client_wrapper.client.create_default_config')
    def test_load_config_json_decode_error(self, mock_create_default_config, mock_open):
        load_config('config.json')
        mock_create_default_config.assert_called_once_with('config.json')

class TestValidateConfig(unittest.TestCase):
    @patch('builtins.input', side_effect=['12345', 'abcde'])
    def test_validate_config(self, mock_input):
        config = {
            'api_id': None,
            'api_hash': None,
            'device_model': 'Rerowros',
            'system_version': '14.8.1',
            'app_version': '8.4',
            'lang_code': 'en',
            'system_lang_code': 'en-US'
        }
        validated_config = validate_config(config)
        self.assertEqual(validated_config['api_id'], '12345')
        self.assertEqual(validated_config['api_hash'], 'abcde')

if __name__ == '__main__':
    unittest.main()