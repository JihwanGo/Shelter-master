# Generated by Django 2.0 on 2017-12-04 11:04

from django.conf import settings
import django.contrib.auth.models
from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
        ('accounts', '0002_user_full_name'),
    ]

    operations = [
        migrations.CreateModel(
            name='Guardian',
            fields=[
                ('user_ptr', models.OneToOneField(auto_created=True, on_delete=django.db.models.deletion.CASCADE, parent_link=True, primary_key=True, serialize=False, to=settings.AUTH_USER_MODEL)),
                ('phone_number', models.CharField(max_length=11, verbose_name='전화번호')),
            ],
            options={
                'verbose_name': 'user',
                'verbose_name_plural': 'users',
                'abstract': False,
            },
            bases=('accounts.user',),
            managers=[
                ('objects', django.contrib.auth.models.UserManager()),
            ],
        ),
        migrations.CreateModel(
            name='Request',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('time', models.DateTimeField(auto_now_add=True, verbose_name='요청 시각')),
                ('lat', models.DecimalField(decimal_places=6, max_digits=9, verbose_name='위도')),
                ('lon', models.DecimalField(decimal_places=6, max_digits=9, verbose_name='경도')),
                ('name', models.CharField(blank=True, max_length=50, verbose_name='이름')),
                ('phone_number', models.CharField(max_length=11, verbose_name='전화번호')),
                ('platform', models.CharField(choices=[('W', 'Web'), ('I', 'iOS'), ('A', 'Android')], default='W', max_length=1, verbose_name='플랫폼')),
            ],
        ),
        migrations.CreateModel(
            name='Shelter',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=50, verbose_name='이름')),
                ('lat', models.DecimalField(decimal_places=6, max_digits=9, verbose_name='위도')),
                ('lon', models.DecimalField(decimal_places=6, max_digits=9, verbose_name='경도')),
            ],
        ),
        migrations.AddField(
            model_name='guardian',
            name='shelter',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='guardians', to='navigator.Shelter', verbose_name='소속'),
        ),
    ]
