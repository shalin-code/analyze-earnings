import pprint
import google.generativeai as palm

#Hide API key in .gitignore
with open('api.txt', 'r') as api_file:
    api_content = api_file.read()
palm.configure(api_key=api_content)

#check what model is being used
models = [m for m in palm.list_models() if 'generateText' in m.supported_generation_methods]
model = models[0].name
# print(model)

# Open the file in read mode using a with statement
with open('input.txt', 'r') as file:
    # Read the entire contents of the file into a string
    file_contents = file.read()

#sentiment anlaysis and summary
# prompt = """

# You are an analyst of an earnings call. Your job is to summarize the earnings transcript in the following format for each speaker you identify:

# 1. Speaker Name: Tim Cook
#     Sentiment: 0.67 (-1 for negative sentiment and 1 for positive sentiment)
#     Highlights in bullet points:
#      - Talked about apple vision launch
#      - Apple TV is growing fast
#      - Huge revenue

# The text is here: 
# """ + str(file_contents)


# prompt = """
# You are analyzing a financial earnings transcript. Perform the following tasks:

# 1. Summarize three key points from the earnings transcript.
# 2. Determine the overall sentiment expressed in the transcript (positive, negative, neutral).
# 3. Identify the most important one-line statement that encapsulates the essence of the earnings discussion.
# """ + str(file_contents)

prompt = """
You are analyzing a financial earnings transcript. Perform the following tasks:

1. Summarize three key points from the earnings transcript.
2. Determine the overall sentiment expressed in the transcript (positive, negative, neutral).
3. Identify the most important one-line statement that encapsulates the essence of the earnings discussion.
""" + str(file_contents)

completion = palm.generate_text(
    model=model,
    prompt=prompt,
    temperature=0,
    # The maximum length of the response
    max_output_tokens=800,
)

print("\n\n\n\n")
print(completion.result)

sentiment = -100
projection = -100

# print("Sentiment Analysis (-1 to 1):  " + str(sentiment) + " \nIncrease projection:  " + str(projection) + "%")