#!/usr/local/bin/python3
import hashlib

def print_hash(file):
    with open(file,'r') as f:
        f_content = f.read()
        
hash_var  = haslib.sha1()
enc_content = f_content.encode()
hash_var.update(enc_content)
print(hash_var.hexdigest())
