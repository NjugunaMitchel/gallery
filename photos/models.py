from django.db import models
from cloudinary.models import CloudinaryField

# Create your models here.

class Editor(models.Model):
    username = models.CharField(max_length =30)
    email = models.EmailField()


    def __str__(self):
        return self.username

    def save_new_editor(self):
        self.save()

    class Meta:
        ordering=['username']


#categories
class category(models.Model):
    name = models.CharField(max_length =255)

    def __str__(self):
        return self.name

#Photo post
class Pictures(models.Model):
    title = models.CharField(max_length =60)
    editor = models.ForeignKey(Editor,on_delete=models.CASCADE)
    category = models.ManyToManyField(category)
    photo_image = CloudinaryField('image')
    info=models.TextField(max_length=255, default="picture details")


    @classmethod
    def search_by_category(cls,search_term):
        photos = cls.objects.filter(title__icontains=search_term)
        return photos