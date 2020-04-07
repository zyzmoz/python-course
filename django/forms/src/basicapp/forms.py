from django import forms
from django.core import validators

# Custom Validation
def check_for_z(value):
  if(value[0].lower() != 'z'):
    raise forms.ValidationError("Name needs to start with 'z'")

class FormName(forms.Form):
  name = forms.CharField(validators=[check_for_z])
  email = forms.EmailField()
  email_confirmation = forms.EmailField(label="Enter your email again")
  text = forms.CharField(widget=forms.Textarea)
  
  botcatcher = forms.CharField(required=False, widget=forms.HiddenInput, validators=[validators.MaxLengthValidator(0)])
  
  def clean(self):
    all_clean_data = super().clean()
    email = all_clean_data['email']
    email_confirmation = all_clean_data['email_confirmation']
    
    if (email != email_confirmation):
      raise forms.ValidationError("Email doesn't math with confirmation")
  
  # def clean_botcatcher(self):
  #   botcatcher = self.cleaned_data['botcatcher']
  #   if (len(botcatcher) > 0):
  #     raise forms.ValidationError("GOTCHA BOT!")
    
  #   return botcatcher