# Generated by Django 2.1.1 on 2018-09-14 02:02

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Patient',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('first_name', models.CharField(max_length=40)),
                ('last_name', models.CharField(max_length=40)),
                ('email', models.EmailField(blank=True, db_index=True, max_length=200, null=True)),
                ('birth_date', models.DateField(db_index=True)),
                ('doc', models.CharField(blank=True, db_index=True, max_length=20, null=True)),
                ('home_phone_number', models.CharField(blank=True, max_length=20, null=True)),
                ('cell_phone_number', models.CharField(blank=True, max_length=20, null=True)),
                ('date_added', models.DateTimeField(auto_now_add=True)),
                ('date_changed', models.DateTimeField(auto_now=True)),
                ('type', models.CharField(choices=[('holder', 'Holder'), ('dependent', 'Dependent')], db_index=True, max_length=20)),
                ('status', models.CharField(choices=[('affiliated', 'Affiliated'), ('disaffiliated', 'Disaffiliated'), ('abeyance', 'Abeyance')], db_index=True, max_length=20)),
            ],
            options={
                'abstract': False,
            },
        ),
        migrations.CreateModel(
            name='Professional',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('first_name', models.CharField(max_length=40)),
                ('last_name', models.CharField(max_length=40)),
                ('email', models.EmailField(blank=True, db_index=True, max_length=200, null=True)),
                ('birth_date', models.DateField(db_index=True)),
                ('doc', models.CharField(blank=True, db_index=True, max_length=20, null=True)),
                ('home_phone_number', models.CharField(blank=True, max_length=20, null=True)),
                ('cell_phone_number', models.CharField(blank=True, max_length=20, null=True)),
                ('date_added', models.DateTimeField(auto_now_add=True)),
                ('date_changed', models.DateTimeField(auto_now=True)),
                ('transfer_value', models.DecimalField(decimal_places=2, max_digits=8)),
                ('registration_number', models.CharField(db_index=True, max_length=20, unique=True)),
                ('service_phone_number', models.CharField(blank=True, max_length=20, null=True)),
                ('status', models.CharField(choices=[('active', 'Active'), ('inactive', 'Inactive'), ('on_hold', 'On hold')], db_index=True, max_length=20)),
            ],
            options={
                'abstract': False,
            },
        ),
    ]
