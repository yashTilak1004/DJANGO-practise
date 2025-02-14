from django.db import models

# Create your models here.
class members(models.Model):
    f_name = models.CharField(max_length = 300)
    l_name = models.CharField(max_length = 300)
    #new columns
    phone = models.IntegerField(null=True)
    mod_date = models.DateField(null=True)

    def __str__(self):
        return f"{self.f_name} {self.l_name} {self.mod_date}"