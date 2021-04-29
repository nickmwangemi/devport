from wagtail.images.blocks import ImageChooserBlock
from wagtail.core import blocks

class ResponsiveImageBlock(ImageChooserBlock):
    class Meta:
        icon = "image"
        template = "streamfieldblocks/responsive_image_block.html"

class CardBlock(blocks.StructBlock):
    image = ImageChooserBlock(required=False)
    title = blocks.CharBlock()
    body = blocks.TextBlock()
    page_link = blocks.PageChooserBlock()

    class Meta:
        icon = "placeholder"
        template = "streamfieldblocks/card_block.html"

class SimpleRichTextBlock(blocks.StructBlock):
    richtext = blocks.RichTextBlock(
        features=['h2','h3','h4','bold','italic','link','ol','ul'])

    class Meta:
        icon = "pilcrow"
        template = "streamfieldblocks/simple_richtext_block.html"