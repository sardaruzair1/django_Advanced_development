from django.shortcuts import render
from django.http import HttpResponse

# Create your views here.
def index(request):
    # return HttpResponse('<h1><u>Hello World from sardar uzair</u></h1>') ia used to return the string
    contex = {
        'name': 'uzair',
        'age': '18',
        'nationality': 'pakistan',
        
    }
    return render(request,'index.html', contex)

def index2(request):
    
    
    return render(request,'index2.html')

def counter(request):
    word = request.GET['word']
    ammount_of_word = len(word.split())
    return render(request,'counter.html',{'ammount': ammount_of_word})