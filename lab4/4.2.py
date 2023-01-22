def swap(a, i, j):
    a[i], a[j] = a[j], a[i]


# HEAP-SORT #
def heap_sort(a):

    def sift_up(heap, kid):
        dad = (kid + 1) // 2 - 1
        while dad >= 0 and heap[dad] > heap[kid]:
            swap(heap, dad, kid)
            kid = dad
            dad = (kid + 1) // 2 - 1

    def to_heap():
        heap = []
        for i in range(len(a)):
            heap.append(a[i])
            sift_up(heap, i)
        return heap

    def sift_down(dad):
        kid1 = dad * 2 + 1
        kid2 = dad * 2 + 2
        if kid2 < len(heap) and heap[kid2] < heap[kid1]:
            min_kid = kid2
        elif kid1 < len(heap):
            min_kid = kid1
        else:
            min_kid = None
        if min_kid and heap[dad] > heap[min_kid]:
            swap(heap, dad, min_kid)
            sift_down(min_kid)

    def heap_min():
        swap(heap, 0, -1)
        min = heap.pop(-1)
        sift_down(0)
        return min

    heap = to_heap()
    for i in range(len(a)):
        a[i] = heap_min()


# BUCKET-SORT #
def bucket_sort(a):

    def insertion_sort(a):
        for i in range(len(a)):
            j = i
            while j > 0 and a[j] < a[j - 1]:
                swap(a, j, j - 1)
                j -= 1

    MIN, MAX, N = min(a), max(a) + .1, len(a)
    buckets = [[] for _ in range(N)]
    for x in a:
        buckets[int(N * (x - MIN) / (MAX - MIN))].append(x)
    k = 0
    for bucket in buckets:
        insertion_sort(bucket)
        for i in range(len(bucket)):
            a[k] = bucket[i]
            k += 1


# import random
# a = [random.randint(-1000, 1000) for _ in range(1000)]
# b = [random.randint(-1000, 1000) for _ in range(1000)]
# heap_sort(a)
# bucket_sort(b)
# print(a, b, sep='\n')
