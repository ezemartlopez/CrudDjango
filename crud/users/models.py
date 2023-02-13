from django.db import models
USER_TYPE =(
    ('Admin','admin'),
    ('User','user'),
    ('Editor','editor'),

)
# Create your models here.
class User(models.Model):
    name = models.CharField(max_length=30, blank=False, null= False)
    last_name = models.CharField(max_length=30, blank=False, null= False)
    email = models.EmailField(max_length=80)
    active = models.BooleanField(default=True)
    type_user = models.CharField(max_length=9, choices=USER_TYPE, default='User')
    photo = models.ImageField(upload_to='images/',default='images/default/no-img.jpg')
    date_created = models.DateField(auto_now=True)
    def __str__(self) -> str:
        return f"{self.name} {self.last_name}"

    def get_date(self):
        return f"{self.date_created.day}/{self.date_created.month}/{self.date_created.year}"