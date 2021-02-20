loi = [i for i in range(1,1001)]

def convert_nums_to_rn(value):
    ints = [1,4,5,9,10,40,50,90,100,400,500,900,1000]
    rn = "I,IV,V,IX,X,XL,L,XC,C,CD,D,CM,M".split(",")
    idx = 12
    ci = ""
    while value != 0:
        if value >= ints[idx]:
             ci += rn[idx]
             value = value - ints[idx]
        if value < ints[idx]:
            idx -= 1
    return ci

convert_nums_to_rn(874)
