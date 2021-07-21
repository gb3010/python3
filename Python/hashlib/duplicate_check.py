In [26]: def print_hash(file):
    ...:     with open(file,'rb') as f:
    ...:         content = f.read()
    ...:     hash_method = hashlib.sha1()
    ...:     hash_method.update(content)
    ...:     return hash_method.hexdigest()



In [46]: for rootdir,childdirs,files in os.walk('test'):
    ...:     for f in files:
    ...:         path = os.path.join(rootdir,f)
    ...:         hashoutput = print_hash(path)
    ...:         #print(hashoutput)
    ...:         #hash_dict[hashoutput] = path
    ...:         if hashoutput in hash_dict and os.stat(path).st_ino != os.stat(hash_dict[hashoutput]).st_ino:
    ...:             print("%s is duplicate file of %s" % (path,hash_dict[hashoutput]))
    ...:         else:
    ...:              hash_dict[hashoutput] = path
    ...: 
    ...: 
    ...: 
    ...: 
    ...: 
test/c/1 is duplicate file of test/a/2
test/b/2 is duplicate file of test/a/1
