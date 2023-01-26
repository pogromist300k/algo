# O(n) #
def merge(a, b):
    merged = [0] * (len(a) + len(b))
    i = j = 0
    for k in range(len(merged)):
        if j == len(b) or i < len(a) and a[i] <= b[j]:
            merged[k] = a[i]
            i += 1
        else:
            merged[k] = b[j]
            j += 1
    return merged


# O(nlogn) #
def merge_sort(a):

    def sort(left, right):

        if right - left == 1:
            return [a[left]]

        mid = (left + right) // 2
        half_1 = sort(left, mid)
        half_2 = sort(mid, right)
        return merge(half_1, half_2)

    sorted = sort(0, len(a))
    for i in range(len(a)):
        a[i] = sorted[i]


# O(logn) #
def binary_search(a, target):

    def search(left, right):

        if right - left < 1:
            return -1

        mid = (left + right) // 2
        if a[mid] == target:
            return mid
        if a[mid] > target:
            return search(left, mid)
        return search(mid + 1, right)

    return search(0, len(a))


# O(n³) #
def sublists_3(a):
    sublist = [None] * 3
    for i in range(len(a) - 2):
        sublist[0] = a[i]
        for j in range(i + 1, len(a) - 1):
            sublist[1] = a[j]
            for k in range(j + 1, len(a)):
                sublist[2] = a[k]
                pass  # do something with sublist
                # print(sublist)


# O(n!) #
def permutations(a):

    def swap(i, j):
        perm[i], perm[j] = perm[j], perm[i]

    def get_perms(prefix_len):
        if prefix_len == len(perm) - 1:
            pass  # do something with perm
            # print(perm)
        else:
            for elem_index in range(prefix_len, len(perm)):
                swap(prefix_len, elem_index)
                get_perms(prefix_len + 1)
                swap(prefix_len, elem_index)

    perm = a.copy()
    get_perms(0)


# a = [4, 2, 1, 3]
# print('a =', a)
# merge_sort(a)
# print('merge_sort(a) ->', a)
# print("binary_search(a, 3) =", binary_search(a, 3))
# print("binary_search(a, 5) =", binary_search(a, 5))
# print('sublists_3(a):')
# sublists_3(a) # uncomment print(sublist) for this
# print('permutations(a):')
# permutations(a) # uncomment print(perm) for this
