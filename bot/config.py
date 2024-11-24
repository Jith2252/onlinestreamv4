from os import environ as env

class Telegram:
    API_ID = int(env.get("TELEGRAM_API_ID", 26842016))
    API_HASH = env.get("TELEGRAM_API_HASH", "3b841db9fa1b140e44f60cc033716f5c")
    OWNER_ID = int(env.get("OWNER_ID", 1952992043))
    ALLOWED_USER_IDS = env.get("ALLOWED_USER_IDS", "").split()
    BOT_USERNAME = env.get("TELEGRAM_BOT_USERNAME", "tmafiletolinkbot")
    BOT_TOKEN = env.get("TELEGRAM_BOT_TOKEN", "6896731780:AAHZo6C5u4eS6IouZrcDalM-kV0pW-t7x5g")
    BOT_WORKERS = env.get("BOT_WORKERS", 10)
    CHANNEL_ID = int(env.get("TELEGRAM_CHANNEL_ID", -1001870465424))
    SECRET_CODE_LENGTH = int(env.get("SECRET_CODE_LENGTH", 8))

class Server:
    BASE_URL = env.get("BASE_URL", "https://tmaadda.info:8443")
    BIND_ADDRESS = env.get("BIND_ADDRESS", "0.0.0.0")
    PORT = int(env.get("PORT", 8443))
    
    #"""if 'DYNO' in environ:
    #    ON_HEROKU = True
     #   APP_NAME = str(getenv('APP_NAME'))
    
    #else:
     #   ON_HEROKU = False
    #ON_HEROKU = False
    #FQDN = (getenv('FQDN', 'tmaadda.info:8443')) if not ON_HEROKU or getenv('FQDN','82.165.5.85') else APP_NAME+'.herokuapp.com'
    #HAS_SSL=bool(getenv('HAS_SSL',True))
    #if HAS_SSL:
     #   URL = "https://{}/".format(FQDN)
    #else:
     #   URL = "http://{}/".format(FQDN)"""

# LOGGING CONFIGURATION
LOGGER_CONFIG_JSON = {
    'version': 1,
    'formatters': {
        'default': {
            'format': '[%(asctime)s][%(name)s][%(levelname)s] -> %(message)s',
            'datefmt': '%d/%m/%Y %H:%M:%S'
        },
    },
    'handlers': {
        'file_handler': {
            'class': 'logging.FileHandler',
            'filename': 'event-log.txt',
            'formatter': 'default'
        },
        'stream_handler': {
            'class': 'logging.StreamHandler',
            'formatter': 'default'
        }
    },
    'loggers': {
        'uvicorn': {
            'level': 'INFO',
            'handlers': ['file_handler', 'stream_handler']
        },
        'uvicorn.error': {
            'level': 'WARNING',
            'handlers': ['file_handler', 'stream_handler']
        },
        'bot': {
            'level': 'INFO',
            'handlers': ['file_handler', 'stream_handler']
        },
        'hydrogram': {
            'level': 'INFO',
            'handlers': ['file_handler', 'stream_handler']
        }
    }
}
