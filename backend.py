import vertexai
from vertexai.preview.vision_models import Image, ImageTextModel


def get_short_form_image_captions(
    project_id: str, location: str, input_file: str
) -> list:
    vertexai.init(project=project_id, location=location)

    model = ImageTextModel.from_pretrained("imagetext@001")
    source_img = Image.load_from_file(location=input_file)

    captions = model.get_captions(
        image=source_img,
        # Optional parameters
        language="en",
        number_of_results=1,
    )

    return captions
