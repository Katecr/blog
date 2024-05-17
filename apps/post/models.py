from django.db import models

# Create your models here.
class Post(models.Model):
    title = models.CharField(max_length=255, verbose_name='Title')
    description = models.TextField(verbose_name='Description')
    order = models.IntegerField(verbose_name='Order')
    created_at = models.DateTimeField(auto_now_add=True, verbose_name='Date created')

    def __str__(self):
        return self.title

    class Meta:
        ordering = ['-created_at']