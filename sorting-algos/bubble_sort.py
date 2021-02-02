def b_s(arr):
   
   swap = False  
 
   #runs
   for i in range(1 , len(arr)): 
       
       for j in range(len(arr) - i):

           if arr[j] > arr[j+1] : 
                  arr[j+1] , arr[j] = arr[j] , arr[j+1]
                  swap = True

       if not swap :
            return 'already sorted'

   return arr


print(b_s([1,2,4,5,6]))





           
          
            
       
        
