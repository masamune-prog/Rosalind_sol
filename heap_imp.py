#  1 3 5 7 2
#  0 1 2 3 4
# max heap
#largest_node is the root

def heapify(arr,n,i):
    root = i
    left_child = 2 * i + 1
    right_child = 2 * i + 2
    # If left child is larger than root
    if left_child < n and arr[left_child] > arr[root]:
        root = left_child

    # If right child is larger than largest so far
    if right_child < n and arr[right_child] > arr[root]:
        root = right_child

    #if largest not root
    if root != i:
        arr[i],arr[root] = arr[root],arr[i]
        #arr[root] = arr[i]
        heapify(arr,n,root)
def buildHeap(arr, n):

    # Index of last non-leaf node
    startIdx = n // 2 - 1;

    # Perform reverse level order traversal
    # from last non-leaf node and heapify
    # each node
    for i in range(startIdx, -1, -1):
        heapify(arr,n,i)
if __name__ == '__main__':
    with open("test.txt", "r") as f:
        n = int(f.readline().strip())
        arr = [int(i) for i in f.readline().strip().split()]
    buildHeap(arr, n)
    for i in range(n):
        print(arr[i], end = " ")
