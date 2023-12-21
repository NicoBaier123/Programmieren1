Weight= float(input("Weight: "))
unit=input("(K)g or (L)bs: ")


if unit.upper() =="K":
    converted= Weight*2.20462262185
    print("Weight in Lbs: "+str(converted))
elif unit.upper()=="L":
    converted= Weight/2.20462262185
    print("Weight in Kgs:"+str(converted))
else:
    print("Error")

