my_ar = [5,2,[7,-1],3,[6,[-13,8],4]]
def check(values, depth=1):
    sum = 0
    for i in values:

        if isinstance(i, int):
            sum+=i
        sum += depth_check(i)

    return sum


def depth_check(array, depdth+1):
    return check(array)
