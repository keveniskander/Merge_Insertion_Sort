# Author: Keven Iskander
# ID: 160634540
# Course: CP312

a = []


# When entering level please note that all trees begin at a root node. For the sake of this recursion the root is at level 1.
n = int((input("Enter tree_level: ")))
n = n-1

elements = str(input("Enter List A: "))
elements = elements.split()
a = [int(i) for i in elements]
#print(a)

g = 0 
m = g-n

print()

# The original merge sort algorithm has been taken from https://www.geeksforgeeks.org/merge-sort/ and modified
def merge_insertion_Sort(arr, k): 

    if k == 0:
        insertionSort(arr)
        print("Calling insertion Sort on: ", arr)

    if k>0: 
        mid = len(arr)//2 #Finding the mid of the array 
        L = arr[:mid] # Dividing the array elements  
        R = arr[mid:] # into 2 halves 

        if k == 1:
            insertionSort(L)
            insertionSort(R)
            print("Calling insertion Sort on: ", L)
            print("Calling insertion Sort on: ", R)
        
        else:
            merge_insertion_Sort(L,k-1) # Sorting the first half 
            merge_insertion_Sort(R,k-1) # Sorting the second half 
        
        
  
        i = j = k = 0

          
        # Copy data to temp arrays L[] and R[] 
        while i < len(L) and j < len(R): 
            if L[i] < R[j]: 
                arr[k] = L[i] 
                i+=1
            else: 
                arr[k] = R[j] 
                j+=1
            k+=1
          
        # Checking if any element was left 
        while i < len(L): 
            arr[k] = L[i] 
            i+=1
            k+=1
          
        while j < len(R): 
            arr[k] = R[j] 
            j+=1
            k+=1
          


def insertionSort(a): 
 
    for i in range(1, len(a)): 
  
        temp = a[i] 
        k = i-1
        while k >= 0 and temp < a[k] : 
                a[k + 1] = a[k] 
                k -= 1
        a[k + 1] = temp


def printList(a): 
    print()
    print("Sorted list:", end = " ")
    for i in range(len(a)):         
        print(a[i],end=" ") 
    print() 
  

merge_insertion_Sort(a,n)
printList(a)
