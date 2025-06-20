from django import forms
from .models import Student
from django.core.exceptions import ValidationError


class StudentRegistrationForm(forms.ModelForm):
    password1 = forms.CharField(label="Password",max_length=10,required=True,widget= forms.PasswordInput(attrs={"placeholder":"Enter your password",'class': 'form-control'}))
    password2 = forms.CharField(
        label="Confirm Password",
        max_length=10, 
        required=True,
        widget= forms.PasswordInput(attrs={
           "placeholder":"Re-Enter your password",
           'class': 'form-control'
        })
        )
    class Meta:
        model = Student
        fields = ["name","email"]
        widgets = {
            'name': forms.TextInput(attrs={'class': 'form-control', 'placeholder': 'Full name'}),
            'email': forms.EmailInput(attrs={'class': 'form-control', 'placeholder': 'Email'}),
        }
        
    
    def clean_email(self):
        email = self.cleaned_data.get('email')
        if Student.objects.filter(email=email).exists():
            raise ValidationError("Email is already registered.")
        return email
    
    def clean(self):
        cleaned_data = super().clean()
        p1 = cleaned_data.get("password1")
        p2 = cleaned_data.get("password2")
                
        if p1 and p2 and p1 != p2:
            print("Passwords do not match!")
            raise forms.ValidationError("Passwords do not match.")
        
        return cleaned_data

        
class StudentLoginForm(forms.Form):
    email = forms.EmailField(
        label="Email",
        widget=forms.EmailInput(attrs={
            'class': 'form-control',
            'placeholder': 'Enter your email'
        })
    )
    password = forms.CharField(label="Password",max_length=10,required=True,widget= forms.PasswordInput(attrs={"placeholder":"Enter your password",'class': 'form-control'}))
    