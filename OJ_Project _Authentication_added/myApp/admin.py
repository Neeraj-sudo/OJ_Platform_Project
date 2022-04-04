from django.contrib import admin

# Register your models here.

from .models import UserData, Problem, Solutions, TestCases


admin.site.register(UserData)
admin.site.register(Problem)
admin.site.register(Solutions)
admin.site.register(TestCases)

