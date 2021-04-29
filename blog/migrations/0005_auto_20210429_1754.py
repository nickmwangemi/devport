# Generated by Django 3.1.8 on 2021-04-29 17:54

from django.db import migrations
import streamfieldblocks.models
import wagtail.core.blocks
import wagtail.core.fields
import wagtail.images.blocks


class Migration(migrations.Migration):

    dependencies = [
        ('blog', '0004_blogpage_main_content'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='blogpage',
            name='body',
        ),
        migrations.AlterField(
            model_name='blogpage',
            name='main_content',
            field=wagtail.core.fields.StreamField([('responsive_image', streamfieldblocks.models.ResponsiveImageBlock()), ('card', wagtail.core.blocks.StructBlock([('image', wagtail.images.blocks.ImageChooserBlock(required=False)), ('title', wagtail.core.blocks.CharBlock()), ('body', wagtail.core.blocks.TextBlock()), ('page_link', wagtail.core.blocks.PageChooserBlock())]))], blank=True),
        ),
    ]