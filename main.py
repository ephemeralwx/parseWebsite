from flask import Flask, jsonify, request
import requests
from bs4 import BeautifulSoup

app = Flask(__name__)

@app.route('/fetch_text', methods=['GET'])
def fetch_body_text_api():
    url = request.args.get('url')

    if not url:
        return jsonify({'error': 'URL parameter is missing'}), 400

    try:
        # Fetch the webpage content
        response = requests.get(url)
        response.raise_for_status()

        # Parse the content with Beautiful Soup
        soup = BeautifulSoup(response.content, 'html.parser')

        # Extract text from all <p> tags and concatenate them
        paragraphs = [p.get_text().strip() for p in soup.find_all('p')]
        body_text = " ".join(paragraphs)

        word_count = len(body_text.split())
        char_count = len(body_text)

        return jsonify({
            'text': body_text.strip(),
            'word_count': word_count,
            'char_count': char_count
        })

    except requests.RequestException as e:
        # Handling any request related errors
        return jsonify({'text': f'Error fetching content: {e}', 'word_count': 0, 'char_count': 0})

    except Exception as e:
        # Handling any other unforeseen errors
        return jsonify({'text': f'Unexpected error: {e}', 'word_count': 0, 'char_count': 0})

if __name__ == '__main__':
    app.run(debug=False)
