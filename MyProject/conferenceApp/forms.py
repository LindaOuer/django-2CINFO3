from django import forms
from .models import Conference

class ConferenceForm(forms.ModelForm):
    class Meta:
        model = Conference
        fields = "__all__"
    
    start_date = forms.DateField(
        label="Conference date début",
        widget=forms.DateInput(
            attrs= {
                'type': 'date',
                'class': 'form-control date-input'
            }
        )
    )
    
    end_date = forms.DateField(
        label="Conference date fin",
        widget=forms.DateInput(
            attrs= {
                'type': 'date',
                'class': 'form-control date-input'
            }
        )
    )