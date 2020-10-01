def clearText(text):
    words = text.replace('.', '').replace(',', '').replace(
        '"', '').replace(':', '').replace('?','').split(' ')
    for word in words:
        if (not word.isalpha()):
            for i in range(len(word)):
                if (not word[i].isalpha):
                    word.replace(word[i], '')
    return words


def insertionSort(vector):
    for j in range (1, len(vector)):
        key = vector[j]
        i = j - 1
        while (i >= 0 and vector[i] > key):
            vector[i + 1] = vector[i]
            i-=1
        vector[i + 1] = key
    return vector

text = input().lower()
words = insertionSort(clearText(text))
print(words)

