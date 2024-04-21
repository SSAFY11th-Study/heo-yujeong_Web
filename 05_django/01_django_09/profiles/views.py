from django.shortcuts import render
from django.contrib.auth import get_user_model

User = get_user_model()

# Create your views here.
def index(request):
    users = User.objects.all()
    context = {
        'users': users,
    }
    return render(request, 'profiles/index.html', context)