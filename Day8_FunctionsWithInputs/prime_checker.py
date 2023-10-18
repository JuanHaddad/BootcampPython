def prime_checker(number):
    prime = True
    if number == 1:
        prime = False
    if number != 2:
        for num in range(2,number):
            if number % num == 0:
                prime = False
    print(f'{number} is {"not" if not prime else ""} a Prime Number.')

n = int(input())
prime_checker(number=n)