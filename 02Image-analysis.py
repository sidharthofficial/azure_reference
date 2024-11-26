# Import necessary libraries
import os
from dotenv import load_dotenv
from PIL import Image, ImageDraw
from matplotlib import pyplot as plt
from azure.ai.vision.imageanalysis import ImageAnalysisClient
from azure.ai.vision.imageanalysis.models import VisualFeatures
from azure.core.credentials import AzureKeyCredential
import requests
import sys

# Load environment variables
load_dotenv()
AI_ENDPOINT = os.getenv('AI_SERVICE_ENDPOINT')
AI_KEY = os.getenv('AI_SERVICE_KEY')

def main():
    # Verify endpoint and key are set
    if not AI_ENDPOINT or not AI_KEY:
        print("Please set AI_SERVICE_ENDPOINT and AI_SERVICE_KEY in your .env file.")
        return

    # Define image file path
    image_file = 'images/street.jpg' if len(sys.argv) < 2 else sys.argv[1]
    
    try:
        with open(image_file, "rb") as f:
            image_data = f.read()

        # Initialize the client
        cv_client = ImageAnalysisClient(
            endpoint=AI_ENDPOINT,
            credential=AzureKeyCredential(AI_KEY)
        )
        
        # Perform analysis
        analyze_image(image_file, image_data, cv_client)
        
        # Perform background removal
        background_foreground(AI_ENDPOINT, AI_KEY, image_file)
        
    except Exception as e:
        print(f"An error occurred: {e}")

def analyze_image(image_filename, image_data, cv_client):
    try:
        # Analyze image for multiple features
        result = cv_client.analyze(
            image_data=image_data,
            visual_features=[
                VisualFeatures.CAPTION,
                VisualFeatures.DENSE_CAPTIONS,
                VisualFeatures.TAGS,
                VisualFeatures.OBJECTS,
                VisualFeatures.PEOPLE
            ]
        )

        # Display the caption result
        if result.caption:
            print(f"\nCaption: '{result.caption.text}' with confidence {result.caption.confidence:.2%}")

        # Display dense captions
        if result.dense_captions:
            print("\nDense Captions:")
            for caption in result.dense_captions.list:
                print(f" '{caption.text}' (confidence: {caption.confidence:.2%})")

        # Display tags
        if result.tags:
            print("\nTags:")
            for tag in result.tags.list:
                print(f" '{tag.name}' (confidence: {tag.confidence:.2%})")

        # Display and annotate objects
        if result.objects:
            print("\nObjects:")
            annotate_image(image_filename, result.objects.list, "objects.jpg")

        # Display and annotate people
        if result.people:
            print("\nPeople:")
            annotate_image(image_filename, result.people.list, "people.jpg")
            
    except Exception as e:
        print(f"Error during analysis: {e}")

def annotate_image(image_filename, items, output_filename):
    try:
        image = Image.open(image_filename)
        draw = ImageDraw.Draw(image)
        for item in items:
            box = item.bounding_box
            draw.rectangle([box.x, box.y, box.x + box.width, box.y + box.height], outline="cyan", width=3)
            draw.text((box.x, box.y), item.tags[0].name, fill="cyan")
        image.save(output_filename)
        print(f"Annotated image saved as '{output_filename}'")
    except Exception as e:
        print(f"Error annotating image: {e}")

def background_foreground(endpoint, key, image_file):
    try:
        print('\nRemoving background...')
        api_version = "2023-02-01-preview"
        mode = "backgroundRemoval"
        url = f"{endpoint}computervision/imageanalysis:segment?api-version={api_version}&mode={mode}"
        headers = {"Ocp-Apim-Subscription-Key": key, "Content-Type": "application/json"}
        image_url = f"https://github.com/MicrosoftLearning/mslearn-ai-vision/blob/main/Labfiles/01-analyze-images/Python/image-analysis/{image_file}?raw=true"
        response = requests.post(url, headers=headers, json={"url": image_url})
        
        if response.status_code == 200:
            with open("background.png", "wb") as file:
                file.write(response.content)
            print("Background removed. Results saved as 'background.png'")
        else:
            print(f"API Error: {response.status_code} - {response.text}")
    except Exception as e:
        print(f"Error during background removal: {e}")

if __name__ == "__main__":
    main()
