from django.db import models
from django.utils.deconstruct import deconstructible
import base64
import os
import PIL

@deconstructible
class PathAndRename(object):

    def __init__(self, sub_path):
        self.path = sub_path

    def __call__(self, instance, filename):
        ext = filename.split('.')[-1]
        fn = filename.split('.')[0]
        b = bytes(fn, 'utf-8')
        file_name_string = base64.urlsafe_b64encode(b)
        # set filename as random string
        filename = '{}.{}'.format(file_name_string, ext)
        # return the whole path to the file
        return os.path.join(self.path, filename)

path_and_rename = PathAndRename("")

# Create your models here.
class Profile(models.Model):
    first_name = models.CharField(max_length=25)
    last_name = models.CharField(max_length=25)
    city = models.CharField(max_length=25)
    state = models.CharField(max_length=2)
    resume = models.FileField(upload_to=path_and_rename,
                              blank=True,
                              null=True)
    profile_image = models.ImageField(upload_to=path_and_rename,
                                      blank=True,
                                      null=True)
    # list of titles
    title = models.ManyToManyField('Titles', related_name='profile_titles')
    projects = models.ManyToManyField('Project', related_name='projects')
    about = models.TextField(null=True, blank=False)

    def __str__(self):
        return "%s %s"%(self.first_name, self.last_name)

    def address(self):

        return "%s, %s"%(self.city, self.state)

    def list_titles(self):
        l = [title for title in self.title.all()]
        return l
    def list_projects(self):
        l = [title for title in self.projects.all()]
        return l

class Titles(models.Model):
    title = models.CharField(max_length=30)

    def __str__(self):
        return self.title

class Project(models.Model):
    proj_title = models.CharField(max_length=20, unique=True)
    description = models.TextField(null=False, blank=True)
    date = models.DateField()
    language = models.ManyToManyField('Language')
    icon = models.ImageField(upload_to=path_and_rename)
    link = models.URLField(null=True, blank=True)

    def list_languages(self):
        l = [title for title in self.language.all()]
        return l


    def __str__(self):
        return self.proj_title

class Language(models.Model):
    name = models.CharField(max_length=25)

    def __str__(self):
        return self.name

class Contact(models.Model):
    name = models.CharField(max_length=75)
    phone = models.CharField(max_length=20)
    email = models.EmailField()
    message = models.TextField()
    date = models.DateTimeField()

    def __str__(self):
        return "%s %s"%(self.name, self.date)

class Analytics(models.Model):
    request_ip = models.CharField(max_length=10)
    func = models.CharField(max_length=50)
    date = models.DateTimeField()
