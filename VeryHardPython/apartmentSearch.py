blocks1 = [
{
"gym": False,
"school": True,
"store": False,
},
{
"gym": True,
"school": False,
"store": False,
},
{
"gym": True,
"school": True,
"store": False,
},
{
"gym": False,
"school": True,
"store": False,
},
{
"gym": False,
"school": True,
"store": True,
},
]
reqs1 = ["gym", "school", "store"]



random = {}
# for i in range(5):
#     for j in range(5,11):
#         if j > i:
            string_value = str(i)
            random [i] = 0
            random[i]+=1
i = 8
string_value = str(i)
random[string_value]=1
random[8] = 3
random["8"] = 5
random[8]+=1
print(random)

def apartment_search(blocks,reqs):
    max_distance_at_blocks = [float("-inf") for block in blocks]
    for i in range(len(blocks)):
        for req in reqs:
            closest_req_distance = float("inf")
            for j in range(len(blocks)):
                if blocks[j][req]:
                    closest_req_distance = min(closest_req_distance, distance_between (i, j))
            max_distance_at_blocks[i] = max(max_distance_at_blocks[i], closest_req_distance)
    return get_idx_at_min_value(max_distance_at_blocks)

def get_idx_at_min_value(array):
    idx_at_min_value = 0
    min_value = float("inf")
    for i in range(len(array)):
        current_value = array[i]
        if current_value < min_value:
            min_value = current_value
            idx_at_min_value = i
    return idx_at_min_value

def distance_between(a, b):
    return abs(a-b)

apartment_search(blocks1, reqs1)

for i in blocks:
    print(i,"This is i")
    for j in i:
        print(j, "This is j")
    for l in blocks:
        print(l, "This is l")
