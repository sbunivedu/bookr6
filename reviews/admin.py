from django.contrib import admin
from reviews.models import (Publisher, Contributor, Book, BookContributor, Review)

class BookAdmin(admin.ModelAdmin):
    list_display = ('title', 'isbn13', 'has_isbn')
    date_hierarchy = 'publication_date'
    list_filter = ('publisher', "publication_date")
    search_fields = ('title', 'isbn', 'publisher__name')
    @admin.display(
        ordering='isbn',
        description='ISBN-13',
        empty_value='-/-'
    )
    def isbn13(self, obj):
        """ '9780316769174' => '978-0-31-676917-4' """
        return "{}-{}-{}-{}-{}".format(
            obj.isbn[0:3], obj.isbn[3:4], obj.isbn[4:6], obj.isbn[6:12], obj.isbn[12:13]
        )

    @admin.display(
        boolean = True,
        description = 'Has ISBN',
    )
    def has_isbn(self, obj):
        """ '9780316769174' => True """
        return bool(obj.isbn)

def initialled_name(self):
    """ self.first_names='Jerome David',
    self.last_names='Salinger'
    => 'Salinger, JD' """

    initials = ''.join([name[0] for name
        in self.first_names.split(' ')])
    return "{}, {}".format(self.last_names, initials)

class ContributorAdmin(admin.ModelAdmin):
    list_display = (initialled_name,)


class ReviewAdmin(admin.ModelAdmin):
    fieldsets = (('Linkage', {'fields': ('creator', 'book')}),
                 ('Review content',
                  {'fields': ('content', 'rating')}))

admin.site.register(Publisher)
admin.site.register(Contributor, ContributorAdmin)
admin.site.register(Book, BookAdmin)
admin.site.register(BookContributor)
admin.site.register(Review, ReviewAdmin)