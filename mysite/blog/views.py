from django.shortcuts import render

def post_list(request):
    return render(request, 'blog/post_list.html', {})

def post_list2(request):
    return render(request, 'blog/post_list2.html', {})

def post_list3(request):
    return render(request, 'blog/post_list3.html', {})

def gif(request):
    return render(request, 'blog/gif.html', {})
