from flask import Flask, request, render_template
from backend import get_short_form_image_captions

app = Flask(__name__)

@app.route('/', methods=['GET', 'POST'])
def index():
    captions = []  # Initialize captions variable
    
    if request.method == 'POST':
        # Get the uploaded file from the form
        uploaded_file = request.files['myfile']
        # Save the file to a temporary location
        uploaded_file.save('temp.jpg')
        # Call the backend function to process the image
        captions = get_short_form_image_captions("amazing-city-418415", "us-east4", 'temp.jpg')
        print(captions)
    return render_template('web_ui.html', captions=captions)

if __name__ == '__main__':
    app.run(debug=False)


