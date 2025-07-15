from django.db import models
from cloudinary.models import CloudinaryField

class About(models.Model):
    title = models.CharField(max_length=200)
    content1 = models.TextField()
    content2 = models.TextField()
    image1 = CloudinaryField('image', blank=True, null=True)
    image2 = CloudinaryField('image', blank=True, null=True)
    added_on = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return self.title

    class Meta:
        verbose_name_plural = "About Us"


class Service(models.Model):
    title = models.CharField(max_length=200)
    description = models.TextField()
    image = CloudinaryField('image')

    def __str__(self):
        return self.title

    class Meta:
        verbose_name_plural = "Our Services"


class Project(models.Model):
    text1 = models.CharField(max_length=200)
    text2 = models.CharField(max_length=200)
    image = CloudinaryField('image')

    def __str__(self):
        return self.text1

    class Meta:
        verbose_name_plural = "Our Projects"


class Testimonial(models.Model):
    client_name = models.CharField(max_length=200)
    profession = models.CharField(max_length=200)
    image = CloudinaryField('image')
    stars = models.IntegerField(default=0)
    comment = models.TextField(default='')

    def __str__(self):
        return self.client_name

    class Meta:
        verbose_name_plural = "Our Testimonials"


class Team(models.Model):
    full_name = models.CharField(max_length=100)
    designation = models.CharField(max_length=100)
    image = CloudinaryField('image')
    twitter_link = models.URLField(blank=True)
    instagram_link = models.URLField(blank=True)
    linkedin_link = models.URLField(blank=True)

    def __str__(self):
        return self.full_name

    class Meta:
        verbose_name_plural = "Our Team"


class Blog(models.Model):
    title = models.CharField(max_length=200)
    content = models.TextField()
    image = CloudinaryField('image')
    category = models.CharField(max_length=100)
    author = models.CharField(max_length=100)
    author_image = CloudinaryField('image')
    date_published = models.DateField(auto_now_add=True)

    def __str__(self):
        return self.title

    class Meta:
        verbose_name_plural = "Our Blog"


class Contact(models.Model):
    name = models.CharField(max_length=250)
    email = models.EmailField()
    number = models.CharField(max_length=12)
    message = models.TextField()
    added_on = models.DateTimeField(auto_now_add=True)
    is_approve = models.BooleanField(default=True)

    def __str__(self):
        return self.name

    class Meta:
        verbose_name_plural = "Contact Table"


class User(models.Model):
    username = models.CharField(max_length=100, unique=True)
    password = models.CharField(max_length=100)
    email = models.EmailField(unique=True)

    def __str__(self):
        return self.username

    class Meta:
        verbose_name_plural = "Registration Table"
