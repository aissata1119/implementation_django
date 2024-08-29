

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Teacher',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('nom', models.CharField(max_length=15)),
                ('prenoms', models.CharField(max_length=50)),
                ('genre', models.CharField(max_length=20)),
                ('dateNaissance', models.DateField()),
                ('matiere', models.CharField(choices=[('MATH', 'MATH'), ('PHYSIQUE', 'PHYSIQUE'), ('SVT', 'SVT'), ('FRANCAIS', 'FRANCAIS')], max_length=20)),
                ('telephone', models.CharField(max_length=30)),
            ],
        ),
    ]
