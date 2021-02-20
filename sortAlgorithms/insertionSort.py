def insertionSort(array):
    # Write your code here.
	for i in range(1,len(array)):
		print("i",i)
		j = i
		while j > 0 and array[j] < array[j-1]:
			array[j], array[j-1] = array[j-1], array[j]
			j-=1
	return array

def insertionSort2(array):
    # Write your code here.
	for i in range(1,len(array)):
		print(range(1,len(array)))
		print("i",i)
		while i > 0 and array[i] < array[i-1]:
			print("second i", i)
			array[i], array[i-1] = array[i-1], array[i]
			i-=1
			print("after minus",i)
	return array
insertionSort2([5, 2, 6, 8, 9, 3, 5])
[2,3,5,5,6,8,9]




def insertionSort3(array):
    # Write your code here.
	for i in range(len(array)):
		print("i",i)
		j = i
		while j > 0 and array[j] < array[j-1]:
			array[j], array[j-1] = array[j-1], array[j]
			j-=1
	return array

insertionSort([5, 2, 6, 8, 9, 3, 5])
insertionSort3([5, 2, 6, 8, 9, 3, 5])

this = "abcdedcba"
def isPalindrome(string):
    # Write your code here.
	new = ""
	if len(string)>1:
		for i in range(1,len(string)+1):
			new+=string[-i]
		return new == string
	if len(string)==1 or len(string)<1:
		return True
isPalindrome(this)


def isP2(string):
    # Write your code here.
	rev = ""
	for i in reversed(range(len(string))):
		print(i)
		rev+=string[i]
	return rev == string
isP2("abcdedcba")

j = []
len(j)-1
