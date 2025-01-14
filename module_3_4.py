def single_root_words(root_word, *other_words):
    answer = []
    for word in other_words:
        if root_word.lower() in word.lower():
            answer.append(word)
        elif word.lower() in root_word.lower():
            answer.append(word)
    return answer

print(single_root_words('rich', 'richiest', 'orichalcum', 'cheers', 'richies'))
print(single_root_words('Disablement', 'Able', 'Mable', 'Disable', 'Bagel'))
