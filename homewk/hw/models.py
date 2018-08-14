from django.db import models

# Create your models here.
class huluwa(models.Model):
    name=models.CharField(
        max_length=30,
        verbose_name="名字"
    )
    atrribute=models.CharField(
        max_length=30,
        verbose_name="属性"
    )
    birthday=models.DateField(
    auto_now_add=True,
        verbose_name="出生日期"
    )
    height=models.IntegerField(
        default=170,
        verbose_name='身高'
    )
    skill=models.CharField(
        max_length=400,
        verbose_name="技能"

    )
    class  Meta:
        db_table="calabash_boy"
