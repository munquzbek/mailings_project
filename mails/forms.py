from django import forms

from mails.models import Settings


class StyleFormMixin:
    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        for field in self.fields:
            self.fields[field].widget.attrs['class'] = 'form-control'


class SettingsCreateForm(StyleFormMixin, forms.ModelForm):
    class Meta:
        model = Settings
        fields = '__all__'


class SettingsOffForm(forms.ModelForm):
    class Meta:
        model = Settings
        fields = ('status',)
