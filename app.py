from flask import Flask, request, session, redirect
from werkzeug.utils import secure_filename

app = Flask(__name__)

@app.route('/')
@app.route('/user/<string:username>', methods=['GET', 'POST', 'PUT', 'PATCH', 'DELETE'])
def home(username=None):
    if username is not None:
        if request.method == 'GET':
            mood = request.args.get('mood', '')
            share_mood = 'You are in a %s mood today !' % mood if mood is not '' else ''

            return 'hi %s !\n%s' % (username, share_mood)

        return 'ty %s\n' % username

    return 'welcome\n'

# curl -F 'data=@path/to/file.ext' http://localhost:5000/upload
@app.route('/upload', methods=['POST'])
def upload_file():
    if request.method == 'POST':
        f = request.files['data']
        f.save('uploads/' + secure_filename(f.filename))

    return f.filename
