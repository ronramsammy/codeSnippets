#Iterative Binary Search

def binarySearch(arr,left,right,x):
    while(left <= right):
        mid = left + (right-left)//2;
        
        if arr[mid] == x:
            return mid
        elif arr[mid] < x:
            left = mid+1
        else:
            right = mid-1
            
    return -1


    # Test array 
arr = [ 2, 3, 4, 10, 40 ] 
x = 40
  
# Function call 
result = binarySearch(arr, 0, len(arr)-1, x) 
  
if result != -1: 
    print ("Element is present at index %d" % result)
else: 
    print ("Element is not present in array")