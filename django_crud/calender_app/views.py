from django.shortcuts import render

# Create your views here.
def calendar_home(request):
    return render(request, 'calender_app/home.html')