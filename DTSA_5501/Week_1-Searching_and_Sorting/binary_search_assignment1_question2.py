def integerCubeRootHelper(n, left, right):
    cube = lambda x: x * x * x # anonymous function to cube a number
    assert(n >= 1)
    assert(left < right)
    assert(left >= 0)
    assert(right < n)
    assert(cube(left) < n), f'{left}, {right}'
    assert(cube(right) > n), f'{left}, {right}'
    # your code here
    
    j = right-left
    mid = j//2
    k = left + mid
    
    if cube(k) <= n and cube(k+1) > n:
        return k
    elif cube(k+1) == n:
        return k+1
    elif cube(k) <= n and cube(k+1) <= n:
        print(f"calling integerCubeRootHelper(n, {k+1}, {right})")
        return integerCubeRootHelper(n, k+1, right)
    else:
        print(f"calling integerCubeRootHelper(n, {left}, {k-1})")
        return integerCubeRootHelper(n, left, k)
    
# Write down the main function
def integerCubeRoot(n):
    print(f"calling integerCubeRoot({n})")
    print("##### ##### ##### ##### #####")
    assert( n > 0)
    if (n == 1): 
        return 1
    if (n == 2):
        return 1
    return integerCubeRootHelper(n, 0, n-1)

assert(integerCubeRoot(1) == 1)
assert(integerCubeRoot(2) == 1)
assert(integerCubeRoot(4) == 1)
assert(integerCubeRoot(7) == 1)
assert(integerCubeRoot(8) == 2)
assert(integerCubeRoot(20) == 2)
assert(integerCubeRoot(26) == 2)
for j in range(27, 64):
    assert(integerCubeRoot(j) == 3)
for j in range(64,125):
    assert(integerCubeRoot(j) == 4)
for j in range(125, 216):
    assert(integerCubeRoot(j) == 5)
for j in range(216, 343):
    assert(integerCubeRoot(j) == 6)
for j in range(343, 512):
    assert(integerCubeRoot(j) == 7)
print('Congrats: All tests passed! (10 points)')