# app.py

import os
from flask import Flask, render_template, request, redirect, flash
from functions.extract import extract_text_from_pdf_images, analyze_key_value_pairs, extract_text_from_image
from werkzeug.utils import secure_filename  # Corrected import statement

app = Flask(__name__)

# Use an absolute path for the upload directory
UPLOAD_FOLDER = os.path.join(os.getcwd(), 'static', 'uploads')
app.config['UPLOAD_FOLDER'] = UPLOAD_FOLDER


@app.route('/', methods=['GET', 'POST'])
def index():
    if request.method == 'POST':
        if 'file' not in request.files:
            flash('No file part')
            return redirect(request.url)
        file = request.files['file']
        if file.filename == '':
            flash('No selected file')
            return redirect(request.url)
        if file:
            # Generate a unique filename for the uploaded file
            filename = secure_filename(file.filename)
            file_path = os.path.join(app.config['UPLOAD_FOLDER'], filename)

            # Save the file to the upload directory
            file.save(file_path)
            extracted_text = ''
            if filename.lower().endswith('.pdf'):
                # Extract text from the uploaded PDF file
                extracted_text = extract_text_from_pdf_images(file_path)
            # Analyze the extracted text to get key-value pairs
            else:
                extracted_text = extract_text_from_image(file_path)
            key_value_pairs = analyze_key_value_pairs(extracted_text)
            print()
            # Pass the key-value pairs to the result template
            return render_template('result.html', key_value_pairs=key_value_pairs)
    return render_template('index.html')


if __name__ == '__main__':
    app.run(debug=True)
