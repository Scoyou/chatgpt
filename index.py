#!/usr/bin/env python

import os
import openai
import sys

openai.api_key = os.getenv("OPENAI_API_KEY")

args = sys.argv[1:]
arg_string = ' '.join(args)

response = openai.ChatCompletion.create(
    model="gpt-3.5-turbo",
    messages=[
        {"role": "user", "content": arg_string}
    ]
)

print('-' * 10)
print(response['choices'][0]['message']['content'])
print('-' * 10)
