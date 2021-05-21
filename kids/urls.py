from django.urls import path
from .views import CreateAndListCategoryView, CreateAndListChannelsView

urlpatterns = [
    path('categories/', CreateAndListCategoryView.as_view(),
         name='create_and_list_kids_categories'),
    path('channels/', CreateAndListChannelsView.as_view(),
         name='create_and_list_kids_categories'),
]
