import os
from flask import Flask, request, redirect, url_for, send_from_directory, abort

UPLOAD_FOLDER = '/Users/michaelstewart/Documents/maps/uploads'
DATA_FOLDER = '/Users/michaelstewart/Documents/maps/data'
ALLOWED_EXTENSIONS = set(['txt', 'csv'])

app = Flask(__name__, static_url_path='')
app.config['UPLOAD_FOLDER'] = UPLOAD_FOLDER
app.config['DATA_FOLDER'] = DATA_FOLDER

@app.route('/')
def root():
    return app.send_static_file('index.html')


def allowed_file(filename):
    return '.' in filename and \
           filename.rsplit('.', 1)[1] in ALLOWED_EXTENSIONS

@app.route('/upload', methods=['POST'])
def upload_file():
    if request.method == 'POST':
        file = request.files['file']
        if file and allowed_file(file.filename):
            filename = file.filename
            file.save(os.path.join(app.config['UPLOAD_FOLDER'], filename))
            return 'OK'
        else:
            abort(400)
    else:
        abort(400)

@app.route('/uploads/<filename>')
def uploaded_file(filename):
    return send_from_directory(app.config['UPLOAD_FOLDER'])

@app.route('/data/<filename>')
def serve_data(filename):
    return send_from_directory(app.config['DATA_FOLDER'], filename)

if __name__ == '__main__':
    app.run(debug=True)