from django import forms
from .models import Book,Category

class BookForm(forms.ModelForm):
    class Meta:
        model =Book
        exclude=['user']
        widgets = {
            'name':forms.TextInput(attrs={'class':'form-control','placeholder':'Book Name'}),
            'author':forms.TextInput(attrs={'class':'form-control','placeholder':'Author'}),
            'price':forms.TextInput(attrs={'class':'form-control'}),
            'category':forms.Select(attrs={'class':'form-control'}),
        }
    def clean_author(self):
        if " " not in self.cleaned_data.get('author'):
            raise forms.ValidationError("invalid data") 
        return self.cleaned_data.get('author') 

class CategoryForm(forms.ModelForm):
    class Meta:
        model = Category
        fields= '__all__'
        widgets = {
            'name':forms.TextInput( attrs={'class':'form-control','placeholder':'Book Name'}),
            'description':forms.Textarea(attrs={'class':'form-control','placeholder':'Description'}),
            'color':forms.TextInput(attrs={'class':'form-control','type':'color'}),

        }