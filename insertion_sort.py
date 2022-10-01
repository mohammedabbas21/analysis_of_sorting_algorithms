# Python implementation of Insertion Sort
# Mohammed Abbas
# https://github.com/mohammedabbas21



from timeit import default_timer as timer

def insertion_sort(seq):
    for i in range(1, len(seq)):
        key = seq[i]
        low, up = 0, i
        while up > low:
            middle = (low + up) // 2
            if seq[middle] < key:
                low = middle + 1              
            else:
                up = middle
        seq[:] = seq[:low] + [key] + seq[low:i] + seq[i + 1:]


if __name__ == '__main__':

    time_taken = 0
    x = int(input("Enter number of trials : "))
    
    for n in range(1,x+1):
        with open("data/random.txt","r") as fileobj:
            list_to_sort = list(map(int, fileobj.readlines()))
            start = timer()
            insertion_sort(list_to_sort)
            current = timer()-start
            print(f"Running test {n} : {current:.2f} seconds")
            time_taken += current
    
    assert sorted(list_to_sort) == list_to_sort
    
    time_taken /= x
    print(f"Insertion sort: average time = {time_taken:.2f} seconds")
 
