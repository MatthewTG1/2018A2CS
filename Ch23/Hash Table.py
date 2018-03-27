def Hash(self,key):
    for i in range(10):
        adr = self.key % 11
    return adr

def insert(NewRecord):
    HashTable = []
    index = Hash(NewRecord.key)
    while HashTable[index] != None:
        index += 1
        if index > 10:
            index = 1
    HashTable[index] = NewRecord

print(Hash(5))
        
    
