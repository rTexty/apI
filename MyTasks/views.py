from rest_framework import viewsets, status
from .models import Task
from .serializers import TaskSerializer
from rest_framework.decorators import action
from rest_framework.response import Response
from django.shortcuts import render, redirect
from rest_framework.generics import ListAPIView, ListCreateAPIView
from rest_framework.renderers import TemplateHTMLRenderer
from .forms import TaskForm


class TasksFunc(viewsets.ModelViewSet):
    queryset = Task.objects.all()
    serializer_class = TaskSerializer
    @action(detail=False, methods=['get'])
    def tasks(self, request):
        tasks = Task.objects.all()
        serializer = TaskSerializer(tasks, many=True)
        return Response(serializer.data)
class CompletedTasks(viewsets.ModelViewSet):
    queryset = Task.objects.filter(status=True).all()
    serializer_class = TaskSerializer
    @action(detail=False, methods=['get'])
    def comptasks(self, request):
        tasks = Task.objects.filter(status=True)
        serializer = TaskSerializer(tasks, many=True)
        return Response(serializer.data)
    

class ListTasks(ListAPIView):
    def get(self, request):
        tasks = Task.objects.all()
        return render(request, 'index.html', {'tasks': tasks})
    


class MyTemplateHTMLRenderer(TemplateHTMLRenderer):
    def get_template_context(self, data, renderer_context):
        response = renderer_context['response']
        if response.exception:
            data['status_code'] = response.status_code
        return {'data': data}



def create_task(request):
    if request.method == 'POST':
        form = TaskForm(request.POST)
        if form.is_valid():
            form.save()
            return render(request, 'success.html')
    else:
        form = TaskForm()
    return render(request, 'create.html', {'form': form})