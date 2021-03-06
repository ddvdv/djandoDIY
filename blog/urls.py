from django.urls import path, include

from blog import views

urlpatterns = [
        path('', views.index, name='index'),
        path('blogs', views.BlogListView.as_view(), name='blogs'),
        path('blogs/<int:pk>', views.BlogDetailView.as_view(), name='blog-detail'),
        path('bloggers', views.BloggerListView.as_view(), name='bloggers'),
        path('blogger/<int:pk>', views.BloggerDetailView.as_view(), name='blogger-detail'),
]
