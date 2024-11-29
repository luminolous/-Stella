def penjumlahan():
    a, b = map(int, input("Masukkan soal: ").split("+"))
    print(a + b)

def pengurangan():
    a, b = map(int, input("Masukkan soal: ").split("-"))
    print(a - b)

def perkalian():
    a, b = map(int, input("Masukkan soal: ").split("x"))
    print(a * b)

def pembagian():
    a, b = map(int, input("Masukkan soal: ").split("/"))
    if b == 0:
        print("Silahkan dicek ulang, tidak dapat dibagi karena pembagi = 0")
    else:
        print(a / b)
    
def perpangkatan():
    a, b = map(int, input("Masukkan soal: ").split("^"))
    print(a ** b)

def prime():
    modusNumber = int(input("Insert number: "))
    if modusNumber == 1:
        print(f'{modusNumber} is not a prime number!')

    for i in range(2, modusNumber):
        a = modusNumber % i
        if a == 0:
            print(f'{modusNumber} is not a prime number!')

    print(f'{modusNumber} is a prime number!')