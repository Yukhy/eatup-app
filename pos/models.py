from django.db import models
from django.db.models.signals import post_save
from django.dispatch import receiver
from django.core.exceptions import ObjectDoesNotExist
from django.contrib.auth.models import User


# Create your models here.
class Pos(models.Model):
    name = models.CharField(max_length=50)
    price = models.IntegerField()
    best_effort = models.DateField(null=True, blank=True) # 賞味期限
    used_by = models.DateField(null=True, blank=True) # 消費期限
    # 画像まだない

class Cart(models.Model):
    user = models.ForeignKey(User, on_delete=models.CASCADE, related_name='cart')
    pos = models.ManyToManyField(Pos, blank=True)
    count = models.IntegerField(default=1)
    is_checked_out = models.BooleanField(default=False)