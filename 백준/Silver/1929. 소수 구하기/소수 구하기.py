def eratosthenes_sieve(m, n):
    sieve = [True] * (n + 1)  # 처음엔 모든 수를 소수라고 가정 (True)
    sieve[0] = sieve[1] = False  # 0과 1은 소수가 아님

    # 2부터 √n까지의 배수를 지움
    for i in range(2, int(n ** 0.5) + 1):
        if sieve[i]:  # i가 소수라면
            for j in range(i * i, n + 1, i):  # i의 배수들은 소수가 아님
                sieve[j] = False

    # m부터 n까지의 소수 출력
    for i in range(m, n + 1):
        if sieve[i]:  # True로 남은 수가 소수
            print(i)

# 입력 예시: m과 n 사이의 소수 출력
m, n = map(int, input().split())
eratosthenes_sieve(m, n)