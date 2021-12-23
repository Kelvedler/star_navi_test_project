# Generated by Django 4.0 on 2021-12-22 21:52

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
        ('users', '0002_user_last_activity'),
    ]

    operations = [
        migrations.CreateModel(
            name='Post',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('body', models.CharField(max_length=280)),
                ('author', models.ForeignKey(on_delete=django.db.models.deletion.RESTRICT, to='users.user')),
            ],
        ),
        migrations.CreateModel(
            name='Like',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('timestamp', models.DateTimeField(auto_now_add=True)),
                ('post', models.ForeignKey(on_delete=django.db.models.deletion.RESTRICT, to='posts.post')),
                ('user', models.ForeignKey(on_delete=django.db.models.deletion.RESTRICT, to='users.user')),
            ],
            options={
                'unique_together': {('post', 'user')},
            },
        ),
    ]
