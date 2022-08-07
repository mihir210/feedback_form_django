from django.shortcuts import render
import imp
from multiprocessing import context
from datetime import datetime
import re
from django.shortcuts import render
from home.models import Contact
from django.contrib import messages
# Create your views here.
from django.http import HttpResponse

# from home.models import Contact
# Create your views here.


def index(request):
   if request.method =="POST":
      name = request.POST.get('name')
      email = request.POST.get('email')
      department = request.POST.get('department')
      roll_no = request.POST.get('roll_no')
      feedback_text = request.POST.get('feedback_text')
      contact = Contact(name=name, email=email, department=department, roll_no=roll_no, feedback_text=feedback_text, date=datetime.today())
      contact.save()
      messages.success(request, 'your massage has been sent')
   return render(request, 'index.html')