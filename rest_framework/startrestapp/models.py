from django.db import models

# Create your models here.
class Book(models.Model):
    bid = models.IntegerField(primary_key=True)
    title = models.CharField(max_length=50)
    author = models.CharField(max_length=50)
    category = models.CharField(max_length=50)
    pages = models.IntegerField()
    price = models.IntegerField()
    published_date = models.DateField()
    description = models.TextField()
    
class Chudb(models.Model):
    bid = models.IntegerField(primary_key=True)
    title = models.CharField(max_length=50, blank=True, null=True)
    author = models.CharField(max_length=50, blank=True, null=True)
    category = models.CharField(max_length=50, blank=True, null=True)
    pages = models.IntegerField(blank=True, null=True)
    price = models.IntegerField(blank=True, null=True)
    published_date = models.DateField(blank=True, null=True)
    description = models.TextField(blank=True, null=True)

    class Meta:
        managed = False
        db_table = 'chudb'
