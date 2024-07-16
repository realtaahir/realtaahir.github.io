from django.contrib import admin
from .models import *

admin.site.register(Section)
admin.site.register(SubSection)
admin.site.register(HeadQuiz)
admin.site.register(Question)
admin.site.register(UserResponse)
