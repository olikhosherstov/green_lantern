from django import forms
from apps.cars.models import Car
from apps.photos.models import Photo


class PhotoForm(forms.ModelForm):
    class Meta:
        model = Photo
        fields = ['image', 'position', 'car']
        widgets = {
            "image": forms.FileInput(attrs={
                'id': 'files', 'required': True, 'multiple': True
            })
        }

    def __init__(self, dealer_id, *args, **kwargs):
        super(PhotoForm, self).__init__(*args, **kwargs)
        self.fields['car'].queryset = Car.objects.filter(dealer=dealer_id)
