from django.shortcuts import HttpResponse,render
from todos.models import Task
def home(request):
    tasks_not=Task.objects.filter(is_completed=False).order_by('updated_at')
    tasks=Task.objects.filter(is_completed=True).order_by('updated_at')
    context={
        'tasks':tasks,'tasks_not':tasks_not
    }
    return render(request,'home.html',context)