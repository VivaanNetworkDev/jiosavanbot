import logging
import logging.config
import importlib
from dotenv import load_dotenv


def main():
    # Get logging configurations
    logging.config.fileConfig('logging.conf')
    logging.getLogger().setLevel(logging.INFO)
    logging.getLogger("pyrogram").setLevel(logging.WARNING)

    load_dotenv()
    
    # Removed uvloop - pyrofork has compatibility issues with it on Python 3.12
    
    bot = importlib.import_module("jiosaavn.bot").Bot
    bot().run()


if __name__ == "__main__":
    main()
