import json

# This function converts space-separated string to list
def stringToList(stringToConvert): 
    newList = stringToConvert.split()
    tempLst = []
    tempStr = ""
    x = 0
    for i in newList[5]: # Make the ports as individual values instead of one string
        x = x + 1
        if i == ",":
            tempLst.extend([tempStr])
            tempStr = ""
            continue
        tempStr = tempStr + i
        if x == len(newList[5]):
            tempLst.extend([tempStr])
            tempStr = ""
    newList[5] = tempLst
    return newList

# json output file - create and write
def createJsonFile(folderPath, nameAndPorts):
    with open(folderPath + "\\" +'output.json', 'w') as f:
        json.dump(nameAndPorts, f)
    f.close()
    print("Done!")
    
# This function creates a list of the output results
def CreateOutputList(folderPath, fileName):
    fullFilePath = folderPath + "\\" + fileName # Creates the full file name
    
    # Preparing the name-to-port list for the final json output
    nameAndPorts = {}
    with open(fullFilePath) as f: 
        lines = f.readlines()
    for line in lines:
        tempVar = stringToList(line)
        nameAndPorts[tempVar[1]] = (tempVar[5])  
    f.close()
    (k := next(iter(nameAndPorts)), nameAndPorts.pop(k)) #delete the first key-item
    createJsonFile(folderPath, nameAndPorts) # Creates the final json file
    
######### Main script #########
CreateOutputList("C:\\Users\\yorap\\Downloads\\Amdocs", "input.txt") # enter 2 arguments here: path and file name.
