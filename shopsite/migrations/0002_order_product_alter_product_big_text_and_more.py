# Generated by Django 4.0.4 on 2023-07-07 09:24

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('shopsite', '0001_initial'),
    ]

    operations = [
        migrations.AddField(
            model_name='order',
            name='product',
            field=models.ForeignKey(null=True, on_delete=django.db.models.deletion.CASCADE, to='shopsite.product'),
        ),
        migrations.AlterField(
            model_name='product',
            name='big_text',
            field=models.TextField(),
        ),
        migrations.AlterField(
            model_name='product',
            name='text',
            field=models.TextField(),
        ),
    ]
