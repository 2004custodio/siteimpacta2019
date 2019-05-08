from django.shortcuts import render
from django.http import HttpResponse

# Create your views here.
def post_list(request):
 return render(request, 'site/index.html')

def cursos(request):
 return render(request, 'site/detalhedecursos.html')

def listadecursos(request):
 return render(request, 'site/listadecursos.html')
