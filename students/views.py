'''
Created on May 29, 2017

@author: jwang02
'''
# django import
from django.http import HttpResponse
from django.shortcuts import render
from django.contrib.auth.decorators import login_required

# python import
import uuid

# custom import
from students.models import Student, StudentCourse, StudentEmployment, Course
from students.forms import StudentForm


@login_required
def students(request):
    # Query the database for a list of ALL categories currently stored.
    # Order the categories by no. likes in descending order.
    # Retrieve the top 5 only - or all if less than 5.
    # Place the list in our context_dict dictionary which will be passed to the template engine.

    # Render the response and send it back!
    return render(request, "students/students.html", {})


def add_student(request):
	form = StudentForm()
	print(form['first_name'])
	print('start adding student')
	if request.method == 'POST':
		print('it\'s POST request')
		form = StudentForm(request.POST)
		# Issues
		# 1. ssn is not saved (fixed)
		# 2. date of birth  is not saved (fixed)
		if form.is_valid():
			print('form is valid')
			form.save(commit=True)
			# Step 1 complete. Move to Step 2 add_studentcourse.
			return HttpResponse('New student created!. Move to step 2!')
		else:
			print(form.errors)

	return render(request, 'students/add_student.html', {'form': form})

# def add_StudentCourse(request):
