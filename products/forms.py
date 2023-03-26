from django import forms
from .models import Product

class ProductForm(forms.ModelForm):

    # Define the structure of the form 
    title = forms.CharField(label='', 
                            widget = forms.TextInput(attrs =
                                            {"placeholder": "Your Title"}))
    email = forms.CharField(label='', 
                            widget = forms.TextInput(attrs =
                                            {"placeholder": "Your Email"}))
    description = forms.CharField(required=False, 
                                  widget=forms.Textarea(attrs= {
        "placeholder":"Your Description",
        "class": "new-class-name two",
        "id": "my-id-for-text-area",
        "rows":20,
        "cols": 120
                                  }))
    price = forms.DecimalField(initial=199.99)
    
    class Meta:
        model = Product
        # Fields that you want from the main App object
        # Fields will look at the structure in the ProductForm Class
        fields = [
            "title",
            "email",
            "description",
            "price"
        ]
        email = forms.EmailField()
    
    def clean_title(self,*args,**kwargs):
        title = self.cleaned_data.get("title")
        if "CFE" in title: 
            raise forms.ValidationError("This is not a valid title")
        if "news" in title: 
            raise forms.ValidationError("This is not a valid title")
        else: 
            return title
        
    def clean_email(self,*args,**kwargs):
        email = self.cleaned_data.get("email")
        if not email.endswith("edu"): 
            raise forms.ValidationError("This is not a valid email")
        return email


class RawProductForm(forms.Form): 
    # Defines the structure of the form. 
    title = forms.CharField(label='', 
                            widget = forms.TextInput(attrs =
                                            {"placeholder": "Your Title"}))
    description = forms.CharField(required=False, 
                                  widget=forms.Textarea(attrs= {
        "placeholder":"Your Description",
        "class": "new-class-name two",
        "id": "my-id-for-text-area",
        "rows":20,
        "cols": 120
                                  }))
    price = forms.DecimalField(initial=199.99)
