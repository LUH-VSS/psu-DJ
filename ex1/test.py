import hashlib

groupid = b"12349876"
userone = "8320"

print(hashlib.sha224(groupid).hexdigest())
print(userone)
