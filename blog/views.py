from django.shortcuts import render,get_object_or_404,redirect
from .models import Project_gate_1
from .forms import PostForm

# Create your views here.


def project_list(request):
    projects = Project_gate_1.objects.all()
    return render(request,'blog/project_list.html',{'projects':projects})


def project_detail(request, pk):
    project = get_object_or_404(Project_gate_1,pk=pk)
    return render(request,'blog/project_detail.html',{'project':project})

def project_new(request):
    if request.method == 'POST':
        form = PostForm(request.POST)
        if form.is_valid():
            project  = form.save(commit=False)
            #post.published_date = timezone.now()
            project.save()
            return redirect('project_detail',pk=project.pk)
    else:
        form = PostForm()
    return render(request,'blog/project_edit.html',{'form':form})
