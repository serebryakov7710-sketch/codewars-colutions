def spin_words(sentence):
    # def spin_words(sentence):
    # Разбиваем строку на список отдельных слов
    words = sentence.split(" ")
    
    # Создаем новый список для измененных слов
    result = []
    
    for word in words:
        if len(word) >= 5:
            # Если в слове 5 или более букв, разворачиваем его
            result.append(word[::-1])
        else:
            # Если меньше 5 букв, оставляем как есть
            result.append(word)
            
    # Собираем слова обратно в одну строку через пробел
    return " ".join(result)
