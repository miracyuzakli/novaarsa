
from django.shortcuts import render
from django.contrib.auth.decorators import login_required

from django.contrib.auth.models import User, Group
from django.http import JsonResponse






@login_required
def users_views(request):
    current_user = request.user

    
    return render(request, 'users.html', {'current_user': current_user})








# @login_required
def user_groups(request):
    users = User.objects.all()
    user_data = []

    for user in users:
        user_groups = user.groups.all()
        groups_data = {group.name: group.name in (g.name for g in user_groups) for group in Group.objects.all()}
        
        if not user.username == 'admin':
            user_data.append({
                'firstname': user.first_name,
                'lastname': user.last_name,
                'groups': groups_data
            })


    print(user_data)
    return JsonResponse({'users': user_data})

