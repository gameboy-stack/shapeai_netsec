import hashlib as hl

def md5hash(text):
    res = hl.md5(text.encode())
    print("The MD5 Hash value for given text is : {}".format(res.hexdigest()))

def sha256hash(text):
    res = hl.sha256(text.encode())
    print("The SHA256 Hash value for given text is : {}".format(res.hexdigest()))

def sha512hash(text):
    res = hl.sha512(text.encode())
    print("The SHA512 Hash value for given text is : {}".format(res.hexdigest()))

def sha384hash(text):
    res = hl.sha384(text.encode())
    print("The SHA384 Hash value for given text is : {}".format(res.hexdigest()))

def sha1hashnsalting(res,iter,salttext):

    res = ''.join([(lambda a,b: b+salttext if(a%2!=0) else b)(i,t) for i,t in enumerate(res)])

    for i in range(iter):
        res = hl.sha1(res.encode()).hexdigest()

    print("The Result Hash value is : {}".format(res))

inptext = str(input("Enter Text :- "))
choice = str(input("""
1. MD5
2. Sha256
3. Sha512
4. Sha384
5. Sha1 with sal
Enter Your Choice :- """))

if(choice=="1"):
    md5hash(inptext)

elif(choice=="2"):
    sha256hash(inptext)

elif(choice=="3"):
    sha512hash(inptext)

elif(choice=="4"):
    sha384hash(inptext)

else:
    salting_text = input("Enter salting text :- ")
    iterinp = int(input("Enter no of iteration to be performed :- "))
    sha1hashnsalting(inptext,iterinp,salting_text)

