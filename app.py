from flask import Flask, render_template, redirect, request
from shortener import Shortener
import sys

app = Flask(__name__, template_folder="")  # Corrected the usage of __name_

shortener1 = Shortener()

@app.route('/')
def home():
    return render_template('home.html')

@app.route('/shorten', methods=['POST'])
def shorten():
    url = request.form.get('url')
    short_url = shortener1.shorten(url)
    return render_template('result.html', short_url=short_url)

@app.route('/<short_url>')
def redirect_to_url(short_url):
    url = shortener1.get_url(short_url)
    if url is None:  # Used "is" instead of "== None"
        return 'URL not found'
    else:
        return redirect(url)

if __name__ == '_main_':  # Corrected the usage of __name_
    port = int(sys.argv[1])
    app.run(debug=True, host="0.0.0.0", port=port)