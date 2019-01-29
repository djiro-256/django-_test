from django.shortcuts import render

def index(request):
    """/トップページ"""
    context = {
        'name': 'Jiro',
    }
    return render(request, 'myapp/index.html', context) 

def about(request):
    """/aboutページ"""
    return render(request, 'myapp/about.html') 

def info(request):
    """/infoページ"""
    return render(request, 'myapp/info.html') 