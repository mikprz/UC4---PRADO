from django.shortcuts import render, HttpResponse, redirect
from django.contrib import messages


# Create your views here.

layout = """
    <h1> Proyecto Web (LP3) | </h1>
    <hr/>
    <ul>
        <li>
            <a href="/inicio"> Inicio</a>
        </li>
        <li>
            <a href="/saludo"> Mensaje de Saludo</a>
        </li>
        <li>
            <a href="/rango"> Mostrar Números [a,b]</a>
        </li>
        <li>
            <a href="/rango2/10/15"> Mostrar Números [10,15]</a>
        </li>
    </ul>
    <hr/>
"""


def index(request):
    estudiantes = [
                    'Jhon Baldeon',
                    'Alexander Gonzales',
                    'Joan Palomino',
                    'Carlos Aquino',
                    'Danne Barzola']

    return render(request , 'index.html',{
        'titulo': 'Inicio',
        'mensaje':'Proyecto Web con Django',
        'estudiantes': estudiantes
    })



def cursos(request):
    return render(request, 'cursos.html')

def crearCurso(request):
    return render(request, 'crearCurso.html')

def carreras(request):
    return render(request, 'carreras.html')

def crearCarreras(request):
    return render(request, 'crearCarreras.html')