from django.db import models

class Information(models.Model):
    name = models.CharField(max_length=200)
    logo = models.ImageField(upload_to = 'academy/static/mage/',blank = True, null = True)
    logo_text = models.ImageField(upload_to = 'academy/static/mage/',blank = True, null = True)
    telephone1 = models.CharField(max_length=200)
    telephone2 = models.CharField(max_length=200)
    fax = models.CharField(max_length=200)
    email = models.EmailField(blank=True, null=True,unique=True )
    address= models.CharField(max_length=800)
    slider = models.ImageField(upload_to='static/image/', blank=True,null=True)

    def __str__(self) :
        return f'{self.name}'
    
class SliderShow(models.Model):
    slider = models.ImageField(upload_to = 'static/image/',blank = True, null = True)
    title = models.CharField(max_length=200)
    discription = models.CharField(max_length=200)
    url = models.CharField(max_length=200)
    create_at = models.DateField()

    def __str__(self) :
        return f'{self.title}'
    
class Menu(models.model):
    icon = models.ImageField(upload_to='static/image/')
    tilte = models.CharField(max_length=200)
    url = models.CharField(max_length=200)
    
    def __str__(self):
        return f'{self.title}'
