from django.contrib.auth.mixins import LoginRequiredMixin
from django.shortcuts import render, redirect, get_object_or_404
from django.urls import reverse_lazy
from django.views import View
from django.views.generic import CreateView, UpdateView, DeleteView

from .forms import BreedForm
from .models import Cat, Breed


class MainView(LoginRequiredMixin,View):
    def get(self,request):
        ca=Cat.objects.all()
        br=Breed.objects.all().count()
        ctx = { 'breed_count':br,'cat_list':ca}
        return render(request,'cats/cat_list.html',ctx)

class BreedView(LoginRequiredMixin,View):
    def get(self,request):
        br=Breed.objects.all()
        ctx = {'breed_list':br}
        return render(request,'cats/breed_list.html',ctx)

class BreedCreate(LoginRequiredMixin,View):
    template_name='cats/breed_form.html'
    success_url=reverse_lazy('cats:all')
    def get(self,request):
        form=BreedForm()
        ctx={'form':form}
        return render(request,self.template_name,ctx)
    def post(self,request):
        form=BreedForm(request.POST)
        if not form.is_valid():
            ctx = {'form': form}
            return render(request, self.template_name, ctx)
        breede = form.save()
        return redirect(self.success_url)

class BreedUpdate(LoginRequiredMixin,View):
    model=Breed
    template='cats/breed_form.html'
    success_url=reverse_lazy('cats:all')
    def get(self,request,pk):
        breed=get_object_or_404(self.model,pk=pk)
        form=BreedForm(instance=breed)
        ctx={'form':form}
        return render(request,self.template,ctx)
    def post(self,request,pk):
        breed=get_object_or_404(self.model,pk=pk)
        form=BreedForm(request.POST,instance=breed)
        if not form.is_valid():
            ctx={'form':form}
            return render(request,self.template,ctx)
        breed=form.save()
        return redirect(self.success_url)

class BreedDelete(LoginRequiredMixin,View):
    model=Breed
    template='cats/breed_confirm_delete.html'
    success_url=reverse_lazy('cats:all')
    def get(self,request,pk):
        breed=get_object_or_404(self.model,pk=pk)
        form=BreedForm(instance=Breed)
        ctx={'form':form}
        return render(request,self.template,ctx)
    def post(self,request,pk):
        breed=get_object_or_404(self.model,pk=pk)
        breed.delete()
        return redirect(self.success_url)

class CatCreate(LoginRequiredMixin,CreateView):
    model = Cat
    fields = '__all__'
    success_url = reverse_lazy('cats:all')

class CatUpdate(LoginRequiredMixin,UpdateView):
    model = Cat
    fields = '__all__'
    success_url = reverse_lazy('cats:all')

class CatDelete(LoginRequiredMixin,DeleteView):
    model = Cat
    fields = '__all__'
    success_url = reverse_lazy('cats:all')


