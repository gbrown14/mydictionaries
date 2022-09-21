

with open('sometext.txt','r') as txt:
    words = txt.read().lower().split(" ")
    txt.close()
print(words)