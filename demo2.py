import argparse
from typing import Optional
import vertexai
from vertexai.preview.vision_models import Image, ImageTextModel
from google.cloud import aiplatform

from google.auth import credentials
from google.oauth2 import service_account

def init_sample(
    project: Optional[str] = None,
    location: Optional[str] = None,
    experiment: Optional[str] = None,
    staging_bucket: Optional[str] = None,
    credentials: Optional[credentials.Credentials] = None,
    encryption_spec_key_name: Optional[str] = None,
    service_account: Optional[str] = None,
):

    from google.cloud import aiplatform

    aiplatform.init(
        project=project,
        location=location,
        experiment=experiment,
        staging_bucket=staging_bucket,
        credentials=credentials,
        encryption_spec_key_name=encryption_spec_key_name,
        service_account=service_account,
    )

# Provide your own values for the parameters
project_id = "amazing-city-418415 "
location = "us-central1"  # or any other supported location
service_account_path = "/Users/benshuttleworth/Downloads/amazing-city-418415-a3bb1c6b4f7d.json"

# Load service account credentials
creds = service_account.Credentials.from_service_account_file(service_account_path)

# Call the init_sample function with appropriate parameters
init_sample(
    project=project_id,
    location=location,
    credentials=creds
)

def get_short_form_image_captions(
    project_id: str, location: str, input_file: str
) -> list:
    """Get short-form captions for a local image.
    Args:
      project_id: Google Cloud project ID, used to initialize Vertex AI.
      location: Google Cloud region, used to initialize Vertex AI.
      input_file: Local path to the input image file."""

    vertexai.init(project=project_id, location=location)
    
    model = ImageTextModel.from_pretrained("imagetext@001")
    source_img = Image.load_from_file(location=input_file)

    captions = model.get_captions(
        image=source_img,
        # Optional parameters
        language="en",
        number_of_results=1,
    )

    print(captions)

    return captions

if __name__ == "__main__":
    init_sample()
    get_short_form_image_captions(project_id, location, "dog.jpg")