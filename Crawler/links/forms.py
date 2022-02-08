from django import forms
from logging import PlaceHolder

from django.forms.widgets import URLInput


class UrlForm(forms.Form):
    Url = forms.URLField(label="URL", widget=URLInput)
    