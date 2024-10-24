from django.shortcuts import render, redirect
from laboratorio.models import Laboratorio

# Create your views here.

def inicio(request):
    return render(request, 'inicio.html')

def acerca_de(request):
    return render(request , 'acerca_de.html')

def mostrar_lab(request):
    laboratorios = Laboratorio.objects.all()
    num_visitas = request.session.get('num_visitas',1)
    request.session['num_visitas'] = num_visitas + 1
    return render(request,'mostrar.html',{'laboratorios':laboratorios,'num_visitas':num_visitas})

def insertar_lab(request):
    if request.method == 'POST':
        lab_nombre = request.POST['lab_nombre']
        lab_ciudad = request.POST['lab_ciudad']
        lab_pais = request.POST['lab_pais']
        laboratorio = Laboratorio(nombre = lab_nombre,
                                  ciudad = lab_ciudad,
                                  pais = lab_pais)
        laboratorio.save()
        return redirect('mostrar_lab')
    else:
        return render(request,'insertar.html')
    
def eliminar_lab(request,pk):
    laboratorio = Laboratorio.objects.get(id=pk)

    if request.method == 'POST':
        laboratorio.delete()
        return redirect('mostrar_lab')

    else:
        return render(request,'eliminar.html',{'laboratorio':laboratorio})
    
def editar_lab(request,pk): 
   laboratorio = Laboratorio.objects.get(id=pk)
   return render(request, 'editar.html', {'laboratorio':laboratorio})

def actualizarlab(request,id): 
    lab_nombre = request.POST['lab_nombre']
    lab_ciudad = request.POST['lab_ciudad']
    lab_pais = request.POST['lab_pais']
    laboratorio = Laboratorio.objects.get(id=id) 
    laboratorio.nombre = lab_nombre
    laboratorio.ciudad = lab_ciudad 
    laboratorio.pais = lab_pais
    laboratorio.save() 
    return redirect('mostrar_lab')