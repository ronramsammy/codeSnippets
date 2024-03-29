# This function takes last element as pivot, places 
# the pivot element at its correct position in sorted 
# array, and places all smaller (smaller than pivot) 
# to left of pivot and all greater elements to right 
# of pivot 
def partition(arr,low,high): 
    i = ( low-1 )         # index of smaller element 
    pivot = arr[high]     # pivot 
  
    for j in range(low , high): 
  
        # If current element is smaller than or 
        # equal to pivot 
        if   arr[j] <= pivot: 
          
            # increment index of smaller element 
            i+=1
            arr[i],arr[j] = arr[j],arr[i] 
  
#    arr[i+1],arr[high] = arr[high],arr[i+1] 
    arr[i+1],arr[high] = pivot,arr[i+1] 
    return ( i+1 ) 
  
# The main function that implements QuickSort 
# arr[] --> Array to be sorted, 
# low  --> Starting index, 
# high  --> Ending index 
  
# Function to do Quick sort 
def _quickSort(arr,low,high): 
    if low < high: 
  
        # pi is partitioning index, arr[p] is now 
        # at right place 
        pi = partition(arr,low,high) 
  
        # Separately sort elements before 
        # partition and after partition 
        _quickSort(arr, low, pi-1) 
        _quickSort(arr, pi+1, high)
        
def quickSort(items):
    _quickSort(items, 0, len(items)-1)
            
arr = [10, 7, 8, 9, 1, 5] 
quickSort(arr) 
print ("Sorted array is:") 
print(arr) 
    
