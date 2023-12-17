
from django.shortcuts import render
from django.contrib.auth.decorators import login_required

from django.contrib.auth.models import User, Group
from django.http import JsonResponse
from django.contrib.auth.decorators import user_passes_test
import json
from django.views.decorators.http import require_http_methods
from ..models import ParcelWaiting
from django.db.models import Sum
from django.core.mail import send_mail

from django.utils.html import strip_tags

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
        # Kullanıcının grup bilgilerini al
        user_groups = user.groups.all()
        groups_data = {group.name: group.name in (g.name for g in user_groups) for group in Group.objects.all()}
        
        # Kullanıcının bekleyen parsel sayısını al
        waiting_count = ParcelWaiting.objects.filter(user=user).aggregate(Sum('parcel_waiting'))['parcel_waiting__sum'] or 0

        if not user.username == 'admin':
            user_data.append({
                'username': user.username,
                'firstname': user.first_name,
                'lastname': user.last_name,
                'groups': groups_data,
                'waiting_count': waiting_count  # Bekleyen parsel sayısını ekle
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
                # print(group_name, in_group )

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




def check_user_groups(request):
    # Örnek olarak 'current_user'ı alın. Gerçek uygulamada request'ten alabilirsiniz.
    current_user = request.user  # veya User.objects.get(username='kullanıcı_adı')

    # Kontrol edilecek grupların listesi
    group_names = ["user_history", "user_operations", "parcel_edits", "analysis"]

    # Kullanıcının grup üyeliklerini kontrol edin
    user_groups = current_user.groups.values_list('name', flat=True)
    group_membership = {group_name: (group_name in user_groups) for group_name in group_names}

    # Sonucu JSON olarak döndür
    return JsonResponse(group_membership)


@login_required
@user_passes_test(is_user_operations)
@require_http_methods(["POST"])  # Sadece POST isteklerini kabul eder
def set_waiting_counter(request):
    data = json.loads(request.body.decode("utf-8"))

    waiting_data = data.get('waiting_data')
    if not waiting_data:
        return JsonResponse({"error": "Geçersiz veri yapısı."}, status=400)

    for username, waiting_count in waiting_data.items():
        print(username, waiting_count)
        try:
            user = User.objects.get(username=username.strip())
            parcel_waiting, created = ParcelWaiting.objects.get_or_create(user=user)
            parcel_waiting.parcel_waiting = waiting_count
            parcel_waiting.save()
        except User.DoesNotExist:
            continue  # Kullanıcı bulunamazsa, döngüdeki sonraki kullanıcıya geç

    return JsonResponse({'message': 'Veriler kaydedildi.'}, status=200)




@login_required
@user_passes_test(is_user_operations)
def get_current_user_waiting_count(request):
    user = request.user
    parcel_waiting = ParcelWaiting.objects.filter(user=user).first()

    waiting_count = parcel_waiting.parcel_waiting if parcel_waiting else 0

    return JsonResponse({'waiting_count': waiting_count})






def send_email(email, html_message):
    subject = 'NOVAARSA PARSEL İZİN'
    from_email = 'novaarsa.info@gmail.com'
    to = [email]
    plain_message = strip_tags(html_message)  # HTML etiketlerini kaldırarak düz metin sürümünü oluşturur

    send_mail(subject, plain_message, from_email, to, html_message=html_message, fail_silently=False)

@login_required
@user_passes_test(is_user_operations)
@require_http_methods(["POST"])  # Sadece POST isteklerini kabul eder
def set_user_parcel_waiting_permit(request):
    data = json.loads(request.body.decode("utf-8"))

    print(data)
    username = data["name"]
    parcel_name = data["parsel_data"]
    current_user_mail = request.user.email
    html_message = f"""
 <div style="padding: 40px; background-color: #19552b; text-align: center;">
        <h2 style="color: rgb(255, 255, 255);">{username}</h1>
            <h2 style="color: rgb(255, 255, 255);">{parcel_name} adlı parsel için izin istiyor</h2>
            <h2 style="color: rgb(255, 255, 255);"><span style="color: rgb(15, 250, 15);">'Kullanıcı işlemleri'</span> arayüzünden izin verebilirsiniz.</h2>
    </div>"""
    send_email(current_user_mail, html_message)



    return JsonResponse({'message': 'Succes.'}, status=200)