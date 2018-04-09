from django.db import models
from django.utils import timezone
# Create your models here.

class Book(models.Model):
    title = models.CharField(max_length=1000)
    author = models.CharField(max_length=1000)
    folder_number = models.IntegerField()
    publisher = models.CharField(max_length=1000)
    number_of_copies = models.IntegerField()
    specialization = models.CharField(max_length=1000)
    created_date = models.DateTimeField(
            default=timezone.now)

    def publish(self):
        self.published_date = timezone.now()
        self.save()

    def __str__(self):
        return self.title

class Admin:
    list_display = ('title', 'publisher', 'created_date')
    list_filter = ('publisher', 'created_date')
    ordering = ('-created_date',)
    search_fields = ('title',)