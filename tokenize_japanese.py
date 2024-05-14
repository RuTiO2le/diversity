import MeCab

# Initialize MeCab tokenizer
mecab = MeCab.Tagger()

# Function to tokenize Japanese sentences
def tokenize_japanese(text):
    mecab.parse('')
    node = mecab.parseToNode(text)
    tokens = []
    while node:
        if node.surface != '':
            tokens.append(node.surface)
        node = node.next
    return tokens