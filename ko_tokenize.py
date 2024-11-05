from kiwipiepy import Kiwi
import json

kiwi = Kiwi()

sent = []

i = 0
for i, line in enumerate(open('wiki.txt', 'r', encoding='utf-8')):
    if i > 0 and i % 10000 == 0:
        fname = f'wiki_morphs/wiki_{i}.json'
        print(fname)
        with open(fname, 'w', encoding='utf-8') as f:
            json.dump(sent, f, ensure_ascii=False)
        sent = []
    
    if line == '' or line == '\n' or line.startswith('<doc') or line.startswith('</doc'):
        continue
    
    result = kiwi.analyze(line)
    tokens, score = result[0]
    
    morphs = []
    for token in tokens:
        morphs.append(token.form)

    sent.append(morphs)
    
if sent:
    with open(f'wiki_morphs/wiki_{i}.json', 'w', encoding='utf-8') as f:
        json.dump(sent, f, ensure_ascii=False)
