from django.urls import path
from .views  import *

urlpatterns = [
    # path('',home,name="book_home"),
    path('',BookListView.as_view(),name="book_home"),

    path('api/',book_list_api,name="book_home_api"), 
    # path('create/',create_book,name="book_create"),
    path('create/',BookCreateView.as_view(),name="book_create"),

    # path('update/<int:id>/',update_book,name="book_update"),
    path('update/<int:id>/',BookUpdateView.as_view(),name="book_update"),

    path('delete/<int:id>/',delete_book,name="book_delete"),

    path('category/',CategoryListView.as_view(),name="category_home"),

    path('category/create/',CategoryCreateView.as_view(),name="category_create"),

    path('category/update/<int:id>/',CategoryUpdateView.as_view(),name="category_update"),

    path('category/delete/<int:id>/',delete_category,name="category_delete"),
]