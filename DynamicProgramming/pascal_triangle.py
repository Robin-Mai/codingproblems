"""
Given an integer numRows, return the first numRows of Pascal's triangle.

In Pascal's triangle, each number is the sum of the two numbers directly above it as shown

Input: numRows = 1
Output: [[1]]

Input: numRows = 5
Output: [[1],[1,1],[1,2,1],[1,3,3,1],[1,4,6,4,1]]

"""

def split_symmetry(current_row):
    even = len(current_row) % 2 == 0
    if even:
        sim_axis = int(len(current_row) / 2)
        split = current_row[:sim_axis]
    else:
        sim_axis = int(len(current_row) / 2) + 1
        return current_row[:sim_axis]
    return split

split_even = split_symmetry([1, 1])
split_odd = split_symmetry([1, 2, 1])

def compute_next_row(current_row: list):
    new_row = list()
    for i in range(len(current_row) - 1):
        r = i
        l = i + 1
        val = current_row[l] + current_row[r]
        new_row.append(val)

    new_row.insert(0, 1)
    new_row.append(1)
    return new_row

result_n3 = compute_next_row([1, 1])
result_n4 = compute_next_row([1, 2, 1])
result_n5 = compute_next_row([1, 3, 3, 1])
print()

def pascal_triangle(n: int):
    if n == 1:
        return [1]
    if n == 2:
        return [1, 1]

    current_row = [1, 1]
    triangle = [[1], current_row]

    for i in range(n-2):
        current_row = compute_next_row(current_row)
        print(current_row)
        triangle.append(current_row)

    return triangle


triangle = pascal_triangle(10)
print(triangle)
print()