from django.shortcuts import render,redirect
from django.http import HttpResponse
from ser.models import *
from ser.forms import *
from django.contrib import messages
from MLproject import settings
# Create your views here.

def Audio(request):
    if request.method == 'POST': 
        rec=req.POST['record']
        data=Audio.objects.create(record=rec)
        data.save()
        form = AudioForm(request.POST,request.FILES or None) 
        if form.is_valid(): 
            form.save() 
            #return render('aud.html')
    else: 
        form = AudioForm() 
    return render(request, 'upload_file.html', {'form' : form}) 

def aud(request):
    messages.success(request,"successfully uploaded")
    return redirect("Audio")

def upload_file(request):
    return render(request,'upload_file.html')

def play_audio(request):
    data = request.POST.get('record')
    import IPython.display as Ipd
    return Ipd.Audio(data)
