import openai
import api_keys
import extract10relevantArticlesURLs
# import twitterapi
import tweepy

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

prompt_start = "I want you to read a few articles I will send to you, and then respond in a few different ways i will write to you as a prompt later."
urls = extract10relevantArticlesURLs.get_top_political_article_urls()


phase1_array = ["Liberal Republican", "Moderate Conservative" ,"Moderate" ,"liberal", "Democratic Socialist"]

phase2_array = ["Conservative", "Moderate Conservative" ,"Moderate" ,"liberal", "Progressive"]

phase3_array = ["Libertarian conservative" ,"Conservative" ,"Moderate" ,"liberal", "antifa member"]

phase4_array = ["Libertarian conservative" ,"Trumpist", "Moderate Conservative", "Socialist" , "antifa member" , ]

phase5_array = ["White Supremacist", "Trumpist" ,"Conservative" ,"Anarcho-communist", "antifa member"]

phases = [phase1_array, phase2_array, phase3_array, phase4_array, phase5_array]

bots_array = [api_keys.dudaTahorLaad, api_keys.oranHaMehandes, api_keys.habiltiNigmar, api_keys.ruvenovedvsadler, api_keys.luriethebrit]

prompt_end = """

I will present to you 5 political views, Remember that the right wing and the left wing always have opposite opinions on topics. 
here are the political views: 
1. "Liberal Republican" ,2."Moderate Conservative", 3."Moderate" ,4. "liberal" ,5."Democratic Socialist"

 for each view, write 3 twitter responses based on the articles you have read above. remember that a twitter response should be no longer than 220 characters.
your reply should be in the following template:
1. "Liberal Republican":
response 1:
response 2:
response 3:
and so on."""

final_prompt = prompt_start + urls + prompt_end

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



parsed_responses = dict_maker_from_string(get_tweets_strings())
print (parsed_responses)

# this function will take the parsed responses that are in a dictionary and each bot will publish its tweets
def publish_tweets(parsed_responses):
    # print(parsed_responses)
    # the first loop will publish each **4 hours** a tweet from each political view (each bot)
    # for i in range (3):
        # now we will go through each bot and publish a tweet from it
        # TODO indentation here
    j = 0
    for view in parsed_responses:
        bot = bots_array[j]
         # TODO i instead of 0
        tweet = parsed_responses[view][0]
        #remove the "response _:" from the tweet
        # TODO str(i+1) instead of str(1) 
        tweet = tweet.removeprefix('Response ' + str(1) + ':')
        #publish the tweet
        client = tweepy.Client(consumer_key=bot.apikey,
                consumer_secret=bot.api_secret,
                access_token=bot.access_token,
                access_token_secret=bot.access_token_secret)
        
        # Replace the text with whatever you want to Tweet about
        response = client.create_tweet(text=tweet)
        print("Tweet published successfully from bot " + bot.name + " with the text: " + tweet)
        j += 1


publish_tweets(parsed_responses)



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
