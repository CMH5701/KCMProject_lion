import imp
from django.shortcuts import render,redirect,get_object_or_404
from kcmapp.forms import CashbookForm,CashbookeditForm ,CommentForm
from django.contrib.auth.decorators import login_required
from django.utils import timezone
from .models import Cashbook , Comment
from django.views.decorators.http import require_POST, require_http_methods


# Create your views here.

def main(request):
    cashbook = Cashbook.objects.all()
    return render(request , 'main.html',{'cashbook':cashbook})

@login_required
def write(request) :
    if not request.user.is_authenticated:
        return redirect('main')
    context = {}
    if request.method == 'POST':
        form = CashbookForm(request.POST, request.FILES)
        if form.is_valid():
            cashbook = form.save(commit=False)
            cashbook.pub_date = timezone.now() 
            cashbook.user = request.user
            cashbook.save()
        return redirect('main')

    else:
        form = CashbookForm
        context['form'] = form
    return render(request, 'write.html', {'form':form})

def read(request) :
    cashbooks = Cashbook.objects.order_by('-id').all() #id 1~#까지 순차적으로 게시글 출력
    comment_form = CommentForm()
    return render(request, 'read.html', {'cashbooks':cashbooks ,'comment_form': comment_form })

def detail(request,id) :
    cashbooks = get_object_or_404(Cashbook, id=id)
    comment_form = CommentForm()
    return render(request, 'detail.html', {'cashbooks':cashbooks ,'comment_form': comment_form })

def edit(request,id) :
    cashbook = get_object_or_404(Cashbook, id=id )
    if cashbook.user != request.user:
        return redirect('read')

    if request.method == 'POST':
        form = CashbookeditForm(request.POST ,request.FILES,instance= cashbook )
        if form.is_valid():
            form = form.save(commit=False)
            form.pub_date = timezone.now() 
            form.save()
            return redirect('read')
    else:
        form = CashbookeditForm(instance= cashbook)
        return render(request, 'edit.html', {'form':form , 'cashbook':cashbook})

def delete(request, id):
    cashbook = get_object_or_404(Cashbook, id=id)
    
    if cashbook.user != request.user:
        return redirect('read')

    cashbook.delete()

    return redirect('read')

@require_POST
def comment_write(request, cashbooks_id):
    #DB에서부터 어떠한 게시글인지에대한 정보를 찾아서 post변수에 저장
    cashbooks = get_object_or_404(Cashbook,  id=cashbooks_id)
    comment_form = CommentForm(request.POST)
    if comment_form.is_valid():
        comment = comment_form.save(commit=False)
        comment.user = request.user
        #comment.post를 통해 comment에 대한 1:N 관계 설정
        comment.post = cashbooks
        comment.save()
        
    return redirect('read')

@require_http_methods(['GET', 'POST'])
def comment_delete(request, cashbooks_id, comment_id):

    comment = get_object_or_404(Comment, id=comment_id)
    
    if comment.user != request.user:
        return redirect('read')

    comment.delete()

    return redirect('read')

def comment_update(request, cashbooks_id, comment_id):
    comment = get_object_or_404(Comment, id=comment_id)

    if request.user != comment.user:
        return redirect('read')

    if request.method == 'POST':
        comment_form = CommentForm(request.POST, instance=comment)
        if comment_form.is_valid():
            comment_form.save()
        return redirect('read')
    
    else:
        comment_form = CommentForm(instance=comment)
        return render(request, 'comment_update.html', {'comment_form':comment_form})






