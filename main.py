import openai
from transformers import pipeline
from dotenv import load_dotenv
import os

# Load environment variables
load_dotenv()

# Set OpenAI API key



# Initialize Hugging Face sentiment analysis pipeline
sentiment_pipeline = pipeline("sentiment-analysis")

def analyze_sentiment(comment):
    result = sentiment_pipeline(comment)
    return result[0]

def generate_response(comment, sentiment):
    prompt = f"Generate a response to the following Instagram comment while maintaining the brand image. The comment is: \"{comment}\". The sentiment of the comment is {sentiment}. Please ensure the response is professional, positive, and aligns with the brand's values."
    
    response = openai.ChatCompletion.create(
        model="gpt-3.5-turbo",
        messages=[
            {"role": "system", "content": "You are a helpful assistant."},
            {"role": "user", "content": prompt}
        ],
        max_tokens=150
    )
    
    return response.choices[0].message['content'].strip()

def main():
    # Input comment
    comment = input("Enter the Instagram comment: ")
    
    # Analyze sentiment
    sentiment_result = analyze_sentiment(comment)
    sentiment = sentiment_result['label']
    
    # Generate response
    response = generate_response(comment, sentiment)
    
    print(f"Sentiment: {sentiment}")
    print(f"Response: {response}")

if __name__ == "__main__":
    main()

# from transformers import pipeline
# generator = pipeline("text-generation", model="openai-community/gpt-3.5-turbo")
# sentiment_analyzer = pipeline("sentiment-analysis", model="distilbert-base-uncased-finetuned-sst-2-english")
# def analyze_sentiment(comment):
#     result = sentiment_analyzer(comment)
#     print(result)
#     return result[0]
# def generate_response(comment, sentiment):
#     print("here")
#     prompt = f"Generate a response to the following Instagram comment while maintaining the brand image. The comment is: \"{comment}\". The sentiment of the comment is {sentiment}. Please ensure the response is professional, positive, and aligns with the brand's values."
    
#     response = generator(prompt, max_length=100, min_length=20, num_return_sequences=1, do_sample=True, temperature=0.7, top_k=50)
#     print("running")
#     return response[0]['generated_text']
# statement = input("Enter the comment: ")
# sentiment = analyze_sentiment(statement)
# response = generate_response(statement, sentiment)
# print(response)

