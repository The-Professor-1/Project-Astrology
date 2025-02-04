from django.shortcuts import render
from django.http import HttpResponse
from .forms import Myform,Contactus
from calculator import library as lb
from .models import Users,Message
from django.urls import reverse
# Create your views here.
def calculator(name,mothername):
    name_sum = 0
    mother_name_sum = 0
    for i in name:
        for j in lb.fidel_value_pair().keys():
            for k in j:
                if k==i:
                    name_sum = (name_sum + lb.fidel_value_pair()[j])%12
    for i in mothername:
        for j in lb.fidel_value_pair().keys():
            for k in j:
                if k == i:
                    mother_name_sum=(mother_name_sum+lb.fidel_value_pair()[j])%12
    finalname = "".join(name)
    finalmothername = "".join(mothername)
    total_sum = (name_sum + mother_name_sum)%12
    title_list = list(lb.kokeb_disc_pair().keys())
    result = title_list[total_sum-1]
    return result,finalname,finalmothername
def homepage(request):
    form = Myform()
    user = None
    if request.method == 'POST':
        action = request.POST.get('action')
        if action == 'calculate':
            self_name = [i for i in request.POST.get('your_name','')]
            mother_name = [i for i in request.POST.get('your_mothers_name','')]
            result,finalname,finalmothername = calculator(self_name,mother_name)
            user = Users(selfname = finalname,mothersname=finalmothername,sign=result,description=lb.kokeb_disc_pair()[result])
            user.save()
        elif action == 'knowsign':

            title = request.POST.get('sign','')
            description = Users.objects.filter(sign=title).values_list('description', flat=True).first()
            context = {'sign':title,'description':description}
            return render(request,'calculator/description.html',context)
    return render(request,'calculator/index.html',{'form':form,'user':user})
def contactus(request):
    form = Contactus()
    if request.method == 'POST':
        action = request.POST.get('action')
        if action == 'send':
            i = 0
            form = Contactus(data=request.POST)
            if form.is_valid():
                instance = form.save(commit=False)
                instance.foreign_key_field_id = Message.id  # Assign the ID
                instance.save()
                homepage_url = reverse('homepage')  # Generate the URL for the 'homepage' view
                response_content = f"<h1><font color='green'>your message sent successfully!</font><br><a href='{homepage_url}'>back to home</a></h1>"
                return HttpResponse(response_content)
    return render(request,'calculator/contactus.html',{'form':form})
def blog(request):
    return render(request,'calculator/blog.html')
def home(request):
    return HttpResponse('hello world!')