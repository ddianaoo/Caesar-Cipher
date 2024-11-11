import os
import io

from flask import Flask, request, render_template, send_file, redirect, flash
from werkzeug.utils import secure_filename
from caesar_cipher import caesar_cipher
from playfair_cipher import playfair_cipher


app = Flask(__name__)
app.config['SECRET_KEY'] = os.environ.get('SECRET_KEY')


@app.route('/')
def home():
    return render_template('index.html')


@app.route('/caesar-cipher/', methods=['GET', 'POST'])
def caesar_cipher_view():
    if request.method == 'POST':
        if 'file' not in request.files:
            flash('No file part')
            return redirect(request.url)
        file = request.files['file']
        if file.filename == '':
            flash('No selected file')
            return redirect(request.url)

        # get shift and mode
        shift = int(request.form.get('shift', 19))
        mode = request.form.get('mode', 'encode')

        if file and file.filename.endswith('.txt'):
            content = file.read().decode('utf-8')
            # encode/decode
            result = caesar_cipher(content, shift, direction=mode)
            result_io = io.BytesIO(result.encode('utf-8'))
            output_filename = f"{mode}_{secure_filename(file.filename)}"
            return send_file(result_io, as_attachment=True, download_name=output_filename, mimetype='text/plain')

    return render_template('caesar_cipher.html')


@app.route('/playfair-cipher/', methods=['GET', 'POST'])
def playfair_cipher_view():
    if request.method == 'POST':
        if 'file' not in request.files:
            flash('No file part')
            return redirect(request.url)
        file = request.files['file']
        if file.filename == '':
            flash('No selected file')
            return redirect(request.url)

         # get shift and mode
        key = request.form.get('key')
        mode = request.form.get('mode', 'encode')

        if file and file.filename.endswith('.txt'):
            content = file.read().decode('utf-8')
            # encode/decode
            result = playfair_cipher(content, key, mode=mode)
            result_io = io.BytesIO(result.encode('utf-8'))
            output_filename = f"{mode}_{secure_filename(file.filename)}"
            return send_file(result_io, as_attachment=True, download_name=output_filename, mimetype='text/plain')

    return render_template('playfair_cipher.html')



if __name__ == '__main__':
    app.run(debug=True)
