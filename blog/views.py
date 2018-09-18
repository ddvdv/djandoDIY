from django.shortcuts import render
from django.views import generic
from blog.models import Blog
from django.contrib.auth.models import User

# Create your views here.
def index(request):
    """View function for home page of site"""
   
    # Generate a couple of stats for the home page
    num_blogs = Blog.objects.all().count()
    num_bloggers = User.objects.all().count()

    context = {
        'num_blogs': num_blogs,
        'num_bloggers': num_bloggers,
    }

    # render the proper html template
    return render(request, 'index.html', context=context)

class BlogListView(generic.ListView):
    model = Blog
    paginate_by = 3

class BlogDetailView(generic.DetailView):
    model = Blog

