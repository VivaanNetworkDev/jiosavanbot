import logging
import logging.config
import asyncio
import sys
import importlib
from dotenv import load_dotenv


def main():
    # Get logging configurations
    logging.config.fileConfig('logging.conf')
    logging.getLogger().setLevel(logging.INFO)
    logging.getLogger("pyrogram").setLevel(logging.WARNING)

    load_dotenv()
    
    # Fix uvloop for Python 3.12+
    if sys.version_info >= (3, 12):
        try:
            import uvloop
            # Create new event loop first, then install uvloop
            loop = asyncio.new_event_loop()
            asyncio.set_event_loop(loop)
            uvloop.install()
        except Exception as e:
            logging.warning(f"Failed to install uvloop: {e}. Using default event loop.")
            loop = asyncio.new_event_loop()
            asyncio.set_event_loop(loop)
    else:
        # Python < 3.12: old behavior works fine
        import uvloop
        uvloop.install()
    
    bot = importlib.import_module("jiosaavn.bot").Bot
    bot().run()


if __name__ == "__main__":
    main()
