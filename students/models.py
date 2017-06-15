# django import
from django.db import models
from django.core.validators import validate_email
from django.template.defaultfilters import slugify

# third party import
from localflavor.us.us_states import STATE_CHOICES
from localflavor.us.models import USStateField, USSocialSecurityNumberField, USZipCodeField
from django_countries.fields import CountryField

# customize import
from students.choices import * # instore all choices in models

# import end

class Student(models.Model):
	# STEP 1 BASIC INFO
	student_id = models.CharField(max_length=128, unique=True)
	first_name = models.CharField(max_length=128)
	last_name = models.CharField(max_length=128)
	ssn = USSocialSecurityNumberField(null=False)
	gender = models.CharField(max_length=128, choices=GENDER_CHOICES)
	dob = models.DateField(auto_now=False, auto_now_add=False, db_column="date of birth")
	contact_number = models.CharField(max_length=128)
	address = models.CharField(max_length=128)
	city = models.CharField(max_length=128)
	state = USStateField(choices=STATE_CHOICES, default='NJ')
	zipcode = USZipCodeField(blank=True)
	country = CountryField(default='US', blank=True)
	home_phone = models.CharField(max_length=128)
	cell_phone = models.CharField(max_length=128)
	email = models.EmailField(max_length=254, validators=[validate_email])
	background = models.CharField(max_length=128, choices=BACKGROUND_CHOICES)
	location = models.CharField(max_length=128, choices=LOCATION_CHOICES, default='south_plainfield')
	workforce = models.CharField(max_length=128, choices=WORKFORCE_CHOICES, default='--')
	source = models.CharField(max_length=128, choices=SOURCE_CHOICES, default='individual')
	refer_by = models.CharField(max_length=128, choices=REFER_BY_CHOICES, default='no refer')
	last_status = models.CharField(max_length=128, choices=LAST_STATUS_CHOICES, default='followup')
	newsletter = models.BooleanField()
	created_by = models.CharField(max_length=128)
	date = models.DateField(auto_now=False, auto_now_add=False)
	notes = models.TextField()

	def __str__(self):
		return self.first_name + self.last_name


class Course(models.Model):
	course_id = models.CharField(max_length=128, unique=True)
	name = models.CharField(max_length=128)
	department = models.CharField(max_length=128)
	# ...

	def __str__(self):
		return self.course_id


class StudentCourse(models.Model):
	# STEP 2 STUDENT AND COURSE
	student = models.ForeignKey(Student)
	course = models.ForeignKey(Course)
	course_status_choices = ( ('selected', 'Selected'), ('drop', 'Drop'), ('pass', 'Pass'), ('fail', 'Fail') )
	course_status = models.CharField(max_length=64, choices=course_status_choices)

	def __str__(self):
		return self.student.student_id + self.course.name


class StudentEmployment(models.Model):
	# STEP 3 EMPLOYMENT INFO
	student = models.ForeignKey(Student)
	company = models.CharField(max_length=128)
	title = models.CharField(max_length=128)
	supervisor = models.CharField(max_length=128)
	dof = models.DateField(name="date of hire")
	hourly_salary = models.PositiveIntegerField()
	hpw = models.PositiveIntegerField(name="hours per week")
	address = models.CharField(max_length=128)
	city = models.CharField(max_length=128)
	state = USStateField(choices=STATE_CHOICES, default='NJ')
	zipcode = USZipCodeField(blank=True)
	country = CountryField(default='US', blank=True)
	work_phone = models.CharField(max_length=128)
	work_phone_ext = models.CharField(max_length=128)
	fax = models.CharField(max_length=128)
	fbr = models.BooleanField(name="fringe benefits received")
	cbub = models.BooleanField(name="covered by unemployment benefits")
	placed_by_choices = (('school', 'School'), ('jcoet', 'JCOET'), ('self', 'Self'), ('other', 'Other'))
	placed_by = models.CharField(max_length=128, choices=placed_by_choices)
	training_related = models.BooleanField()
	notes = models.TextField()

	def __str__(self):
		return self.student.student_id + self.company

