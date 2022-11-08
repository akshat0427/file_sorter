import os

import shutil



l = []
d = {}
c =0

for i in os.listdir():
    
    l.append(i.split('.')[1])   
    
for i in set(l):
    # os.mkdir(f'./{i}')
    
    l2 = []
    
    for j in os.listdir():
        
        if j.split('.')[1] == i:
            
            
            # print(i, j)
            l2.append(j)
        
        else:
            pass
        d[i] = l2
    os.makedirs(f"./{i}")
    

# for i in set(l):

    

for j in d.keys():
    # print(j)
    for i in d[j]:
        print(i)
        
        original = f'./{i}'
        target = f'./{j}/'

        shutil.move(original, target)
    print('done')
        