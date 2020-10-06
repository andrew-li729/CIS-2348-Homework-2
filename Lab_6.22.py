# Andrew Li
# 1824794
x = 0
y = 0

a = int(input())  # var for 1st equation
b = int(input())
c = int(input())

d = int(input())  # var for 2nd equation
e = int(input())
f = int(input())

solution_x = 1000  # initializes final values for x and y, if true values are found below, they will be changed
solution_y = 1000

for x in range(-10, 11):
    for y in range(-10, 11):
        equation1 = a * x + b * y  # ax + by
        equation2 = d * x + e * y  # dx - ey
        if equation1 == c and equation2 == f:
            solution_x = x  # changes previously set values to solution
            solution_y = y


if solution_x != 1000 and solution_y != 1000:  # if the values were changed, meaning the equations were solved,
    print(solution_x, solution_y)              # print x and y, else print no solution since they were not changed
else:                                          # meaning no solution was found
    print("No solution")
