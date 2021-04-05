from django.db import models
from django.contrib.auth.models import User
from accounts.models import User
# Create your models here.


class Category(models.Model):
    id = models.BigAutoField(
        primary_key=True
    )
    name = models.CharField(
        max_length=20,
        unique=True,
    )
    description = models.TextField(
        verbose_name='description'
    )
    color=models.CharField(
        max_length=10
    )
    def __str__(self):
        return self.name

class Book(models.Model):
    class Meta:
        db_table='book'

    id =models.BigAutoField(
        primary_key=True
    )
    name=models.CharField(
        max_length=150,
        unique=True,
        verbose_name='Book Name',
    )
    author = models.CharField(
        max_length=70,
        verbose_name='Author',
    )
    price=models.IntegerField(
        verbose_name='Price',
        default=0
    )
    created_on =models.DateTimeField(
        auto_now=True,
    )
    updated_on=models.DateTimeField(
        auto_now=True,
    )

    category=models.ForeignKey(
        to=Category,
        on_delete=models.CASCADE,
        default=1
    )
    user=models.ForeignKey(
        to=User,
        on_delete=models.PROTECT
    )
    

    def __str__(self):
        return self.name