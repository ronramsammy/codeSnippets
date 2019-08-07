# Returns index of x in arr if present, else -1 

def binarySearchR(arr,x):
    res =  _binarySearchR(arr,0,len(arr)-1,x)
    print(f"res={res}")
    return res


def _binarySearchR(arr, left, right, x ):
    print (f"checking array {arr[left:right]}")
    if( right >= left ):
        mid = left + (right-left)//2
        print(f"mid = {mid}")
        
        if(arr[mid]==x):
            print(f"returning index(mid) = {mid}")
            return mid
        elif( x<arr[mid]):
            return _binarySearchR(arr, left, mid-1, x)
        else:
            return _binarySearchR(arr, mid+1, right, x)
            
    else:
        return -1
        



# Test array 
arr = [ 2, 3, 4, 10, 40 ] 
x = 99
  
# Function call 
result = _binarySearchR(arr,0, len(arr)-1, x) 
  
if result != -1: 
    print ("Element is present at index %d" % result )
else: 
    print ("Element is not present in array"    )