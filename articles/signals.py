from django.db.models.signals import pre_save
from django.dispatch import receiver
from .models import Article
from django.utils.text import slugify

@receiver(pre_save,sender=Article)
def create_post(sender,instance,*args,**kwargs):
    if not instance.slug:
        instance.slug =create_uniqe_slug(instance)

def create_uniqe_slug(instance,newslug=None):
    if newslug is not None:
        slug = newslug
    else:
        slug = slugify(instance.title,allow_unicode=True)

    instanClass = instance.__class__
    qs = instanClass.objects.filter(slug=slug)

    if qs.exists():
        newslug = f"{slug}-{qs.filter().id}"
        return create_uniqe_slug(instance,newslug)

    return slug
