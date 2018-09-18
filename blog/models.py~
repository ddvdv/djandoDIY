from django.db import models
from django.contrib.auth.models import User

# Create your models here.
class Blog(models.Model):
    """Class defining model of a blog post"""

    title = models.CharField(max_length=100, help_text="Define your blog title in a concise way (max 100 characters)")
    datetime = models.DateTimeField(auto_now=True, null=False)
    content = models.TextField(help_text="Content of the article")
    author = models.ForeignKey(User, on_delete=models.CASCADE, null=True)

    class Meta:
        ordering = ['-datetime']

    def __str__(self):
        return f'{self.title}, by {self.author} ({self.datetime})'

    def get_absolute_url(self):
        """Returns the url to access detail record for this blog post"""
        return reverse('blog-detail', args=[str(self.id)])
    

class Comment(models.Model):
    """ Class defining the model for a comment on a particular blog post"""

    content = models.TextField(help_text="Content of the comment")
    datetime = models.DateTimeField(auto_now=True, null=False, help_text="Date and time of the posting of the comment")
    origin_blog = models.ForeignKey('Blog', on_delete=models.CASCADE, null=False)
    author = models.ForeignKey(User, on_delete=models.CASCADE, null=False)
