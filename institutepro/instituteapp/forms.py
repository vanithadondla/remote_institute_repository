from django import forms
from multiselectfield import MultiSelectFormField

class ContactForm(forms.Form):
    name=forms.CharField(
        label="Enter your name",
        widget=forms.TextInput(
            attrs={
                'class':'form-control',
                'placeholder':'your name'
            }
        )
    )
    email=forms.EmailField(
        label="Enter your email",
        widget=forms.EmailInput(
            attrs={
                'class':'form-control',
                'placeholder':'your email'
            }
        )
    )
    mobile=forms.IntegerField(
        label="Enter your mobile",
        widget=forms.NumberInput(
            attrs={
                'class':'form-control',
                'placeholder':'your mobile'
            }
        )
    )
    COURSES_CHOICES=(
        ('python','Python'),
        ('django' ,'Django'),
        ('ui','Ui'),
        ('restapi', 'Restapi'),
        ('flask' ,'Flask'),
    )
    courses=MultiSelectFormField(max_length=100,choices=COURSES_CHOICES)

    LOCATION_CHOICES =(
        ('hyd','Hyderabad'),
        ('bang','Bangalore'),
        ('chi','Chennai'),
    )
    location= MultiSelectFormField(max_length=100,choices=LOCATION_CHOICES)
    SHIFT_CHOICES= (
        ('morning' ,'Morning'),
        ('afternoon' ,'Afternoon'),
        ('evening','Evening'),
        ('night','Night'),
    )
    shift= MultiSelectFormField(max_length=100,choices=SHIFT_CHOICES)

class FeedbackForm(forms.Form):
    name=forms.CharField(
        label="Enter your name",
        widget=forms.TextInput(
            attrs={
                'class':'form-control',
                'placeholder':'your name'
            }
        )
    )
    rating = forms.IntegerField(
        label="Enter your rating",
        widget=forms.NumberInput(
            attrs={
                'class': 'form-control',
                'placeholder': 'your rating'
            }
        )
    )
    feedback=forms.CharField(
        label="Enter your feedback",
        widget=forms.Textarea(
            attrs={
                'class':'form-control',
                'placeholder':'your feedback'
            }
        )
    )