import os

os.chdir('5-oy/9-dars/')

count = 0
from string import punctuation
with open('avto.txt','r') as f:
    text = f.read()
    for punc in punctuation:
        print(punc)
        text = text.replace(punc,text)
with open('avto.txt','w') as f:
    f.write(text)

# with open(file_path, 'r', encoding='utf-8') as f:
#     text = f.read()
#     text = text.replace(shart, '')
# with open(file_path, 'w', encoding='utf-8') as f:
#     f.write(text)