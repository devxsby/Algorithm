N = int(input())
stars = [[' ' for _ in range(N)] for _ in range(N)]

# 별 찍는 재귀 함수
def drawStars(size, x, y):
    if size == 1:
        stars[y][x] = '*'
    else:
        next_size = size // 3
        for dx in range(3):
            for dy in range(3):
                if dx != 1 or dy != 1:
                    drawStars(next_size, x + dx*next_size, y + dy*next_size)

drawStars(N, 0, 0)
for i in stars:
    print(''.join(i))