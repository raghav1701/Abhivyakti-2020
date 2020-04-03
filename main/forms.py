from django import forms
from .models import *


class AgtForm(forms.ModelForm):
    name = forms.CharField(widget=forms.TextInput(
        attrs ={
            'class':"input--style-3",
             'type' : "text",
              'placeholder': "Name",
               'name':"name",
        }
    ))
    email = forms.CharField(widget=forms.TextInput(
        attrs={
            'class': "input--style-3",
            'type': "text",
            'placeholder': "Email",
            'name': "email",
        }
    ))
    college = forms.CharField(widget=forms.TextInput(
        attrs={
            'class': "input--style-3",
            'type': "text",
            'placeholder': "College",
            'name': "college",
        }
    ))
    contactno = forms.CharField(widget=forms.TextInput(
        attrs={
            'class': "input--style-3",
            'type': "text",
            'placeholder': "Phone",
            'name': "contactno",
        }
    ))
    perform = forms.CharField(widget=forms.TextInput(
        attrs={
            'class': "input--style-3",
            'type': "text",
            'placeholder': "Type of Performance",
            'name': "perform",
        }
    ))
    class Meta:
        model = Agt
        fields = ['name', 'college', 'email', 'contactno', 'perform']


class BigRoarForm(forms.ModelForm):
    name = forms.CharField(widget=forms.TextInput(
        attrs={
            'class': "input--style-3",
            'type': "text",
            'placeholder': "Name",
            'name': "name",
        }
    ))
    email = forms.CharField(widget=forms.TextInput(
        attrs={
            'class': "input--style-3",
            'type': "text",
            'placeholder': "Email",
            'name': "email",
        }
    ))
    college = forms.CharField(widget=forms.TextInput(
        attrs={
            'class': "input--style-3",
            'type': "text",
            'placeholder': "College",
            'name': "college",
        }
    ))
    contactno = forms.CharField(widget=forms.TextInput(
        attrs={
            'class': "input--style-3",
            'type': "text",
            'placeholder': "Phone",
            'name': "contactno",
        }
    ))

    class Meta:
        model = BigRoar
        fields = ('name', 'college', 'email', 'contactno')


class AntraForm(forms.ModelForm):
    name = forms.CharField(widget=forms.TextInput(
        attrs={
            'class': "input--style-3",
            'type': "text",
            'placeholder': "Name",
            'name': "name",
        }
    ))
    email = forms.CharField(widget=forms.TextInput(
        attrs={
            'class': "input--style-3",
            'type': "text",
            'placeholder': "Email",
            'name': "email",
        }
    ))
    college = forms.CharField(widget=forms.TextInput(
        attrs={
            'class': "input--style-3",
            'type': "text",
            'placeholder': "College",
            'name': "college",
        }
    ))
    contactno = forms.CharField(widget=forms.TextInput(
        attrs={
            'class': "input--style-3",
            'type': "text",
            'placeholder': "Phone",
            'name': "contactno",
        }
    ))
    class Meta:
        model = Antra
        fields = ('name', 'college', 'email', 'contactno')


class CraftixForm(forms.ModelForm):
    name = forms.CharField(widget=forms.TextInput(
       attrs={
           'class': "input--style-3",
           'type': "text",
           'placeholder': "Name",
           'name': "name",
       }
   ))
    email = forms.CharField(widget=forms.TextInput(
       attrs={
           'class': "input--style-3",
           'type': "text",
           'placeholder': "Email",
           'name': "email",
       }
   ))
    college = forms.CharField(widget=forms.TextInput(
       attrs={
           'class': "input--style-3",
           'type': "text",
           'placeholder': "College",
           'name': "college",
       }
   ))
    contactno = forms.CharField(widget=forms.TextInput(
       attrs={
           'class': "input--style-3",
           'type': "text",
           'placeholder': "Phone",
           'name': "contactno",
       }
    ))

    class Meta:
        model = Craftix
        fields = ('name', 'college', 'email', 'contactno')

class KavyanForm(forms.ModelForm):
    name = forms.CharField(widget=forms.TextInput(
        attrs={
            'class': "input--style-3",
            'type': "text",
            'placeholder': "Name",
            'name': "name",
        }
    ))
    email = forms.CharField(widget=forms.TextInput(
        attrs={
            'class': "input--style-3",
            'type': "text",
            'placeholder': "Email",
            'name': "email",
        }
    ))
    college = forms.CharField(widget=forms.TextInput(
        attrs={
            'class': "input--style-3",
            'type': "text",
            'placeholder': "College",
            'name': "college",
        }
    ))
    contactno = forms.CharField(widget=forms.TextInput(
        attrs={
            'class': "input--style-3",
            'type': "text",
            'placeholder': "Phone",
            'name': "contactno",
        }
    ))
    class Meta:
        model = kavyanjali
        fields = ('name', 'college', 'email', 'contactno')


class TalkForm(forms.ModelForm):
    name = forms.CharField(widget=forms.TextInput(
        attrs={
            'class': "input--style-3",
            'type': "text",
            'placeholder': "Name",
            'name': "name",
        }
    ))
    email = forms.CharField(widget=forms.TextInput(
        attrs={
            'class': "input--style-3",
            'type': "text",
            'placeholder': "Email",
            'name': "email",
        }
    ))
    college = forms.CharField(widget=forms.TextInput(
        attrs={
            'class': "input--style-3",
            'type': "text",
            'placeholder': "College",
            'name': "college",
        }
    ))
    contactno = forms.CharField(widget=forms.TextInput(
        attrs={
            'class': "input--style-3",
            'type': "text",
            'placeholder': "Phone No.",
            'name': "contactno",
        }
    ))
    topic = forms.CharField(widget= forms.TextInput(
        attrs={
            'class': "input--style-3",
            'type': "text",
            'placeholder': "Topic",
            'name': "topic",
        }
    ))

    class Meta:
        model = TalkMasters
        fields = ('name', 'college', 'email', 'contactno', 'topic')

class ToTheBeatForm(forms.ModelForm):
    name = forms.CharField(widget=forms.TextInput(
        attrs={
            'class': "input--style-3",
            'type': "text",
            'placeholder': "Name",
            'name': "name",
        }
    ))
    email = forms.CharField(widget=forms.TextInput(
        attrs={
            'class': "input--style-3",
            'type': "text",
            'placeholder': "Email",
            'name': "email",
        }
    ))
    college = forms.CharField(widget=forms.TextInput(
        attrs={
            'class': "input--style-3",
            'type': "text",
            'placeholder': "College",
            'name': "college",
        }
    ))
    contactno = forms.CharField(widget=forms.TextInput(
        attrs={
            'class': "input--style-3",
            'type': "text",
            'placeholder': "Phone",
            'name': "contactno",
        }
    ))
    class Meta:
        model = ToTheBeat
        fields = ('name', 'college', 'email', 'contactno')


class ToTheBeatGForm(forms.ModelForm):
    name = forms.CharField(widget=forms.TextInput(
        attrs={
            'class': "input--style-3",
            'type': "text",
            'placeholder': "Name",
            'name': "name",
        }
    ))
    email = forms.CharField(widget=forms.TextInput(
        attrs={
            'class': "input--style-3",
            'type': "text",
            'placeholder': "Email",
            'name': "email",
        }
    ))
    college = forms.CharField(widget=forms.TextInput(
        attrs={
            'class': "input--style-3",
            'type': "text",
            'placeholder': "College",
            'name': "college",
        }
    ))
    contactno = forms.CharField(widget=forms.TextInput(
        attrs={
            'class': "input--style-3",
            'type': "text",
            'placeholder': "Phone",
            'name': "contactno",
        }
    ))
    number_of_parts = forms.IntegerField(widget=forms.TextInput(
        attrs={
            'class': "input--style-3",
            'type': "text",
            'placeholder': "No. of Praticipants",
            'name': "number_of_part",
        }
    ))

    class Meta:
        model = ToTheBeatGroup
        fields = ('leader_name', 'college', 'email', 'leader_contactno', 'number_of_part')


class vyaktitvaForms(forms.ModelForm):
    name = forms.CharField(widget=forms.TextInput(
        attrs={
            'class': "input--style-3",
            'type': "text",
            'placeholder': "Name",
            'name': "name",
        }
    ))
    email = forms.CharField(widget=forms.TextInput(
        attrs={
            'class': "input--style-3",
            'type': "text",
            'placeholder': "Email",
            'name': "email",
        }
    ))
    college = forms.CharField(widget=forms.TextInput(
        attrs={
            'class': "input--style-3",
            'type': "text",
            'placeholder': "College",
            'name': "college",
        }
    ))
    contactno = forms.CharField(widget=forms.TextInput(
        attrs={
            'class': "input--style-3",
            'type': "text",
            'placeholder': "Phone",
            'name': "contactno",
        }
    ))
    class Meta:
        model = Vyaktitva
        fields = ('name', 'college', 'email', 'contactno')



