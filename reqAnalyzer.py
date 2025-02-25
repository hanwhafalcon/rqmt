import spacy
#import sys

# Uncomment if you want to see all the modules loaded during runtime.
#print(sys.modules.keys())

# Load the Small English Model predownloaded by the spacy library.
# python -m spacy download en_core_web_sm
nlp = spacy.load('en_core_web_sm')

def categorize_requirement(requirement):
    requirement = requirement.lower()
    if 'must' in requirement or 'shall' in requirement:
        return 'mandatory'
    elif 'should' in requirement or 'could' in requirement:
        return 'optional'
    else:
        return 'unknown'

def extract_breakdown(doc):
    breakdown = {
        'actor': None,  # None means "not found yet"
        'verb': None,
        'entity': None
    }
    for token in doc:  # Look at each word (token) in the sentence
        if token.dep_ == 'nsubj':  # Subject of the sentence
            breakdown['actor'] = token.text
        elif token.dep_ == 'ROOT':  # Main verb
            breakdown['verb'] = token.text
        elif token.dep_ == 'dobj':  # Direct object
            breakdown['entity'] = token.text
    return breakdown

def main():
    print("Enter a requirement (or 'quit' to exit):")
    while True:
        requirement = input("> ")
        if requirement.lower() == 'quit':
            break
        doc = nlp(requirement)  # Let SpaCy analyze the sentence
        category = categorize_requirement(requirement)
        breakdown = extract_breakdown(doc)
        print(f"Category: {category}")
        print(f"Actor: {breakdown['actor']}")
        print(f"Verb: {breakdown['verb']}")
        print(f"Entity: {breakdown['entity']}")
        print()

if __name__ == "__main__":
    main()