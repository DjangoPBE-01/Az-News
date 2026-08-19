from django.db import models

from apps.base.models import BaseModel
from django_ckeditor_5.fields import CKEditor5Field

# Create your models here.

class NewsCategory(BaseModel):
    name = models.CharField(max_length=255, verbose_name='Category Name', help_text='The filed is saved news category name.')
    
    class Meta:
        verbose_name = 'News Category'
        verbose_name_plural = 'News Categories'
        
    
    def __str__(self):
        return self.name

class News(BaseModel):
    title = models.CharField(max_length=255, verbose_name='News Title', help_text='The filed is saved news title.')
    description = models.TextField(verbose_name='News Description', help_text='The filed is saved news description.')
    image = models.ImageField(upload_to='news/', null=True, blank=True, verbose_name='News Image', help_text='The filed is saved news image.')
    content = CKEditor5Field('Content', config_name='extends')
    category = models.ForeignKey(NewsCategory, on_delete=models.SET_NULL, null=True, blank=True, verbose_name='News Category', help_text='The filed is saved news category.')
    
    
    class Meta:
        verbose_name = 'News'
        verbose_name_plural = 'News'
        
        
    def __str__(self):
        return self.title
    
    
