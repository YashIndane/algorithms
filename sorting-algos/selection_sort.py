def s_s(arr):
  
       for i in range(len(arr) - 1):
            
            min = i

            for j in range(i , len(arr) - 1):
                
                   if arr[j+1] < arr[min] :
                        min = j+1
                        
            if arr[i] != arr[min] :
                    arr[i] , arr[min] =  arr[min] , arr[i]
       
       return arr


print(s_s([1,2,3,4,5,6]))

                   
 
                    

            

 
