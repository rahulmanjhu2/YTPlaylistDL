import logging

logging.basicConfig(
    level=logging.WARNING, format="%(asctime)s - %(name)s - %(levelname)s - %(message)s"
)
logger = logging.getLogger(__name__)
logging.getLogger("pyrogram").setLevel(logging.WARNING)

import pyrogram, os

if __name__ == "__main__":
    plugins = dict(root="plugins")
    app = pyrogram.Client(
        "bot",
        bot_token=os.environ.get("TOKEN","5949667242:AAH9MW1nebhYP0TQyFf3kInlytQREhhHA34"),
        api_id=int(os.environ.get("APP_ID", 2308011)),
        api_hash=os.environ.get("API_HASH","d5c1012797406492f13dc9199bdcb753"),
        plugins=plugins,
    )
    app.run()
