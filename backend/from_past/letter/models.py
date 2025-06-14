from django.core.exceptions import ValidationError
from django.db import models
from users.models import User
from datetime import date

# Create your models here.
def validate_today_date(value):
    if value == date.today():
       raise ValidationError('Нельзя установить сегодняшнюю дату') 

class Letter(models.Model):
    user = models.ForeignKey(User, on_delete=models.CASCADE, verbose_name='Пользователь')
    for_who = models.CharField(max_length=200, verbose_name='Кому')
    from_who = models.CharField(max_length=200, verbose_name='От кого')
    letter_text = models.TextField(verbose_name='Текст письма')
    date_arrival = models.DateField(validators=[validate_today_date])

    def is_date_arrival(self):
        if self.date_arrival == date.today():
            return True
        return False

    def __str__(self):
        return f'Письмо в будущее №{self.pk}'

    class Meta:
        verbose_name = 'Письмо'
        verbose_name_plural = 'Письма'
