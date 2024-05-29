from django.db import models
from django.contrib.auth.models import User
from django.utils import timezone

# models.
class Post(models.Model):
    """ fields definition.
    Constraints:
        null is for database.
        blank is for form.
    fields with null set to true, indicates that the field can be null in the database.
    fields with blank set to True, indicates that the field can be empty in the form, this would enable the form to pass validation.

    vice-versa for fields set to False.
    """
    
    title = models.CharField(max_length=250)
    slug = models.SlugField(max_length=250)
    content = models.TextField()
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True, null=True)
    published_at = models.DateTimeField(null=True, blank=True)
    author = models.ForeignKey(User, on_delete=models.CASCADE, related_name='blog_post')

    # update Django default settings
    class Meta:
        db_table = 'djangoblog_posts' #table name.
        ordering = ['-published_at']  # query ordering (descending order).

        indexes = [
            models.Index(fields=['-published_at'])
        ]

    
    def update_published_at(self):
        """Responsible for updating published_at field with the current time when the post is made published. (made public), for instance a post saved to Drafts has not been posted, so it makes no sense to update the updated_at in our database, we can only update the time when the post is made public.
        """
        self.published_at = timezone.now()

    def is_published(self):
        """checks if a post is published by comparing if the published_at time is less or equal to timezone current time.
        """
        return self.published_at <= timezone.now
    
    # returns a string representation of our model when we query our database (eg: GOD IS THE GREATEST).
    def __str__(self) -> str:
        return f"{self.title}"
