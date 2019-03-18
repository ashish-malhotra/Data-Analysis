import numpy as np

def WaterStoredInPlatform(platform):
    save = 0
    print(platform)
    flag = False
    for i in range(platform.shape[1]):
        if i == 0 or i == platform.shape[1]-1:
            continue

        temp = platform[:,i] 
        
        if flag:
            flag = False
            continue
        
        min_val = min(temp[0],temp[-1])
        max_val = min(temp[0],temp[-1])
        temp_save=0
        for j in range(len(temp)):     

            if j == 0 or j==len(temp)-1 or temp[j+1]==0 or temp[j]==0 or temp[j-1]==0: # filter out border cases
                continue
            
            if max_val-temp[j] < 0:
                continue
            
            temp_save+=max_val-temp[j]
            
        save+=temp_save    
#        print(temp_save)    
        if 0 in temp: 
            flag = True


    print('Final units saved: '+str(save))

   

    

    
platform1 = np.array([[2,2,2],[2,2,2],[2,2,2]])
platform2 = np.array([[2,2,2,2],[2,1,2,1],[2,2,2,1]])
platform3 = np.array([[3,3,3,3,3,3],[3,1,2,3,1,3],[3,1,2,3,1,3],[3,3,3,1,3,3]])
platform4 = np.array([[3,3,3,3,5,3],[3,0,2,3,1,3],[3,1,2,3,1,3],[3,3,3,1,3,3]])
platform5 = np.array([[5,5,5,5,5],[9,1,1,1,5],[5,1,5,1,5],[5,1,1,1,5],[5,5,5,5,5]])

WaterStoredInPlatform(platform1)

#print(platform.shape)
