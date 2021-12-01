from django.shortcuts import render
from .models import Course

# Create your views here.

def index(request):
    courses = Course.objects.all()
    return render(request, 'course/index.html', {'courses': courses})