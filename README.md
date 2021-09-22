# scispacy-webapp
A simple web app for visualising dependency grammar of scientific sentences using (sci)spaCy

The NLP side utilises [spaCy](https://spacy.io/) using [scispaCy's `en_core_sci_sm` model](https://allenai.github.io/scispacy/).
The API is built using [FastAPI](https://fastapi.tiangolo.com/), which uses the ASGI server [uvicorn](https://www.uvicorn.org/).
The simple HTML interface uses [Jinja](https://jinja.palletsprojects.com/en/3.0.x/) templates. 
It is hosted on [Heroku](https://www.heroku.com/) using [Gunicorn](https://gunicorn.org/) as the WSGI server.

Access the web app [here](https://scispacy-webapp.herokuapp.com/) (it may take a long time to initially load, as Heroku powers off the server after a period of inactivity).

(As the scispaCy model has been trained on biomedical and scientific text, it is well-suited for analysing scientific sentences.
Note that the web app uses the smaller `en_core_sci_sm` model due to Heroku's resource limitations.)

## Example usage

If you entered: "This is an example sentence, albeit one lacking in scientific content.", then you should see

![this dependency graph](https://github.com/joshuachristie/scispacy-webapp/blob/master/static/example.svg)

For background on interpreting dependency relationships, see [universal dependencies](https://universaldependencies.org/) (e.g. for adjectival modifier, see the entry for [`amod`](https://universaldependencies.org/u/dep/amod.html)).
