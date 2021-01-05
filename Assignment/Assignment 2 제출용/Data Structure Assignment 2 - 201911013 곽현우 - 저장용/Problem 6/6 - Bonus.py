# 6 - Bonus answer)
def heapsort(a):
    n = len(a)
    for index1 in range(n):
        if index1 == 0:
            continue
        parent = []
        index1_1 = index1
        while True:
            parent_index = (index1_1 - 1) // 2
            parent.append(parent_index)
            index1_1 = parent_index
            if index1_1 <= 0:
                if parent[-1] < 0:
                    parent.remove(parent[-1])
                break

        for in_index1 in parent:
            if a[index1] > a[in_index1]:
                a[index1], a[in_index1] = a[in_index1], a[index1]
            for i in range(len(parent)):
                if (i + 1) < len(parent) and a[parent[i]] > a[parent[i + 1]] :
                    a[parent[i]] , a[parent[i + 1]] = a[parent[i + 1]],a[parent[i]]
                else:
                    break
            else:
                break
    len_heap = len(a)
    for index2 in range(len_heap):
        a[0], a[(len_heap - 1)] = a[(len_heap - 1) ], a[0]
        len_heap -= 1
        if len_heap <= 0:
            break
        parent1 = []
        index2_1 = index2
        while True:
            parent1_index = (index2_1 - 1) // 2
            parent1.append(parent1_index)
            index2_1 = parent1_index
            if index2_1 < 0:
                if parent1[-1] < 0:
                    parent1.remove(parent1[-1])
                break
        for in_index2 in parent1:
            if a[index2] > a[in_index2]:
                a[index2], a[in_index2] = a[in_index2], a[index2]
            for i in range(len(parent1)):
                if (i + 1) < len(parent1) and a[parent1[i]] > a[parent1[i + 1]] :
                    a[parent1[i]], a[parent1[i + 1]] = a[parent1[i + 1]], a[parent1[i]]
                else:
                    break
            else:
                break
    return a
