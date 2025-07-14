# from google.cloud import generative_ai
import google.generativeai as genai

# Set up your API key (you need to get this from Google Cloud)
api_key = "AIzaSyB7r8d42I-l0e02c0CFywRxCZhcFyig1QA"
genai.configure(api_key)

# Make a request to the API
response = genai.generate_text(prompt="Tell me a joke")

# Output the response
print(response)
