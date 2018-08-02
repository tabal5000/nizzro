# from django import forms

# class ComputerForm(forms.Form):
#     title = forms.CharField(label='Naziv', max_length=128)
#     description = forms.CharField(label='Opis', max_length=2048)
#     serial_number = forms.CharField(label='Serijska številka', max_length=128)
#     #date_created = forms.DateField(label='Leto izdelave')
#     keywords = forms.CharField(label='Ključne besede', max_length=256)

#     """ def clean_datum(self):
#         datum = self.cleaned_data.get('datum')

#         slovenia_holidays = holidays.CountryHoliday('SI')
#         #izpiti_predmeta_datumi = Izpit.objects.filter(predmet_id=self.pk).values_list('datum',flat=True)
#         if datum.weekday() >= 5 or datum in slovenia_holidays:
#             raise forms.ValidationError("Izpit ne sme biti v soboto, nedeljo ali na praznik.")
#         if datum > datetime.date.today():
#             raise forms.ValidationError("Izpitni rok ne sme biti v prihodnost.")
#         return datum

#     def clean_ocena(self):
#         ocena = self.cleaned_data.get('ocena')
#         if ocena < 1 or ocena > 10:
#             raise forms.ValidationError("Ocena mora biti med 1 in 10")
#         return ocena

#     def __init__(self, *args, **kwargs):
#         if kwargs:
#             self.pk = kwargs.pop('pk')
#         super(DirektenVpisOceneForm, self).__init__(*args, **kwargs)
#         nosilci = Nosilci.objects.filter(predmet_leto=self.pk)
#         profesorji = [x.nosilec.id for x in nosilci]
#         self.fields['izprasevalec'].queryset = Profesor.objects.filter(id__in=profesorji) """

from django import forms
from main.models import Computer

class ComputerForm(forms.ModelForm):
    class Meta:
        model = Computer
        fields = ['title','description','serial_number','date_created','keywords']
        widgets = {
            'description' : forms.Textarea(attrs={'rows' : 6, 'placeholder' : 'Tukaj vnesite podatke o komponentah računalnika.'}),
            'serial_number' : forms.TextInput(attrs={'placeholder' : 'Npr. : 601-7577-010B0903273465'}),
            'keywords' : forms.TextInput(attrs={'placeholder' : 'Npr. Intel, AMD, Pentium,...'}),
            'title' : forms.TextInput(attrs={'placeholder' : 'Naziv računalnika'}),
        }
        labels = {
        "title" : "Naziv",
        "description" : "Opis",
        "serial_number" : "Serijska številka",
        "date_created" : "Datum izdelave",
        "keywords" : "Ključne besede",
        }