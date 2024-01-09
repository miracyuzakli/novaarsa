from django.contrib.auth.models import Group


# Grup adını ve isteğe bağlı olarak izinleri belirtin
group_name = "user_history"
group, created = Group.objects.get_or_create(name=group_name)
if created:
    print(f"Grup '{group_name}' başarıyla oluşturuldu.")

# Grup adını ve isteğe bağlı olarak izinleri belirtin
group_name = "user_operations"
group, created = Group.objects.get_or_create(name=group_name)
if created:
    print(f"Grup '{group_name}' başarıyla oluşturuldu.")

group_name = "parcel_edits"
group, created = Group.objects.get_or_create(name=group_name)
if created:
    print(f"Grup '{group_name}' başarıyla oluşturuldu.")

group_name = "analysis"
group, created = Group.objects.get_or_create(name=group_name)
if created:
    print(f"Grup '{group_name}' başarıyla oluşturuldu.")
