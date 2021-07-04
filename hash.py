import hashlib as hl

def md5hash(text):
    res = hl.md5(text.encode())
    print("this is md5",res.hexdigest())

def sha256hash(text):
    res = hl.256(text.encode())
    print("this is sha256")

def sha512hash(text):
    res = hl.sha512(text.encode())
    print("this is sha512")

def sha384hash(text):
    print("sha384")

def sha1hash(text,iter):
    print("this is sha1")

inptext = str(input("Enter Text :-"))
choice = input("""
1. MD5
2. Sha256
3. Sha512
4. Sha384
5. Sha1 with sal

Enter Your Choice:-""")
md5hash(inptext)

