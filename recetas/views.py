from django.shortcuts import render, get_object_or_404
from .models import Receta
from django.contrib.auth.decorators import login_required
from django.core.exceptions import PermissionDenied
from django.shortcuts import redirect

from .forms import RecetaForm


def lista_recetas(request):
    recetas = Receta.objects.select_related(
        'categoria', 'autor'
    ).order_by('-fecha_creacion')

    return render(request, 'recetas/lista_recetas.html', {
        'recetas': recetas
    })


def detalle_receta(request, pk):
    receta = get_object_or_404(Receta, pk=pk)

    return render(request, 'recetas/detalle_receta.html', {
        'receta': receta
    })


@login_required
def crear_receta(request):

    if request.method == 'POST':
        formulario = RecetaForm(
            request.POST,
            request.FILES
        )

        if formulario.is_valid():
            receta = formulario.save(commit=False)
            receta.autor = request.user
            receta.save()

            return redirect('recetas:detalle', pk=receta.pk)

    else:
        formulario = RecetaForm()

    return render(request, 'recetas/form_receta.html', {
        'formulario': formulario,
        'titulo_pagina': 'Crear nueva receta'
    })


@login_required
def editar_receta(request, pk):

    receta = get_object_or_404(Receta, pk=pk)

    if receta.autor != request.user:
        raise PermissionDenied

    if request.method == 'POST':
        formulario = RecetaForm(
            request.POST,
            request.FILES,
            instance=receta
        )

        if formulario.is_valid():
            formulario.save()

            return redirect('recetas:detalle', pk=receta.pk)

    else:
        formulario = RecetaForm(instance=receta)

    return render(request, 'recetas/form_receta.html', {
        'formulario': formulario,
        'titulo_pagina': 'Editar receta'
    })


@login_required
def eliminar_receta(request, pk):

    receta = get_object_or_404(Receta, pk=pk)

    if receta.autor != request.user:
        raise PermissionDenied

    if request.method == 'POST':
        receta.delete()
        return redirect('recetas:lista')

    return render(request, 'recetas/eliminar_receta.html', {
        'receta': receta
    })