import hashlib

groupid = b"12349876"
userone = "8320"
usertwo = "9596"

print(hashlib.sha224(groupid).hexdigest())
print(userone)
print(usertwo)
