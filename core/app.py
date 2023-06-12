from flask import Flask, render_template

from core.models import models, database
from core.views import audio_app
from core.api import api_app

models.Base.metadata.create_all(bind=database.engine)

app = Flask(__name__)

@app.route("/")
def index():
    return render_template("index.html")

# bluprints registration
app.register_blueprint(audio_app, url_prefix="/data_list")
app.register_blueprint(api_app, url_prefix="/api")
