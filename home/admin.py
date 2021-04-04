from django.contrib import admin
from home.models import snippet_table , Contact , codeforce_submission

# Register your models here.
admin.site.register(snippet_table)
admin.site.register(Contact)
admin.site.register(codeforce_submission)
