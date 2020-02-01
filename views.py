from django.shortcuts import render
def index(request):
    return render(request, 'homePage.html')

def index2(request):
    return render(request, 'designsPage.html')

def index3(request):
    return render(request, 'sitesPage.html')
# Create your views here.
