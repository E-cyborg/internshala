from django.db import models


class Blog(models.Model):
    blog_title=models.CharField(max_length=150)
    description=models.TextField()

    def __str__(self) -> str:
        return self.blog_title
    

class Comments(models.Model):
    blog=models.ForeignKey(Blog, on_delete=models.CASCADE,related_name='comments')
    message=models.CharField(max_length=250)
     
    def __str__(self) -> str:
        return self.message