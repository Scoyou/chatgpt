#!/usr/bin/env python

import os
import sys
from chat_bot import ChatBot

args = sys.argv[1:]
arg_string = ' '.join(args)

api_key = os.getenv("OPENAI_API_KEY")

chat_bot = ChatBot(api_key)

chat_bot.save_user_message(arg_string)
chat_bot.save_assistant_message(chat_bot.run(arg_string))