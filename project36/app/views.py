from django.shortcuts import render

# Create your views here.

def userdeffilter(request):
    d = {'data' : 'HEY! HOw ArE You??'}
    return render(request, 'userdef_filter.html',d)