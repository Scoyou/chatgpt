import openai
from pymongo import MongoClient

CHAT_GPT_MODEL = "gpt-3.5-turbo"

class ChatBot:
  def __init__(self, api_key):
    openai.api_key = api_key
    self.client = MongoClient("mongodb://localhost:27017/")
    self.db = self.client.chatbot
    self.messages = self.db.messages

  def save_user_message(self, user_msg):
    self.messages.insert_one({"role": "user", "content": user_msg})
    print(user_msg)

  def save_assistant_message(self, assistant_msg):
    self.messages.insert_one({"role": "assistant", "content": assistant_msg})
    print(assistant_msg)

  def get_all_messages(self):
    collection = self.messages
    return collection.find().sort('_id', -1)

  def run(self, user_msg):
    response = openai.ChatCompletion.create(
      model=CHAT_GPT_MODEL,
      # TODO: get_all_messages needs to go here in the future
      messages=[
        {"role": "user", "content": user_msg},
      ]
    )
    return response['choices'][0]['message']['content']