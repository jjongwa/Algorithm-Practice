import spacy
nlp = spacy.load('en_core_web_sm')

doc = nlp('John ate an apple Oh John')
# for ent in doc.ents:
#     print(ent.text, ent.label_)
#
# print()
# sentence_tokenized_list = [sent.text for sent in doc.sents]
tokenized = list(doc)

print("Noun phrases:", [chunk.text for chunk in doc.noun_chunks])
for entity in doc.ents:
    print(entity.text, entity.label_)

# print(tokenized)
# n_s = ''
# space = 0
# for t in tokenized:
#     if t
#     print(t.text, t.tag_, t.pos_, t.lemma_, t.is_stop)

