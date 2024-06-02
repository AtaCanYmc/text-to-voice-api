import os
import uuid
from flask import Flask, Blueprint, request, send_file
from gtts import gTTS
import PyPDF2


app = Flask(__name__)
api_blueprint = Blueprint('api_blueprint', __name__)


@api_blueprint.route('/')
def hello():
    return {
        'message': 'Welcome to Voice Generator!',
        'endpoints': [
            '/text-to-voice'
        ],
        'supportedLanguages': [
            'en', 'tr', 'fr'
        ]
    }


@api_blueprint.route('/text-to-voice', methods=['POST'])
def text_to_voice():
    text = request.json.get('text')
    lang = request.json.get('lang', 'en')

    if not text:
        return 'Error: No text provided', 400

    tts = gTTS(text=text, lang=lang)
    output_filename = str(uuid.uuid4()) + '.mp3'
    tts.save(output_filename)
    response = send_file(output_filename, mimetype='audio/mp3')
    os.remove(output_filename)

    return response


@api_blueprint.route('/txt-to-voice/<lang>', methods=['POST'])
def txt_to_voice(lang):
    text_file = request.files.get('file')
    if not text_file or not text_file.filename.endswith('.txt'):
        return 'Error: No valid text file provided', 400

    text = text_file.read().decode('utf-8')
    tts = gTTS(text=text, lang=lang)
    output_filename = str(uuid.uuid4()) + '.mp3'
    tts.save(output_filename)
    response = send_file(output_filename, mimetype='audio/mp3')
    os.remove(output_filename)

    return response


@api_blueprint.route('/pdf-to-voice/<lang>', methods=['POST'])
def pdf_to_voice(lang):
    pdf_file = request.files.get('file')
    if not pdf_file or not pdf_file.filename.endswith('.pdf'):
        return 'Error: No valid PDF file provided', 400

    pdf_reader = PyPDF2.PdfFileReader(pdf_file)
    text = ''
    for page_num in range(pdf_reader.numPages):
        text += pdf_reader.getPage(page_num).extractText()

    tts = gTTS(text=text, lang=lang)
    output_filename = str(uuid.uuid4()) + '.mp3'
    tts.save(output_filename)
    response = send_file(output_filename, mimetype='audio/mp3')
    os.remove(output_filename)

    return response


app.register_blueprint(api_blueprint, url_prefix='/api/v1')
if __name__ == '__main__':
    app.run()
