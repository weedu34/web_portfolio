# main/views.py

from django.shortcuts import render, get_object_or_404, redirect
from django.contrib import messages
from django.core.mail import send_mail
from django.conf import settings
from .models import Project
from .forms import ContactForm

def home(request):
    """View for the home page"""
    # Get the 3 most recent projects
    projects = Project.objects.all()[:3]
    context = {
        'projects': projects
    }
    return render(request, 'main/home.html', context)

def about(request):
    """View for the about page"""
    return render(request, 'main/about.html')

def projects(request):
    """View for the projects page"""
    projects = Project.objects.all()
    context = {
        'projects': projects
    }
    return render(request, 'main/projects.html', context)

def project_detail(request, pk):
    """View for the project detail page"""
    project = get_object_or_404(Project, pk=pk)
    
    # Split the technologies string into a list
    technologies = [tech.strip() for tech in project.technology.split(',')] if project.technology else []
    
    # Get previous and next projects for navigation
    prev_project = Project.objects.filter(created_at__gt=project.created_at).order_by('created_at').first()
    next_project = Project.objects.filter(created_at__lt=project.created_at).order_by('-created_at').first()
    
    # Get related projects (same technology)
    related_projects = Project.objects.filter(technology__icontains=project.technology).exclude(id=project.id)[:3]
    
    context = {
        'project': project,
        'technologies': technologies,  # Add the split technologies list
        'prev_project': prev_project,
        'next_project': next_project,
        'related_projects': related_projects
    }
    return render(request, 'main/project_detail.html', context)

def contact(request):
    """View for the contact page with form handling"""
    if request.method == 'POST':
        form = ContactForm(request.POST)
        if form.is_valid():
            name = form.cleaned_data['name']
            email = form.cleaned_data['email']
            subject = form.cleaned_data['subject']
            message = form.cleaned_data['message']
            
            # Email content
            email_subject = f"Portfolio Contact: {subject}"
            email_message = f"Name: {name}\nEmail: {email}\n\nMessage:\n{message}"
            
            # Send email
            try:
                send_mail(
                    email_subject,
                    email_message,
                    settings.DEFAULT_FROM_EMAIL,
                    [settings.CONTACT_EMAIL],
                    fail_silently=False,
                )
                messages.success(request, "Your message has been sent successfully. I'll get back to you soon!")
                return redirect('contact')
            except Exception as e:
                messages.error(request, f"An error occurred: {str(e)}")
    else:
        form = ContactForm()
    
    context = {
        'form': form
    }
    return render(request, 'main/contact.html', context)