from django.shortcuts import render
from django.http import HttpResponse
from django.shortcuts import render_to_response, get_object_or_404
from blog.models import Blog, Category
from django.core.urlresolvers import reverse
from django.views import generic

'''
def index(request):
    return render_to_response('index.html', {
        'categories': Category.objects.all(),
        'posts': Blog.objects.all()[:5]
    })
def view_post(request, slug):
    return render_to_response('view_post.html', {
        'post': get_object_or_404(Blog, slug=slug)
    })
def view_category(request, slug):
    category = get_object_or_404(Category, slug=slug)
    return render_to_response('view_category.html', {
        'category': category,
        'posts': Blog.objects.filter(category=category)[:5]
    })
'''
def index(request):
    #return HttpResponse("Hello, world. You're at the polls index.")
    latest_question_list = Blog.objects.order_by('-pub_date')[:5]
    context = {'latest_question_list': latest_question_list}
    return render(request, 'index.html', context)
def view_post(request):
    return HttpResponse("You're looking at question " )
def view_category(request):
    response = "You're looking at the results of question ."
    return HttpResponse(response)

class DetailView(generic.DetailView):
    model = Blog
    template_name = 'view_post.html'



