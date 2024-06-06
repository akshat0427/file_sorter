import os

import shutil



files = []  # stores all the unique file types
dirs = {} # list of files to their corresponding file type

c =0

for i in os.listdir():
    
    files.append(i.split('.')[1])   


for i in set(files): ''' creates a new folder for every unique file type (ie- .jpg , .txt)   '''
    # os.mkdir(f'./{i}')
    
    l2 = []
    
    for j in os.listdir():
        
        if j.split('.')[1] == i:
            
            
            # print(i, j)
            l2.append(j)
        
        else:
            pass
        dirs[i] = l2
    os.makedirs(f"./{i}")
    

# for i in set(l):

    

for j in dirs.keys():    ''' moves the files of simillar type to their folder  '''
    # print(j)
    for i in dirs[j]:
        print(i)
        
        original = f'./{i}'
        target = f'./{j}/'

        shutil.move(original, target)
    print('done')
        
