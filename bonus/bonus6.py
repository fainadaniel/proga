h = int(input("Tell me your height in cm\n"))
m = int(input("Tell me your weight in kg\n"))
hh = h/100
i = m/(hh**2)
print("imt =", i)
if i <= 16:
    print('Выраженный дефицит массы тела')
if i > 16 and i <= 18.5:
    print('Недостаточная (дефицит) масса тела')
if i > 18.5 and i <= 24.99:
    print('Норма')
if i > 24.99 and i <= 30:
    print('Избыточная масса тела (предожирение)')
if i > 30 and i <= 35:
    print('Ожирение первой степени')
if i > 35 and i <= 40:
    print('Ожирение второй степени')
if i > 40:
    print('Ожирение третьей степени (морбидное)')
