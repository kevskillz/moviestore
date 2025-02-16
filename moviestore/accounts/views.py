from django.shortcuts import render
from django.contrib.auth import login as auth_login, authenticate, logout as auth_logout

from .models import UserSecurityQuestion
from .forms import CustomUserCreationForm, CustomErrorList, SecurityQuestionForm
from django.shortcuts import redirect
from django.contrib.auth.decorators import login_required
from django.contrib.auth.models import User
from django.contrib.auth.forms import PasswordChangeForm
from django.contrib.auth import update_session_auth_hash
from django.contrib.auth.forms import SetPasswordForm
@login_required
def logout(request):
    auth_logout(request)
    return redirect('home.index')
def login(request):
    template_data = {}
    template_data['title'] = 'Login'
    if request.method == 'GET':
        return render(request, 'accounts/login.html',
            {'template_data': template_data})
    elif request.method == 'POST':
        user = authenticate(
            request,
            username = request.POST['username'],
            password = request.POST['password']
        )
        if user is None:
            template_data['error'] = 'The username or password is incorrect.'
            return render(request, 'accounts/login.html',
                {'template_data': template_data})
        else:
            auth_login(request, user)
            return redirect('home.index')
def signup(request):
    template_data = {}
    template_data['title'] = 'Sign Up'
    if request.method == 'GET':
        template_data['form'] = CustomUserCreationForm()
        return render(request, 'accounts/signup.html',
            {'template_data': template_data})
    elif request.method == 'POST':
        form = CustomUserCreationForm(request.POST, error_class=CustomErrorList)
        if form.is_valid():
            user = form.save()
            security_answer = form.cleaned_data['security_answer']
            UserSecurityQuestion.objects.create(user=user, security_answer=security_answer)
            return redirect('accounts.login')
        else:
            template_data['form'] = form
            return render(request, 'accounts/signup.html',
                {'template_data': template_data})
        
@login_required
def orders(request):
    template_data = {}
    template_data['title'] = 'Orders'
    template_data['orders'] = request.user.order_set.all()
    return render(request, 'accounts/orders.html',
        {'template_data': template_data})
def forgot_password(request):
    template_data = {'title': 'Forgot Password'}
    
    if request.method == 'POST':
        username = request.POST.get('username')
        answer = request.POST.get('answer')
        
        if not username or not answer:
            template_data['error'] = 'Username and answer are required.'
        else:
            try:
                user = User.objects.get(username=username)
                user_security_question = UserSecurityQuestion.objects.get(user=user)
                
                if user_security_question.security_answer == answer:
                    # If the answer is correct, redirect to a page to set a new password
                    return redirect('accounts.set_new_password', username=username)
                else:
                    template_data['error'] = 'Incorrect security question answer.'
            
            except User.DoesNotExist:
                template_data['error'] = 'Username not found.'
            except UserSecurityQuestion.DoesNotExist:
                template_data['error'] = 'Security question not found for this user.'
    
    return render(request, 'accounts/forgot_password.html', {'template_data': template_data})


def set_new_password(request, username):
    user = User.objects.get(username=username)
    
    if request.method == 'POST':
        form = SetPasswordForm(user, request.POST)
        if form.is_valid():
            form.save()
            return redirect('accounts.login')  # Redirect to login after setting the password
    else:
        form = SetPasswordForm(user)
    
    return render(request, 'accounts/set_new_password.html', {'form': form})