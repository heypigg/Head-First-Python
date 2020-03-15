

def search4vowels(phrase: str) -> set:
    """Return a boolean based on any vowels found."""
    vowels = set('aeiou')
    return vowels.intersection(set(phrase))
search4vowels('alphabet')


def search4letters(phrase: str, letters: str) -> set:
    """Return a set of the 'letters' found in 'phrase'."""
    return set(letters).intersection(set(phrase))