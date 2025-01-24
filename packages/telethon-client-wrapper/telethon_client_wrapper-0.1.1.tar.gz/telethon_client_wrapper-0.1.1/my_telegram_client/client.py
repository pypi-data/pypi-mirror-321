import json
from telethon import TelegramClient

def create_client(config_path='config.json'):
    try:
        with open(config_path, 'r', encoding='utf-8') as config_file:
            config = json.load(config_file)
    except FileNotFoundError:
        config = {}
    except json.JSONDecodeError as e:
        exit(1)

    try:
        (
            device_model,
            system_version,
            app_version,
            lang_code,
            system_lang_code,
            api_id,
            api_hash,
        ) = (
            config[key] for key in [
                "device_model",
                "system_version",
                "app_version",
                "lang_code",
                "system_lang_code",
                "api_id",
                "api_hash",
            ]
        )
    except KeyError as e:
        exit(1)

    client = TelegramClient(
        'session_name',
        api_id,
        api_hash,
        device_model=device_model,
        system_version=system_version,
        app_version=app_version,
        lang_code=lang_code,
        system_lang_code=system_lang_code
    )
    return client