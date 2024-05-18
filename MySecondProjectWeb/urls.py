from django.urls import path
from . import views
urlpatterns = [
path('',views.index,name='index'),
path('login',views.login,name="login"),
path('index',views.index,name="index"),
path('loginhandler',views.loginhandler,name="loginhandler"),
path('register',views.register,name="register"),
path('viewuserprofile',views.viewuserprofile,name="viewuserprofile"),
path('updateuserprofile',views.updateuserprofile,name="updateuserprofile"),
path('uhome',views.uhome,name="uhome"),
path('registerhandler',views.registerhandler,name="registerhandler"),
path('updateuserprofilehandler',views.updateuserprofilehandler,name="updateuserprofilehandler"),
path('sellerloginhandler',views.sellerloginhandler,name="sellerloginhandler"),
path('sellerregister',views.sellerregister,name="sellerregister"),
path('viewsellerprofile',views.viewsellerprofile,name="viewsellerprofile"),
path('updatesellerprofile',views.updatesellerprofile,name="updatesellerprofile"),
path('shome',views.shome,name="shome"),
path('sellerregisterhandler',views.sellerregisterhandler,name="sellerregisterhandler"),
path('updatesellerprofilehandler',views.updatesellerprofilehandler,name="updatesellerprofilehandler"),
path('sellerlogin',views.sellerlogin,name="sellerlogin"),
path('adminlogin',views.adminlogin,name="adminlogin"),
path('adminloginhandler',views.adminloginhandler,name="adminloginhandler"),
path('viewuser',views.viewuser,name="viewuser"),
path('viewseller',views.viewseller,name="viewseller"),
path('ahome',views.ahome,name="ahome"),
path('deleteuserhandler',views.deleteuserhandler,name="deleteuserhandler"),

path('deletesellerhandler',views.deletesellerhandler,name="deletesellerhandler"),
path('adminsellerapprovehandler',views.adminsellerapprovehandler,name="adminsellerapprovehandler"),
path('productdetail',views.productdetail,name="productdetail"),
path('userbuyrequesthandler',views.userbuyrequesthandler,name="userbuyrequesthandler"),

path('usertrackorder',views.usertrackorder,name="usertrackorder"),
path('sellerviewproductlist',views.sellerviewproductlist,name="sellerviewproductlist"),
path('adminviewproduct',views.adminviewproduct,name="adminviewproduct"),
path('adminproductapprovehandler',views.adminproductapprovehandler,name="adminproductapprovehandler"),


path('sellerbuyrequest',views.sellerbuyrequest,name="sellerbuyrequest"),
path('sellerproductapprovehandler',views.sellerproductapprovehandler,name="sellerproductapprovehandler"),
path('buyerpayhandler',views.buyerpayhandler,name="buyerpayhandler"),
path('payhandler',views.payhandler,name="payhandler"),
path('lastpayhandler',views.lastpayhandler,name="lastpayhandler"),

path('sellerproductpackedhandler',views.sellerproductpackedhandler,name="sellerproductpackedhandler"),
path('buyerreceivedhandler',views.buyerreceivedhandler,name="buyerreceivedhandler"),

path('buyerratedhandler',views.buyerratedhandler,name="buyerratedhandler"),

path('adminvieworder',views.adminvieworder,name="adminvieworder"),
path('userfeedback',views.userfeedback,name="userfeedback"),
path('userfeedbackhandler',views.userfeedbackhandler,name="userfeedbackhandler"),
path('userviewfeedback',views.userviewfeedback,name="userviewfeedback"),

path('sellerfeedback',views.sellerfeedback,name="sellerfeedback"),
path('sellerfeedbackhandler',views.sellerfeedbackhandler,name="sellerfeedbackhandler"),
path('sellerviewfeedback',views.sellerviewfeedback,name="sellerviewfeedback"),

path('adminviewfeedback',views.adminviewfeedback,name="adminviewfeedback"),
path('adminreplyhandler',views.adminreplyhandler,name="adminreplyhandler"),


path('selleruploadproduct',views.selleruploadproduct,name="selleruploadproduct"),
path('productuploadhandler',views.productuploadhandler,name="productuploadhandler"),
path('contact',views.contact,name="contact"),
path('searchhandler',views.searchhandler,name="searchhandler"),
path('new1',views.new1,name="new1"),
path('directsearch',views.directsearch,name="directsearch"),


path('adminpostnotification',views.adminpostnotification,name="adminpostnotification"),
path('deletenotificationhandler',views.deletenotificationhandler,name="deletenotificationhandler"),
path('adminnotificationsendhandler',views.adminnotificationsendhandler,name="adminnotificationsendhandler"),
path('adminviewnotification',views.adminviewnotification,name="adminviewnotification"),
path('consumerviewnotification',views.consumerviewnotification,name="consumerviewnotification"),
path('respondnotificationhandler',views.respondnotificationhandler,name="respondnotificationhandler"),

path('usersearchhandler',views.usersearchhandler,name="usersearchhandler"),

path('userpriscriptionuploadhandler',views.userpriscriptionuploadhandler,name="userpriscriptionuploadhandler"),
path('useruploadpriscription',views.useruploadpriscription,name="useruploadpriscription"),

path('deletefeedbackhandler',views.deletefeedbackhandler,name="deletefeedbackhandler"),
path('deleteuserfeedbackhandler',views.deleteuserfeedbackhandler,name="deleteuserfeedbackhandler"),
]
