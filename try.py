import openai
import api_keys
import extract10relevantArticlesURLs

# Set up an array to store the replies
replies = []

# Set up your OpenAI API credentials
openai.api_key = api_keys.openai_api_key

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



def parse_twitter_responses(response_string):
    response_dict = {}

    responses = response_string.split('\n\n')
    for response in responses:
        view, *tweets = response.split('\n')
        response_dict[view.strip()] = [tweet.strip() for tweet in tweets if tweet.strip()]

    return response_dict

prompt1 = "I want you to read a few articles I will send to you, and then respond in a few different ways i will write to you as a prompt later."
prompt2 = extract10relevantArticlesURLs.get_top_political_article_urls
prompt3 = """i will present to you 5 political views, Remember that the right wing and the left wing always have opposite opinions on topics. 
here are the political views: 
1. "Libertarian conservative" ,2."Conservative", 3."Liberal Republicans" ,4. "Moderate Conservative" ,5."Moderate" 

 for each view, write 3 twitter responses based on the articles you have read above. remember that a twitter response should be no longer than 220 characters.
your reply should be in the following template:
1. "Libertarian conservative":
response 1:
response 2:
response 3:
and so on."""

final_prompt = """
I want you to read a few articles I will send to you, and then respond in a few different ways i will write to you:

https://www.bbc.com/news/world-europe-65662563
https://abcnews.go.com/US/3-dead-kansas-city-lounge-shooting/story?id=99487967
https://www.usatoday.com/story/news/world/2023/05/21/ukraine-russia-war-live-updates/70240834007/
https://www.space.com/spacex-ax-2-private-axiom-space-launch-what-time
https://thehill.com/homenews/campaign/4014220-senate-republican-i-dont-think-trump-can-win-a-general-election/
https://apnews.com/article/g7-japan-hiroshima-ukraine-biden-zelenskyy-kishida-59b037197eef2d36cbbe882f0378ac99
https://www.reuters.com/technology/chinas-regulator-says-finds-serious-security-issues-us-micron-technologys-2023-05-21/
https://www.cnn.com/2023/05/21/politics/debt-ceiling-talks-biden-mccarthy/index.html
https://www.cnbc.com/2023/05/21/ford-capital-markets-convince-wall-street-skeptics.html
https://www.wsbtv.com/news/local/atlanta/rise-kiahyundai-thefts-comes-same-time-local-womans-class-action-lawsuit/NG6FZVRNRBBU5P4X7GVXB2UJDA/


i will present to you 5 political views, Remember that the right wing and the left wing always have opposite opinions on topics. 
here are the political views: 
1. "Libertarian conservative" ,2."Conservative", 3."Liberal Republicans" ,4. "Moderate Conservative" ,5."Moderate" 

 for each view, write 3 twitter responses based on the articles you have read above. remember that a twitter response should be no longer than 220 characters.
your reply should be in the following template:
1. "Libertarian conservative":
response 1:
response 2:
response 3:
and so on."""


# this function returns the string that chatgpt built that has the tweets, with the right template
def get_tweets_strings():
    generate_and_store_prompt(final_prompt)
    # print(replies[0])
    return replies[0]




def dict_maker_from_string(input_string):
    responses = {}
    lines = input_string.strip().split("\n")
    i = 0
    while i < len(lines):
        political_view = lines[i].strip(":")
        i += 1
        response_array = []
        for j in range(3):
            response = lines[i].strip()
            i += 1
            response_array.append(response)
        responses[political_view] = response_array
    return responses


# Example usage:
twitter_response_string = '''
1. "Libertarian conservative":
response 1: "Tragic incidents like the Kansas City shooting highlight the need to protect Second Amendment rights and focus on mental health support. #LibertarianConservative"
response 2: "Space exploration should be driven by private enterprises like SpaceX. Less government involvement leads to innovation and progress. #LibertarianConservative"
response 3: "Serious security issues in technology companies like Micron highlight the importance of free market competition and protecting intellectual property rights. #LibertarianConservative"

2. "Conservative":
response 1: "Strong borders and immigration reforms are crucial to ensure national security and protect American jobs. #Conservative"
response 2: "Biden's debt ceiling talks with McCarthy raise concerns about reckless spending and the need for fiscal responsibility. #Conservative"
response 3: "Ford's success in capital markets demonstrates the effectiveness of pro-business policies and supports job growth. #Conservative"

3. "Liberal Republicans":
response 1: "Supporting common-sense gun control measures is essential to prevent tragic incidents like the Kansas City shooting. #LiberalRepublicans"
response 2: "Ukraine-Russia conflict calls for diplomatic solutions and international cooperation to maintain peace and stability. #LiberalRepublicans"
response 3: "Biden's focus on infrastructure investment aligns with liberal Republican values of promoting economic growth and creating job opportunities. #LiberalRepublicans"

4. "Moderate Conservative":
response 1: "Balancing gun rights and public safety is crucial. Comprehensive background checks can help prevent tragedies like the Kansas City shooting. #ModerateConservative"
response 2: "Addressing the debt ceiling requires bipartisan collaboration and responsible fiscal policies. Both sides need to find common ground. #ModerateConservative"
response 3: "Hyundai/Kia thefts raise concerns about consumer protection. Striking a balance between regulation and market competition is key. #ModerateConservative"

5. "Moderate":
response 1: "Ensuring individual freedoms while maintaining public safety is crucial. A thoughtful approach is needed to address gun violence. #Moderate"
response 2: "Engaging in diplomacy and international cooperation is vital to de-escalate the Ukraine-Russia conflict and prevent further bloodshed. #Moderate"
response 3: "Biden's focus on infrastructure investment can stimulate the economy and create jobs. Bipartisan support is crucial for its success. #Moderate"
'''



parsed_responses = dict_maker_from_string(get_tweets_strings())
print(parsed_responses)