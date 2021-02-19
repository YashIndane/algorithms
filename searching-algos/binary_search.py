def b_s(arr , v):
    
    current_head = len(arr)//2
    for _ in range(len(arr)):
 
       if arr[current_head] == v:
          return 'Found'

       elif len(arr) == 1 and arr[current_head] != v:
          return  'Not Found'

       elif arr[current_head] > v:
          arr = arr[:current_head]
          current_head = len(arr)//2

       elif arr[current_head] < v:
          arr = arr[current_head + 1:]
          current_head = len(arr)//2
       
print(b_s([2,3,5,6,9,10,12,12] , 12))          

        
       
           
     

 
