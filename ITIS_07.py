file = open("47100387.txt", "r")
text = file.read(encoding='latin1')
# Преобразование текста в список слов
words = text.lower().split()
# Создание словаря для подсчета частоты слов 
word_count = {}
# Подсчет частоты слов
for word in words:
# Удаление символов пунктуации word = word.strip('.,?!')
    if word in word_count:
        word_count[word] += 1
    else:
        word_count[word] = 1
# Вывод результатов
end = len(word_count)
hoare_sort(word_count, 0, end)
print("Слова и их частота:")
for word, count in word_count.items(): 
    print(f"{word}: {count}")
file.close()

def hoare_sort(array, start, end):
    if end == start:
        return
    pivot = array[end]
    store_index = start
    for i in range(start, end):
        if array[i] <= pivot:
            array[i], array[store_index] = array[store_index], array[i]
            store_index += 1

    array[store_index], array[end] = array[end], array[store_index]
    if store_index > start:
        hoare_sort(array, start, store_index - 1)
    if store_index < end:
        hoare_sort(array, store_index + 1, end)