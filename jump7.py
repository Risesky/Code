a=0
while a < 100:
    a+=1
    if a%7 == 0 or a%10 == 7:
        continue
    elif a >= 70 and a <= 79:
        continue
    else:
        print(a)
