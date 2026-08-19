from django.db import models
from apps.base.models import BaseModel
# Create your models here.

class BlogCategory(BaseModel):
    name = models.CharField(max_length=255, verbose_name='Category Name', help_text='The filed is saved blog category name.')
    
    
    class Meta:
        verbose_name = 'BLog Category'
        verbose_name_plural = 'Blog Categories'

    def __str__(self):
        return self.name
    
    
    
class Blog(BaseModel):
    title = models.CharField(max_length=255, verbose_name='Blog Title', help_text='The filed is saved blog title.')
    description = models.TextField(verbose_name='Blog Description', help_text='The filed is saved blog description.')
    image = models.ImageField(upload_to='blog/', null=True, blank=True, verbose_name='Blog Image', help_text='The filed is saved blog image.')
    category = models.ManyToManyField('BlogCategory', through='BlogCategoryBlog', verbose_name='Blog Category', help_text='The filed is saved blog category.')
    
    class Meta:
        verbose_name = 'Blog'
        verbose_name_plural = 'Blogs'
        
    def __str__(self):
        return self.title
    
class BlogCategoryBlog(BaseModel):
    blog = models.ForeignKey(Blog, on_delete=models.SET_NULL, null=True, blank=True, verbose_name='Blog', help_text='The filed is saved blog.')
    blog_category = models.ForeignKey(BlogCategory, on_delete=models.SET_NULL, null=True, blank=True, verbose_name='Blog Category', help_text='The filed is saved blog category.')

    class Meta:
        verbose_name = 'Blog Category Blog'
        verbose_name_plural = 'Blog Category Blogs'
        
        
    def __str__(self):
        return f"{self.blog} - {self.blog_category}"