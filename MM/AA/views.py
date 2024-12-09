from django.shortcuts import render
from.models import *
from django.views.generic import *
from django.urls import reverse_lazy

def A(req):
    AAll = Course.objects.all()
    return render(req,'A.html',{"mod":AAll})

def B(req):
    B_id = req.GET.get('B_id','')
    BS = Course.objects.filter(id__icontains=B_id)
    return render(req, 'B.html',{'mods':BS})
   

def C(req):
    C_name = req.GET.get('C_name','')
    CS = Course.objects.filter(name__icontains=C_name)
    return render(req,'C.html',{'modss':CS})


class D(UpdateView):
    model = Course
    fields = '__all__'
    template_name ='D.html'
    success_url = reverse_lazy('A')
    
class E(DeleteView):
    model = Course
    template_name = 'E.html'
    success_url = reverse_lazy('A')
    