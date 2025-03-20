from django.shortcuts import render, redirect ,get_object_or_404
from .models import Blog, Comment
from .forms import CommentForm

# Create your views here.

def blogPage(request):
    blogItems = Blog.objects.all().order_by("-published_at")
    context ={
        'blogItems':blogItems
    }
    return render(request, 'blog/blog.html', context)



# this is the blog detail section
# where we can see the details of each blogs


def blog_detail(request, slug):
    blog = get_object_or_404(Blog, slug=slug)

    # Increment the view count
    blog.views += 1
    blog.save()

    if request.method == 'POST':
        form = CommentForm(request.POST)
        if form.is_valid():
            comment = form.save(commit=False)
            comment.blog = blog  # Associate the comment with the blog post

            # Check if the comment is a reply (has a parent)
            parent_comment_id = request.POST.get('parent')
            if parent_comment_id:
                parent_comment = Comment.objects.get(id=parent_comment_id)
                comment.parent = parent_comment  # Associate the comment with the parent comment

            comment.save()  # Save the comment (or reply)
            return redirect('blog:blog_detail', slug=blog.slug)  # Redirect to the same page to show the new comment

    else:
        form = CommentForm()

    # Retrieve all top-level comments (without parent)
    comments = blog.comments.filter(parent=None)

    return render(request, 'blog/blog_detail.html', {
        'blog': blog,
        'form': form,
        'comments': comments
    })

