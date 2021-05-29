from django.db import models

from wagtail.core.models import Page
from wagtail.core.fields import RichTextField
from wagtail.admin.edit_handlers import FieldPanel
from wagtail.images.edit_handlers import ImageChooserPanel


class BlogListingPage(Page):
    background_image = models.ForeignKey(
        'wagtailimages.Image',
        blank=False,
        null=True,
        related_name='+',
        help_text='Header background image',
        on_delete=models.SET_NULL,
    )

    headline_text = models.CharField(
        max_length=70,
        blank=True, 
        help_text='Blog listing page header text.'
    )

    content_panels = Page.content_panels + [
        ImageChooserPanel("background_image"), 
        FieldPanel("headline_text"),
    ]


class BlogPage(Page):
    date = models.DateField("Article Date")
    intro = models.TextField("Introduction")
    blog_image = models.ForeignKey(
        'wagtailimages.Image',
        blank=False,
        null=True,
        related_name='+',
        help_text='blog image',
        on_delete=models.SET_NULL,
    )

    body = RichTextField(
        blank=True,
    )

    content_panels = Page.content_panels + [
        ImageChooserPanel("blog_image"), 
        FieldPanel('date'),
        FieldPanel('intro'),
        FieldPanel('body', classname="full"),
    ]