from django.db import models
# Create your models here.


class BaseModel(models.Model):
    create_time = models.DateTimeField(auto_now_add=True)
    update_time = models.DateTimeField(auto_now=True)

    class Meta(object):
        abstract = True


class Student(BaseModel):
    id = models.AutoField(primary_key=True)
    name = models.CharField(max_length=20)
    age = models.IntegerField(default=20)
    birthday = models.DateField(default='2024-04-30')
    ismarired = models.BooleanField(default=False)

    class Meta:
        db_table = 'student'


    def __str__(self):
        return self.name
