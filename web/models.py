from django.db import models

class PortifolioImage(models.Model):
    image = models.ImageField(upload_to='portifolio')

class PortifolioCategory(models.Model):
    name = models.CharField(max_length=255)
    
    def __str__(self) -> str:
        return self.name
    
class Portifolio(models.Model):
    name = models.CharField(max_length=255)
    url = models.CharField(max_length=255)
    image = models.ForeignKey(PortifolioImage, on_delete=models.CASCADE)
    category = models.ForeignKey(PortifolioCategory, on_delete=models.CASCADE)
    
    def __str__(self) -> str:
        return self.name

