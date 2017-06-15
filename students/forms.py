# django import
from django import forms
from django.core.validators import validate_email

# third party import
from localflavor.us.us_states import STATE_CHOICES
from localflavor.us.forms import USStateField, USSocialSecurityNumberField, USZipCodeField
from django_countries import countries

# customize import
from students.models import Student
from students.choices import *


class StudentForm(forms.ModelForm):
	# STEP 1 FORM
	student_id = forms.CharField(max_length=128, label="Student ID")
	first_name = forms.CharField(max_length=128, label="First Name")
	last_name = forms.CharField(max_length=128, label="Last Name")
	ssn = USSocialSecurityNumberField(label="SSN", help_text="Format: xxx-xx-xxxx")
	gender = forms.ChoiceField(label="Gender", choices=GENDER_CHOICES)
	dob = forms.DateField(label="Date of birth", help_text="Format: yyyy-mm-dd")
	contact_number = forms.CharField(max_length=128, label="Contact number")
	address = forms.CharField(max_length=128, label="Address")
	city = forms.CharField(max_length=128, label="City")
	state = forms.ChoiceField(choices=STATE_CHOICES, initial="NJ", label="State")
	zipcode = USZipCodeField(label="zipcode")
	country = forms.ChoiceField(choices=countries, label="Country")
	home_phone = forms.CharField(max_length=128, label="Home phone")
	cell_phone = forms.CharField(max_length=128, label="Cell phone")
	email = forms.EmailField(max_length=254, validators=[validate_email], label="Email")
	background = forms.ChoiceField(choices=BACKGROUND_CHOICES, label="Background")
	location = forms.ChoiceField(choices=LOCATION_CHOICES, initial="south_plainfield", label="Location")
	workforce = forms.ChoiceField(choices=WORKFORCE_CHOICES, initial="--", label="Workforce")
	source = forms.ChoiceField(choices=SOURCE_CHOICES, initial="individual", label="Source")
	refer_by = forms.ChoiceField(choices=REFER_BY_CHOICES, initial="no refer", label="Refer by")
	last_status = forms.ChoiceField(choices=LAST_STATUS_CHOICES, initial="followup", label="Last status")
	newsletter = forms.BooleanField(label="Newsletter", required=False)
	created_by = forms.CharField(max_length=128, label="Created by")
	date = forms.DateField(label="Date", help_text="Format: yyyy-mm-dd")
	notes = forms.CharField(widget=forms.Textarea(), label="note", help_text="less than 1000 characters")

	class Meta:
		model = Student
		fields = ('student_id', 'first_name', 'last_name', 'ssn', 'gender', 'dob', 'contact_number', 'address', 'city', 'state', 'zipcode', 'country', 'home_phone', 'cell_phone', 'email', 'background', 'location', 'workforce', 'source', 'refer_by', 'last_status', 'newsletter', 'created_by', 'date', 'notes')