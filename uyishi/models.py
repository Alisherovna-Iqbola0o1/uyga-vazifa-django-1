from django.db import models

# Create your models here.


class Haftakun(models.Model):
    nomi = models.CharField(max_length=100)
    dam_olish = models.BooleanField(default=False)
    created_at = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return self.nomi


class Kurs(models.Model):
    nomi = models.CharField(max_length=150)
    narxi = models.DecimalField(max_digits=10, decimal_places=2)
    aktivligi = models.BooleanField(default=True)
    boshlanish_sanasi = models.DateTimeField()
    tugash_vaqti = models.DateTimeField()
    oquvchilar_soni = models.IntegerField()
    rasmi = models.ImageField(upload_to="kurslar/")
    yaratilgan_vaqt = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return self.nomi


class Oquvchi(models.Model):
    ismi = models.CharField(max_length=150)
    familya = models.CharField(max_length=150)
    yosh = models.IntegerField()
    rasmi = models.ImageField(upload_to="oquvchilar/")
    maktabda_oqiydimi = models.BooleanField(default=True)
    yaratilgan_vaqt = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return self.ismi
