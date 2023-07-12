
def search4vowels(phrase: str):

    """Returns the set of vowels found in 'phrase'."""
    return set('aeiou').intersection(set(phrase))


def search4letters(phrase: str, letters: str='aeiou'):

    """Returns the set of 'letters' found in 'phrase'."""
    return set(letters).intersection(set(phrase))

def log_request(req, res):
    with open('vsearch.log', 'a') as vs:
        print(req,res,file=vs)












