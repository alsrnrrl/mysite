
from django.contrib import admin
from django.urls import path, include
from . import views

urlpatterns = [
    # path('admin/', admin.site.urls),
    # path('polls/', include('polls.urls')),
    path('', views.index, name='index'),
    path('<int:question_id'>/)

]
