def main1():
    for i in range(10):
        print("Hello ")

def main2():
    for i in range(11):
        if i == 0:
            continue
        print(i*i)

def main3():
    n = int(input("Введите натуральное число: "))
    sum = 0
    while n > 0:
        digit = n % 10
        sum += digit
        n //= 10
    print(sum)

def main4():
    s = str(int(input()))
    zero = s.count('0')
    nine = s.count('9')
    print('0' if zc > nc else '9')

def main5():
    s = 1
    while True:
        x = int(input())
        if x == 0:
            break
        s *= x
    print(s)

def main6():
    input_str = input()
    for i in range(len(input_str) + 1):
        print(input_str[i])
        if input_str[i] in ("i", "e", "a"):
            print("нашлась!")
            return
    print("Распечатали все буквы")

def main7():
    input_str = input() 
    n = 0 
    for i in range(len(input_str) + 1):
        if input_str[i] >= 100000:
            n = n+1
    print(n)

def main8():
    items = ['рюкзак', 'палатка', 'каремат', 'топор', 'тарелка', 'ложка', 'кружка', 'розжиг']
    print(*items, sep = "\n")

def main9():
    n = int(input())
    for i in range(1, n+1): 
        print("*" * i)

def main10():
    list = [79, -53, 44, 60, -41, -40, 53, 75, -77, 20]
    positive = []
    negative = []
    for x in list:
        if (x >= 0):
            positive.append(x)
        else:
            negative.append(x)

def main11():
    n = int(input())
    m = int(input())
    s = input()
    for x in range(m):
    print(s*n)