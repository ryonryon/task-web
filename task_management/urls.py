from django.urls import path
# from .. import task_management
from . import views

urlpatterns = [
    path('', views.IndexView.as_view(), name='index'),
    path('<int:question_id>/', views.DetailView.as_view(), name='detail'),
    # path('<int:question_id>/results/', views.results, name='results'),
    # path('<int:question_id>/votes/', views.vote, name='vote'),
]
