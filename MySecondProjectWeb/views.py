from django.shortcuts import render
import time
import mysql.connector
from django.core.files.storage import FileSystemStorage

# Create your views here.
def index(request):
    return render(request,'index.html')
def login(request):
    return render(request,'login.html')
def index(request):
    return render(request,'index.html')

def register(request):
    return render(request,'register.html')
def loginhandler(request):
    a=request.GET.get("uname")
    b=request.GET.get("psd")
    mydb=mysql.connector.connect(host='localhost',user='root',password='',database='idlelinctusdb')
    mycursor=mydb.cursor()
    q="select * from user where username='"+a+"' and password='"+b+"'";
    print(q)
    mycursor.execute(q)
    row=mycursor.fetchone()
    mydb.close()
    if row != None :
      request.session['sname']=row[1]
      request.session['suno']=row[0]
      
      return render(request,'user.html',{'dname':request.session['sname']})
    else :
      return render(request,'login.html',{'dmsg':'Invalid Username or Password'})  

def viewuserprofile(request):
    id=request.session['suno']
    mydb=mysql.connector.connect(host='localhost',user='root',password='',database='idlelinctusdb')
    mycursor=mydb.cursor()
    q="select * from user where uno="+str(id)
    mycursor.execute(q)
    row=mycursor.fetchone()
    mydb.close()
    return render(request,'viewuserprofile.html',{'dname':request.session['sname'],'drow':row})

def updateuserprofile(request):
    id=request.session['suno']
    mydb=mysql.connector.connect(host='localhost',user='root',password='',database='idlelinctusdb')
    mycursor=mydb.cursor()
    q="select * from user where uno="+str(id)
    mycursor.execute(q)
    row=mycursor.fetchone()
    mydb.close()
    return render(request,'updateuserprofile.html',{'dname':request.session['sname'],'drow':row})

def uhome(request):
    return render(request,'user.html',{'dname':request.session['sname']})

def registerhandler(request):
    b=request.GET.get("nm")
    c=request.GET.get("g")
    d=request.GET.get("dob")
    e=request.GET.get("ph")
    f=request.GET.get("e")
    g=request.GET.get("unm")
    h=request.GET.get("pass")
    mydb=mysql.connector.connect(host='localhost',user='root',password='',database='idlelinctusdb')
    mycursor=mydb.cursor()
    q="INSERT INTO `user`(`uname`, `ugender`, `udob`, `uphone`, `uemail`, `username`, `password`) VALUES ('"+b+"','"+c+"','"+d+"','"+e+"','"+f+"','"+g+"','"+h+"')"
    mycursor.execute(q)
    mydb.commit()
    mydb.close()
    return render(request,'register.html',{'dmsg':'Registered successfully !'})

def updateuserprofilehandler(request):
    id=request.session['suno']
    b=request.GET.get("p")
    c=request.GET.get("e")
    d=request.GET.get("ps")
    mydb=mysql.connector.connect(host='localhost',user='root',password='',database='idlelinctusdb')
    mycursor=mydb.cursor()
    q="update user set uphone='"+b+"',uemail='"+c+"',password='"+d+"' where uno= "+str(id)
    mycursor.execute(q)
    mydb.commit()   
    row=mycursor.fetchone()
    mydb.close()
    return updateuserprofile(request)




def sellerlogin(request):
    return render(request,'sellerlogin.html')

def sellerregister(request):
    return render(request,'sellerregister.html')

def sellerloginhandler(request):
    a=request.GET.get("uname")
    b=request.GET.get("psd")
    mydb=mysql.connector.connect(host='localhost',user='root',password='',database='idlelinctusdb')
    mycursor=mydb.cursor()
    q="select * from consumer where username='"+a+"' and password='"+b+"'";
    print(q)
    mycursor.execute(q)
    row=mycursor.fetchone()
    mydb.close()
    if row != None :
      request.session['ssname']=row[1]
      request.session['ssuno']=row[0]
      request.session['sstatus']=row[8]
      if request.session['sstatus']=="Approved" :
       return render(request,'seller.html',{'dname':request.session['ssname']})
      else :
       return render(request,'sellerlogin.html',{'dmsg':'you are not approved'})
  
    else :
      return render(request,'sellerlogin.html',{'dmsg':'Invalid Username or Password'})
    
def sellerregisterhandler(request):
    b=request.GET.get("nm")
    c=request.GET.get("g")
    d=request.GET.get("dob")
    e=request.GET.get("ph")
    f=request.GET.get("e")
    g=request.GET.get("unm")
    h=request.GET.get("pass")
    mydb=mysql.connector.connect(host='localhost',user='root',password='',database='idlelinctusdb')
    mycursor=mydb.cursor()
    q="INSERT INTO consumer (cname, gender, dob, phone, email, username, password) VALUES ('"+b+"','"+c+"','"+d+"','"+e+"','"+f+"','"+g+"','"+h+"')"
    mycursor.execute(q)
    print(q)
    mydb.commit()
    mydb.close()
    return render(request,'sellerregister.html',{'dmsg':'Registered successfully !'})

def viewsellerprofile(request):
    id=request.session['ssuno']
    mydb=mysql.connector.connect(host='localhost',user='root',password='',database='idlelinctusdb')
    mycursor=mydb.cursor()
    q="select * from consumer where cno="+str(id)
    mycursor.execute(q)
    row=mycursor.fetchone()
    mydb.close()
    return render(request,'viewsellerprofile.html',{'dname':request.session['ssname'],'drow':row})



def updatesellerprofile(request):
    id=request.session['ssuno']
    mydb=mysql.connector.connect(host='localhost',user='root',password='',database='idlelinctusdb')
    mycursor=mydb.cursor()
    q="select * from consumer where cno="+str(id)
    mycursor.execute(q)
    row=mycursor.fetchone()
    mydb.close()
    return render(request,'updatesellerprofile.html',{'dname':request.session['ssname'],'drow':row})


def shome(request):
    return render(request,'seller.html',{'dname':request.session['ssname']})

def updatesellerprofilehandler(request):
    id=request.session['ssuno']
    b=request.GET.get("p")
    c=request.GET.get("e")
    d=request.GET.get("ps")
    mydb=mysql.connector.connect(host='localhost',user='root',password='',database='idlelinctusdb')
    mycursor=mydb.cursor()
    q="update consumer set phone='"+b+"',email='"+c+"',password='"+d+"' where cno= "+str(id)
    mycursor.execute(q)
    mydb.commit()   
    row=mycursor.fetchone()
    mydb.close()
    return viewsellerprofile(request)



def adminlogin(request):
    return render(request,'adminlogin.html')


def adminloginhandler(request):
    a=request.GET.get("uname")
    b=request.GET.get("psd")
    if a=="admin" and b=="admin" :
      return render(request,'admin.html')
    else :
      return render(request,'adminlogin.html',{'dmsg':'invalid username or password'})  

def viewuser(request):
    mydb=mysql.connector.connect(host='localhost',user='root',password='',database='idlelinctusdb')
    mycursor=mydb.cursor()
    q="select * from user ";
    print(q)
    mycursor.execute(q)
    row=mycursor.fetchall()
    mydb.close()
    if row != None :
     return render(request,'viewuser.html',{'drow':row})
    
    
def viewseller(request):
    mydb=mysql.connector.connect(host='localhost',user='root',password='',database='idlelinctusdb')
    mycursor=mydb.cursor()
    q="select * from consumer ";
    print(q)
    mycursor.execute(q)
    row=mycursor.fetchall()
    mydb.close()
    if row != None :
     return render(request,'viewseller.html',{'drow':row})


def ahome(request):
    return render(request,'admin.html')


def deleteuserhandler(request):
    a=request.GET.get("selectedid")
    mydb=mysql.connector.connect(host='localhost',user='root',password='',database='idlelinctusdb')
    mycursor=mydb.cursor()
    q="delete from user where uno="+str(a)
    print(q)
    mycursor.execute(q)
    mydb.commit()
    mydb.close()
    return viewuser(request)


def deletesellerhandler(request):
    a=request.GET.get("selectedid")
    mydb=mysql.connector.connect(host='localhost',user='root',password='',database='idlelinctusdb')
    mycursor=mydb.cursor()
    q="delete from consumer where cno="+str(a)
    print(q)
    mycursor.execute(q)
    mydb.commit()
    mydb.close()
    return viewseller(request)


def adminsellerapprovehandler(request):
    a=request.GET.get("sellerapprovedid")
    mydb=mysql.connector.connect(host='localhost',user='root',password='',database='idlelinctusdb')
    mycursor=mydb.cursor()
    q="update consumer set status='Approved' where cno="+str(a)
    print(q)
    mycursor.execute(q)
    mydb.commit()
    mydb.close()
    return viewseller(request)



def productdetail(request):
    mydb=mysql.connector.connect(host='localhost',user='root',password='',database='idlelinctusdb')
    mycursor=mydb.cursor()
    q="select * from medicine where status='Approved'"
    mycursor.execute(q)
    row=mycursor.fetchall()
    mydb.close()
    return render(request,'productdetail.html',{'dname':request.session['sname'],'drow':row})




def userbuyrequesthandler(request):
    b=request.GET.get("selectedpid")
    c=request.GET.get("selectedpname")
    d=request.GET.get("selectedpspec")
    e=request.GET.get("selectedprice")
    f=request.GET.get("selectedsellerid")
    g=request.GET.get("selectedsellername")
    h=request.session['sname']
    i=request.session['suno']
    tt=time.localtime(time.time())
    j=time.strftime("%b-%d-%y",tt)

    mydb=mysql.connector.connect(host='localhost',user='root',password='',database='idlelinctusdb')
    mycursor=mydb.cursor()
    q="INSERT INTO request( medicineId,medicinename, exdate, price, consumerid, consumername, buyerid, buyername, date ) VALUES ('"+str(b)+"','"+c+"','"+d+"','"+e+"','"+str(f)+"','"+g+"','"+str(i)+"','"+h+"','"+j+"')"
    mycursor.execute(q)
    print(q)
    mydb.commit()
    mydb.close()
    return useruploadpriscription(request)



def usertrackorder(request):
    a=request.session['suno']
    mydb=mysql.connector.connect(host='localhost',user='root',password='',database='idlelinctusdb')
    mycursor=mydb.cursor()
    q="select * from  request where buyerid="+str(a) ;
    print(q)
    mycursor.execute(q)
    row=mycursor.fetchall()
    mydb.close()
    if row != None :
     return render(request,'userordertrack.html',{'dname':request.session['sname'],'drow':row})


def sellerviewproductlist(request):
    a=request.session['ssuno']
    mydb=mysql.connector.connect(host='localhost',user='root',password='',database='idlelinctusdb')
    mycursor=mydb.cursor()
    q="select * from medicine where consumerid="+str(a) ;
    print(q)
    mycursor.execute(q)
    row=mycursor.fetchall()
    mydb.close()
    if row != None :
     return render(request,'sellerviewproduct.html',{'dname':request.session['ssname'],'drow':row})


def adminviewproduct(request):
   
    mydb=mysql.connector.connect(host='localhost',user='root',password='',database='idlelinctusdb')
    mycursor=mydb.cursor()
    q="select * from medicine " ;
    print(q)
    mycursor.execute(q)
    row=mycursor.fetchall()
    mydb.close()
    if row != None :
     return render(request,'adminviewproduct.html',{'drow':row})




def adminproductapprovehandler(request):
    a=request.GET.get("productapprovedid")
    mydb=mysql.connector.connect(host='localhost',user='root',password='',database='idlelinctusdb')
    mycursor=mydb.cursor()
    q="update medicine set status='Approved' where mno="+str(a)
    print(q)
    mycursor.execute(q)
    mydb.commit()
    mydb.close()
    return adminviewproduct(request)


def sellerbuyrequest(request):
    
    mydb=mysql.connector.connect(host='localhost',user='root',password='',database='idlelinctusdb')
    mycursor=mydb.cursor()
    q="select * from request ";
    print(q)
    mycursor.execute(q)
    row=mycursor.fetchall()
    mydb.close()
    if row != None :
     return render(request,'sellerbuyrequest.html',{'drow':row})

def sellerproductapprovehandler(request):
    a=request.GET.get("sellerproductapprovedid")
    mydb=mysql.connector.connect(host='localhost',user='root',password='',database='idlelinctusdb')
    mycursor=mydb.cursor()
    q="update request set status='Approved' where rid="+str(a)
    print(q)
    mycursor.execute(q)
    mydb.commit()
    mydb.close()
    return sellerbuyrequest(request)

def buyerpayhandler(request):
    a=request.GET.get("buyerpayid")
    mydb=mysql.connector.connect(host='localhost',user='root',password='',database='idlelinctusdb')
    mycursor=mydb.cursor()
    q="select * from request where rid="+str(a) ;
    print(q)
    mycursor.execute(q)
    row=mycursor.fetchone()
    mydb.close()
    if row != None :
     return render(request,'buyerpay.html',{'dname':request.session['sname'],'drow':row})

def payhandler(request):
    a=request.GET.get("buyerid")
    b=request.GET.get("productprice")
    return render(request,'paymentgateway.html',{'dprice':b,'did':a,'dname':request.session['sname']})


def lastpayhandler(request):
    a=request.GET.get("id")
    mydb=mysql.connector.connect(host='localhost',user='root',password='',database='idlelinctusdb')
    mycursor=mydb.cursor()
    q="update request set status='paid' where rid="+str(a)
    print(q)
    mycursor.execute(q)
    mydb.commit()
    mydb.close()
    return  usertrackorder(request)

def sellerproductpackedhandler(request):
    a=request.GET.get("packedid")
    b=request.GET.get("selectrmk")
    mydb=mysql.connector.connect(host='localhost',user='root',password='',database='idlelinctusdb')
    mycursor=mydb.cursor()
    q="update request set status='packed', packedremark='"+b+"' where rid="+str(a);
    print(q)
    mycursor.execute(q)
    mydb.commit()
    mydb.close()
    return  sellerbuyrequest(request)



def buyerreceivedhandler(request):
    a=request.GET.get("receivedid")
    mydb=mysql.connector.connect(host='localhost',user='root',password='',database='idlelinctusdb')
    mycursor=mydb.cursor()
    q="update request set status='received' where rid="+str(a)
    print(q)
    mycursor.execute(q)
    mydb.commit()
    mydb.close()
    return  usertrackorder(request)




def buyerratedhandler(request):
    a=request.GET.get("rateid")
    b=request.GET.get("selectedrate")
    mydb=mysql.connector.connect(host='localhost',user='root',password='',database='idlelinctusdb')
    mycursor=mydb.cursor()
    q="update request set productrate='"+str(b)+"' where rid="+str(a)
    print(q)
    mycursor.execute(q)
    mydb.commit()
    mydb.close()
    return  usertrackorder(request)




def adminvieworder(request):
    mydb=mysql.connector.connect(host='localhost',user='root',password='',database='idlelinctusdb')
    mycursor=mydb.cursor()
    q="select * from request " ;
    print(q)
    mycursor.execute(q)
    row=mycursor.fetchall()
    mydb.close()
    if row != None :
     return render(request,'adminvieworder.html',{'drow':row})

def userfeedback(request):
    return render(request,'userfeedback.html',{'dname':request.session['sname']})


def userfeedbackhandler(request):
    a=request.GET.get("f1")
    b=request.GET.get("d1")
    c=request.session['sname']
    d=request.session['suno']
    tt=time.localtime(time.time())
    e=time.strftime("%b-%d-%y",tt)

    mydb=mysql.connector.connect(host='localhost',user='root',password='',database='idlelinctusdb')
    mycursor=mydb.cursor()
    q="INSERT INTO feedback( userid, username, usertype, feedback, details, date) VALUES ('"+str(d)+"','"+c+"','buyer','"+a+"','"+b+"','"+e+"')"
    mycursor.execute(q)
    print(q)
    mydb.commit()
    mydb.close()
    return userfeedback(request)
    

def userviewfeedback(request):
    a=request.session['suno']
    mydb=mysql.connector.connect(host='localhost',user='root',password='',database='idlelinctusdb')
    mycursor=mydb.cursor()
    q="select * from feedback where usertype='buyer' and userid="+str(a)  ;
    print(q)
    mycursor.execute(q)
    row=mycursor.fetchall()
    mydb.close()
    if row != None :
     return render(request,'userviewfeedback.html',{'drow':row,'dname':request.session['sname']})


def sellerfeedback(request):
    return render(request,'sellerfeedback.html',{'dname':request.session['ssname']})


def sellerfeedbackhandler(request):
    a=request.GET.get("f1")
    b=request.GET.get("d1")
    c=request.session['ssname']
    d=request.session['ssuno']
    tt=time.localtime(time.time())
    e=time.strftime("%b-%d-%y",tt)

    mydb=mysql.connector.connect(host='localhost',user='root',password='',database='idlelinctusdb')
    mycursor=mydb.cursor()
    q="INSERT INTO feedback( userid, username, usertype, feedback, details, date) VALUES ('"+str(d)+"','"+c+"','seller','"+a+"','"+b+"','"+e+"')"
    mycursor.execute(q)
    print(q)
    mydb.commit()
    mydb.close()
    return sellerfeedback(request)
    

def sellerviewfeedback(request):
    a=request.session['ssuno']
    mydb=mysql.connector.connect(host='localhost',user='root',password='',database='idlelinctusdb')
    mycursor=mydb.cursor()
    q="select * from feedback where usertype='seller' and userid="+str(a) ;
    print(q)
    mycursor.execute(q)
    row=mycursor.fetchall()
    mydb.close()
    if row != None :
     return render(request,'sellerviewfeedback.html',{'dname':request.session['ssname'],'drow':row})



def adminviewfeedback(request):
    mydb=mysql.connector.connect(host='localhost',user='root',password='',database='idlelinctusdb')
    mycursor=mydb.cursor()
    q="select * from feedback ";
    print(q)
    mycursor.execute(q)
    row=mycursor.fetchall()
    mydb.close()
    if row != None :
     return render(request,'adminviewfeedback.html',{'drow':row})

    
def adminreplyhandler(request):
    a=request.GET.get("id")
    b=request.GET.get("reply")
    mydb=mysql.connector.connect(host='localhost',user='root',password='',database='idlelinctusdb')
    mycursor=mydb.cursor()
    q="update feedback set remark='"+str(b)+"' where fid="+str(a)
    print(q)
    mycursor.execute(q)
    mydb.commit()
    mydb.close()
    return  adminviewfeedback(request)




def selleruploadproduct(request):
    return render(request,'selleruploadproduct.html',{'dname':request.session['ssname']})


def productuploadhandler(request):
    a=request.POST.get("pname")
    b=request.POST.get("pspec")
    e=request.POST.get("price")
    f=request.POST.get("pdate")
    c=request.session['ssname']
    d=request.session['ssuno']    
    path="MySecondProjectWeb\static\img"
    if request.FILES["pimage"] : 
        file=request.FILES["pimage"]
        fs=FileSystemStorage(location=path)
        filename=fs.save(a+file.name,file)
        uploadfile_url=fs.url(filename)
    path2="MySecondProjectWeb\static\img"
    if request.FILES["pimage2"] : 
        file=request.FILES["pimage2"]
        fs=FileSystemStorage(location=path2)
        filename2=fs.save(a+file.name,file)
        uploadfile_url=fs.url(filename2)
            
    mydb=mysql.connector.connect(host='localhost',user='root',password='',database='idlelinctusdb')
    mycursor=mydb.cursor()
    q="INSERT INTO medicine ( mname, exdate, consumerid, consumername, image, priscription, price) VALUES  ('"+a+"','"+f+"','"+str(d)+"','"+c+"','"+filename+"','"+filename2+"','"+e+"')"
    mycursor.execute(q)
    print(q)
    mydb.commit()
    mydb.close()
    return sellerviewproductlist(request)




def contact(request):
    return render(request,'contact.html')

def new1(request):
    return render(request,'new 1.html')

def searchhandler(request):
    a=request.GET.get("search")
    mydb=mysql.connector.connect(host='localhost',user='root',password='',database='idlelinctusdb')
    mycursor=mydb.cursor()
    q="select * from medicine where mname='"+a+"' ";
    print(q)
    mycursor.execute(q)
    row=mycursor.fetchone()
    mydb.close()
    if row != None :
     return render(request,'new 1.html',{'drow':row})
    else :
     return render(request,'no.html',{'dmsg':'no such product'})


def directsearch(request):
    mydb=mysql.connector.connect(host='localhost',user='root',password='',database='idlelinctusdb')
    mycursor=mydb.cursor()
    q="select * from medicine where status='Approved'";
    print(q)
    mycursor.execute(q)
    row=mycursor.fetchall()
    mydb.close()
    if row != None :
     return render(request,'d.html',{'drow':row})

def adminpostnotification(request):
    mydb=mysql.connector.connect(host='localhost',user='root',password='',database='idlelinctusdb')
    mycursor=mydb.cursor()
    q="select * from consumer ";
    print(q)
    mycursor.execute(q)
    row=mycursor.fetchall()
    mydb.close()
    if row != None :
     return render(request,'notification.html',{'drow':row})



def adminnotificationsendhandler(request):
    a=request.GET.get("sellerapprovedid")
    b=request.GET.get("notification")
    c=request.GET.get("sellername")
    tt=time.localtime(time.time())
    e=time.strftime("%b-%d-%y",tt)

    mydb=mysql.connector.connect(host='localhost',user='root',password='',database='idlelinctusdb')
    mycursor=mydb.cursor()
    q="INSERT INTO notification(consumerid, consumername, notification,date) VALUES ('"+str(a)+"','"+c+"','"+b+"','"+e+"')"
    mycursor.execute(q)
    print(q)
    mydb.commit()
    mydb.close()
    return adminpostnotification(request)

def adminviewnotification(request):
    mydb=mysql.connector.connect(host='localhost',user='root',password='',database='idlelinctusdb')
    mycursor=mydb.cursor()
    q="select * from notification " ;
    print(q)
    mycursor.execute(q)
    row=mycursor.fetchall()
    mydb.close()
    if row != None :
     return render(request,'adminviewnotification.html',{'drow':row})


def deletenotificationhandler(request):
    a=request.GET.get("selectedid")
    mydb=mysql.connector.connect(host='localhost',user='root',password='',database='idlelinctusdb')
    mycursor=mydb.cursor()
    q="delete from notification where nid="+str(a)
    print(q)
    mycursor.execute(q)
    mydb.commit()
    mydb.close()
    return adminviewnotification(request)



def consumerviewnotification(request):
    a=request.session['ssuno']
    mydb=mysql.connector.connect(host='localhost',user='root',password='',database='idlelinctusdb')
    mycursor=mydb.cursor()
    q="select * from notification where consumerid= " +str(a);
    print(q)
    mycursor.execute(q)
    row=mycursor.fetchall()
    mydb.close()
    if row != None :
     return render(request,'consumerviewnotification.html',{'drow':row,'dname':request.session['ssname']})




def respondnotificationhandler(request):
    a=request.GET.get("selectedid")
    mydb=mysql.connector.connect(host='localhost',user='root',password='',database='idlelinctusdb')
    mycursor=mydb.cursor()
    q="update notification set status='viewed' where nid="+str(a)
    print(q)
    mycursor.execute(q)
    mydb.commit()
    mydb.close()
    return  consumerviewnotification(request)





def usersearchhandler(request):
    a=request.GET.get("search")
    mydb=mysql.connector.connect(host='localhost',user='root',password='',database='idlelinctusdb')
    mycursor=mydb.cursor()
    q="select * from medicine where mname='"+a+"' ";
    print(q)
    mycursor.execute(q)
    row=mycursor.fetchall()
    mydb.close()
    if row != None :
     return render(request,'new 3.html',{'dname':request.session['sname'],'drow':row})






def useruploadpriscription(request):
    
    mydb=mysql.connector.connect(host='localhost',user='root',password='',database='idlelinctusdb')
    mycursor=mydb.cursor()
    q="select * from  request order by rid desc limit 1"  ;
    print(q)
    mycursor.execute(q)
    row=mycursor.fetchall()
    mydb.close()
    if row != None :
     return render(request,'useruploadpriscription.html',{'dname':request.session['sname'],'drow':row})
    

def userpriscriptionuploadhandler(request):
    a=request.POST.get("id")
    
    
    path2="MySecondProjectWeb\static\img"
    if request.FILES["pimage2"] : 
        file=request.FILES["pimage2"]
        fs=FileSystemStorage(location=path2)
        filename2=fs.save(file.name,file)
        uploadfile_url=fs.url(filename2)
            
    mydb=mysql.connector.connect(host='localhost',user='root',password='',database='idlelinctusdb')
    mycursor=mydb.cursor()
    q="update request set buyerpriscription='"+filename2+"' where rid="+str(a)
    mycursor.execute(q)
    print(q)
    mydb.commit()
    mydb.close()
    return usertrackorder(request)




def deletefeedbackhandler(request):
    a=request.GET.get("deletedid")
    mydb=mysql.connector.connect(host='localhost',user='root',password='',database='idlelinctusdb')
    mycursor=mydb.cursor()
    q="delete from feedback where fid="+str(a)
    print(q)
    mycursor.execute(q)
    mydb.commit()
    mydb.close()
    return sellerviewfeedback(request)



def deleteuserfeedbackhandler(request):
    a=request.GET.get("deletedid")
    mydb=mysql.connector.connect(host='localhost',user='root',password='',database='idlelinctusdb')
    mycursor=mydb.cursor()
    q="delete from feedback where fid="+str(a)
    print(q)
    mycursor.execute(q)
    mydb.commit()
    mydb.close()
    return userviewfeedback(request)




