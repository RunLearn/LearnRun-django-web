def decorator(func):
    def decorated(N,H,W):
        if N==3:
            print('삼각형의 넓이')
            func(N,H,W)
        elif N==4:
            print('사각형의 넓이')
            func(N, H, W)
    return decorated

@decorator
def space(N,H,W):
    if N == 3:
        print( H * W * 0.5)
    elif N == 4:
        print(H * W)


N, H, W = map(int,input().split())

space(N,H,W)