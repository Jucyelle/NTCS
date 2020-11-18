P, R = input().split(" ")

P = int(P)
R = int(R)

if (P == 0 and (R == 1 or R == 0)):
    print("C")
elif (P == 1 and R == 1):
    print("A")
elif (P == 1 and R == 0):
    print("B")
else:
    print("Apenas os números 1 ou 0 são aceitos")


