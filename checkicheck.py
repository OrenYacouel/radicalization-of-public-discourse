import openai

# Set up OpenAI API credentials
openai.api_key = 'YOUR_API_KEY'

def chat_with_gpt(prompt1, prompt2, prompt3):
    conversation = f"{prompt1}\n\n{prompt2}\n\n{prompt3}"
    response = openai.Completion.create(
        engine='text-davinci-003',
        prompt=conversation,
        max_tokens=100,
        n=1,
        stop=None,
        temperature=0.7,
        top_p=1.0,
        frequency_penalty=0.0,
        presence_penalty=0.0
    )
    return response.choices[0].text.strip()

# Example conversation prompts
prompt1 = "User: Hi there! How are you doing today?"
prompt2 = "AI: I'm an AI language model trained by OpenAI. How can I assist you?"
prompt3 = "User: Can you help me with some Python programming examples?"

# Chat with the model and retrieve response to the third prompt
response = chat_with_gpt(prompt1, prompt2, prompt3)
print(response)