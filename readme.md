# NOVAARSA


### Proje gereksinimleri:
* Python3.10 ve üzeri versiyonlar.


### Proje başlatma

Proje klasörüne girdikten sonra teminal içerisine sanal ortam oluşturma

windows için
```
python -m venv env 
env/bin/activate

```
linux/macOs için
```
python3 -m venv env 
source env/bin/activate

```

sanal ortamı aktive ettikten sonra proje için gerekli modülleri yüklememiz gerek, bunun için;

```
pip install -r requirements.txt

```

yükleme başarıyla tamamlandıktan sonra projeyi başlatmamız gerek


windows için
```
python manage.py runserver 0.0.0.0:8000

```
linux/macOs için
```
python3 manage.py runserver 0.0.0.0:8000

```

Proje başlatıldıktan sonra kullanılan `https://ip_adresi:8000` portundan web sayfasına giriş yapılabilir.

<hr>

# Mail Konfigürasyonu

`novaarsa/settings.py` içerisinde en alt kısımda 

```
EMAIL_BACKEND = 'django.core.mail.backends.smtp.EmailBackend'
EMAIL_HOST = 'smtp.gmail.com'
EMAIL_PORT = 587
EMAIL_USE_TLS = True
EMAIL_HOST_USER = 'sizinemail@gmail.com'  # Gmail adresiniz
EMAIL_HOST_PASSWORD = 'sizinşifreniz'     # Gmail şifreniz veya uygulama şifreniz

```
gerekli bilgilerin girilmesi.