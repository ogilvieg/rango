from django.contrib import admin
from models import Question, Choice

# Register your models here.

class ChoiceInLine(admin.TabularInline):
    model = Choice
    extra = 3

class QuestionAdmin(admin.ModelAdmin):
    list_display = ('question_text', 'date_published')
    list_filter = ['date_published']
    search_fields = ['question_text']

    fieldsets = [(None, {'fields': ['question_text']}),
        ('Date information', {'fields': ['date_published'],
                              'classes': ['collapse']}),
    ]
    inlines = [ChoiceInLine]


admin.site.register(Question, QuestionAdmin)
admin.site.register(Choice)