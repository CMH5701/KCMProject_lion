from dataclasses import fields
from django import forms 
from .models import Cashbook , Comment, Hashtag
from django.forms import ModelForm, TextInput, EmailInput, NumberInput #나머지는 폼 더 커스텀 할 때 쓰자리..

class CashbookForm(forms.ModelForm):
    class Meta:
        model = Cashbook
        fields = ['title' , 'content' ,'name' ,'email' ,'image','hashtags']
        labels = {
            'title' : '제목' ,
            'content' : '할말하않',
            'name' : '이름',
            'email' : '이메일 주소',
            'image' : '이미지',
            'hashtags':'해시태그'
        }
        widgets = {
            'email' : EmailInput(attrs={
                'class': "form-fix",
                'placeholder': '이메일 작성해줭',
                }),    
        }
    def init(self, args, **kwargs):
        super(CashbookForm, self).init(args, **kwargs)
        self.fields['title'].required = False

class CashbookeditForm(forms.ModelForm): 
    class Meta:
        model = Cashbook
        fields = ['title' , 'content' ,'email' ,'image','hashtags']
        labels = {
            'title' : '제목' ,
            'content' : '할말하않',
            'email' : '이메일 주소',
            'image' : '이미지',
            'hashtags':'해시태그'
        }
        widgets = {
            'email' : EmailInput(attrs={
                'class': "form-fix",
                'placeholder': '이메일 수정은 못한다 이말이야.',
                'readonly': 'True',
                }),    
        }    
    def init(self, args, **kwargs):
        super(CashbookeditForm, self).init(args, **kwargs)
        self.fields['title'].required = False


class CommentForm(forms.ModelForm):
    class Meta:
        model = Comment
        fields = ['content']
        widgets = {
            'content': forms.TextInput(attrs={'placeholder':'댓글을 입력하세요'})
        }

class HashtagForm(forms.ModelForm):
    class Meta:
        model = Hashtag
        fields = ['name']