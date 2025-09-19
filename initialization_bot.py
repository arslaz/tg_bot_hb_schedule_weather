from aiogram import Bot, Dispatcher, types, Router

from config import *
import logging

bot = Bot(token=bot_config['bot_token'])
logging.basicConfig(level=logging.INFO)
logger = logging.getLogger(__name__)

router = Router()