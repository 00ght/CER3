from django.shortcuts import render

# Create your views here.
def index(request):
    title = ""
    data = {
        "title": title,
    }
    return render(request, 'base.html', data)
