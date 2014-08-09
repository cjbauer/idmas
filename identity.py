import time
import config
import names
import crypto

nationalitiessum = sum(map((lambda x: x[1]),config.nationalities))

def getidentity(k,c):
   (k0,_) = crypto.ckdpriv(k,c,0)
   (k1,_) = crypto.ckdpriv(k,c,1)
   (k2,_) = crypto.ckdpriv(k,c,2)
   (k3,_) = crypto.ckdpriv(k,c,3)
   (k4,_) = crypto.ckdpriv(k,c,4)
   (k5,_) = crypto.ckdpriv(k,c,5)
   gmale=k0%(config.gender_male+config.gender_female) < config.gender_male
   gp='M'
   if not gmale:
      gp='F'
   natn=k1%nationalitiessum
   nc=0
   nat=None
   for na in config.nationalities:
      nc=nc+na[1]
      if nc>natn and nat == None:
         nat=na[0]
   unixtimebday=config.birthday_lowerbound+(k2%(config.birthday_upperbound-config.birthday_lowerbound))
   bday=time.gmtime(unixtimebday)
   age=(int(time.time()) - unixtimebday)/31536000
   firstnames=config.firstnames[gp+nat]
   lastnames=config.lastnames[nat]
   numfirstnames=len(firstnames)
   numlastnames=len(lastnames)
   fname = firstnames[k3%numfirstnames]
   lname = lastnames[k5%numlastnames]
   if nat in config.twosurnames:
      mname = lastnames[k4%numlastnames]
      if lname==mname:
         mname=lastnames[(k4 >> 64)%numlastnames] # to make repeated names less likely
   else:
      mname = firstnames[k4%numfirstnames]
      if fname==mname:
         mname=firstnames[(k4 >> 64)%numfirstnames] # to make repeated names less likely
   return(gmale,nat,bday,age,fname,mname,lname)

def reportidentity(k,c):
   (gmale,nat,bday,age,fname,mname,lname)=getidentity(k,c)
   print "Name: "+fname+" "+mname+" "+lname
   if gmale:
      print "Gender: Male"
   else:
      print "Gender: Female"
   print "Nationality: "+nat
   print "Birthday: "+time.strftime("%B %d, %Y",bday)
   print "Age: "+str(age)
