def i_s(arr):

    for i in range(1 , len(arr)):
          
        cur = arr[i]
         
        while (i > 0 and arr[i - 1] > cur) :
             
            arr[i] = arr[i - 1]
            arr[i - 1] = cur

            i -= 1

    return arr


print(i_s([4,6,3,6,9,7,6,8,5,4,7,0,7,6,6,8,5,6,9,7,0,5,8,6]))





