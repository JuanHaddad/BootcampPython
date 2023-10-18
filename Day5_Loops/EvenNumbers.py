#Write your code below this row 👇
soma = 0
for i in range(2, 101, 2):
    soma += i
print(soma)

soma = 0
for i in range(1, 101):
    if i % 2 == 0:
        soma += i 
print(soma)