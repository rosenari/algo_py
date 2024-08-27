h, m = map(int, input().split())
need = int(input())

time = h * 60 + m + need

if time >= 1440:
    time = time - abs(1440)

print(f"{time//60} {time%60}")