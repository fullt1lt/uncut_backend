from django.contrib import admin

from myappback.models import CategoryActivity, Doctors, ProcedureActivity

admin.site.register(CategoryActivity)
admin.site.register(ProcedureActivity)
admin.site.register(Doctors)