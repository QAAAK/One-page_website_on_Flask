from flask import Flask, render_template, request
from search_alpha import *


app = Flask(__name__)


@app.route('/')
def hello():
    return 'Hello world from Flask!'
@app.route('/search4', methods=['POST'])
def do_search():
    phrase = request.form['phrase']
    letters = request.form['letters']
    results = str(search4letters(phrase, letters))
    return render_template('results.html', the_title='Here are your results: ',
                            the_letters=letters, the_phrase=phrase, the_results=results)
@app.route('/entry')
def entry_page():
    return render_template('entry.html', the_title='Welcome to search4letters on the web!')


app.run()
