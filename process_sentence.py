import spacy


def render(sentence, nlp, filepath):
    doc = nlp(sentence)
    img = spacy.displacy.render(doc, style="dep")
    filepath.open("w").write(img)
