

from flask import Flask, render_template, request


def search4vowels(phrase: str) -> set:
    """Return a boolean based on any vowels found."""
    vowels = set('aeiou')
    return vowels.intersection(set(phrase))
search4vowels('alphabet')


def search4letters(phrase: str, letters: str) -> set:
    """Return a set of the 'letters' found in 'phrase'."""
    return set(letters).intersection(set(phrase))

app = Flask(__name__)

@app.route('/search4', methods=['POST'])
def do_search() -> 'html':
    phrase = request.form['phrase']
    letters = request.form['letters']
    title = 'Here are your results:'
    results = str(search4letters(phrase, letters))
    return render_template('results.html',
                           the_phrase=phrase,
                           the_letter=letters,
                           the_title=title,
                           the_results=results, )

@app.route('/')
@app.route('/entry')
def entry_page() -> 'html':
    return render_template('entry.html',
                           the_title='Welcome to search4letters on the web!')
if __name__ == '__main__':
app.run(debug=True)