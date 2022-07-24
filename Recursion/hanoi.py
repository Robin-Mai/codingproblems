"""
Tower of Hanoi is a mathematical puzzle where we have three rods and n disks. The objective of the puzzle is to move the entire stack to another rod, obeying the following simple rules:

The end rod can be any rod

Only one disk can be moved at a time.
Each move consists of taking the upper disk from one of the stacks and placing it on top of another stack i.e. a disk can only be moved if it is the uppermost disk on a stack.
No disk may be placed on top of a smaller disk.

"""


def TowerOfHanoi(n, from_rod, to_rod, aux_rod):
    if n == 0:
        return
    TowerOfHanoi(n - 1, from_rod, aux_rod, to_rod)
    print("Move disk", n, "from rod", from_rod, "to rod", to_rod)
    TowerOfHanoi(n - 1, aux_rod, to_rod, from_rod)











n = 1
TowerOfHanoi(n, 'A', 'B', 'C')
"""

def inizialize_hanoi(n: int):
    stack_A = list()
    stack_B = list()
    stack_C = list()
    for i in range(n):
        stack_A.append(i)
    return stack_A, stack_B, stack_C

def move(stack_from, stack_over, stack_to):
    disk = stack_from.pop(0)
    stack_to.insert(0, disk)
    print('moved from {0} to {1}'.format(stack_from, stack_to))

def solve(n: int):
    a, b, c = inizialize_hanoi(n)

    if n == 1:
        move(a,c)
    if n == 2:
        move(a, b)
        move(a, c)
        move(a, c)
    if n == 3:
        pass




a, b, c = inizialize_hanoi(5)
move(b, c)
"""

print()
