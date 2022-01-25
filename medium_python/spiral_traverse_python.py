
new = [1,2,3,4,5]
print(new)
print(len(new))
print(range(len(new)-1))

new = [[1,2,3,4],[5,6,7,8],[9,10,11,12]]
new2 = [
   [ 0, 1, 2, 3],
   [ 9,10,11, 4],
   [ 8, 7, 6, 5],
   ]
start_row, end_row = 0, len(new2) - 1
print(start_row, end_row)
start_col, end_col = 0, len(new2[0])-1
print(start_col, end_col)
print(new2[1][3])



print(new)
new.pop(1)
print(new)
new.insert(1,2)
print(new)
