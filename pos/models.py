from django.db import models

# Create your models here.
class Pos(models.Model):
    pos_number = models.IntegerField()
    item_name = models.CharField(max_length=50)

class Eatup_db(models.Model):
    pos = models.OneToOneField(Pos, on_delete=models.CASCADE, related_name='eatip_db')
    best_effort = models.DateField(null=True) # 賞味期限
    used_by = models.DateField(null=True) # 消費期限
