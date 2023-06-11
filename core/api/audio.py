from flask import Blueprint, jsonify, make_response, send_file, request
from sqlalchemy.exc import IntegrityError
from io import BytesIO
from pydub import AudioSegment

from core.models import Session, User, AudioRecord


api_app = Blueprint("api_app", __name__)

@api_app.route('/registration/', methods=['POST'])
def registration():
    data = request.get_json()
    username = data.get('username')
    
    session = Session()
    
    user = session.query(User).filter_by(username=username).first()
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
    file_wav = request.files.get('file_wav')
    
    session = Session()
    
    user = session.query(User).filter_by(user_token=user_token, id_user=id_user).first()
    if user is None:
        return jsonify({"error": "Permission denied"})
    
    if not file_wav.filename.lower().endswith('.wav'):
        return jsonify({"error": "Invalid audio format"})
    
    filename = file_wav.filename.rsplit('.', 1)[0]
    
    audio = AudioSegment.from_file(file_wav, format='wav')
    
    mp3_data = BytesIO()
    audio.export(mp3_data, format='mp3')
    mp3_data.seek(0)
    mp3_bytes = mp3_data.read()
    
    new_audiorecord = AudioRecord(
        id_user=id_user,
        filename=filename,
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
            f"http://127.0.0.1:5000/api/download?id_record={new_audiorecord.id_record}&id_user={new_audiorecord.id_user}"
    })
    
@api_app.route('/download', methods=['GET']) 
def download():
    id_record = request.args.get('id_record')
    id_user = request.args.get('id_user')
    
    session = Session()
    
    file_mp3 = session.query(AudioRecord).filter_by(id_record=id_record, id_user=id_user).first()
    if file_mp3 is None:
        return jsonify({"error": "Audiorecord not found"})
    
    file_data = file_mp3.file_data
    filename = f"{file_mp3.filename}.mp3"
    
    response = make_response(send_file(BytesIO(file_data), mimetype='audio/mpeg'))
    response.headers['Content-Disposition'] = 'attachment; filename=' + filename
    
    session.close()

    return response
