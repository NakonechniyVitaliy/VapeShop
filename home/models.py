from django.db import models


class NewProduct(models.Model):
    # 3
    name = models.CharField(max_length=100)
    about = models.TextField(max_length=500)
    category = models.CharField(max_length=100)
    producer = models.CharField(max_length=100)
    photo = models.FileField(upload_to='home/')
    price = models.FloatField()

    def __str__(self) -> str:
        return str(self.name)
