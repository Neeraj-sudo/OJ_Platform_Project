from django.contrib import admin

# Register your models here.

from .models import User, Problem, Solutions, TestCases

admin.site.register(User)
admin.site.register(Problem)
admin.site.register(Solutions)
admin.site.register(TestCases)
