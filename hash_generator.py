import hashlib

def sha256_gen(input_data):
    sha256_hash = hashlib.sha256()
    sha256_hash.update(input_data.encode('utf-8'))
    return sha256_hash.hexdigest()

data = "Hello, world!"
hash_result = sha256_gen(data)
print(f"SHA-256 of '{data}' is: {hash_result}")