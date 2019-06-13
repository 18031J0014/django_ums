# Generated by Django 2.2.2 on 2019-06-09 17:34

from django.db import migrations, models
import phone_field.models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Student',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=20)),
                ('email', models.EmailField(max_length=254)),
                ('phone', phone_field.models.PhoneField(blank=True, help_text='Contact phone number', max_length=31)),
                ('rollno', models.CharField(max_length=10)),
                ('gender', models.CharField(choices=[('male', 'male'), ('female', 'female')], max_length=50)),
                ('department', models.CharField(choices=[('IT', 'IT'), ('CSE', 'CSE'), ('ECE', 'ECE'), ('EEE', 'EEE')], max_length=50)),
                ('address', models.TextField(max_length=100)),
                ('password', models.CharField(default='Student', max_length=20)),
                ('image', models.ImageField(blank=True, upload_to='images')),
                ('date_added', models.DateField(auto_now_add=True)),
            ],
            options={
                'ordering': ['-id'],
            },
        ),
    ]
