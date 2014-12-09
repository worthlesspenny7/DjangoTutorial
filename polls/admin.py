from django.contrib import admin

# Register your models here.
from polls.models import Choice, Question

#admin.site.register(Question) #First form (automatic)

# start 2nd round - reordering fields
# class QuestionAdmin(admin.ModelAdmin):
#     fields = ['pub_date', 'question_text']
    
# admin.site.register(Question, QuestionAdmin)
# end 2nd round

# start 3rd round - collapse & added choice admin
# class QuestionAdmin(admin.ModelAdmin):
#     fieldsets = [   (None, {'fields':['question_text']}), 
#                     ('Date Information', {'fields':['pub_date'], 'classes': ['collapse']}),
#     ]
    
# admin.site.register(Question, QuestionAdmin)
# admin.site.register(Choice)
# end 3rd round

# start 4th round - add multiple choices with each question
class ChoiceInline(admin.TabularInline):
    model = Choice
    extra = 3
    
class QuestionAdmin(admin.ModelAdmin):
    fieldsets = [   (None, {'fields':['question_text']}), 
                    ('Date Information', {'fields':['pub_date'], 'classes': ['collapse']}),
    ]
    inlines = [ChoiceInline]
    list_display = ('question_text', 'pub_date', 'was_published_recently')
    list_filter = ['pub_date']
    search_fields = ['question_text']
    
admin.site.register(Question, QuestionAdmin)