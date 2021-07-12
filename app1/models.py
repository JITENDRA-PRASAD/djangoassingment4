from django.db import models
from django.db.models.deletion import SET_NULL

# Create your models here.
class Author(models.Model):
    first_name = models.CharField(max_length=200)
    last_name = models.CharField(max_length=200)
    email_address = models.EmailField()

    def __str__(self):
        return "{} {}".format(self.first_name,self.last_name)

class Tag(models.Model):
    caption = models.CharField(max_length=200)

    def __str__(self):
        return "{}".format(self.caption)

class Post(models.Model):
    title = models.CharField(max_length=200)
    summary = models.CharField(max_length=200)
    image = models.CharField(max_length=200)
    date = models.DateTimeField(auto_now=True)
    slug = models.SlugField()
    content = models.TextField()
    author = models.ForeignKey(Author,on_delete=SET_NULL, null=True)
    tag = models.ManyToManyField(Tag)
    
    
    def __str__(self):
        return "{} ".format(self.title)

class Comment(models.Model):
    user_name = models.CharField(max_length=200, unique=True)
    user_email = models.CharField(max_length=200)
    text = models.CharField(max_length=200)
    post = models.ForeignKey(Post, on_delete=SET_NULL, null=True)

    def __str__(self):
        return "{}".format(self.post)
    
    