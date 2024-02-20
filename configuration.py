import configparser
import logging
import sys
import validators

opts = [opt for opt in sys.argv[1:] if opt.startswith("-")]
args = [arg for arg in sys.argv[1:] if not arg.startswith("-")]


def validateUrl(url):
    if validators.domain(url) or validators.url(url):
        return True
    return False


config = configparser.ConfigParser()
file = None

if "-h" in opts:
    print(f"Usage:")
    raise SystemExit(f"Usage {sys.argv[0]} (-c | -h) <arguments>...")
elif "-c" in opts:
    try:
        file = open(args[-1], "r")
        config.read(file.name)
    except FileNotFoundError:
        logging.error("Config file not found.")
        raise SystemExit
    except configparser.MissingSectionHeaderError or configparser.NoOptionError:
        logging.error(f"The specified config file is invalid")
        raise SystemExit

else:
    raise SystemExit(f"Usage {sys.argv[0]} (-c | -h) <arguments>...")

API_ID = config["TOKENS"]["api_id"]
API_HASH = config["TOKENS"]["api_hash"]
BOT_TOKEN = config["TOKENS"]["bot_token"]
BOT_NAME = config["NAME"]["bot_name"]
