from django import forms


class ImageForm(forms.Form):
    user_image = forms.FileField(required=True, help_text="Image to be sharpened.")
