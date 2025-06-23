from django.http import HttpResponse, HttpResponseRedirect
from django.shortcuts import render, redirect
from .forms import usersForm
from service.models import Service
from news.models import News 
from django.core.paginator import Paginator
from contact.models import contact
def homePage(request):
    # newsData=News.objects.all();
    # servicesData=Service.objects.all().order_by('service_title')##[2:5] ##to get only 3 data
    
    # for a in servicesData:
    #     print(a.service_icon)
    # print(Service)

    query = request.GET.get('query','')  # get search text from input
    newsData = News.objects.all()

    if query:
        servicesData = Service.objects.filter(service_title__icontains=query)
        
    else:
        servicesData = Service.objects.all().order_by('service_title')
    # data={
    #     'servicesData':servicesData,
    #     'newsData':newsData
    # }                    

    # return render(request, "MY PROJECT.html",data)

    data = {
        'servicesData': servicesData,
        'newsData': newsData,
        'query': query or ""  # optional, for showing the current search
    }

    return render(request, "MY PROJECT.html", data)
def contact(request):
    if request.method == 'POST':
        name = request.POST.get('name')
        email = request.POST.get('email')
        phone = request.POST.get('phone')
        message = request.POST.get('message')
        website = request.POST.get('website')

    data={
        'name': name,
        'email': email,
        'phone': phone,
        'message': message,
        'website': website
    }


    return render(request, "contact.html", data)

        

def newsDetails(request,id):
    newsDetails=News.objects.get(id=id)
    data={
        'newsDetails':newsDetails
    }
    return render(request, "newsDetails.html",data)

def submitform(request):
    try:
        if request.method == 'POST':  # ✅ Corrected here
            n1 = int(request.POST.get('num1'))
            n2 = int(request.POST.get('num2'))
            finalans = n1 + n2
            data={
                'n1':n1,
                'n2':n2,
                'output':finalans
            }

            return HttpResponse(finalans)
    except:
        pass;  

def marksheet(request):
    m =p=t= 0
    n1 = n2 =n3=n4=n5= 0
    data1 = {}

    try:
        if request.method == "POST":  # ✅ Corrected method check
            n1 = int(request.POST.get('num1'))
            n2 = int(request.POST.get('num2'))
            n3 = int(request.POST.get('num3'))
            n4 = int(request.POST.get('num4'))
            n5 = int(request.POST.get('num5'))
            t=n1+n2+n3+n4+n5
            p=t*100/500
            if p>=60:
                m="First Div"

            elif p>40:
                m="Second Div"

            elif p>35:
                m="Third Div"

            else:
                m="Fail"

        request.session['t'] = t
        request.session['m'] = m
        request.session['p'] = p

        data1 = {
        'n1': n1,
        'n2': n2,
        'n3':n3,
        'n4':n4,
        'n5':n5,
        't':t,
        "p":p,
        "m":m

    }


    except Exception as e:
        print("Error:", e)


    return render(request, "marksheet.html", data1)

def signIN(request):
    return render(request, "task2.html")

def Return(request):
    return render(request, "return.html")

def course(request):
    return HttpResponse("<b>Welcome to my page1.<b>")

def courseDetails(request, courseid):
    return HttpResponse(courseid)

def calculator(request):
    c = 0
    n1 = n2 = 0
    data1 = {}

    try:
        if request.method == "POST":  # ✅ Corrected method check
            n1 = int(request.POST.get('num1'))
            n2 = int(request.POST.get('num2'))
            opr = request.POST.get('opr')

            if opr == "+":
                c = n1 + n2
            elif opr == "-":
                c = n1 - n2
            elif opr == "*":
                c = n1 * n2
            elif opr == "/":
                c = n1 / n2

            request.session['c'] = c  # Optional: store in session

    except Exception as e:
        print("Error:", e)

    data1 = {
        'n1': n1,
        'n2': n2,
        'c': c
    }

    return render(request, "calculator.html", data1)

def userForm(request):
    finalans = 0
    fn=usersForm()
    data = {'form':fn}
    try:
        if request.method == 'POST':  # ✅ Corrected here
            n1 = int(request.POST.get('num1'))
            n2 = int(request.POST.get('num2'))
            finalans = n1 + n2
            data={
                'form':fn,
                'n1':n1,
                'n2':n2,
                'output':finalans
            }
            request.session['output'] = finalans  # ✅ Store in session
            return redirect('/thankyou/')
    except Exception as e:
        print("Error:", e)  # Debug purpose

    return render(request, "Userform.html", data)

def thankYou(request):
    output = request.session.get('output')  # ✅ Read from session
    return render(request, "thank-you.html", {'output': output})


def saveevenodd(request):
    t=0
    n=0
    data={}
    try:
        if request.method == "POST":  # ✅ Corrected method check
            n = eval(request.POST.get('num'))
            if n%2==0:
                t="Even number"
            else:
                t="ODD number"

            request.session['t'] = t   


    except Exception as e:
        print("Error:", e)


    data1 = {
        'n': n,
        't':t
        
    }

    return render(request, "evenodd.html", data1)