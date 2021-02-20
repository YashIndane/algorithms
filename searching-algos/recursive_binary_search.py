def b_s(arr , v):
    
       current_head = len(arr)//2
 
       #this is the base condition to terminate 
       if arr[current_head] == v:
          return 'Found'

       #this is the base condition to terminate
       elif len(arr) == 1 and arr[current_head] != v:
          return  'Not Found'

       elif arr[current_head] > v:
          arr = arr[:current_head]
          current_head = len(arr)//2

       elif arr[current_head] < v:
          arr = arr[current_head + 1:]
          current_head = len(arr)//2


       return b_s(arr , v)
       
print(b_s([2,3,5,6,9,9,9,10,10,12,12,34,55,58,67,344,345] , 345))
