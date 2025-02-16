from django.contrib.auth.forms import UserCreationForm
from django.forms.utils import ErrorList
from django.utils.safestring import mark_safe
from django import forms

class CustomErrorList(ErrorList):
    def __str__(self):
        if not self:
            return ''
        return mark_safe(''.join([f'<div class="alert alert-danger" role="alert">{e}</div>' for e in self]))
class CustomUserCreationForm(UserCreationForm):
    security_answer = forms.CharField(
        label='What is your favorite color?',
        max_length=100,
        widget=forms.TextInput(attrs={'class': 'form-control'}),
        help_text="This is your security question for account recovery."
    )

    def __init__(self, *args, **kwargs):
        super(CustomUserCreationForm, self).__init__(*args, **kwargs)
        # Remove help text for fields like username and passwords
        for fieldname in ['username', 'password1', 'password2']:
            self.fields[fieldname].help_text = None
            self.fields[fieldname].widget.attrs.update({'class': 'form-control'})


class SecurityQuestionForm(forms.Form):
    answer = forms.CharField(label='What is your favorite color?', max_length=100)
