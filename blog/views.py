from django.shortcuts import render
from django.views import generic
from blog.models import Blog
from django.contrib.auth.models import User
from django.db.models import Q

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

class BloggerListView(generic.ListView):
    model = User
    context_object_name = 'blogger_list'
    queryset = User.objects.filter(groups__name="bloggers")
    template_name = 'blog/blogger_list.html'

class BloggerDetailView(generic.DetailView):
    model = User
    context_object_name = "blogger"
    template_name = 'blog/blogger_detail.html'

    def get_context_data(self, **kwargs):
        context = super(BloggerDetailView, self).get_context_data(**kwargs)
        context['blogs'] = Blog.objects.filter(author=self.kwargs['pk'])
        return context
