from django.shortcuts import render

# Create your views here.
def tradex_home(request):
    return render(request, "tradex_home.html", {})