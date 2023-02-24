import openai
import os

# API Key and OS env
API_KEY='YOUR_KEY_HERE'
os.environ['OPENAI_Key']=API_KEY
openai.api_key=os.environ['OPENAI_Key']

# Initial prompt asking for the name
name = input("What is your name? ") # Ask the user for their name

# Checks if the user entered a name
if name: 
    print("Hello, " + name + ", please write a question:") # Display the user's name
else:
    print("You didn't enter a name. No formalities? Then just write a question:") # If no name was entered

# The whole deal, prompts each time after a text is entered and then prompts again after the response is given (limited by the amount of tokens)
keep_prompting=True
while keep_prompting:
    prompt=input('> ')
    if prompt=='quit':
        keep_prompting=False
    else:
        response=openai.Completion.create(engine='text-davinci-003',prompt=prompt,max_tokens=200)
        print(response['choices'][0]['text'])