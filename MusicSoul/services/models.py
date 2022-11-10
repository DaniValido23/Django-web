from django.db import models
from ckeditor_uploader.fields import RichTextUploadingField

# from ckeditor.fields import RichTextField

class Order(models.Model):
    name = models.CharField(max_length=100, verbose_name='Nombre')
    address = models.CharField(max_length=200, verbose_name='Dirección')
    colonia = models.CharField(max_length=200, verbose_name='Colonia')
    total = models.DecimalField(verbose_name='Total', max_digits=8, decimal_places=2)
    email = models.EmailField(verbose_name='Email')
    date = models.DateTimeField(auto_now_add=True, verbose_name='Fecha del pedido')

    class Meta:
        verbose_name = 'Pedido'
        verbose_name_plural = 'Pedidos'
        ordering = [ 'date' ]

    def __str__(self):
        return str(self.id)

class Service(models.Model):
    title = models.CharField(max_length=200, verbose_name='Título')
    subtitle = models.CharField(max_length=200, verbose_name='Subtítulo')
    content = RichTextUploadingField(verbose_name='Contenido')
    image = models.ImageField(upload_to='services', null=True, blank=True, verbose_name='Imagen')
    created = models.DateTimeField(auto_now_add=True, verbose_name='Fecha de creación')
    updated = models.DateTimeField(auto_now=True, verbose_name='Fecha de actualización')

    class Meta:
        verbose_name = 'Servicio'
        verbose_name_plural = 'Servicios'
        ordering = [ '-updated' ]

    def __str__(self):
        return self.title
