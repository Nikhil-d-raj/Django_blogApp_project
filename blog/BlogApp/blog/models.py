from distutils.command.upload import upload
from platform import release
from pyexpat import model
from tabnanny import verbose
from turtle import title
from unicodedata import category
from unittest.util import _MAX_LENGTH
from django.db import models
from django.contrib.auth.models import User


class Category(models.Model):
    title = models.CharField(max_length=255)
    slug = models.SlugField()

    class Meta():
        ordering = ('title',)
        verbose_name_plural = 'Categories'
    def __str__(self) :
        return self.title



class Post(models.Model):
    category = models.ForeignKey(Category, related_name='posts', on_delete=models.CASCADE)
    title = models.CharField(max_length=255)
    slug = models.SlugField()
    intro = models.TextField()
    body = models.TextField()
    published_at = models.DateTimeField(auto_now_add=True)

    class Meta():
        ordering = ('-published_at',)
    def __str__(self) :
        return self.title

class Comment(models.Model):
    post = models.ForeignKey(Post, related_name='comments', on_delete=models.CASCADE)
    name = models.CharField(max_length=255)
    email = models.EmailField()
    body = models.TextField()
    created_at = models.DateTimeField(auto_now_add=True)
    
    def __str__(self):
        return self.name
class Movie(models.Model):
    title = models.CharField(max_length=255)
    image = models.ImageField(null=True, blank=True, upload_to="images/")
    year = models.DateField()
    plot = models.TextField()
    review = models.TextField(null=True, blank=True)

    def __str__(self):
        return self.title   
class Muser(models.Model):
    user = models.OneToOneField(User, null=True, blank=True, on_delete=models.CASCADE)
    name = models.CharField(max_length=255)
    email = models.EmailField()
    phone = models.CharField(max_length=255, null=True)
    profile_pic = models.ImageField(default="outline_person_black_24dp.png", null=True)
    joined_on = models.DateTimeField()

    def __str__(self):
        return self.name

class Job(models.Model):
    posted_by = models.ForeignKey(Muser, related_name = 'jobs', on_delete = models.CASCADE)
    Job_title = models.CharField(max_length=255)
    description = models.TextField()
    posted_on = models.DateField()
    job_sal = models.IntegerField(null = True, blank = True)
    job_loc = models.CharField(max_length=255)
    job_exp = models.CharField(max_length=200)



