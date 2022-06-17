from django.db import models

class portfolio(models.Model):
    logo = models.CharField('Логотип', max_length=150)
    fio = models.CharField('ФИО', max_length=150)
    school = models.CharField('Школа', max_length=150)
    objects_school = models.CharField('Предмет', max_length=150)
    date = models.DateField('Дата')
    biograf = models.TextField('Биография')
    diploma1 = models.CharField('Дипломы1', max_length=150, blank=True)
    diploma2 = models.CharField('Дипломы2', max_length=150, blank=True)
    diploma3 = models.CharField('Дипломы3', max_length=150, blank=True)
    diploma4 = models.CharField('Дипломы4', max_length=150, blank=True)
    diploma5 = models.CharField('Дипломы5', max_length=150, blank=True)
    diploma6 = models.CharField('Дипломы6', max_length=150, blank=True)
    diploma7 = models.CharField('Дипломы7', max_length=150, blank=True)
    diploma8 = models.CharField('Дипломы8', max_length=150, blank=True)
    education = models.CharField('Образование', max_length=150)
    experience = models.CharField('Стаж работы', max_length=150)
    qualif = models.CharField('Повышение квалификации', max_length=150)

    def __str__(self):
        return self.fio
    
    class Meta:
        verbose_name = 'Портволио'
        verbose_name_plural = 'Портволио'