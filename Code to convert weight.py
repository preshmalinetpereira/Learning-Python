#https://www.youtube.com/watch?v=kqtD5dpn9C8&t=804s

#Excercise #36.57

w = float(input("Weight: "))
unit = input("(K)g or (L)bs: ").lower()
if unit == 'l':
    print("Weight in Kg: " + str(w*0.45))
elif unit == 'k':
    print("Weight in Lbs: " + str(w*2.20))
else:
    print("Icorrect input: Input can only be K or L")