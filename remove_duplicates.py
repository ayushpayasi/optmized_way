# this program shows time taken by different methods to remove duplicates from a list
# use time.time() method to find the initial and end time of the method
# make sure to use enough input to see the difference in the outputs
# below is the rank of the methods
'''
method 3 (best)
method 2 (nearly same as method 3)
method 1 (bad)
method 4 (worst)

'''

temp = []

ints_list = input().split()
def method1(ints_list):
    for x in ints_list:
        if x not in temp:
            temp.append(x)
    return temp

def method2(ints_list):
    return list(set(ints_list))

def method3(ints_list):
    return list(dict.fromkeys(ints_list))

def method4(ints_list):
    for x in ints_list:
        if ints_list.count(x) > 1:
            ints_list.remove(x)
    return (ints_list)  # [1, 2, 3, 4]




start = time.time()
temp = method4(ints_list)
end = time.time()
print(f'time taken by this method is ={end -start}')