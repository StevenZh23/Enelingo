from google.cloud import vision
import io
from PersonalDatabase import get_database

def analyze_image(image_path):
    # Initialize the Vision API client
    client = vision.ImageAnnotatorClient()

    # Read the image file
    with io.open(image_path, 'rb') as image_file:
        content = image_file.read()

    # Create the Image object
    image = vision.Image(content=content)

    # Perform label detection on the image
    response = client.label_detection(image=image)

    # Check if there are errors in the response
    if response.error.message:
        raise Exception(f"API Error: {response.error.message}")

    # Print out the labels detected in the image
    #print("Labels detected in the image:")
    most_likely_appliance = [label.description for label in response.label_annotations]
    #for label in response.label_annotations:
    #    print(f"{label.description} (score: {label.score})")

    # If you want to check for text detection (OCR)
    #if response.text_annotations:
    #    print("Text detected in the image:")
        #for text in response.text_annotations:
         #   most_likely_appliance.append(text.description)
    return most_likely_appliance


image_path = "Ultratoaster.jpg"
x = analyze_image(image_path)
db = get_database()
list = db["all_appliances"].find({"appliance_type":x[1]})[0]
print(list)