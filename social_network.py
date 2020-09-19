def socialGraphs(counts):
    # find first X people with group size X
    # print their locations to console

    big_arr = []
    i = 0
    arr = []
    while i < len(counts):
        if counts[i] == 1:
            arr.append(i)
            big_arr.append(arr)
            # print(i)
            arr = []
            i += 1
        else:
            tot = 1
            for j in range(i, len(counts)):
                if counts[j] == counts[i] and tot < counts[i]:
                    arr.append(j)
                    tot += 1
            big_arr.append(arr)
            arr=[]
            i += tot
    for little_arr in big_arr:
        print(little_arr)


def socialGraphs2(counts):
    # find first X people with group size X
    # print their locations to console
    grp_info = {}
    for elem in set(counts):
        # grps = []
        indices = [i for i, x in enumerate(counts) if x == elem]
        breakpoint()
        # if len(indices) > elem:
        #     for y in range(len(indices) / elem):
        #         grps.append()
        grp_info[elem] = indices

def socialGraphs(counts):
    # find first X people with group size X
    # print their locations to console
    grp_info = {}
    for elem in set(counts):
        grps = []
        indices = [i for i, x in enumerate(counts) if x == elem]
        if len(indices) > elem:
            j = 0
            for y in range(len(indices) / elem):
                grps.append(indices[j : j + elem])
                j += elem
        else:
            grps.append(indices)
        grp_info[elem] = indices


    breakpoint()

if __name__ == '__main__':
    arr=[3,3,3,3,3,1,3]
    socialGraphs2(arr)
