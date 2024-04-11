import vertexai
from vertexai.preview.vision_models import Image, ImageTextModel


def get_short_form_image_captions(
    project_id: str, location: str, input_file: str
) -> list:
    """Get short-form captions for a local image.
    Args:
      project_id: amazing-city-418415
      location: us-east4
      input_file: dog.jpg """

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
    get_short_form_image_captions("amazing-city-418415","us-east4","test.jpg")