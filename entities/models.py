from django.db import models


class Sector(models.Model):
    nombreSector = models.CharField(max_length=100)
    mail = models.EmailField(blank=False, default="mesadeayuda@frm.utn.edu.ar")

    def __str__(self):
        return str(self.id) + "-" + self.nombreSector

    class Meta:
        verbose_name_plural = "Sectores"



class TipoProblema(models.Model):
    descripcionTipoProblema = models.CharField(max_length=100)
    sectoresEncargados = models.ManyToManyField(Sector, blank=True)


    def __str__(self):
        return str(self.id) + "-" + self.descripcionTipoProblema

    class Meta:
        verbose_name_plural = "Tipos de Problema"


class Accion(models.Model):
    nombreTipoAccion = models.CharField(max_length=30)


    def __str__(self):
        return str(self.id) + "-" + self.nombreTipoAccion

    class Meta:
        verbose_name_plural = "Acciones"

class TipoSolicitante(models.Model):
    nombreTipoSolicitante = models.CharField(max_length=30)
    tiposProblema = models.ManyToManyField(TipoProblema, blank=True)

    def __str__(self):
        return str(self.id) + "-" + self.nombreTipoSolicitante

    class Meta:
        verbose_name_plural = "Tipos de Solicitante"

DEFAULT_TIPO_SOLICITANTE=1
class Solicitante(models.Model):
    nombreSolicitante = models.CharField(max_length=50, blank=False)
    apellidoSolitante = models.CharField(max_length=50, blank=False)
    emailSolicitante = models.EmailField(max_length=100, default=str(nombreSolicitante)+"."+str(apellidoSolitante)+"@"+"alumnos.frm.edu.ar")
    tipoSolicitante = models.ForeignKey(TipoSolicitante, on_delete=models.CASCADE, default=DEFAULT_TIPO_SOLICITANTE)
    legajo = models.IntegerField(blank=True, default="0")
    class Meta:
        verbose_name_plural = "Solicitantes"

    def __str__(self):
        return str(self.tipoSolicitante.nombreTipoSolicitante) + "-" + str(self.legajo) + "-" + str(self.nombreSolicitante) + " " + str(self.apellidoSolitante)

class EstadoConsulta(models.Model):
    nombreEstadoConsulta = models.CharField(max_length=100)

    class Meta:
        verbose_name_plural = "Estados de Consulta"

    def __str__(self):
        return str(self.id) + "-" + self.nombreEstadoConsulta


class Consulta(models.Model):
    asuntoConsulta = models.CharField(max_length=50)
    descripcionConsulta = models.TextField()
    fechayHoraConsulta = models.DateTimeField(auto_now=True)
    tipoProblema = models.ForeignKey(TipoProblema, null=True, on_delete=models.CASCADE)
    solicitante = models.ForeignKey(Solicitante, null=True, on_delete=models.CASCADE)
    estadoConsulta = models.ForeignKey(EstadoConsulta, on_delete=models.CASCADE, null=True)
    nombreSolicitante = models.CharField(max_length=50, null=True)
    apellidoSolicitante = models.CharField(max_length=50, null=True)
    emailSolicitante = models.EmailField(max_length=100, null=True)
    incidente = models.IntegerField(null=True)

    class Meta:
        verbose_name_plural = "Consultas"

    def __str__(self):
        return str(self.id) + "-" + self.asuntoConsulta






