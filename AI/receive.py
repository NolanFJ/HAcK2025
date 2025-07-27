
# TODO: import your module
import requests
import os
import sys
from send_to_openai import processImage

# Get the folder where the script is located, done for you
script_dir = os.path.dirname(os.path.abspath(__file__))
filename = os.path.join(script_dir, "../frontend/public/downloaded_image.jpg")

url = "http://192.168.0.113/1024x768.jpg"           # You will have to change the IP Address

# Function to download the image from esp32, given to you
def download_image():
    response = requests.get(url)

    if response.status_code == 200:
        with open(filename, "wb") as f:
            f.write(response.content)
        print(f"Image saved to: {filename}")
        return True
    else:
        print("Failed to download image. Status code:", response.status_code)
        return False

# TODO: Download the image and get a response from openai
if download_image():
    try:
        aiResponse = processImage()
        print(f"AI responded")
    except Exception as e:
        print(f"Error processing OpenAI: {e}")

# TODO: How to control when to take photo?

