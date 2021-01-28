from django.shortcuts import render
from django.utils import timezone
from .models import Post

def post_list(request):
    posts = Pos.objects.filter(Published_date__lte=timezone.now()).order_by('publishe_date')
    return render(request, 'blog/post_list.html',{'posts':posts})
# Create your views here.
