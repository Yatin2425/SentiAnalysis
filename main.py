import openai
from transformers import pipeline
from dotenv import load_dotenv
import os

# Load environment variables
load_dotenv()




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

