n = int(input())
for i in range(n):
    X1, Y1, X2, Y2, X3, Y3 = map(int, input().split())
    if X3 >= min(X1, X2) and Y3 >= min(Y1, Y2) and X3 <= max(X1, X2) and Y3 <= max(Y1, Y2):
    #     火樹的X座標>=兩座標中較小的X座標，火樹的Y座標>=兩座標中較小的Y座標，火樹的X座標<=兩座標中較大的X座標，火樹的Y座標<=兩座標中較大的Y座標
        if X3 - X1 != 0 and X2 - X3 != 0:
            if (Y3 - Y1) / (X3 - X1) == (Y2 - Y3) / (X2 - X3):
                print('該死的東西!竟敢想讓我死！')
            else:
                print('父親大人!母親大人!我快到了！')
        elif X3 - X1 == 0 and X2 - X3 == 0:
            print('該死的東西!竟敢想讓我死！')
        else:
            print('父親大人!母親大人!我快到了！')
    else:
        print('父親大人!母親大人!我快到了！')