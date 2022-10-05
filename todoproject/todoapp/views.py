from django.shortcuts import render, redirect
from django.urls import reverse_lazy

from .models import Task
from .forms import TodoForm
from django.views.generic import ListView
from django.views.generic.detail import DetailView
from django.views.generic.edit import UpdateView,DeleteView
# Create your views here.

class Tasklistview(ListView):
    model=Task
    template_name = 'home.html'
    context_object_name = 'task1'
class Taskdetailview(DetailView):
    model = Task
    template_name = 'detail.html'
    context_object_name = 'task'
class Taskupdateview(UpdateView):
    model = Task
    template_name = 'update.html'
    context_object_name = 'task'
    fields = ('name','priority','date')

    def get_success_url(self):
        return reverse_lazy('cbvdetail',kwargs={'pk':self.object.id})

class Taskdeleteview(DeleteView):
    model = Task
    template_name = 'delete.html'
    success_url = reverse_lazy('cbvhome')


def todo(request):
    JJ=Task.objects.all()
    if request.method=="POST":
        XX=request.POST.get('task','')
        YY=request.POST.get('priority','')
        UU = request.POST.get('date', '')
        AA=Task(name=XX,priority=YY,date=UU)
        AA.save()

    return render(request,'home.html',{'task1':JJ})

# def detail(request):
#     task1=Task.objects.all()
#     return render(request,'detail.html',{'task1': task1})

def delete(request,taskid):
    AB=Task.objects.get(id=taskid)
    if request.method=='POST':
        AB.delete()
        return redirect('/')
    return render(request,'delete.html')


def update (request,task_id):
    ABA=Task.objects.get(id=task_id)
    f=TodoForm(request.POST or None, instance=ABA)
    if f.is_valid():
        f.save()
        return redirect('/')
    return render(request,'edit.html',{'f':f,'task':ABA})
