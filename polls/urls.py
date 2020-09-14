from django.urls import path
from . import views

app_name = 'polls'
urlpatterns = [
    path('', views.IndexView.as_view(), name='index'),
    path('<int:pk>/', views.DetailView.as_view(), name='ques-detail'),
    path('<int:pk>/results/', views.ResultsView.as_view(), name='ques-results'),
    path('<int:question_id>/vote/', views.vote, name='ques-vote')
]