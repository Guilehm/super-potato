# Generated by Django 2.1.1 on 2018-09-08 23:43

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Patient',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('registration', models.CharField(db_index=True, max_length=11)),
                ('name', models.CharField(max_length=40)),
                ('email', models.EmailField(blank=True, db_index=True, max_length=200, null=True)),
                ('birth_date', models.DateField(db_index=True)),
                ('doc', models.CharField(blank=True, db_index=True, max_length=20, null=True)),
                ('home_phone_number', models.CharField(blank=True, max_length=20, null=True)),
                ('cell_phone_number', models.CharField(blank=True, max_length=20, null=True)),
                ('type', models.CharField(choices=[('holder', 'Holder'), ('dependent', 'Dependent')], db_index=True, max_length=20)),
                ('status', models.CharField(choices=[('affiliated', 'Affiliated'), ('disaffiliated', 'Disaffiliated'), ('abeyance', 'Abeyance')], db_index=True, max_length=20)),
                ('date_added', models.DateTimeField(auto_now_add=True)),
                ('date_changed', models.DateTimeField(auto_now=True)),
                ('holder', models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.SET_NULL, related_name='dependents', to='people.Patient')),
            ],
        ),
    ]
