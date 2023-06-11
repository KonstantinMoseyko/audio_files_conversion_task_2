from flask import Blueprint, render_template
from werkzeug.exceptions import NotFound

from core.models import User, Session

session = Session()

audio_app = Blueprint("audio_app", __name__)

@audio_app.route("/", endpoint="list")
def users_list():
    users = session.query(User).all()
    return render_template("audio/list.html", users=users)

@audio_app.route("/<int:id_user>/", endpoint="details")
def user_details(id_user):
    user = session.query(User).filter_by(id=id_user).first()
    if user is None:
        raise NotFound
    return render_template("user/details.html", user=user)
