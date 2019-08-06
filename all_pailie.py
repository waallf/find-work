def P_l(st,number):

    if number ==-1:
        print(st)
        return

    dels = list(st)
    dels[number]= " "
    P_l("".join(dels),number-1)
    P_l(st,number-1)

P_l('abc',number=2)