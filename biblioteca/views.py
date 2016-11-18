from django.shortcuts import render

from django.shortcuts import render, get_object_or_404
from django.utils import timezone

from django.shortcuts import redirect
# Create your views here.

def post_detail(request, pk):
        post = get_object_or_404(Postear, pk=pk)
        return render(request, 'blog/detalle_articulo.html', {'Postear': post})
