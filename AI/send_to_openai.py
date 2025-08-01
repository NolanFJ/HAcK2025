import base64
from openai import OpenAI
from pathlib import Path

# import key
from key import API_KEY

client = OpenAI(api_key = API_KEY)

# Image encoding, code provided
def encode_image(image_path):
    with open(image_path, "rb") as image_F:
        return base64.b64encode(image_F.read()).decode("utf-8")

def processImage():
    # path to image
    script_dir = Path(__file__).parent
    image_path = script_dir.parent / "frontend" / "public" / "downloaded_image.jpg"

    # Getting the base64 string
    base64_image = encode_image(image_path)

    # Sending a request and getting a response
    response = client.responses.create(
        model="gpt-4.1",
        input=[
            {
                "role": "user",
                "content": [
                    { "type": "input_text", "text": "what's in this image?" },
                    {
                        "type": "input_image",
                        "image_url": f"data:image/jpeg;base64,{base64_image}",
                    },
                ],
            }
        ],
    )

    # make things audible
    speech_file_path = Path(__file__).parent.parent / "frontend" / "public" / "speech.mp3"

    with client.audio.speech.with_streaming_response.create(
        model='gpt-4o-mini-tts',
        voice="coral",
        input=(response.output_text),
        instructions="Speak in a cheerful and positive tone.",
    ) as response:
        response.stream_to_file(speech_file_path)

