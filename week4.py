# no 1

nama = input("Masukan nama anda:")
x = 1

while x <= 50 :
    print(x , nama)
    x +=1

# no 2

def barisan_terbalik(n):
    for i in range(n, 0, -1):
        for j in range(i):
            print(j + 1, end='')
        print()

n = int(input("Masukan bilangan:"))
barisan_terbalik(n)