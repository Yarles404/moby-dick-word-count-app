# Source Allies Moby Dick Word Counts Project
## Overview
This is a simple Flask application that displays the word counts of Moby Dick.
On startup, I use PySpark to produce the word counts. There is some cleaning involved, including removal of comments in stop-words.txt and empty strings from mobydick.txt.

Since stop-words.txt is relatively small, I load it in as a set. I then use the set to filter out the stop words from the word counts.
All words were converted to their lowercase version.

Then, the application starts with a single page at /

## Project File Structure
Root directory contains basic files for the project, including the README.md, requirements.txt, and Dockerfile.

app/ contains the application.
It's a typical structure for a simple flask application, with static/ containing styles, scripts, and the corpus of text.
templates/ contains the html templates.

## Running the Application
### Locally
To run the application locally, you will need to have a recent version of Python 3 installed.
Pretty sure any version of Python 3.6+ will work, but don't quote me on that.
3.10.2 is a safe bet, as that's what I'm using. You can download it from [here](https://www.python.org/downloads/).

Set an environment variable PYSPARK_PYTHON=\<whatever command you use to start python\>. For Windows, I use "py".
Additionally, you will need Java 8+ installed and have JAVA_HOME environment variable set.
I used OpenJDK 8. You can download it from [here](https://adoptopenjdk.net/).


Once you have Python and Java installed, you can install the requirements.
I recommend using a virtual environment via [pipenv](https://pypi.org/project/pipenv/).
If you're using pipenv, use `pipenv install -r requirements.txt`. Otherwise, use `pip install -r requirements.txt`.
`cd` into the app/ directory and run `python app.py`.
You should see some output in your console. Navigate to [http://localhost:5000/](http://localhost:5000) to see the application.

### Docker
If you have Docker installed, then you don't have to worry about any of the prerequisites in the above section.
Simply run `docker build -t mobydick .` to build the image.
Then, run `docker run -p 5000:5000 mobydick` to run the container.
Navigate to [http://localhost:5000/](http://localhost:5000) to see the application.
