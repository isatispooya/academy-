from django.db import models
from authentication.models import Teacher

class Grouping(models.Model):
    title = models.CharField(max_length=200)
    def __str__(self) :
        return f'{self.title}'
    
    
class Video(models.Model):
    video = models.FileField(upload_to='static/image', null=True, blank=True)
    name = models.CharField(max_length=200)
    time = models.IntegerField()
    def __str__(self) :
        return f'{self.name}'

class Course(models.Model):
    name=models.CharField(max_length=300)
    kind_of_course = [('o','آنلاین'),('v','حضوری'),('d','ویدیویی')]
    course = models.CharField(max_length=1,choices=kind_of_course)
    price = models.CharField(max_length=100)
    # create_at = models.DateTimeField()
    grouping = models.ForeignKey(Grouping,on_delete=models.CASCADE)
    period_of_time = models.IntegerField()
    headline = models.CharField(max_length=800)
    teacher = models.ForeignKey(Teacher, on_delete=models.CASCADE)
    event_place = models.CharField(max_length=100)
    video = models.ForeignKey(Video,on_delete=models.CASCADE, null=True, blank=True)
    def __str__(self) :
        return f'{self.name}'



