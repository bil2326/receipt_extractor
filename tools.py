from mistralai import Mistral
from dotenv import load_dotenv
load_dotenv()

import base64

import os

def encode_image(image_path):
    """Encode the image to base64."""
    try:
        with open(image_path, "rb") as image_file:
            return base64.b64encode(image_file.read()).decode('utf-8')
    except FileNotFoundError:
        print(f"Error: The file {image_path} was not found.")
        return None
    except Exception as e:  # Added general exception handling
        print(f"Error: {e}")
        return None





def read_file(file_path):
    try:
        with open(file_path, 'r', encoding='utf-8') as file:
            content = file.read()
            return content
    except FileNotFoundError:
        return f"Error: the file '{file_path}' does not exist."
    except Exception as e:
        return f"An error occurred: {e}"



def extract_infos_from_receipt(image_path):

    api_key = os.environ["MISTRAL_API_KEY"]

    # Specify model
    model = "pixtral-12b-2409"

    # Initialize the Mistral client
    client = Mistral(api_key=api_key)

    base64_image = encode_image(image_path)

    # Define the messages for the chat
    messages = [
        {
            "role": "system",
            "content": read_file(file_path="./context.txt")
        },
        {
            "role": "user",
            "content": [
                {
                    "type": "text",
                    "text": read_file(file_path="./prompt.txt")
                },
                {
                    "type": "image_url",
                    "image_url": f"data:image/jpeg;base64,{base64_image}" 
                }
            ]
        }
    ]

    # Get the chat response
    chat_response = client.chat.complete(
        model=model,
        messages=messages,
        response_format = {
          "type": "json_object",
        }
    )

    # Print the content of the response
    return chat_response.choices[0].message.content