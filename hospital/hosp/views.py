from django.shortcuts import render,redirect
from django.http import HttpResponse
from.models import *
from django.contrib import messages
def fun1(request):
    return HttpResponse("hello world")
def fun2(request):
    return render(request,'html.html')
def fun3(request):
    data={'name':'Karthika',
          'age':'20',
          'place':'N.Paravoor'}
    return render(request,'html2.html',data)
def fun4(request):
    num={'n':-5}
    return render(request,'html3.html',num)
def fun5(request):
    number={'num':[1,2,3,4,5]}
    return render(request,'html4.html',number)
def fun6(request):
    return render(request,'html5.html')
def fun7(request):
    return render(request,'html6.html')
def fun8(request):
    if request.method=='POST':
        name=request.POST['uname']
        psw=request.POST['password']
        data=user.objects.create(name=name,password=psw)
        data.save()
    return render(request,'html7.html')
def fun9(request):
    return render(request,'html8.html')
def fun10(request):
    if request.method == 'POST':
        name = request.POST['uname']
        psw = request.POST['password']
        gender = request.POST['gender']
        data = user2.objects.create(name=name, password=psw, gender=gender)
        data.save()
    return render(request,'html7.html')
def fun11(request):
    return render(request,'index.html')
def fun12(request):
    return render(request,'admin.html')
def fun13(request):
    return render(request,'user.html')
def signup2(request):
    if request.method=='POST':
        name =request.POST['name']
        phn=request.POST['mob']
        mail=request.POST['email']
        user=request.POST['uname']
        psw=request.POST['pasw']
        radio=request.POST['gender']
        data=user_log.objects.create(full_name=name,phone=phn,gmail=mail,username=user,password=psw,gender=radio)
        data.save()
    messages.success(request,"SignUp Successfull!")
    return redirect(fun13)
def fun14(request):
    return render(request,'signup.html')
def home(request):
    if request.method == 'POST':
        mail = request.POST['email']
        pswd=request.POST['password']
        data = user_log.objects.filter(gmail=mail)
        if data:
            data1 = user_log.objects.get(gmail=mail)
            if data1.password == pswd:
                request.session['id'] = mail
                return render(request,'home.html')
            else:
                messages.info(request,'invalid E-mail or password')
                return redirect(fun13)
        else:
            messages.info(request,'invalid E-mail or password')
            return redirect(fun13)
def logout(request):
    if 'id' in request.session:
        request.session.flush()
        return redirect(fun11)
def admin2(request):
    d=user_log.objects.all()
    return render(request,'admin2.html',{'data':d})

def admin_log2(request):
    if request.method == 'POST':
        name=request.POST['name']
        pswd=request.POST['password']
        data=admin_log.objects.filter(name=name)
        if data:
            data1 = admin_log.objects.get(name=name)
            if data1.password == pswd:
                request.session['id'] = name
                return redirect(admin2)
            else:
                messages.info(request,'invalid username or password')
                return redirect(fun12)
        else:
            messages.info(request,'invalid username or password')
            return redirect(fun12)
def fun15(request):
    return render(request,'doctor.html')

def doctor_form(request):
    if request.method == 'POST':
        doc_name = request.POST['dname']
        doc_id = request.POST['did']
        doc_img = request.POST['dpic']
        dep = request.POST['dep']
        data = doctor_form1.objects.create(doctor_name=doc_name,doctor_id=doc_id,doctor_img=doc_img,doctor_dept=dep)
        data.save()
        messages.info(request,'Doctor Added Successfully!')
        return render(request,'doctor.html')
    else:
        messages.info(request,'Something Went Wrong Please Try Again')
        return render(request,'doctor.html')
def reg_docs(request):
    d=doctor_form1.objects.all()
    return render(request,'registered doctor.html',{'data':d})

def del_doc(request,id):
    doctor_form1.objects.filter(pk=id).delete()
    return redirect(reg_docs)

def appoint_booking1(request):
    if request.method == 'POST':
        fname=request.POST['fname']
        email=request.POST['email']
        radio=request.POST['gender']
        bkdate=request.POST['date']
        depart=request.POST['dept']
        phn=request.POST['phone']
        msg=request.POST['message']
        payment=request.POST['payment']
        data=appoint_booking.objects.create(name=fname,email=email,gender=radio,date=bkdate,phone=phn,department=depart,message=msg,payment_id=payment)
        data.save()
    messages.info(request,'Booking successfull !')
    return render(request,'home.html')

def fun16(request):
    d=appoint_booking.objects.filter(status='pending')
    return render(request,'pend_appointment.html',{'data':d})

def del_app(request,id):
    appoint_booking.objects.filter(pk=id).delete()
    return redirect(fun16)

def accept_app(request,id):
    appoint_booking.objects.filter(pk=id).update(status='approve')
    return redirect(fun16)
def accept_app(request,id):
    appoint_booking.objects.filter(pk=id).update(status='approve')
    return redirect(fun16)

def booking_details(request):
    pending_bookings=[]
    history=[]
    d=appoint_booking.objects.filter(status='pending')
    for i in d:
        if i.email==request.session['id']:
            pending_bookings.append(i)
    d1=appoint_booking.objects.filter(status='approve')
    for j in d1:
        if j.email==request.session['id']:
            history.append(j)
    return render(request, 'booking details.html', {'data': pending_bookings, 'data1': history})

# Create your views here.
