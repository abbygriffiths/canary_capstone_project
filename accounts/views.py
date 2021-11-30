from django.contrib.auth import get_user_model
from django.shortcuts import redirect, render

User = get_user_model()


def register(request):
    """Show the registration form to add new users."""
    if request.method == 'POST':
        first_name = request.POST.get('first_name')
        last_name = request.POST.get('last_name')
        username = request.POST.get('username')
        email = request.POST.get('email')
        password = request.POST.get('password')

        user = User.objects.create_user(
            username=username, 
            password=password, 
            email=email, 
            first_name=first_name, 
            last_name=last_name)
        user.save()
        print(user)
        return redirect('list_accounts')
    elif request.method == 'GET':
        return render(request, 'accounts/register.html')


def list(request):
    """Show all the users in the database."""
    users = User.objects.all()
    return render(request, 'accounts/list.html', {'users': users})
