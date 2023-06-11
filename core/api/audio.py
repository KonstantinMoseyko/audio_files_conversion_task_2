from flask import Blueprint, jsonify, request
from sqlalchemy.exc import IntegrityError
import uuid
import base64
from io import BytesIO
from pydub import AudioSegment

from core.models import Session, User, AudioRecord


api_app = Blueprint("api_app", __name__)

@api_app.route('/registration/', methods=['POST'])
def registration():
    data = request.get_json()
    username = data.get('username')
    
    session = Session()
    
    user = session.query(User).filter(User.username == username).first()
    if user:
        return jsonify({"error": "User with this name already exists"})

    new_user = User(username=username)

    session.add(new_user)
    try:
        session.commit()
    except IntegrityError:
        return jsonify({"error": "Data processing error"})
    session.refresh(new_user)
    
    session.close()
    
    return jsonify({
        'id_user': new_user.id_user,
        'user_token': new_user.user_token
    })

@api_app.route('/upload_audiorecord/', methods=['POST']) 
def upload_audiorecord():
    id_user = request.form.get('id_user')
    user_token = request.form.get('user_token')
    file_wav = request.files.get('audiorecord')
    
    session = Session()
    
    audio = AudioSegment.from_file(file_wav, format='wav')
    
    mp3_data = BytesIO()
    audio.export(mp3_data, format='mp3')
    mp3_data.seek(0)
    mp3_bytes = mp3_data.read()
    
    new_audiorecord = AudioRecord(
        id_user=id_user, 
        file_data=mp3_bytes,
    )
    session.add(new_audiorecord)
    try:
        session.commit()
    except IntegrityError:
        return jsonify({"error": "Data processing error"})
    session.refresh(new_audiorecord)
    
    session.close()
    
    return jsonify({
        'URL for download': 
            f"http://127.0.0.1:5000/api/download?id={new_audiorecord.id_record}&user={new_audiorecord.id_user}"
    })