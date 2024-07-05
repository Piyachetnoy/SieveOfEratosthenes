# SieveOfEratosthenesというアルゴリズムを使う
def SOE(num):
    # 要素Trueがnum+1個ある配列primeを作成
    prime = [True for i in range(num + 1)]
    p = 2

    # p*p<=numの間、素数pで割り切れる整数を全てFalseとする
    while p * p <= num:
        if prime[p]:
            for i in range(p * p, num + 1, p):
                prime[i] = False
        p += 1

    # primeのTrueである要素は何番目かを表示
    for p in range(2, num + 1):
        if prime[p]:
            print(p)

# num以下の素数を表示する
num = 1000
print("The prime numbers smaller than or equal to", num)
SOE(num)
