# Generated by Django 2.0 on 2017-12-05 00:53

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('navigator', '0001_initial'),
    ]

    operations = [
        migrations.AlterModelOptions(
            name='guardian',
            options={'verbose_name': '선생님', 'verbose_name_plural': '선생님'},
        ),
        migrations.AlterModelOptions(
            name='request',
            options={'verbose_name': '도움 요청', 'verbose_name_plural': '도움 요청'},
        ),
        migrations.AlterModelOptions(
            name='shelter',
            options={'verbose_name': '쉼터', 'verbose_name_plural': '쉼터'},
        ),
    ]
