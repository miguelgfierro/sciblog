from django.shortcuts import render
from django.http import HttpResponse
from django.shortcuts import render_to_response, get_object_or_404
from blog.models import Post, Category
from django.core.urlresolvers import reverse
from django.views import generic
from django.template import RequestContext, loader


def index(request):
    return render_to_response('index.html', {
        'categories': Category.objects.all(),
        'posts': Post.objects.all()[:5]
    })
def view_post(request, slug):
    return render_to_response('view_post.html', {
        'post': get_object_or_404(Post, slug=slug)
    })
def view_category(request, slug):
    category = get_object_or_404(Category, slug=slug)
    return render_to_response('view_category.html', {
        'category': category,
        'posts': Post.objects.filter(category=category)[:5]
    })

'''
def index(request):
    #return HttpResponse("Hello, world. You're at the polls index.")
    posts = Post.objects.order_by('-pub_date')[:5]
    #template = loader.get_template('Post/index.html')
    #context = RequestContext(request, {'posts': posts, })
    #return HttpResponse(template.render(context))
    context = {'posts': posts}
    return render(request, 'index.html', context)
def view_post(request):
    return HttpResponse("You're looking at question " )
def view_category(request):
    response = "You're looking at the results of question ."
    return HttpResponse(response)
'''


class PostView(generic.DetailView):
    model = Post
    template_name = 'view_post.html'
    #context_object_name = 'post'

class CategoryView(generic.DetailView):
    model = Category
    template_name = 'view_category.html'

class IndexView(generic.ListView):
    template_name = 'index.html'
    context_object_name = 'posts'
    def get_queryset(self):
        return Post.objects.order_by('-pub_date')[:5]

class CategoryListView(generic.ListView):
    template_name = 'view_category.html'

    def get_queryset(self):
        slug = self.kwargs['slug']
        try:
            category = Category.objects.get(slug=slug)
            return Post.objects.filter(category=category)
        except Category.DoesNotExist:
            return Post.objects.none()

    def get_context_data(self, **kwargs):
        context = super(CategoryListView, self).get_context_data(**kwargs)
        slug = self.kwargs['slug']
        try:
            context['category'] = Category.objects.get(slug=slug)
        except Category.DoesNotExist:
            context['category'] = None
        return context
