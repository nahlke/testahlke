from django import forms

class Person(forms.Form):
    name = forms.CharField(label='Dein Name', max_length = 30)
    alter = forms.IntegerField(label='Dein Alter')