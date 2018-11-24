from django.db import models
# Create your models here.


class Materia(models.Model):
    idCuatrimestre = models.IntegerField()
    estado = models.BooleanField()
    codigo = models.CharField(max_length=20)
    descripcion = models.CharField(max_length=150)
    creditos = models.IntegerField()

    def __str__(self):
        return self.descripcion

class Horario(models.Model):
    idMateria = models.ForeignKey(Materia, on_delete=models.PROTECT)
    estado = models.BooleanField()
    aula = models.CharField(max_length=20)
    grupo = models.IntegerField()
    lun = models.CharField(max_length=20,null=True,blank=True)
    mar = models.CharField(max_length=20,null=True,blank=True)
    mier = models.CharField(max_length=20,null=True,blank=True)
    jue = models.CharField(max_length=20,null=True,blank=True)
    vie = models.CharField(max_length=20,null=True,blank=True)
    sab = models.CharField(max_length=20,null=True,blank=True)
    dom = models.CharField(max_length=20,null=True,blank=True)
    modulo = models.IntegerField(null=True,blank=True)

    def save(self, *args, **kwargs):
        from .tests import TestStringMethods

        test_instance = TestStringMethods()

        test_instance.test_aula_len(self.aula)

        test_instance.test_modulo_no_negativo(self.modulo)

        res = super(Horario, self).save(*args,**kwargs)

    def __str__(self):
        return "Horario " + self.idMateria.descripcion


# class Cuatrimestre(models.Model):
#     numero = models.IntegerField()
#     materias = models.ManyToManyField(Materia)
#
#     def __str__(self):
#         return "Cuatrimestre # "+ self.numero