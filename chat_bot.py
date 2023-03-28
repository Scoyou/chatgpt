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

  def save_assistant_message(self, assistant_msg):
    self.messages.insert_one({"role": "assistant", "content": assistant_msg})
    print(assistant_msg)

  def get_all_messages(self):
    collection = self.messages.find({}, {"_id":0}).sort('_id', 1)
    message_array = []
    for x in collection:
      message_array.append(x)
    return message_array
  
  def delete_all_messages(self):
    result = self.messages.delete_many({})
    print(result.deleted_count, " documents deleted.")

  def run(self, user_msg):
    response = openai.ChatCompletion.create(
      model=CHAT_GPT_MODEL,
      # TODO: get_all_messages needs to go here in the future
      messages=self.get_all_messages()
    )
    return response['choices'][0]['message']['content']