"""
Design HashMap

Design a HashMap without using any built-in hash table libraries.
To be specific, your design should include these functions:

put(key, value) : Insert a (key, value) pair into the HashMap. If the value already exists in the HashMap, update the value.
get(key): Returns the value to which the specified key is mapped, or -1 if this map contains no mapping for the key.
remove(key) : Remove the mapping for the value key if this map contains the mapping for the key.

Example:
MyHashMap hashMap = new MyHashMap();
hashMap.put(1, 1);          
hashMap.put(2, 2);         
hashMap.get(1);            // returns 1
hashMap.get(3);            // returns -1 (not found)
hashMap.put(2, 1);          // update the existing value
hashMap.get(2);            // returns 1 
hashMap.remove(2);          // remove the mapping for 2
hashMap.get(2);            // returns -1 (not found) 

Note:
All keys and values will be in the range of [0, 1000000].
The number of operations will be in the range of [1, 10000].
Please do not use the built-in HashMap library.
"""


class MyHashMap:

    def __init__(self):
        """
        Initialize the data structure here.
        """
        self.l = [[] for _ in range(1000)]

    def put(self, key: int, value: int) -> None:
        """
        Value will always be non-negative.
        """
        i = (sum(map(lambda x: ord(x), key)))
        i %= 100  # Considering Bucket size as 100
        self.l[i] = value

    def get(self, key: int) -> int:
        """
        Returns the value to which the specified key is mapped, or -1 if this map contains no mapping for the key
        """
        i = (sum(map(lambda x: ord(x), key)))
        i %= 100
        if self.l[i] == []:
            return -1
        return self.l[i]

    def remove(self, key: int) -> None:
        """
        Removes the mapping of the specified value key if this map contains a mapping for the key
        """
        i = (sum(map(lambda x: ord(x), key)))
        i %= 100
        self.l[i] = []


# MyHashMap object will be instantiated and called as such:
obj = MyHashMap()
obj.put("Aa", 32)
print(obj.get("aA"))  # Should have returned -1 as keys are "unique"
# param_2 = obj.get(key)
# obj.remove(key)
