from django.db import models

class Stack(models.Model):
    feature_name = models.CharField(max_length=50, unique=True,
                                    verbose_name='Название функции')
    what_do = models.TextField(max_length=1500, verbose_name='Что делает')
    how_did = models.TextField(max_length=1500, verbose_name='Как реализовано')

    def __str__(self):
        return str(self.feature_name).capitalize()

    class Meta():
        db_table='stack'
        verbose_name='Фича'
        verbose_name_plural='Фичи'