print ("Hello")
time = 15
cycle = "прошлое" if time < 0 else "ночь" \
    if time < 6 else "утро" if time < 12 else "день" \
    if time < 18 else "вечер" if time < 24 else "будущее"
n = 0
while n <= 5:
    print(n)
    n += 1
print(cycle)
print(round(0.3333, 2))
round(0,33333)
round(0.3333, 2)
numbers = [5, 9, 22, 3]
for num in numbers:
    print(num)
for s in "cat":
    print(s)   
for animal in ["dog", "cat", "parrot"]:
     if animal == "cat":
         break
     print(animal) 
for animal in ["dog", "cat", "parrot"]:
    print(animal)     
    for letter in animal:
        print(letter)

n = 5
factorial = 1
while n > 1:
    factorial *= n 
    n -= 1
print (factorial)
n = 0
factorial = 1
if n == 0: 
    factorial = 1
else:
    while n > 1:
        factorial *= n 
        n -= 1
print (factorial)
def factorial(n):
    assert n >= 0, "Число должно быть неотрицательным"
    if n == 0:
        return 1
    elif n == 1:
        return n
    else:
        return n * factorial(n - 1)

print("Факториал 5 равен:", factorial(5))
print("Факториал 0 равен:", factorial(0))