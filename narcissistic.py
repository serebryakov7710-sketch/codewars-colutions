def narcissistic(value):
    num_str = str(value)
    power = len(num_str)
    
    total_sum = 0
    for char in num_str:
        digit = int(char)
        total_sum += digit ** power
        
    return total_sum == value
