# Generated by Django 4.2.3 on 2024-05-24 19:43

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Category',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('image', models.ImageField(upload_to='category-image')),
                ('name', models.CharField(max_length=50)),
            ],
        ),
        migrations.CreateModel(
            name='ColorImage',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('image', models.ImageField(blank=True, null=True, upload_to='color')),
                ('name', models.CharField(blank=True, max_length=50, null=True)),
            ],
        ),
        migrations.CreateModel(
            name='Product',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=255)),
                ('description', models.TextField(blank=True)),
                ('category', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='product_app.category')),
            ],
        ),
        migrations.CreateModel(
            name='Size',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=20)),
            ],
        ),
        migrations.CreateModel(
            name='Color',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=50)),
                ('images', models.ManyToManyField(related_name='colors', to='product_app.colorimage')),
                ('product', models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.CASCADE, to='product_app.product')),
            ],
        ),
        migrations.CreateModel(
            name='ProductVariant',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('actual_price', models.DecimalField(blank=True, decimal_places=2, max_digits=10, null=True)),
                ('discount_price', models.DecimalField(blank=True, decimal_places=2, max_digits=10, null=True)),
                ('stock', models.PositiveIntegerField(default=0)),
                ('color', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='product_app.color')),
                ('product', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='product_app.product')),
                ('size', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='product_app.size')),
            ],
            options={
                'unique_together': {('product', 'size', 'color')},
            },
        ),
    ]
