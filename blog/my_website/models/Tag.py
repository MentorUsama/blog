from django.db import models
class Tag(models.Model):
    caption=models.CharField(max_length=20)
    def __str__(self):
        return f'{self.caption}'