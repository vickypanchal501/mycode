from django.db import models

class subject(models.Model):
    Hindi= models.IntegerField()
    English= models.IntegerField()
    Chemistry= models.IntegerField()
    Maths= models.IntegerField()
    physics= models.IntegerField()
    


class names(models.Model):
    name = models.CharField(max_length=125, null=True)
    class1 = models.IntegerField(null=True)
    date_created = models.DateTimeField(auto_now_add=True, null=True)

    