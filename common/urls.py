from django.urls import path

from common.views import CategoryListView, CategoryCreateView

urlpatterns = [
    path("", CategoryListView.as_view(), name='category-list'),
    path("create/", CategoryCreateView.as_view(), name='category-create'),
]
