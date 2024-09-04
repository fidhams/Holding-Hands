from django.conf import settings
from django.conf.urls.static import static
from django.urls import path
from . import views


urlpatterns=[
    path('',views.home,name='home'),
    path('contactus/',views.contactus,name='contactus'),
    path('itemsreq/',views.itemsreq,name='itemsreq'),
    path('login/',views.login_view,name='login'),
    path('orghome/',views.orghome,name='orghome'),
    path('orgsignup/',views.orgsignup,name='orgsignup'),
    path('signup/',views.signup,name='signup'),
    path('volunteerreq/',views.volunteerreq,name='volunteerreq'),
    path('user/',views.user,name='user'),
    path('userdonate/',views.userdonate,name='userdonate'),
    path('uservolunteer/',views.uservolunteer,name='uservolunteer'),
    path('viewd/',views.viewd,name='viewd'),

]

if settings.DEBUG:
    urlpatterns += static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)