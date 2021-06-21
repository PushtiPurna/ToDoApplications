#from django.shortcuts import render
# from django.http import HttpResponse

# def tasklist(request):
#     return HttpResponse("hello")

#class base view
from django.views.generic.list import ListView
from django.views.generic.detail import DetailView
from django.views.generic.edit import CreateView, UpdateView, DeleteView
from django.urls import reverse_lazy

from django.contrib.auth.views import LoginView

from django.contrib.auth.mixins import LoginRequiredMixin

from .models import Task

class CustomLoginView(LoginView):
    template_name = 'todoapp/login.html'
    fields = "__all__"
    redirect_authenticated_user = True

    def get_success_url(self):
        return reverse_lazy('task')

class TaskList(LoginRequiredMixin, ListView):
    model = Task
    context_object_name = 'task'
    

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context['task'] = context['task'].filter(user=self.request.user)
        return context


class TaskDetail(LoginRequiredMixin, DetailView):
    model = Task
    context_object_name = 'task'
    template_name = 'todoapp/taskdetail.html'
    #this template_name is used to rename the html file,as we use the file name as define by django
    #so by using this we can edit that.

class TaskCreate(LoginRequiredMixin, CreateView):
    model = Task
    fields = "__all__"
    success_url = reverse_lazy('task')

class TaskUpdate(LoginRequiredMixin, UpdateView):
    model = Task
    fields = "__all__"
    success_url = reverse_lazy('task')

class TaskDelete(LoginRequiredMixin, DeleteView):
    model = Task
    success_url = reverse_lazy('task')
    
