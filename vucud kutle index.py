kilo=int(input("kilonu yaz"))
boy=int(input("boyunu yaz"))
boy=boy/100
vki=kilo/boy**2

if vki<18:
    print("ariq:",vki)
elif vki>=13.5 and vki<24:
    print("normal:",vki)
elif vki>25.5 and vki<30:
    print("obez:", vki)
elif vki>=30:
    print("çox kilolu", vki)


        


