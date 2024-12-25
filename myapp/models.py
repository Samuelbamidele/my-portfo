from django.db import models

# Create your models here.

# Portfolio Model

class Project(models.Model):
    title = models.CharField(max_length=200)  # Project title
    description = models.TextField(blank=True)  # Optional description
    image = models.ImageField(upload_to='portfolio_images/')  # Project image
    link = models.URLField(blank=True)  # Optional link to project or more details

    def __str__(self):
        return self.title


# Blog Model

class Blog(models.Model):
    title = models.CharField(max_length=200)  # Blog title
    description = models.TextField(blank=True)  # Blog description
    date = models.DateField(auto_now_add=True, null=True)  # Blog date (auto-added)
    image = models.ImageField(upload_to='blog_images/', blank=True, null=True, default='images/blog-img1.png')  # New image field
    link = models.URLField(max_length=300, blank=True, null=True)  # Field for an optional external link
    def __str__(self):
        return self.title



# Services Model
#class Service(models.Model):
    #title = models.CharField(max_length=200)
    #image = models.ImageField(upload_to='blog_images/')
    #description = models.TextField()

    #def __str__(self):
        #return self.title

# About Model (for dynamic about section)

class AboutMe(models.Model):
    content = models.TextField()
    resume = models.FileField(upload_to='resumes/', default='Not providede')

    def __str__(self):
        return "About Me"
