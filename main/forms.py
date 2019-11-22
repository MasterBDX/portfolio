from django import forms

class Contact(forms.Form):
	name = forms.CharField(widget=forms.TextInput(attrs={'class':"form-control",
														 'id':"name",
														 'type':"text",
														 'placeholder':"Name",
														 'required':"required",
														 'data-validation-required-message':"Please enter your name."
														 }))

	email = forms.EmailField(widget=forms.TextInput(attrs={'class':"form-control",
														   'id':"email",
														   'type':"email" ,
														   'placeholder':"Email Address",
														   'required':"required" ,
														   'data-validation-required-message':"Please enter your email address."
														   }))
	
	phone_number = forms.CharField(widget=forms.TextInput(attrs={'class':"form-control",
															     'id':"phone" ,
															     'type':"tel",
															     'placeholder':"Phone Number" ,
															     'required':"required" ,
															     'data-validation-required-message':"Please enter your phone number."
															     }))
	
	message = forms.CharField(widget=forms.Textarea(attrs={'class':"form-control",
														    'id':"message",
														    'rows':"5",
														    'placeholder':"Message",
														    "required":"required",
														    'data-validation-required-message':"Please enter a message."
														   }))