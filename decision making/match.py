n=int(input())
match(n):
    case i if i>=90 and i<=100:
        print("A")
    case i if i>=75 and i<=90:
        print("B")
    case i if i>=50 and i<=75:
        print("C")
    case i if i>=35 and i<=50:
        print("D")
    case _:
        print("F")


    