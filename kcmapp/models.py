from django.db import models
from django.core.exceptions import ValidationError
from django.conf import settings
from django.contrib.auth.models import User
# Create your models here.
#모델 object 별로 변수에 접근하기 때문에 변수명은 겹쳐도 상관없음 근데 가독성 떨어짐 ex)Cashbook.name , user.name 
class Cashbook(models.Model):
    user = models.ForeignKey(settings.AUTH_USER_MODEL, on_delete=models.CASCADE)
    title = models.CharField(max_length=200)
    pub_date = models.DateTimeField('data published')
    content = models.TextField()
    name = models.CharField(max_length=10)
    email = models.EmailField(max_length=100, blank=True)
    image = models.ImageField(upload_to  = 'images/' , blank = True)
    hashtags = models.ManyToManyField('kcmapp.Hashtag' , blank = True)
    
    def __str__ (self) :
        return self.title

    def clean(self):
        title = self.title
        if title == "":
            raise ValidationError("글을 작성해주세요.")
        return super(Cashbook, self).clean()
    
class Comment(models.Model):
    user = models.ForeignKey(settings.AUTH_USER_MODEL, on_delete=models.CASCADE)
    post = models.ForeignKey(Cashbook, on_delete=models.CASCADE)
    content = models.TextField()
    
    def __str__ (self) :
        return self.content

class Hashtag(models.Model) :
    name = models.CharField(max_length=50)
    hash_id = models.ForeignKey(Cashbook, on_delete=models.CASCADE, null=True)
    

    def __str__(self) :
        return self.name  

