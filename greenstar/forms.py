from .models import portfolio
from django.forms import ModelForm, TextInput, DateInput, Textarea
class portfolioFrom(ModelForm):
    class Meta:
        model = portfolio
        fields = [
            'logo','fio','school','objects_school','date','biograf',
            'diploma1','diploma2','diploma3','diploma4','diploma5','diploma6','diploma7','diploma8',
            'education','experience','qualif'
        ]
        widgets = {
            'logo': TextInput(attrs={'class': 'form-control mb-2','placeholder': 'Ссылка на ваш логотип'}),
            'fio': TextInput(attrs={'class': 'form-control mb-2','placeholder': 'Фамилия имя отчество'}),
            'school': TextInput(attrs={'class': 'form-control mb-2','placeholder': 'Школа'}),
            'objects_school': TextInput(attrs={'class': 'form-control mb-2','placeholder': 'Предмет'}),
            'date': DateInput(attrs={'class': 'form-control mb-2','placeholder': 'Дата год-месяц-день (2022-06-17)'}),
            'biograf': Textarea(attrs={'class': 'form-control mb-2','placeholder': 'Биография','rows': '3'}),
            'diploma1': TextInput(attrs={'class': 'form-control mb-2','placeholder': 'Ссылка на диплом 1', 'id': 'example1'}),
            'diploma2': TextInput(attrs={'class': 'form-control mb-2','placeholder': 'Ссылка на диплом 2', 'id': 'example1'}),
            'diploma3': TextInput(attrs={'class': 'form-control mb-2','placeholder': 'Ссылка на диплом 3', 'id': 'example1'}),
            'diploma4': TextInput(attrs={'class': 'form-control mb-2','placeholder': 'Ссылка на диплом 4', 'id': 'example1'}),
            'diploma5': TextInput(attrs={'class': 'form-control mb-2','placeholder': 'Ссылка на диплом 5', 'id': 'example1'}),
            'diploma6': TextInput(attrs={'class': 'form-control mb-2','placeholder': 'Ссылка на диплом 6', 'id': 'example1'}),
            'diploma7': TextInput(attrs={'class': 'form-control mb-2','placeholder': 'Ссылка на диплом 7', 'id': 'example1'}),
            'diploma8': TextInput(attrs={'class': 'form-control mb-2','placeholder': 'Ссылка на диплом 8', 'id': 'example1'}),
            'education': TextInput(attrs={'class': 'form-control mb-2','placeholder': 'Образование'}),
            'experience': TextInput(attrs={'class': 'form-control mb-2','placeholder': 'Стаж работы'}),
            'qualif': TextInput(attrs={'class': 'form-control mb-2','placeholder': 'Повышение квалификации'}),
        }