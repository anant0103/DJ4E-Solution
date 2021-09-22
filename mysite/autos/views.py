from django.contrib.auth.mixins import LoginRequiredMixin
from django.shortcuts import render, redirect, get_object_or_404
from django.views import View
from django.views.generic.edit import CreateView, UpdateView, DeleteView
from django.urls import reverse_lazy

from .models import Auto, make
from .forms import MakeForm

class MainView(LoginRequiredMixin,View):
    def get(self,request):
        mc=make.objects.all().count()
        al=Auto.objects.all()
        ctx = { 'make_count':mc,'auto_list':al}
        return render(request,'autos/auto_list.html',ctx)

class MakeView(LoginRequiredMixin,View):
    def get(self,request):
        ml=make.objects.all()
        ctx = { 'make_list':ml }
        return render(request,'autos/make_list.html',ctx)

class MakeCreate(LoginRequiredMixin,View):
    template='autos/make_form.html'
    success_url=reverse_lazy('autos:all')
    def get(self,request):
        form=MakeForm()
        ctx={'form':form}
        return render(request, self.template, ctx)
    def post(self,request):
        form=MakeForm(request.POST)
        if not form.is_valid():
            ctx={'form':form}
            return render(request,self.template,ctx)
        make=form.save()
        return redirect(self.success_url)

class MakeUpdate(LoginRequiredMixin,View):
    model=make
    template='autos/make_form.html'
    success_url=reverse_lazy('autos:all')
    def get(self,request,pk):
        make=get_object_or_404(self.model,pk=pk)
        form=MakeForm(instance=make)
        ctx={'form':form}
        return render(request,self.template,ctx)
    def post(self,request,pk):
        make=get_object_or_404(self.model,pk=pk)
        form=MakeForm(request.POST,instance=make)
        if not form.is_valid():
            ctx={'form':form}
            return render(request,self.template,ctx)
        make=form.save()
        return redirect(self.success_url)

class MakeDelete(LoginRequiredMixin,View):
    model=make
    template='autos/auto_confirm_delete.html'
    success_url=reverse_lazy('autos:all')
    def get(self,request,pk):
        make=get_object_or_404(self.model,pk=pk)
        form=MakeForm(instance=make)
        ctx={'form':form}
        return render(request,self.template,ctx)
    def post(self,request,pk):
        make=get_object_or_404(self.model,pk=pk)
        make.delete()
        return redirect(self.success_url)

class AutoCreate(LoginRequiredMixin,CreateView):
    model = Auto
    fields = '__all__'
    success_url = reverse_lazy('autos:all')

class AutoUpdate(LoginRequiredMixin,UpdateView):
    model = Auto
    fields = '__all__'
    success_url = reverse_lazy('autos:all')

class AutoDelete(LoginRequiredMixin,DeleteView):
    model = Auto
    fields = '__all__'
    success_url = reverse_lazy('autos:all')




    

