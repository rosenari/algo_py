# All numbers divided by 2 have a remainder of 1 or 0

def power(exp):
    if exp == 1:
        return A % C  # I didn't think this through ㅠ

    v = (power(exp//2) ** 2) % C

    if exp % 2 == 0:
        return v

    return (v * A) % C


A, B, C = map(int, input().split())
print(power(B))