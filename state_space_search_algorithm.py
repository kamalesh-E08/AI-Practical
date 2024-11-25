import random

def generate_random_list(size, min_value, max_value):
    return [random.randint(min_value, max_value) for _ in range(size)]

def hill_climbing_max(numbers):
    current_max = max(numbers)
    while True:
        index_to_change = random.randint(0, len(numbers) - 1)
        new_number = random.randint(min(numbers), max(numbers))
        new_numbers = numbers.copy()
        new_numbers[index_to_change]=new_number
        new_max= max(new_numbers)
        if new_max > current_max:
            current_max = new_max
            numbers=new_numbers
        else:
            break 
    return current_max

if __name__=="__main__":
    size=int(input("Enter the size of the list: "))
    min_value = int(input("Enter the minimum value for numbers: "))
    max_value = int(input("Enter the maximum value for numbers: "))
    numbers= generate_random_list(size, min_value, max_value)
    print("Original list of numbers:", numbers)
    max_value_found=hill_climbing_max(numbers)
    print(f"Maximum value found: {max_value_found}")