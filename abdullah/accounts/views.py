from django.shortcuts import render, redirect,get_object_or_404
from django.contrib import messages
from django.core.mail import send_mail
from django.conf import settings
from django.contrib.auth.decorators import login_required
from .forms import CustomUserCreationForm, ProjectForm 
from .forms import Project

def register(request):
    if request.method == "POST":
        form = CustomUserCreationForm(request.POST)
        if form.is_valid():
            user = form.save()
            username = form.cleaned_data.get('username')

          
            send_mail(
                subject="Welcome to Abdullah Portfolio",
                message=f"Hi {username}, thank you for registering on our site. Your account has been created successfully!",
                from_email=settings.DEFAULT_FROM_EMAIL,
                recipient_list=[user.email],
                fail_silently=False,
            )

            messages.success(request, "Your account has been created! A confirmation email has been sent.")
            return redirect('login')
    else:
        form = CustomUserCreationForm()

    return render(request, 'accounts/register.html', {'form': form})



@login_required
def create_project(request):
    if request.method == 'POST':
        form = ProjectForm(request.POST, request.FILES)
        if form.is_valid():
            project = form.save(commit=False)
            project.owner = request.user
            project.save()
            form.save_m2m()
            return redirect('project_list')  # ✅ fixed here
    else:
        form = ProjectForm()
    return render(request, 'accounts/project_form.html', {'form': form})




def project_list(request):
    projects = Project.objects.all().order_by('-created')
    return render(request, 'accounts/project_list.html', {'projects': projects})

def delete_project(request,pk):
    project=get_object_or_404(Project,pk=pk)
    if request.method == 'POST':
        project.delete()
        return redirect('project_list')
    
    return redirect(request,'accounts/project_confirm_delete.html',{'project':project})

def update_project(request, pk):
    project = get_object_or_404(Project, pk=pk)
    
    if request.method == 'POST':
        form = ProjectForm(request.POST, request.FILES, instance=project)
        if form.is_valid():
            form.save()
            return redirect('project_list')
    else:
        form = ProjectForm(instance=project)

    return render(request, 'accounts/project_form.html', {'form': form})

    
    


def home(request):
    return render(request, 'accounts/home.html')
