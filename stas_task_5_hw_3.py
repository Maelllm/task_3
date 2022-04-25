text = input('Show me your BIG text ').lower()
list_1 = text.split()
word_bad = 'черт'
word_good = '####'
for i in list_1:
    if word_bad in list_1:
        index_word = list_1.index(word_bad)
        list_1[index_word] = word_good
text_2 = " ".join(list_1)
print(text_2)
