import openai

# Set up an array to store the replies
replies = []

# Set up your OpenAI API credentials
openai.api_key ="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"

# Generate prompts and store replies in the array
def generate_and_store_prompt(prompt):
    # Generate a reply using ChatGPT
    response = openai.ChatCompletion.create(
        model="gpt-3.5-turbo",
        messages=[
            {"role": "system", "content": "You are a helpful assistant."},
            {"role": "user", "content": prompt}
        ]
    )
    
    # Extract the reply
    reply = response['choices'][0]['message']['content']
    
    # Store the reply in the array
    replies.append(reply)

# usage
prompt_array = []

phase1_array = ["Libertarian conservative" ,"Conservative", "Liberal Republicans" , "Moderate Conservative" ,"Moderate" ,"liberal", "Progressive", "Democratic Socialist" , "Antifa member" , "Anarcho-communist"]

phase2_array = ["White Supremacist", "Libertarian conservative" ,"Conservative", "Moderate Conservative" ,"Moderate" ,"liberal", "Progressive","Democratic Socialist" , "antifa member" , "Anarcho-communist"]

phase3_array = ["White Supremacist", "Libertarian conservative" ,"Fascist", "Moderate Conservative" ,"Moderate" ,"liberal", "Progressive","Socialist" , "antifa member" , "Anarcho-communist"]

phase4_array = ["White Supremacist", "Evangelicalist" ,"Fascist", "Trumpist" ,"Moderate" ,"liberal", "Progressive", "communist" , "antifa member" , "Anarcho-communist"]

phases = [phase1_array, phase2_array, phase3_array]

def prompts_generator(phases, prompt_array):
    for i in range(4):
        prompt = "Generate a few short twitter respones to the most hot topic on current affairs , each tweet representing a different political view. Remember that the right wing and the left wing always have opposite opinions on topics. here are the political views: \n"
        num = 0
        for word in phases[i]:
            prompt = switch(num, prompt)
            prompt += word + ",\n"
            num += 1

        prompt_array.append(prompt)
    return prompt_array

def switch(num, prompt):
    if num == 0:
        prompt += "first view: "
    elif num == 1:
        prompt += "second view: "
    elif num == 2:
        prompt += "third view: "
    elif num == 3:  
        prompt += "fourth view: "
    elif num == 4:
        prompt += "fifth view: "
    elif num == 5:
        prompt += "sixth view: "
    elif num == 6:
        prompt += "seventh view: "
    elif num == 7:
        prompt += "eighth view: "
    elif num == 8:
        prompt += "ninth view: "
    elif num == 9:
        prompt += "tenth view: "
    return prompt
   

def phase_generator(prompt_array):
    for prompt in prompt_array:
        generate_and_store_prompt(prompt)
    return replies

prompt_array = prompts_generator(phases, prompt_array)
print(prompt_array)
replies = phase_generator(prompt_array)

# Access the replies from the array
for reply in replies:
    print(reply)
