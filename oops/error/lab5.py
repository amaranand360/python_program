class formulaError(Exception):
    pass

try:
    exp =input("Enter your formula:")
    if(len(exp) != 3):
        raise formulaError("formula Length is invalide !")

    op=exp[1]
    li=exp.split(op)
    li[0]=float(li[0])
    li[1]=float(li[1])

    if (op != '+' and op !='-'):
        raise formulaError("Invalide oprand!")

except formulaError as f:
    print(f)

except ValueError as v:
    print(v)

else:
    if(op =='+'):
        print("sum = ",li[0]+li[1])
    else:
        print("diff = ",li[0]-li[1])