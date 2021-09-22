# scispacy-webapp
A simple web app for visualising dependency grammar of scientific sentences using (sci)spaCy

The NLP side utilises [spaCy](https://spacy.io/) using [scispaCy's `en_core_sci_sm` model](https://allenai.github.io/scispacy/).
The API uses [FastAPI](https://fastapi.tiangolo.com/), and the html interface uses [Jinja](https://jinja.palletsprojects.com/en/3.0.x/) templates. 
It is hosted on [Heroku](https://www.heroku.com/) using [Gunicorn](https://gunicorn.org/) as the WSGI server.

Access the web app [here](https://scispacy-webapp.herokuapp.com/).
