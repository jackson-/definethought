from django.shortcuts import render
from django.views.generic import View

# Create your views here.
class PostList(View):
    template_name = "post_list.html"

    def get(self, request):
        return render(request, self.template_name, {})



class PostDetail(View):
    template_name = "post_detail.html"

    def get(self, request, slug):
        return render(request, self.template_name, {})