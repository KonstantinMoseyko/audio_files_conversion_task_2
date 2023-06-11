from flask import Blueprint, render_template

from core.models import Session, User, AudioRecord

session = Session()

audio_app = Blueprint("audio_app", __name__)

@audio_app.route("/", endpoint="list")
def users_list():
    audiorecords = session.query(AudioRecord).all()
    return render_template("audio/list.html", audiorecords=audiorecords)
