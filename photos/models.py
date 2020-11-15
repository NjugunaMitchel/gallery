from django.db import models

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
    photo_image = models.ImageField(upload_to = 'photos/',default="url_for('image.jpg')")


    @classmethod
    def search_by_category(cls,search_term):
        photo = cls.objects.filter(category__icontains=search_term)
        return photo