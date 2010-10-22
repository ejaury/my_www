from django import forms

class ImageDownloaderForm(forms.Form):
  url = forms.CharField(max_length=100)
