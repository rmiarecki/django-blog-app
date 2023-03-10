from django.db import models
from django.contrib.auth import get_user_model
User=get_user_model()

class Entry(models.Model):
    title = models.CharField(max_length=50)  
    slug = models.SlugField()
    body = models.TextField()
    date = models.DateTimeField(auto_now_add=True)

    class Meta:
        db_table = 'entries'

    def __str__(self):
        return self.title

    def reduction(self):
        return self.body[:280] + '...'
    
class Comment(models.Model):
    entry = models.ForeignKey(Entry, related_name='comments', on_delete=models.CASCADE)
    name = models.ForeignKey(User, on_delete=models.CASCADE)
    content = models.TextField()
    date_added = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return 'Comment by {} - on {}'.format(self.name, self.entry) 