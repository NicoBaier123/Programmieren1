
def find_max(list):
    maximal=max(list)
    return maximal

def find_min(list):
    minimal=min(list)
    return minimal

def remove_duplicates(list):
    newlist=set(list)
    return(newlist)

if __name__ == '__main__':
    list = [1, 2, 3, 4, 5, 33, 57, 6, 45, 43, 12, 45, 8, 7, 67, 56, 45, 98, 99, 34, 57, 21, 22, 33, 43, 45, 65, 23, 31]
    print(find_max(list))
    print(find_min(list))
    print(remove_duplicates(list))