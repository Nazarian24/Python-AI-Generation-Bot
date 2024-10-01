import requests
import base64


def generate_image(query):
    # Prep request info
    payload = {
        "prompt": query
    }
    #Call base64 image from Craiyon
    print("Loading...")
    response = requests.post("https://backend.craiyon.com/generate", json=payload)

    base64Image = response.json()["images"][0]


    #Generate Image from base64
    image_64_decode = base64.decodebytes(bytes(base64Image, encoding="utf-8"))
    image_result = open('result.jpg', 'wb') # create a writable image and write the decoding result
    image_result.write(image_64_decode)

    image_result.close()