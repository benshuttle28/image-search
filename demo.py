
# Imports the Google Cloud client library
from google.cloud import vision



def run_quickstart() -> vision.EntityAnnotation:
    """Provides a quick start example for Cloud Vision."""

    # Instantiates a client
    client = vision.ImageAnnotatorClient()

    # image file 
    file_name = "dog.jpg"
    
    # Loads the image into memory
    with open(file_name, 'rb') as image_file:
        content = image_file.read()

    image = vision.Image(content=content)

    # Performs label detection on the image file
    response = client.label_detection(image=image)
    labels = response.label_annotations

    print("Labels:")
    for label in labels:
        print(label.description)

    return labels

if __name__ == "__main__":
    run_quickstart()