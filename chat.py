# Example code for using the Files API to upload an image for chatgpt.
# https://platform.openai.com/docs/guides/images-vision?api-mode=responses&format=file

from urllib import response
from dotenv import load_dotenv
import os
import openai

load_dotenv()
openai.api_key = os.getenv("OPENAI_API_KEY")
client = openai.OpenAI()

from openai import OpenAI
client = OpenAI()

# Function to create a file with the Files API
def create_file(file_path):
  with open(file_path, "rb") as file_content:
    result = client.files.create(
        file=file_content,
        purpose="vision",
    )
    return result.id

def create_prompt(prompt_path):
    with open(prompt_path, "r", encoding="utf-8") as f:
        return f.read().strip()

def chat_with_image(prompt, file_id):
    response = client.responses.create(
        model="gpt-5",
        input=[{
            "role": "user",
            "content": [
                {
                    "type": "input_text", 
                    "text": prompt,
                },
                {
                    "type": "input_image",
                    "file_id": file_id,
                },
            ],
        }],
    )
    
    return response

if __name__ == "__main__":
    import argparse
    parser = argparse.ArgumentParser(description="Chat with an image using GPT-5")
    parser.add_argument("--infile", type=str, required=True, help="Path to the input image file")
    parser.add_argument("--prompt", type=str, required=True, help="Text prompt to accompany the image")
    args = parser.parse_args()
    
    # Getting the file ID
    file_id = create_file(args.infile)
    prompt = create_prompt(args.prompt)
    response = chat_with_image(prompt, file_id)
    
    print(response.output_text)
