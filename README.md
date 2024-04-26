# image-search
File structure: The main file app.py is the top level file. The backend code can be found in the backend.py file. The HTML code for the webpage can be found under the "templates" folder. The "demo.py" file exists to serve as a test of an API to Google Cloud. The "dog.jpg" image is a simple picture of a dog used for testing. The "temp.jgp" file stores the uploaded image locally before it is sent to the API. The "requirements.txt" file is part of the work-in-progress effort to host the website on the Internet. Finally, the "env" folder contains all the associated files for the Python virtual environment that was used for development. 

Design Overview: For my final project, I chose to create a website that allows a user to use an image to generate a search query. Simply called Image search, the website takes an uploaded image and uses the Google Vertex AI API to return a description of the uploaded image. The description is generated after the Upload and Process button is clicked. This description is then automatically placed in an embedded search bar on the webpage where the user can then click submit to see the results of the search query. The Google Custom Search API is leveraged to perform the Google search.  

Design Implementation: In order to implement my design, I created three different subcomponents. The first was the backend Python file that contains a function to take in the uploaded image, send it to the API, and return the description of the image. 
The second is subcomponent is a frontend UI file that contains all of the HTML code for the website, as well as JavaScript functions that perform actions like filling the search box with the description automatically, performing the search query API call, and displaying the results of the search query. 
The final subcomponent is the top-level Python file app file. This file uses the Flask framework integrate my backend Python code with my frontend HTML code to make a standalone web application. This file calls the function to send the uploaded image to the Vertex AI API and also passes the description of the image to the HTML file. When this file is run, it creates an instance of the web application that is locally hosted. 
My design process was the same as creating any other application. I wanted to have separate code for the backend and the frontend, and I knew that I would need a way to integrate them together. I found Flask as an easy way to integrate Python web apps and used that as the top-level Python file to run the app. Flask is an easy framework to use with good documentation, and I did not experience any challenges.

Stay tuned for the link to access the website on your own device!

