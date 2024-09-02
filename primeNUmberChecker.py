def is_prime(num):
    """Check if the number is Prime"""

    if num == 2 or num == 1:
        return True

    for i in range(2,num,1):
        if num % i == 0:
            return False
    
    return True

print(is_prime(75))