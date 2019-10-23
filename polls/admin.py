from django.contrib import admin

# Register your models here.
from .models import Poll,Choice

# 관리자 화면 customizing.

#class ChoiceInline (admin.StackedInline):
class ChoiceInline (admin.TabularInline):
    model = Choice
    extra = 3

class PollModelAdmin (admin.ModelAdmin):
    fieldsets = [
        (None, {'fields': ['question_txt']}),
        ('Date info.', {'fields': ['pub_date']}),
    ]
    inlines = [ChoiceInline]

    # 목록에 보이는 항목 편집.
    list_display = ('question_txt', 'pub_date', 'was_published_recently')

    # filter 추가.
    list_filter = ['pub_date']

    # search 기능.
    search_fields = ['question_txt']

admin.site.register(Poll, PollModelAdmin)
admin.site.register(Choice)