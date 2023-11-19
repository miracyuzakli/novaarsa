
from django.shortcuts import render
from django.contrib.auth.decorators import login_required

from django.contrib.auth.models import User, Group
from django.http import JsonResponse
from django.contrib.auth.decorators import user_passes_test
import json
from django.views.decorators.http import require_http_methods


# Erişim kontrolü fonksiyonu
def is_user_operations(user):
    return user.groups.filter(name="user_operations").exists()


# Kullanıcı editörler grubuna aitse bu sayfaya erişebilir




@login_required
@user_passes_test(is_user_operations)
def users_views(request):
    current_user = request.user

    
    return render(request, 'users.html', {'current_user': current_user})







@login_required
@user_passes_test(is_user_operations)
def user_groups(request):
    users = User.objects.all()
    user_data = []

    for user in users:
        user_groups = user.groups.all()
        groups_data = {group.name: group.name in (g.name for g in user_groups) for group in Group.objects.all()}
        
        if not user.username == 'admin':
            user_data.append({
                'username': user.username,
                'firstname': user.first_name,
                'lastname': user.last_name,
                'groups': groups_data
            })

    return JsonResponse({'users': user_data})





@login_required
@user_passes_test(is_user_operations)
@require_http_methods(["POST"])  # Sadece POST isteklerini kabul eder
def set_user_operations(request):
    data = json.loads(request.body.decode("utf-8"))

    # Veri yapısını kontrol edin
    user_data = data.get('user_data')
    if not user_data:
        return JsonResponse({"error": "Geçersiz veri yapısı."}, status=400)

    for username, permissions in user_data.items():
        try:
            # Kullanıcıyı bul
            user = User.objects.get(username=username.strip())

            # Her grup ve izin için
            for group_name, in_group in permissions.items():
                group, _ = Group.objects.get_or_create(name=group_name)

                if in_group:
                    # Kullanıcıyı gruba ekle
                    group.user_set.add(user)
                else:
                    # Kullanıcıyı gruptan çıkar
                    group.user_set.remove(user)

        except User.DoesNotExist:
            # Kullanıcı bulunamazsa hata döndür
            return JsonResponse({"error": f"Kullanıcı '{username}' bulunamadı."}, status=404)

    return JsonResponse({'message': 'Veriler kaydedildi.'}, status=200)
