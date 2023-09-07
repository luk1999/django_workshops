# Creating and displaying comments

We're going to create comments section under every article.

## Create `Comment` model
* Open file `blog/models.py`.
* Add new model on the bottom of file:
  ```python
  class Comment(models.Model):
      post = models.ForeignKey(Post, on_delete=models.CASCADE)
      comment = models.TextField()
      created_by = models.ForeignKey(User, on_delete=models.RESTRICT)
      created_at = models.DateTimeField(auto_now_add=True)

      def __str__(self):
          return self.comment[:50]
  ```
# Create and apply database migrations
* Run command to create migration file:
  ```bash
  python manage.py makemigrations
  ```
* File `blog/migrations/0002_comment.py` should be created
* Run command to apply changes on database:
  ```bash
  python manage.py migrate
  ```

## Make `Comment` model editable in admin
* Open file `blog/admin.py`
* Import `Comment` model:
  ```python
  from blog.models import Comment, Post
  ```
* Add new `CommentAdmin`, similar to `PostAdmin`:
  ```python
  class CommentAdmin(admin.ModelAdmin):
      list_display = ("post", "created_by", "created_at")
      exclude = ("created_by",)

      def save_model(self, request, obj, form, change):
          obj.created_by = request.user
          super().save_model(request, obj, form, change)
  ```
* Register `CommentAdmin` on the bottom of file:
  ```python
  admin.site.register(Comment, CommentAdmin)
  ```
* Go to Admin Panel page. There should be `Comment` and `Post` in `Blog` app section available.
* Try to add few new comments to existing posts.

## List comments on post detail page
* Open file `blog/views.py`
* Import `Comment` model:
  ```python
  from blog.models import Comment, Post
  ```
* Go to `PostDetailView` and add `get_context_data` method:
  ```python
  class PostDetailView(DetailView):
      # ... Other code
      def get_context_data(self, **kwargs):
          context = super().get_context_data(**kwargs)
          post_id = self.object.pk
          context["comments"] = Comment.objects.filter(post_id=post_id).order_by("-created_at")
          return context
  ```
* Open file `templates/blog/detail.html`.
* Add list of comments on the bottom of file:
  ```html
  <hr>
  <h2>Comments</h2>
  {% for comment in comments %}
      <p>
          <small>
              Written by: {{ comment.created_by }},
              Created at: {{ comment.created_at }}
          </small>
          <br>{{ comment.comment|linebreaksbr }}
      </p>    
  {% empty %}
  <p>Could not find any comments.</p>
  {% endfor %}
  ```
* Open [http://127.0.0.1:8000](http://127.0.0.1:8000) in web browser and click on any post that have at least one comment. You should see a section `Comments` under post content.
