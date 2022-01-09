from django.contrib import admin
from django.urls import path
from django.conf import settings
from django.conf.urls.static import static

from mysite.core import views
#from mysite.login import loginviews
#from login import base


urlpatterns = [
    path('', views.Home.as_view(), name='home'),
    #path('', loginviews.base(),name="base"),
    path('upload/', views.upload, name='upload'),
    path('books/', views.fil_list, name='book_list'),
    #path('user_login/',views.user_login,name='user_login'),
    
    
    #path('books/upload/', views.upload_book, name='upload_book'),
    #path('books/<int:pk>/', views.delete_book, name='delete_book'),

    #path('class/books/', views.BookListView.as_view(), name='class_book_list'),
    #path('class/books/upload/', views.UploadBookView.as_view(), name='class_upload_book'),

    path('admin/', admin.site.urls),
]

if settings.DEBUG:
    urlpatterns += static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)
