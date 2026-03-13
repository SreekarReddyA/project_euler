def maximum_path_sum_one(data):
    elements = [[int(element) for element in line.split(" ")] for line in data.splitlines()]
    # get to the penultimate row and move up to the first row
    for i in range(len(elements) - 2, -1, -1):
        for j in range(len(elements[i])):
            elements[i][j] = elements[i][j] + max(elements[i+1][j], elements[i+1][j+1])
    
    return elements[0][0]

with open("triangle.txt", "r") as f:
    data = f.read()
print(maximum_path_sum_one(data))