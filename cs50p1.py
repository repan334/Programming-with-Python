name = input("whats your name? ")
print("hello " +name)
# belajar variable dan command 

x = int(input("apa itu x?"))
y = int(input("apa itu y?"))
score1 = int(input("masukan nilai score 1: "))
score2 = int(input("masukan nilai score 2: "))

if x > y or y < x:
    print(f"nilai x adalah {x} dan nilai y adalah {y} jadi nilai x lebih besar dari y")
elif x == y and score1 != score2:
    print(f"nilai x adalah {x} dan nilai y adalah {y} jadi nilai x sama dari y")
else : 
    print("angka diluar perhitungan")
# kondisional python

def main():
    x = int(input("apa itu x? "))
    if score2(x):
        print("gatau")
    else:
        print("perkalian dari x adalah ")

def is_even(n):
    return True if n % 2 == 0 else False

match name:
    case "Revan":
        print(f"hello revan")
    case "Reva":
        print(f"hello Reva")
    case "dylan":
        print("hello dylan")
    case "":
        print("hello siapa lu?")
