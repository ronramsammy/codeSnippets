# Returns index of x in arr if present, else -1 
def _binarySearchR (arr, l, r, x): 
  
    # Check base case 
    if r >= l: 
  
        mid = l + (r - l)//2
  
        # If element is present at the middle itself 
        if arr[mid] == x: 
            return mid 
          
        # If element is smaller than mid, then it can only 
        # be present in left subarray 
        elif arr[mid] > x: 
            return _binarySearchR(arr, l, mid-1, x) 
  
        # Else the element can only be present in right subarray 
        else: 
            return _binarySearchR(arr, mid+1, r, x) 
  
    else: 
        # Element is not present in the array 
        return -1

def binarySearchR(arr,x):
    res =_binarySearchR(arr,0,len(arr)-1,x)
    return res

# Test array 
arr = [ 2, 3, 4, 10, 40 ] 
x = 4
  
# Function call 
result = binarySearchR(arr, x) 
  
if result != -1: 
    print ("Element is present at index %d" % result )
else: 
    print ("Element is not present in array"    )