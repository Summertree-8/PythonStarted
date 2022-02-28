def min_heapify(array, i):
    left = 2*i + 1
    right = 2*i + 2
    length = len(array) - 1
    smallest = i

    if left <= length and array[smallest] > array[left]:
        smallest = left
    if right <= length and array[smallest] > array[right]:
        smallest = right
    if smallest != i: #hrap changed
        array[i], array[smallest] = array[smallest], array[i] #exchange
        min_heapify(array, smallest)

def build_min_heap(array):
    for i in reversed(range(len(array)//2)):  #after n/2+1 is leaf
        min_heapify(array,i)