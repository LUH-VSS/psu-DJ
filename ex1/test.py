import hashlib

groupid = b"83209596"

print(hashlib.sha224(groupid).hexdigest())
