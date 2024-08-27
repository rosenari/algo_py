h, m = map(int, input().split())

time = h * 60 + m - 45
if time < 0:
    time = 1440 - abs(time)

print(f"{time//60} {time%60}")