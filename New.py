import openai
import os

openai.api_key  = os.getenv('OPENAI_API_KEY')


print(f"###This script provides two functions and a system context\n")
print(f"1. get_completion(prompt). This does not keep context\n")
print(f"2. collect_message(prompt). This keeps context\n")
content = input("\n###Please enter a system role content for chatgpt\n\n")
context = [ {'role':'system', 'content': content} ]

def get_completion(prompt, model="gpt-3.5-turbo"):
    messages = [{"role": "user", "content": prompt}]
    response = openai.ChatCompletion.create(
        model=model,
        messages=messages,
        temperature=0, # this is the degree of randomness of the model's output
    )
    return response.choices[0].message["content"]

def get_completion_from_messages(messages, model="gpt-3.5-turbo", temperature=0):
    response = openai.ChatCompletion.create(
        model=model,
        messages=messages,
        temperature=temperature, # this is the degree of randomness of the model's output
    )
    #print(str(response.choices[0].message))
    return response.choices[0].message["content"]

def collect_messages(prompt):
    context.append({'role':'user', 'content':f"{prompt}"})
    response = get_completion_from_messages(context) 
    context.append({'role':'assistant', 'content':f"{response}"})
    print(response)
