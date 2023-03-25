import hashlib

def hash_function(data):
    hash_object = hashlib.md5(data.encode())
    hex_dig = hash_object.hexdigest()
    print(hex_dig)


hash_function("holaa12")
