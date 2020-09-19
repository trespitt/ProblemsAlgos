from collections import Counter

def itemsSort(items):
    new_arr = []
    freq = Counter(items)
    #for val, frq in freq.items():
    for x in range(1, max(freq.values()) + 1):
        freq_sub = {k: v for k, v in freq.items() if v == x}
        key_arr = []
        for k, v in freq_sub.items():
            for y in range(x):
                key_arr.append(k)
        key_arr.sort() 
        #new_arr.append(key_arr)
        for elem in key_arr:
            new_arr.append(elem)
    print(new_arr)


if __name__=='__main__':
    itemsSort([5,4,6,5,4,3])
