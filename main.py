#!/usr/bin/env python

import os
import sys
from chat_bot import ChatBot


api_key = os.getenv("OPENAI_API_KEY")
chat_bot = ChatBot(api_key)

args = sys.argv[1:]
arg_string = ' '.join(args)

if arg_string == 'delete all messages':
    chat_bot.delete_all_messages()

chat_bot.save_user_message(arg_string)
chat_bot.save_assistant_message(chat_bot.run(arg_string))
