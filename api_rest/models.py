from django.db import models

class Places(models.Model):
    name = models.CharField(max_length=100, primary_key=True, default='')
    city = models.CharField(max_length=100, default='')
    about = models.CharField(max_length=500, default='')
    visitable = models.BooleanField(default=True)
    foto = models.ImageField(upload_to='fotos/')

    def __str__(self):
        return f'{self.name} | {self.city}'
