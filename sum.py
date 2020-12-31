def prime_number(number):
    if number <= 1:
        return False
    for i in range(2, number):
        if number % i == 0:
            return False
    return True


def sum_prime_number():
    list_prime = []
    for i in range(1, 10001):
        if prime_number(i):
            list_prime.append(i)
    print(sum(list_prime))


sum_prime_number()
