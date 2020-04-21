from django.contrib.auth.models import User
from django.db import models


class Hero(models.Model):
    STATUS_CHOICES = (
        ('draft', 'Druft'),
        ('published', 'Public')
    )
    nickname = models.CharField(max_length=128, verbose_name='Nickname')
    real_name = models.CharField(max_length=128, verbose_name='Real name')
    origin_description = models.TextField(blank=True, max_length=330, verbose_name='Origin Description')
    superpowers = models.TextField(blank=True, max_length=330, verbose_name='Superpowers')
    catch_phrase = models.TextField(blank=True, max_length=330, verbose_name='Catch phrase')
    status = models.CharField(max_length=10, choices=STATUS_CHOICES, default='published', verbose_name='Public?')
    images = models.ImageField(upload_to='images/', null=True, blank=True, verbose_name='Image main')
    img1 = models.ImageField(upload_to='images/', null=True, blank=True, verbose_name='Image 1')
    img2 = models.ImageField(upload_to='images/', null=True, blank=True, verbose_name='Image 2')
    img3 = models.ImageField(upload_to='images/', null=True, blank=True, verbose_name='Image 3')
    img4 = models.ImageField(upload_to='images/', null=True, blank=True, verbose_name='Image 4')
    img5 = models.ImageField(upload_to='images/', null=True, blank=True, verbose_name='Image 5')
    img6 = models.ImageField(upload_to='images/', null=True, blank=True, verbose_name='Image 6')
    img7 = models.ImageField(upload_to='images/', null=True, blank=True, verbose_name='Image 7')
    img8 = models.ImageField(upload_to='images/', null=True, blank=True, verbose_name='Image 8')
    img9 = models.ImageField(upload_to='images/', null=True, blank=True, verbose_name='Image 9')
    img10 = models.ImageField(upload_to='images/', null=True, blank=True, verbose_name='Image 10')

    class Meta:
        verbose_name_plural = 'Superheroes'
        verbose_name = 'Superheroes'

    def __str__(self):
        return self.nickname