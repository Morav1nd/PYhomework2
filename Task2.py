# Петя и Катя – брат и сестра. Петя – студент, а Катя – школьница.
# Петя помогает Кате по математике. Он задумывает два натуральных числа X и Y (X,Y≤1000), а Катя должна их отгадать.
# Для этого Петя делает две подсказки.
# Он называет сумму этих чисел S и их произведение P. Помогите Кате отгадать задуманные Петей числа.

x = input()
x = int(x)

y = input()
y = int(y)

S = x + y
print(S)

P = x * y
print(P)

x1 = int((S + ((-S) ** 2 - 4 * P) ** 0.5) / 2)
print(x1)

y1 = S - x1
print(y1)
