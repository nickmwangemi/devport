from django.db import models

from streamfieldblocks.models import CardBlock, ResponsiveImageBlock, SimpleRichTextBlock
from wagtail.core.fields import StreamField
from wagtail.admin.edit_handlers import FieldPanel, StreamFieldPanel
from wagtail.images.edit_handlers import ImageChooserPanel


from wagtail.core.models import Page



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

    def get_context(self, request):
        context = super().get_context(request)
        blogpages = self.get_children().live().order_by('-first_published_at')
        context['blogpages'] = blogpages
        return context

class BlogPage(Page):
    date = models.DateField("Article Date")
    intro = models.TextField("Introduction")
    main_content = StreamField([
        ('richtext', SimpleRichTextBlock()),
        ('responsive_image', ResponsiveImageBlock()),
        ('card', CardBlock()),
    ], blank=True)
    featured = models.BooleanField(default=False)

    content_panels = Page.content_panels + [
        FieldPanel('date'),
        FieldPanel('featured'),
        FieldPanel('intro'),
        StreamFieldPanel('main_content'),
    ]
