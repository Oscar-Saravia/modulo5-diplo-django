# Generated by Django 5.0.7 on 2024-07-26 21:43

import django.db.models.deletion
import rewardPrime.validators
from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Character',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=100)),
                ('status', models.CharField(choices=[('Alive', 'Alive'), ('Dead', 'Dead'), ('Unknown', 'Unknown')], default='Alive', max_length=50)),
                ('species', models.CharField(max_length=50)),
                ('gender', models.CharField(choices=[('Male', 'Male'), ('Female', 'Female'), ('Genderless', 'Genderless'), ('Unknown', 'Unknown')], default='Unknown', max_length=20)),
                ('origin', models.CharField(max_length=100)),
                ('last_location', models.CharField(max_length=100)),
                ('image', models.URLField()),
                ('created_at', models.DateTimeField(auto_now_add=True)),
                ('updated_at', models.DateTimeField(auto_now=True)),
            ],
        ),
        migrations.CreateModel(
            name='Location',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.TextField(max_length=100)),
                ('type_location', models.TextField(max_length=100)),
                ('dimension', models.TextField(max_length=100)),
            ],
        ),
        migrations.CreateModel(
            name='Bounty',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('title', models.CharField(blank=True, max_length=50, null=True)),
                ('search_status', models.CharField(choices=[('Alive', 'Alive'), ('Dead', 'Dead'), ('Anyway', 'Anyway')], default='Alive', max_length=10)),
                ('description', models.TextField(blank=True, max_length=200, null=True, validators=[rewardPrime.validators.isAdviceValidated])),
                ('amount', models.DecimalField(decimal_places=2, default=1000, max_digits=10, validators=[rewardPrime.validators.isAmountValidated])),
                ('currency_type', models.CharField(choices=[('USD', 'US Dollar'), ('BFL', 'Blemflarcks'), ('FLB', 'Flurbo'), ('SCM', 'Schmeckle'), ('FPZ', 'Frapprizzos'), ('KBS', 'Kronobucks'), ('GPF', 'Gazorpazorpfield'), ('KCM', 'Kronometrics'), ('ZFD', 'Zibblefluds'), ('SDG', 'Smidgens'), ('GPS', 'Greeps'), ('BHS', 'Brohams'), ('SPF', 'Shrumpflesh'), ('PLT', 'Plutons'), ('GBB', 'Gooble Boxes'), ('FPC', 'Froopyland Credits'), ('MIB', 'Miblons'), ('PBF', 'Pebbles'), ('CPF', 'Crystal Puffs'), ('GFP', 'Greasy Gumflars'), ('RBK', 'Ribbleblanks')], default='USD', max_length=4)),
                ('created_at', models.DateTimeField(auto_now_add=True)),
                ('updated_at', models.DateTimeField(auto_now=True)),
                ('character_id', models.ForeignKey(default=1, on_delete=django.db.models.deletion.CASCADE, to='rewardPrime.character')),
            ],
        ),
        migrations.CreateModel(
            name='LogCharacter',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('description', models.TextField(max_length=100)),
                ('date_time', models.DateTimeField(auto_now_add=True)),
                ('character_id', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='rewardPrime.character')),
                ('location_id', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='rewardPrime.location')),
            ],
        ),
    ]
