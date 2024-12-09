from django import template
from blog.models import Post,Category,Comment
register = template.Library()

@register.inclusion_tag('blog/blog-popular.html')
def latestposts():
    posts = Post.objects.filter(status=1).order_by('published_date')[:3]
    return {"posts":posts}

@register.simple_tag(name='comments_count')
def function(pid):
    return Comment.objects.filter(post=pid,approved=True).count()

@register.inclusion_tag('blog/blog-postcatgories.html')
def postcategories():
    posts = Post.objects.filter(status=1)
    categories = Category.objects.all()
    cat_dict = {}
    
    for name in categories:
        filtered_posts = posts.filter(category=name)
        
        count = filtered_posts.count()
        
        cat_dict[name] = count
    
    return {'categories': cat_dict}
