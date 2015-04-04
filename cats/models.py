from django.db import models

class Cat(models.Model):
    name     = models.CharField(max_length=50)
    fluffy   = models.BooleanField()
    pettable = models.BooleanField()
    adopted  = models.BooleanField(default=False)
    color    = models.CharField(max_length=30)
    age      = models.IntegerField()
    blurb    = models.TextField(max_length=5000, default="")
    pict_url = models.CharField(max_length=500, default="")

    def adopt(self):
        self.adopted = True
        self.save()

    def __str__(self):
        return self.name



# Create your models here.
