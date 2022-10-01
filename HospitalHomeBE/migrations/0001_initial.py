# Generated by Django 4.1.1 on 2022-09-30 23:17

from django.conf import settings
from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
        ('auth', '0012_alter_user_first_name_max_length'),
    ]

    operations = [
        migrations.CreateModel(
            name='Medico',
            fields=[
                ('id', models.AutoField(primary_key=True, serialize=False)),
                ('especialidad', models.CharField(max_length=45)),
                ('registro', models.CharField(max_length=20)),
            ],
        ),
        migrations.CreateModel(
            name='Rol',
            fields=[
                ('tipo_usuario', models.CharField(choices=[('Paciente', 'Paciente'), ('Familiar', 'Familiar'), ('Auxiliar', 'Auxiliar'), ('Medico', 'Medico'), ('Enfermero', 'Enfermero')], max_length=9, primary_key=True, serialize=False)),
                ('permisos', models.IntegerField(default=0)),
            ],
        ),
        migrations.CreateModel(
            name='Usuario',
            fields=[
                ('last_login', models.DateTimeField(blank=True, null=True, verbose_name='last login')),
                ('is_superuser', models.BooleanField(default=False, help_text='Designates that this user has all permissions without explicitly assigning them.', verbose_name='superuser status')),
                ('id', models.BigAutoField(primary_key=True, serialize=False)),
                ('rol', models.CharField(max_length=50, verbose_name='Rol')),
                ('nombre', models.CharField(max_length=50, verbose_name='Nombre')),
                ('apellido', models.CharField(max_length=50, verbose_name='Apellido')),
                ('celular', models.CharField(max_length=50, verbose_name='Telefono')),
                ('e_mail', models.EmailField(max_length=50, verbose_name='Correo')),
                ('direccion', models.CharField(max_length=50, verbose_name='Direccion')),
                ('username', models.CharField(max_length=50, unique=True, verbose_name='Usuario')),
                ('password', models.CharField(max_length=256, verbose_name='Contraseña')),
                ('groups', models.ManyToManyField(blank=True, help_text='The groups this user belongs to. A user will get all permissions granted to each of their groups.', related_name='user_set', related_query_name='user', to='auth.group', verbose_name='groups')),
                ('user_permissions', models.ManyToManyField(blank=True, help_text='Specific permissions for this user.', related_name='user_set', related_query_name='user', to='auth.permission', verbose_name='user permissions')),
            ],
            options={
                'abstract': False,
            },
        ),
        migrations.CreateModel(
            name='Paciente',
            fields=[
                ('id', models.AutoField(primary_key=True, serialize=False)),
                ('medico', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='HospitalHomeBE.medico')),
                ('usuario', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to=settings.AUTH_USER_MODEL)),
            ],
        ),
        migrations.AddField(
            model_name='medico',
            name='usuario',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to=settings.AUTH_USER_MODEL),
        ),
        migrations.CreateModel(
            name='Historia',
            fields=[
                ('id', models.BigAutoField(primary_key=True, serialize=False)),
                ('oximetria', models.JSONField(null=True)),
                ('f_respiratoria', models.JSONField(null=True)),
                ('f_cardiaca', models.JSONField(null=True)),
                ('temperatura', models.JSONField(null=True)),
                ('presion_arterial', models.JSONField(null=True)),
                ('glicemias', models.JSONField(null=True)),
                ('diagnostico', models.TextField(null=True)),
                ('cuidados', models.TextField(null=True)),
                ('paciente', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='HospitalHomeBE.paciente')),
            ],
        ),
        migrations.CreateModel(
            name='Familiar',
            fields=[
                ('id', models.BigAutoField(primary_key=True, serialize=False)),
                ('parentezco', models.CharField(max_length=40, null=True)),
                ('usuario', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to=settings.AUTH_USER_MODEL)),
            ],
        ),
        migrations.CreateModel(
            name='Enfermero',
            fields=[
                ('id', models.AutoField(primary_key=True, serialize=False)),
                ('area', models.CharField(max_length=50, verbose_name='Area')),
                ('usuario', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to=settings.AUTH_USER_MODEL)),
            ],
        ),
    ]
