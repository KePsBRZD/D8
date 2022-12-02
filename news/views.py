from django.shortcuts import render
from datetime import datetime
from django.views.generic import ListView, DetailView, CreateView, UpdateView, DeleteView
from .models import Post
from .filters import PostFilter
from .forms import PostForm
from django.urls import reverse_lazy
from django.http import HttpResponseRedirect

# Create your views here.

class PostsList(ListView):

    model = Post
    ordering = "created"

    template_name = "news.html"
    context_object_name = "posts"
    paginate_by = 5

    def get_queryset(self):
        queryset = super().get_queryset()
        self.filterset = PostFilter(self.request.GET, queryset=queryset)

        return self.filterset.qs


    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context['filterset'] = self.filterset
        return context


class PostDetail(DetailView):

    model = Post
    template_name = "new.html"
    context_object_name = "post"

    def get_context_data(self, **kwargs):

        context = super().get_context_data(**kwargs)
        context["time_now"] = datetime.utcnow()

        return context

class PostCreate(CreateView):

    form_class = PostForm
    model = Post
    template_name = 'create.html'

class PostSearch(ListView):

        model = Post
        ordering = 'created'
        template_name = 'search.html'
        context_object_name = 'posts_search'
        paginate_by = 5

        def get_queryset(self):
            queryset = super().get_queryset()
            self.filterset = PostFilter(self.request.GET, queryset=queryset)

            return self.filterset.qs

        def get_context_data(self, **kwargs):
            context = super().get_context_data(**kwargs)
            context['filterset'] = self.filterset
            return context

class PostUpdate(UpdateView):

    form_class = PostForm
    model = Post
    template_name = 'new_edit.html'

class PostDelete(DeleteView):

    model = Post
    template_name = 'new_delete.html'
    success_url = reverse_lazy('post_list')