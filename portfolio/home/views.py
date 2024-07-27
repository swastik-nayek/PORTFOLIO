from django.shortcuts import render, HttpResponse
from home.models import Contact, Post
from django.contrib import messages

# Create your views here.

def index(request):
    return render(request,'index.html')
    #return HttpResponse("This is index!")

def home(request):
    return(render(request,'index.html'))

def contact(request):
    if request.method == "POST":
        name = request.POST.get('name')
        email = request.POST.get('email')
        phone = request.POST.get('phone')
        catagory = request.POST.get('catagory')
        message = request.POST.get('message')
        if len(name)<2 or len(email)<3 or len(phone)<10:
            messages.error(request, "Fill the form correctly!")
        else:
            contact = Contact(name=name, email=email, phone=phone, catagory = catagory, message = message)
            contact.save()
            messages.success(request, "Your massages has been sent")
    return(render(request,'contact.html'))

def about(request):
    return render(request,'about.html')

def blogWrite(request):
    if request.method == "POST":
        title = request.POST.get('title')
        content = request.POST.get('content')
        author = request.POST.get('author')
        slug = request.POST.get('slug')

        post = Post(title=title, content=content, author=author, slug=slug)
        post.save()
        messages.success(request, "Your massages has been sent")
    return render(request,'blogWrite.html')

def blogHome(request):
    allPosts = Post.objects.all()
    context = {'allPosts': allPosts}
    return render(request,'blogHome.html',context)

def blogPost(request, slug):
    post = Post.objects.filter(slug=slug).first()
    context = {'post': post}
    return render(request, 'blogPost.html',context)

def search(request):
    query = request.GET['query']
    if len(query)>78:
        allPosts = Post.objects.none()
    else:
        allPostsTitle = Post.objects.filter(title__icontains=query)
        allPostscontaines = Post.objects.filter(content__icontains=query)
        allPosts = allPostsTitle.union(allPostscontaines)

    if allPosts.count() == 0:
        messages.warning(request, "OOPS! You trying to search something which is not here, try another query...")
    params = {'allPosts': allPosts, 'query': query}
    return(render(request,'search.html', params))

# def CV(request):
#     return(render(request,'CV.html'))