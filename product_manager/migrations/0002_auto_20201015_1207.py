# Generated by Django 3.1.2 on 2020-10-15 06:22

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('product_manager', '0001_initial'),
    ]

    operations = [
        migrations.CreateModel(
            name='Brand',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=200)),
                ('is_active', models.BooleanField()),
            ],
        ),
        migrations.CreateModel(
            name='Category',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=200)),
                ('is_active', models.BooleanField()),
            ],
        ),
        migrations.RenameField(
            model_name='product',
            old_name='address',
            new_name='image_url',
        ),
        migrations.RenameField(
            model_name='product',
            old_name='age',
            new_name='quantity',
        ),
        migrations.RemoveField(
            model_name='product',
            name='remarks',
        ),
        migrations.AddField(
            model_name='product',
            name='color_code',
            field=models.CharField(default=1, max_length=20),
            preserve_default=False,
        ),
        migrations.AddField(
            model_name='product',
            name='is_active',
            field=models.BooleanField(default=1),
            preserve_default=False,
        ),
        migrations.AddField(
            model_name='product',
            name='price',
            field=models.FloatField(default=3500),
            preserve_default=False,
        ),
        migrations.AddField(
            model_name='product',
            name='registered_on',
            field=models.DateTimeField(default="2020-10-15"),
            preserve_default=False,
        ),
        migrations.AddField(
            model_name='product',
            name='brand',
            field=models.ForeignKey(default=1, on_delete=django.db.models.deletion.CASCADE, to='product_manager.brand'),
            preserve_default=False,
        ),
        migrations.AddField(
            model_name='product',
            name='category',
            field=models.ForeignKey(default=1, on_delete=django.db.models.deletion.CASCADE, to='product_manager.category'),
            preserve_default=False,
        ),
    ]
