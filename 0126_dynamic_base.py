# 피보나치 함수를 재귀 함수로 구현
def fibo(x):
    if x == 1 or x == 2:
        return 1
    return fibo(x - 1) + fibo(x - 2)


print(fibo(4))

# 피보나치 수열 소스코드(재귀적)

# 한 번 계산된 결과를 Memoization하기 위한 리스트 초기화
d = [0] * 100


# 피보나치 함수를 재귀함수로 구현(Top-down 다이나믹 프로그래밍)
def fibo(x):
    # 종료 조건(1 or 2일 때 1을 반환)
    if x == 1 or x == 2:
        return 1
    # 이미 계산한 적 있는 문제라면 그대로 반환
    if d[x] != 0:
        return d[x]
    # 아직 계산하지 않은 문제라면 점화식에 따라서 피보나치 결과 반환
    d[x] = fibo(x - 1) + fibo(x - 2)
    return d[x]


print(fibo(99))

d = [0] * 100

def pibo(x):
    print('f(' + str(x) + ')', end = ' ')
    if x == 1 or x == 2:
        return 1
    if d[x] != 0:
        return d[x]
    d[x] = pibo(x-1) + pibo(x-2)
    return d[x]

pibo(6)

# 피보나치 수열 소스코드(반복적)
d = [0] * 100

# 첫 번째 피보나치 수와 두 번째 피보나치 수는 1
d[1] = 1
d[2] = 1
n = 99

# 피보나치 함수 반복문으로 구현(Bottom-up 다이나믹 프로그래밍)
for i in range(3, n+1):
    d[i] = d[i - 1] + d[i - 2]

print(d[n])