from django.conf.urls import url

from ..views import bookmarks

urlpatterns = [
    url(r'^$',
        bookmarks.user_bookmarks,
        name='cab_user_bookmarks'),
    url(r'^add/(?P<snippet_id>\d+)/$',
        bookmarks.add_bookmark,
        name='cab_bookmark_add'),
    url(r'^delete/(?P<snippet_id>\d+)/$',
        bookmarks.delete_bookmark,
        name='cab_bookmark_delete'),
]
