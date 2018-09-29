from django.db import models
from django.utils.timezone import now
from django.utils.text import slugify
from django.db.models.signals import pre_save

# Create your models here.
class PostQuerySet(models.QuerySet):
    def rank_1(self):
        return self.filter(rating='5')


class PostManager(models.Manager):
    def get_queryset(self):
        return PostQuerySet(self.model,using=self._db)

    def rank_1(self):
        return self.get_queryset().rank_1()


    # def rank_1(self):
    #     return self.get_queryset().rank_1()

class Category(models.Model):
    category=models.CharField(max_length=50)
    rating=models.IntegerField(default=0)
    date = models.DateTimeField(default=now)

    def __str__(self):
        return self.category

class Post(models.Model):
    category=models.ForeignKey(Category,on_delete=models.CASCADE)
    title=models.CharField(max_length=500,blank=True)
    post = models.TextField(blank=True)
    post_para_2 = models.TextField(blank=True)
    post_para_3 = models.TextField(blank=True)
    captions=models.TextField(blank=True)
    captions_para_2 = models.TextField(blank=True)
    captions_para_3 = models.TextField(blank=True)
    quote=models.CharField(max_length=200,blank=True)
    quote_by=models.CharField(max_length=100,blank=True)
    image=models.ImageField(upload_to='post_image/%Y/%m/%d/',blank=True)
    date= models.DateTimeField(default=now)
    related_post_1 = models.CharField(max_length=100,blank=True)
    related_link_1 = models.CharField(max_length=100,blank=True)
    related_post_2 = models.CharField(max_length=100,blank=True)
    related_link_2 = models.CharField(max_length=100,blank=True)
    related_post_3 = models.CharField(max_length=100,blank=True)
    related_link_3 = models.CharField(max_length=100,blank=True)
    rating=models.IntegerField(default=0)

    slug =models.SlugField(unique=True,max_length=100)


    objects=PostManager()

    def __str__(self):
        return self.title

def create_slug(instance,new_slug=None):
    slug=slugify(instance.title)
    if new_slug is not None:
        slug=new_slug
    qs =Post.objects.filter(slug=slug).order_by("-id")
    exist=qs.exist()
    if exist:
        new_slug="%s-%s"%(instance.title,qs.first().id)
        return create_slug(instance,new_slug)
    return slug

def pre_save_post_receiver(sender,instance,*args,**kwargs):
    if not instance.slug:
        instance.slug=create_slug(instance)


    # slug=slugify(instance.title)
    # exist=Post.objects.filter(slug=slug).exist()
    # if exist:
    #     slug="%s-%s"%(slug,instance.id)
    # instance.slug=slug


pre_save.connect(pre_save_post_receiver,sender=Post)


