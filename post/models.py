from django.db import models
from django.utils.timezone import now
from django.db.models import Q

# Create your models here.
class PostQuerySet(models.QuerySet):
    def search(self, query=None):
        qs = self
        if query is not None:
            or_lookup = (
                         Q(title__icontains = query) |
                         Q(post__icontains=query) |
                         Q(category__category__icontains=query)
                         )
            qs = qs.filter(or_lookup).distinct()  # distinct() is often necessary with Q lookups
        return qs

    def rank_1(self):
        return self.filter(rating='5')


class PostManager(models.Manager):
    def get_queryset(self):
        return PostQuerySet(self.model,using=self._db)

    def search(self,query=None):
        return self.get_queryset().search(query=query)

    def rank_1(self):
        return self.get_queryset().rank_1()



class CategoryQuerySet(models.QuerySet):
    def search(self, query=None):
        qs = self
        if query is not None:
            or_lookup = (
                         Q(category__icontains = query) |
                         Q(date__icontains=query)
                         )
            qs = qs.filter(or_lookup).distinct()  # distinct() is often necessary with Q lookups
        return qs

class CategoryManager(models.Manager):
    def get_queryset(self):
        return CategoryQuerySet(self.model,using=self._db)

    def search(self,query=None):
        return self.get_queryset().search(query=query)

class Category(models.Model):
    category=models.CharField(max_length=50)
    rating=models.IntegerField(default=0)
    date = models.DateTimeField(default=now)

    objects = CategoryManager()

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



