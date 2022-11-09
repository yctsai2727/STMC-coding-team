#myFiles = #['File1','File2','File3'] # 10000 entries

myFiles = [f'File{i+1}' for i in range(100)] # Make 100 files

for i in range(len(myFiles)):
    file = myFiles[i]
    # Processing file
    if i % 20 == 0:
        print(f'The {i}th file have been processed. Name is: {myFiles[i]}')
