import face_recognition
from flask import Blueprint, jsonify, request, redirect, session
from mongoengine import NotUniqueError

from db.models import UserPhoto, User

users = Blueprint('users', __name__)

ALLOWED_EXTENSIONS = {'png', 'jpg', 'jpeg', 'gif'}


def allowed_file(filename):
    return '.' in filename and \
           filename.rsplit('.', 1)[1].lower() in ALLOWED_EXTENSIONS


@users.route('/users/new/', methods=['GET', 'POST'])
def upload_image():
    # Check if valid image was uploaded
    if request.method == 'POST':
        if 'file' not in request.files or 'first_name' not in request.form \
                or 'last_name' not in request.form or 'phone_number' not in request.form \
                or 'card_number' not in request.form or 'login' not in request.form or 'password' not in request.form:
            return redirect(request.url)

        file = request.files['file']
        first_name = request.form['first_name']
        last_name = request.form['last_name']
        phone_number = request.form['phone_number']
        card_number = request.form['card_number']
        login = request.form['login']
        password = request.form['password']

        if file.filename == '' or first_name == '' or last_name == '' or phone_number == '' \
                or card_number == '' or login == '' or password == '':
            return redirect(request.args)

        if file and allowed_file(file.filename):
            return save_user(file, first_name, last_name, phone_number, card_number, login, password)

    return '''
    <!doctype html>
    <title>Save picture?</title>
    <h1>Register</h1>
    <form method="POST" enctype="multipart/form-data">
      <label>First Name: </label><input type="text" name="first_name"><br>
      <label>Last Name: </label><input type="text" name="last_name"><br>
      <label>Phone Number: </label><input type="text" name="phone_number"><br>
      <label>Card Number: </label><input type="text" name = "card_number"><br>
      <label>First Login: </label><input type="text" name="login"><br>
      <label>First Password: </label><input type="text" name="password"><br>
      <input type="file" name="file"><br>
      <input type="submit" value="Upload">
    </form>
    '''


def save_user(file_stream, first_name, last_name, phone_number, card_number, login, password):
    img = face_recognition.load_image_file(file_stream)
    new_face_encodings = face_recognition.face_encodings(img)
    new_list = new_face_encodings[0].tolist()

    user_dict = {
        "first_name": first_name,
        "last_name": last_name,
        "phone_number": phone_number,
        "card_number": card_number,
        "login": login,
        "password": password
    }

    photo_dict = {
        "first_name": first_name,
        "last_name": last_name,
        "phone_number": phone_number,
        "img_encoding": new_list
    }

    user_body = user_dict
    ph_body = photo_dict
    try:
        user = User(**user_body).save()
        UserPhoto(**ph_body).save()
    except NotUniqueError:
        print("Login, phone number and card number must be unique!")
        return redirect(request.url)

    user_id = user.id

    return jsonify({'id': str(user_id)}), 200


@users.route('/users/all/', methods=['GET'])
def get_all_photos():
    all_photos = UserPhoto.objects.all()
    return jsonify(all_photos)
