# pycleint.py
# Import the argparse library
import argparse

import http.client
import json

conn = http.client.HTTPConnection('localhost:4000')

endpoint = '/translate'

headers = {'Content-type': 'application/json'}

# Create the parser
translate_parser = argparse.ArgumentParser(
    description='Command line client to make Http Post request'
    )

# Add the arguments
translate_parser.add_argument(
    'sentence',
    metavar='sentence',
    type=str,
    help='the sentence to translate'
    )

# Execute the parse_args() method
args = translate_parser.parse_args()

sentence_to_translate = args.sentence

sentence = {'sentence': sentence_to_translate}
json_data = json.dumps(sentence)

conn.request('POST', endpoint, json_data, headers)

response = conn.getresponse()
print(response.read().decode())
