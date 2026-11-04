def find_outlier(integers):
    # Берем первые 3 числа и смотрим их остатки от деления на 2
    sample = [x % 2 for x in integers[:3]]
    
    # Если нулей (четных чисел) больше одного, значит большинство четные
    majority_even = sample.count(0) > 1
    
    # Ищем элемент, нарушающий правило большинства
    for x in integers:
        if majority_even and x % 2 != 0:
            return x
        if not majority_even and x % 2 == 0:
            return x
