while True:
    x=input()
    try :
        x=int(x)
    except Exception as e:
        print(-10000000)
        break
    else:
        print(x)
        break