from django.db import models
from django.utils import timezone
from usuarios.models import User
from django.urls import reverse
from embed_video.fields import EmbedVideoField

def upload_to(instance, filename):
    now = timezone_now()
    filename_base, filename_ext = os.path.splitext(filename)
    return "quotes/%s%s" % (
        now.strftime("%Y/%m/%Y%m%d%H%M%S"),
        filename_ext.lower(),

    )



class Post(models.Model):
    title = models.CharField(max_length=100, verbose_name="Titulo")
    content = models.TextField(verbose_name="Comentario")
    date_posted = models.DateTimeField(default=timezone.now)
    author = models.ForeignKey(User, on_delete=models.CASCADE, blank=True, verbose_name="Autor")
    video = EmbedVideoField(blank=True, null=True)
    image = models.ImageField(null=True, blank=True, upload_to='blog/')
    #ImageField(upload_to='upload/blog/blogcatImg/', blank=True, null=True)

    #def image_tag(self):
        #return format_html(
            #'<img src="/abcd/show/{}" style="width:40px;height:40px;border-radius:50%;" />'.format(self.image))

    def __str__(self):
        return self.title   

    def get_absolute_url(self):
        return reverse('post-detail', kwargs={'pk': self.pk})