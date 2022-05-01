while True:
    try:
        a = input()
        temp = 'yes'
        for i in range(0, len(a)//2):
            if(a[i] != a[len(a)-1-i]):
                temp = 'no'
        print(temp)
    except:
        break