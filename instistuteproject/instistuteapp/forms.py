from django import forms
from multiselectfield import MultiSelectFormField
class FeedbackForm(forms.Form):
    name=forms.CharField(
        label="Enter your name",
        widget=forms.TextInput(
            attrs={
                'class':'form-control',
                'placeholder':'your Name'
            }
        )
    )
    rating=forms.IntegerField(
        label="Enter your rating",
        widget=forms.NumberInput(
            attrs={
                'class':'form-control',
                'placeholder':'rating'
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

class ContactForm(forms.Form):
    name=forms.CharField(
        label="Enter your name",
        widget=forms.TextInput(
            attrs={'class':'form-control',
                   'placeholder':"Your name"
            }

        )
    )
    email=forms.EmailField(
        label="Enter your email",
        widget=forms.EmailInput(
            attrs={
                'class':'form-control',
                'placeholder':"Enter your email"
            }

        )
    )
    mobile=forms.IntegerField(
        label="Enter your mobile number",
        widget=forms.NumberInput(
            attrs={
                'class':'form-control',
                'placeholder':"Your mobile number"
            }
        )

    )
    COURSES_CHOICES = (
        ('py', 'Python'),
        ('dj', 'Django'),
        ('ui','UI'),
        ('rest', 'REST APi')
    )
    courses = MultiSelectFormField(max_length=200, choices=COURSES_CHOICES)

    SHIPT_CHOICES = (
        ('mrg', 'Morning'),
        ('aftn', 'Afternoon'),
        ('ge', 'Evening'),
        ('night', 'Night')
    )
    shifts = MultiSelectFormField(max_length=100, choices=SHIPT_CHOICES)

    LOCATION_CHOICES = (
        ('hyd', 'Hydrabad'),
        ('bang', 'Banglore'),
        ('che', 'Chennai'),
        ('pune', 'Pune')

    )
    location = MultiSelectFormField(max_length=100, choices=LOCATION_CHOICES)

    GENDER_CHOICES=(
        ('m',"Male"),
        ('f',"Female")
    )

    gender=forms.ChoiceField(widget=forms.RadioSelect,choices=GENDER_CHOICES)

    start_date=forms.DateField(widget=forms.SelectDateWidget)


