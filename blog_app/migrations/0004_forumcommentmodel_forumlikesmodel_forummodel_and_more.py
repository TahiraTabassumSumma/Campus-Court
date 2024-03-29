# Generated by Django 4.0.4 on 2022-05-13 11:33

from django.conf import settings
from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
        ('blog_app', '0003_remove_blog_category'),
    ]

    operations = [
        migrations.CreateModel(
            name='ForumCommentModel',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('comment', models.TextField()),
                ('comment_date', models.DateTimeField(auto_now_add=True)),
            ],
            options={
                'ordering': ('-comment_date',),
            },
        ),
        migrations.CreateModel(
            name='ForumLikesModel',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
            ],
        ),
        migrations.CreateModel(
            name='ForumModel',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('title', models.CharField(max_length=250, verbose_name='Forum Title')),
                ('content', models.TextField(verbose_name='Forum Content')),
                ('slug', models.SlugField(max_length=250, unique=True)),
                ('published_date', models.DateTimeField(auto_now_add=True)),
                ('edit_date', models.DateTimeField(auto_now=True)),
                ('user', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='user_forum', to=settings.AUTH_USER_MODEL)),
            ],
        ),
        migrations.RenameModel(
            old_name='Blog',
            new_name='BlogModel',
        ),
        migrations.RemoveField(
            model_name='blogcomment',
            name='blog',
        ),
        migrations.RemoveField(
            model_name='blogcomment',
            name='user',
        ),
        migrations.RemoveField(
            model_name='bloglikes',
            name='blog',
        ),
        migrations.RemoveField(
            model_name='bloglikes',
            name='user',
        ),
        migrations.DeleteModel(
            name='Category',
        ),
        migrations.DeleteModel(
            name='BlogComment',
        ),
        migrations.DeleteModel(
            name='BlogLikes',
        ),
        migrations.AddField(
            model_name='forumlikesmodel',
            name='forum_post',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='forum_like', to='blog_app.forummodel'),
        ),
        migrations.AddField(
            model_name='forumlikesmodel',
            name='user',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='user_like', to=settings.AUTH_USER_MODEL),
        ),
        migrations.AddField(
            model_name='forumcommentmodel',
            name='forum_post',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='forum_post', to='blog_app.forummodel'),
        ),
        migrations.AddField(
            model_name='forumcommentmodel',
            name='user',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='user_forum_comment', to=settings.AUTH_USER_MODEL),
        ),
    ]
