from django.core.management.base import BaseCommand
from django.contrib.auth.models import Group, Permission
from django.contrib.contenttypes.models import ContentType
from app.models import ParcelUserHistory  # myapp, projenizin uygulama adına göre değişmelidir

class Command(BaseCommand):
    help = 'Create a user history group with permissions'

    def handle(self, *args, **kwargs):
        # Grup oluşturma
        group, created = Group.objects.get_or_create(name='Kullanici_Islem_Gecmisi')

        # Model ve izinleri al
        content_type = ContentType.objects.get_for_model(ParcelUserHistory)
        view_permission = Permission.objects.get(codename='view_parceluserhistory')

        # Gruba izinleri ekleme
        group.permissions.add(view_permission)
        group.save()
