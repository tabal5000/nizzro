import django_filters
from django import forms
from .models import *

class ListElementsFilter(django_filters.FilterSet):

    syslist_id = django_filters.ModelChoiceFilter(queryset=Lists.objects.all(), empty_label = None,widget=forms.Select(attrs={'class':'ui dropdown','onchange':'this.form.submit()'}))

    class Meta:
        model = ListElements
        fields = ['syslist_id']