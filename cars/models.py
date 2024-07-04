from django.db import models


class Car(models.Model):
    name = models.CharField(max_length=150)
    color = models.CharField(max_length=150)
    year = models.IntegerField()
    price = models.IntegerField()
    description = models.TextField()
    photo = models.ImageField(upload_to='cars/images/')
    is_active = models.BooleanField(default=True)

    def __str__(self):
        return self.name

    class Meta:
        ordering = ['id']
        verbose_name = 'Car'
        verbose_name_plural = 'Cars'


class Booking(models.Model):
    user = models.ForeignKey('auth.User', on_delete=models.CASCADE)
    car = models.ForeignKey(Car, on_delete=models.CASCADE)

    def __str__(self):
        return f"{self.user} booked {self.car}"

