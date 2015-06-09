# Use Python's string, hashlib and hmac libraries
import string
import hashlib
import hmac

# Elliptische Kurve secp256k1
# p : 256 bit prime number for secp256k1
p = 0xfffffffffffffffffffffffffffffffffffffffffffffffffffffffefffffc2f

# operations modulo p
def amp(x,y):
    return (x+y)%p

def mmp(x,y):
    return (x*y)%p

def smp(x,y):
    return amp(x,p-y)

# Extended Euclidean Algorithm, mod p
def eea(a,b):
    x, lastx, y, lasty = 0, 1, 1, 0
    while (b>0):
        q=a/b
        r=a%b
        a, b = b, r
        x, lastx = smp(lastx,mmp(q,x)), x
        y, lasty = smp(lasty,mmp(q,y)), y
    return (lastx,lasty)

# multiplicative inverse mod p
def imp(x):
    (u,v)=eea(p,x%p)
    return v

# Operation ("addition") der Elliptische Kurve Gruppe
# P is either a pair (x,y) or None (representing the zero point); same for Q
def addP(P,Q):
  if P==None:
      return Q
  else:
      if Q==None:
          return P
      else:
          (xP,yP)=P
          (xQ,yQ)=Q
          if xP==xQ:
              if amp(yP,yQ)==0:
                  print "sigh"
                  return None
              else:
                  s=mmp(imp(mmp(2,yP)),mmp(3,(mmp(xP,xP))))
                  xR=amp(mmp(s,s),mmp(p-2,xP))
                  yR=(p-amp(yP,mmp(s,smp(xR,xP))))%p
                  return (xR,yR)
          else:
              s=mmp(smp(yP,yQ),imp(xP-xQ))
              xR=smp(mmp(s,s),amp(xP,xQ))
              yR=(p-amp(yP,mmp(s,smp(xR,xP))))%p
              return (xR,yR)

# Skalare Multiplikation : int mal Punkt
def smulP(k,P):
    if k>0:
        Q=addP(P,P)
        R=smulP(k>>1,Q)
        if k%2==0:
            return R
        else:
            return addP(P,R)
    else:
        return None

# Skalar Mult by Base Punkt (secp256k1)
def point(priv):
    return smulP(priv,(0x79be667ef9dcbbac55a06295ce870b07029bfcdb2dce28d959f2815b16f81798,0x483ada7726a3c4655da4fbfc0e1108a8fd17b448a68554199c47d08ffb10d4b8))

# Gruppe Order "n"
groupord = 0xfffffffffffffffffffffffffffffffebaaedce6af48a03bbfd25e8cd0364141

# base58 representation
base58chars='123456789ABCDEFGHJKLMNPQRSTUVWXYZabcdefghijkmnopqrstuvwxyz'

def inttobase58(x,r=""):
    if x>0:
        return inttobase58(x/58,base58chars[x%58]+r)
    else:
        return r

def base58toint(x):
    try:
        r=0
        for i in range(len(x)):
            r=r*58+string.index(base58chars,x[i])
        return r
    except ValueError:
        raise ValueError("frombase58 given non base58 string: "+x)

def parse256(x):
    r=0
    for c in x:
        r=r*256+ord(c)
    return r

def serb(x,b):
    r=""
    for i in range(b):
        r=chr(x%256)+r
        x=x>>8
    return r

def ser256(x):
    return serb(x,32)

def ser32(x):
    return serb(x,4)

# generation of wifs and addresses for cryptocoins
def wif(priv,prefix):
    s1 = ""
    for i in range(32):
        s1 = chr(priv%256)+s1
        priv=priv>>8
    s1=prefix+s1
    h=hashlib.sha256(s1)
    s2=h.digest()
    h=hashlib.sha256(s2)
    s3=h.digest()
    return inttobase58(parse256(s1+s3[0:4]))

def wifc(priv,prefix):
    s1 = ""
    for i in range(32):
        s1 = chr(priv%256)+s1
        priv=priv>>8
    s1=prefix+s1+chr(1)
    h=hashlib.sha256(s1)
    s2=h.digest()
    h=hashlib.sha256(s2)
    s3=h.digest()
    return inttobase58(parse256(s1+s3[0:4]))

def btcwif(priv):
    return wif(priv,'\x80')

def btcwifc(priv):
    return wifc(priv,'\x80')

def ltcwif(priv):
    return wif(priv,'\xb0')

def drkwif(priv):
    return wif(priv,'\xcc')

def numnullchars(x):
    i=0
    while i<len(x) and x[i]=='\x00':
       i=i+1
    return i

def btcaddr(P):
    if P == None:
        raise ValueError("Nullpunkt not public key")
    else:
        (xP,yP) = P
        epub='\x04'+ser256(xP)+ser256(yP)
        h=hashlib.sha256(epub)
        s1=h.digest()
        h=hashlib.new('ripemd160')
        h.update(s1)
        s2=h.digest()
        h=hashlib.sha256('\x00'+s2)
        s3=h.digest()
        h=hashlib.sha256(s3)
        s4=h.digest()
        return '1'*(1+numnullchars(s2))+inttobase58(parse256(s2+s4[0:4]))

def btcaddrc(P):
    if P == None:
        raise ValueError("Nullpunkt not public key")
    else:
        (xP,yP) = P
        if (yP%2==0):
            epub='\x02'+ser256(xP)
        else:
            epub='\x03'+ser256(xP)
        h=hashlib.sha256(epub)
        s1=h.digest()
        h=hashlib.new('ripemd160')
        h.update(s1)
        s2=h.digest()
        h=hashlib.sha256('\x00'+s2)
        s3=h.digest()
        h=hashlib.sha256(s3)
        s4=h.digest()
        return '1'*(1+numnullchars(s2))+inttobase58(parse256(s2+s4[0:4]))

def addr(P,prefix):
    if P == None:
        raise ValueError("Nullpunkt not public key")
    else:
        (xP,yP) = P
        epub='\x04'+ser256(xP)+ser256(yP)
        h=hashlib.sha256(epub)
        s1=h.digest()
        h=hashlib.new('ripemd160')
        h.update(s1)
        s2=prefix+h.digest()
        h=hashlib.sha256(s2)
        s3=h.digest()
        h=hashlib.sha256(s3)
        s4=h.digest()
        return inttobase58(parse256(s2+s4[0:4]))

def ltcaddr(P):
    return addr(P,'\x30')

def drkaddr(P):
    return addr(P,'\x4c')

# BIP0032
def serP(P):
    if P == None:
        raise ValueError("Nullpunkt not public key")
    else:
        (xP,yP) = P
        if yP%2==0:
            return '\x02'+ser256(xP)
        else:
            return '\x03'+ser256(xP)

def hmacsha512(key,msg):
    h = hmac.new(key,msg,hashlib.sha512)
    return h.digest()

# master extended private key
def master(s):
    I = hmacsha512('Bitcoin seed',s)
    return (I[0:32],I[32:64])

# private child derivation
def ckdprivI(kpar,cpar,i):
    if (i>>31)%2==1: # use hardened derivation
        return hmacsha512(ser256(cpar),'\x00'+ser256(kpar)+ser32(i))
    else:
        return hmacsha512(ser256(cpar),serP(point(kpar))+ser32(i))

def ckdpriv(kpar,cpar,i):
    I = ckdprivI(kpar,cpar,i)
    IL, IR = I[0:32], I[32:64]
    pIL = parse256(IL)
    ki = (pIL + kpar) % groupord
    if pIL >= groupord or ki == 0:
        raise ValueError("Problem Child")
    else:
        return (ki,parse256(IR))

# public child derivation
def ckdpub(Kpar,cpar,i):
    if (i>>31)%2==1: # use hardened derivation
        raise ValueError("Cannot compute extended public key of hardened child")
    else:
        I = hmacsha512(ser256(cpar),serP(Kpar)+ser32(i))
        IL, IR = I[0:32], I[32:64]
        pIL = parse256(IL)
        Ki = addP(point(pIL),Kpar)
        if pIL >= groupord or Ki == None:
            raise ValueError("Problem Child")
        else:
            return (Ki,parse256(IR))

def harden(i):
    return (1<<31)+i

# paths (e.g., "0'/3/2'/9")
def parsepath(path):
    j=0
    r=[]
    while j<len(path):
        i=0
        cont=True
        while j<len(path) and cont:
            c=ord(path[j])
            if c >= 48 and c <= 57:
                i=10*i+(c-48)
                j=j+1
            elif c == 39:
                i=harden(i)
                j=j+1
                cont=False
                if j<len(path) and path[j]=="/":
                    j=j+1
            else:
                if c == 47:
                    j=j+1
                    cont=False
                else:
                    raise ValueError("Illformed Path")
        r.append(i)
    return r

# compute extended private key of a path
def ckdprivpath(kpar,cpar,path):
    for i in path:
        (kpar,cpar) = ckdpriv(kpar,cpar,i)
    return (kpar,cpar)

# compute extended public key of a path
def ckdpubpath(Kpar,cpar,path):
    for i in path:
        (Kpar,cpar) = ckdpub(Kpar,cpar,i)
    return (Kpar,cpar)

def postpath(ppath,k,K,c):
   if k==None:
      (K,c) = ckdpubpath(K,c,ppath)
      return (None,K,c)
   else:
      (k,c) = ckdprivpath(k,c,ppath)
      return (k,point(k),c)

def print_node_info(k,K,c):
   if k != None:
      print "priv "+inttobase58(k)+" "+inttobase58(c)
   if K != None:
      (xK,yK) = K
      print "pub "+inttobase58(xK)+" "+inttobase58(yK)+" "+inttobase58(c)
