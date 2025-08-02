# builder/forms.py

from django import forms

class WebsiteGenerationForm(forms.Form):
    """
    This form collects all the necessary information from the user
    to generate their personal website.
    """
    
    # Each field here corresponds to a placeholder in our template.html
    
    business_name = forms.CharField(
        label="Business Name",
        max_length=100,
        help_text="The name of your brand or portfolio.",
        widget=forms.TextInput(attrs={'placeholder': 'e.g., Jane Doe Photography'})
    )

    tagline = forms.CharField(
        label="Tagline / Subtitle",
        max_length=200,
        required=False, # This field is optional
        help_text="A short, catchy phrase that appears under your business name.",
        widget=forms.TextInput(attrs={'placeholder': 'e.g., Capturing Moments That Matter'})
    )

    about_text = forms.CharField(
        label="About Section",
        help_text="Write a paragraph or two about yourself or your business.",
        widget=forms.Textarea(attrs={'rows': 6, 'placeholder': 'Tell your story here...'})
    )

    contact_email = forms.EmailField(
        label="Contact Email Address",
        help_text="The email address people can use to contact you.",
        widget=forms.EmailInput(attrs={'placeholder': 'e.g., contact@janedoe.com'})
    )