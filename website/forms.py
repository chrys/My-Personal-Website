from django import forms
import re


class ContactForm(forms.Form):
    name = forms.CharField(
        max_length=120,
        widget=forms.TextInput(attrs={
            "placeholder": "Your full name",
            "autocomplete": "name",
        }),
    )
    email = forms.EmailField(
        widget=forms.EmailInput(attrs={
            "placeholder": "you@example.com",
            "autocomplete": "email",
        }),
    )
    message = forms.CharField(
        min_length=20,
        max_length=2000,
        widget=forms.Textarea(attrs={
            "rows": 7,
            "placeholder": "Tell me about your project, question, or collaboration idea.",
        }),
    )
    website = forms.CharField(
        required=False,
        widget=forms.TextInput(attrs={
            "autocomplete": "off",
            "tabindex": "-1",
            "aria-hidden": "true",
            "class": "contact-honeypot-input",
        }),
    )

    def clean_message(self):
        message = self.cleaned_data['message']
        link_matches = re.findall(r'https?://|www\.|<a\s+href', message, flags=re.IGNORECASE)
        if len(link_matches) > 2:
            raise forms.ValidationError('Please include at most 2 links in your message.')
        return message
