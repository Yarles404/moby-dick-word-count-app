# Source Allies Moby Dick Word Counts Project
## Overview
This is a simple Flask application that displays the word counts of Moby Dick.
On startup, I use PySpark to produce the word counts. There is some cleaning involved, including removal of comments in stop-words.txt and empty strings from mobydick.txt.

## Project File Structure
Root directory contains basic files for the project, including the README.md, requirements.txt, and Dockerfile.

app/ contains the application.
It's a typical structure for a simple flask application, with static/ containing styles, scripts, and the corpus of text.
templates/ contains the html templates.

## Running the Application
### Locally
To run the application locally, you will need to have a recent version of Python 3 installed.