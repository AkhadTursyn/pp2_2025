def is_prime(n):
    if n < 2:
        return False
    for i in range(2, int(n ** 0.5) + 1):
        if(n % i == 0):
            return False
    return True

def filter_prime(numbers):
    return [num for num in numbers if is_prime(num)]

numbers = list(map(int, input("Enter numbers with spaces: ").split()))
prime_numbers = filter_prime(numbers)
print(f"Prime numbers: {prime_numbers}")