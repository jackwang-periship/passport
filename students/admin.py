from django.contrib import admin
from students.models import Student


class StudentAdmin(admin.ModelAdmin):
	list_display = ('student_id', 'first_name', 'last_name', 'zipcode', 'city', 'state')

admin.site.register(Student, StudentAdmin)
