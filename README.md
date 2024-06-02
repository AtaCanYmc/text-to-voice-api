
## Usage

### Convert Plain Text to Speech

To convert plain text into speech, make a POST request to `/api/v1/text-to-voice` with JSON data containing the text and language code (optional, default is English).

### Convert TXT File to Speech

To convert a TXT file into speech, make a POST request to `/api/v1/txt-to-voice/<lang>` with a TXT file attached to the request and language code specified in the URL.

### Convert PDF File to Speech

To convert a PDF file into speech, make a POST request to `/api/v1/pdf-to-voice/<lang>` with a PDF file attached to the request and language code specified in the URL.

## API Endpoints

- `/api/v1/text-to-voice`: Convert plain text into speech.
- `/api/v1/txt-to-voice/<lang>`: Convert a TXT file into speech in the specified language.
- `/api/v1/pdf-to-voice/<lang>`: Convert a PDF file into speech in the specified language.

## Supported Languages

The supported languages for text-to-speech conversion are:

- English (en)
- Turkish (tr)
- French (fr)
