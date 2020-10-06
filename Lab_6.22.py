# Andrew Li
# 1824794
x = 0
y = 0

for x in range(-10, 11):
    for y in range(-10, 11):
        equation1 = 8 * x + 7 * y
        equation2 = 3 * x - 5 * y
        if equation1 == 38 and equation2 == -1:
            solution_x = x
            solution_y = y
            print(solution_x, solution_y)

equation1 = 8 * solution_x + 7 * solution_y
equation2 = 3 * solution_x - 5 * solution_y

if equation1 != 38 and equation2 != -1:
    print("No solution")
