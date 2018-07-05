import re
sentence = "A, very very; irregular_sentence"
sent = re.sub('[\W _]',' ',sentence)
print(sentence)