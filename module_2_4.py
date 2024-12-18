from contextlib import nullcontext

numbers = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11, 12, 13, 14, 15]
not_primes = []
primes = []

for i in range(1, len(numbers)):
    for j in range(1, len(numbers)):
        if numbers[i] < numbers[j]:
            break
        elif numbers[i] % numbers[j] == 0 and numbers[i] != numbers[j]:
            not_primes.append(numbers[i])
            break
        elif numbers[i] % numbers[j] == 0 and numbers[i] == numbers[j]:
            primes.append(numbers[i])
            break

print(f'Исходный код:\n{numbers}')
print(f'Primes: {primes}')
print(f'Not primes: {not_primes}')
