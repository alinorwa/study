from django.db import models
from django.utils.text import slugify
from django.contrib.auth.models import User

# Create your models here.
class Category(models.Model):
    name=models.CharField(max_length=150,db_index=True)
    slug=models.SlugField(unique=True,blank=True)
    class Meta:
        ordering=('-name',)
    def __str__(self):
        return self.name

    def save(self,*args,**kwargs):
        self.slug  = slugify(self.name)
        super(Category,self).save(*args,**kwargs) 

    

class Post(models.Model):
    options = (
        ('draft', 'Draft'),
        ('published', 'Published'),
    )
    category   = models.ForeignKey(Category,on_delete=models.CASCADE)
    title      = models.CharField(max_length=200)
    body       = models.TextField(db_index=True)
    img        = models.ImageField(upload_to='img/',blank=True,null=True)
    status     = models.CharField(max_length=10, choices=options, default='published')
    author     = models.ForeignKey(User, on_delete=models.CASCADE, related_name='blog_posts_author')
    likes      = models.ManyToManyField( User, related_name='like', default=None, blank=True)
    like_count = models.BigIntegerField(default='0')
    date       = models.DateTimeField(auto_now_add=True)
    class Meta:
        ordering=('-title',)
    def __str__(self):
        return self.title   
    

class Comment(models.Model):
    post   = models.ForeignKey(Post, related_name='comments' , on_delete=models.CASCADE)
    user   = models.ForeignKey(User, related_name='user_comment' , on_delete=models.CASCADE)
    body   = models.TextField()
    create = models.DateTimeField(auto_now_add=True)

    def __str__(self) -> str:
        return self.user.username + ' | ' + self.post.title 
    

class Contact(models.Model):
    name    = models.CharField(max_length=200)
    email   = models.EmailField()
    message = models.TextField()
    def __str__(self):
         return self.name 