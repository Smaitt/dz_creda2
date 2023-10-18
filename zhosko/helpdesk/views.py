from django.shortcuts import render, redirect, get_object_or_404, HttpResponseRedirect
from django.urls import reverse
from .forms import *
from .models import *
from django.contrib.auth import login, authenticate
from .forms import RegistrationForm, LoginForm
from django.contrib.auth.models import Group

def home(request):
    return render(request, 'helpdesk/home.html')

def create_issue(request):
    if request.method == 'POST':
        form = IssueForm(request.POST)
        if form.is_valid():
            request_new = form.save(commit=False)
            reception_group = Group.objects.get(name='Reception')
            request_new.assigned_user = reception_group.user_set.first() 
            request_new.save()
            return HttpResponseRedirect(reverse('issue_list'))
    else:
        form = IssueForm()
        
    return render(request, 'helpdesk/create_issue.html', {'form': form})


def issue_list(request):
    if request.user.groups.filter(name="Tester").exists():
        issues = Issue.objects.filter(assigned_user=request.user, status='resolved').order_by('-created_date')
    else:
        issues = Issue.objects.filter(assigned_user=request.user).exclude(status='resolved').order_by('-created_date')
    user = request.user
    return render(request, 'helpdesk/issue_list.html', {'issues': issues, 'user':user})


def issue_detail(request, issue_id):
    issue = get_object_or_404(Issue, pk=issue_id)

    if request.method == 'POST':
        issue.actions = request.POST['actions']
        issue.status = request.POST['status']
        issue.save()
        return HttpResponseRedirect(reverse('issue_list'))
    
        if issue.status == 'resolved':
            issue.resolved_user = issue.assigned_user
            tester_group = Group.objects.get(name='Tester')
            issue.assigned_user = tester_group.user_set.first()
            issue.save()
    user = request.user
    is_tester = user.groups.filter(name='Tester').exists()

    return render(request, 'helpdesk/issue_detail.html', {'issue': issue,'is_tester' : is_tester})

def register(request):
    if request.method == 'POST':
        form = RegistrationForm(request.POST)
        if form.is_valid():
            user = form.save()
            login(request, user)
            return redirect('home')  
    else:
        form = RegistrationForm()
    return render(request, 'helpdesk/register.html', {'form': form})

def user_login(request):
    if request.method == 'POST':
        form = LoginForm(data=request.POST)
        if form.is_valid():
            username = form.cleaned_data['username']
            password = form.cleaned_data['password']
            user = authenticate(request, username=username, password=password)
            if user:
                login(request, user)
                return redirect('home')  
    else:
        form = LoginForm()
    return render(request, 'helpdesk/login.html', {'form': form})