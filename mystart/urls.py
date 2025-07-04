"""
URL configuration for mystart project.

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/5.2/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  path('', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  path('', Home.as_view(), name='home')
Including another URLconf
    1. Import the include() function: from django.urls import include, path
    2. Add a URL to urlpatterns:  path('blog/', include('blog.urls'))
"""
from django.contrib import admin
from django.urls import path
from mystart import views

urlpatterns = [
    path('admin/', admin.site.urls),
    path('',views.homePage),
    path('sign-in/',views.signIN),
    path('return/',views.Return),
    path('course/',views.course),
    path('calculator/',views.calculator),
    path('contact/',views.contact,name="contact"),
    path('course/<courseid>',views.courseDetails),
    path('submitform/',views.submitform,name="submitform"),
    path('Userform/',views.userForm),
    path('thankyou/',views.thankYou),
    path('evenodd/',views.saveevenodd),
    path('marksheet/',views.marksheet),
    path('newsDetails/<id>',views.newsDetails)
]
