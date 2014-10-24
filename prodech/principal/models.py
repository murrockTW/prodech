#encoding:utf-8
from django.db import models

# Create your models here.

class Jugador(object):
	"""Clase que representa a los jugadores"""
	def __init__(self, arg):
		super(Jugador, self).__init__()
		self.arg = arg
		
	nombre = models.CharField(max_length=50, unique=True)
	#email = models.EmailField()
	#password = models.CharField()
	tiempo_registro = models.DateTimeField(auto_now=True)
	usuario = models.ForeignKey(User)

    def __unicode__(self):
    	return self.nombre

class Equipo(object):
	"""Clase que representa equipos de futbol"""
	def __init__(self, arg):
		super(Equipo, self).__init__()
		self.arg = arg

	nombre = models.CharField(max_length=50, unique=True)
	
	def __unicode__(self):
    	return self.nombre

class Torneo(object):
	"""Clase que representa los distintos torneos en donde participan los equipos"""
	def __init__(self, arg):
		super(Torneo, self).__init__()
		self.arg = arg
	
	nombre = models.CharField(max_length=50, unique=True)
	equipo = models.ManyToManyField(Equipo)

	def __unicode__(self):
    	return self.nombre

class Fecha(object):
	"""Clase que representa a los partidos que se realizan en un torneo"""

	Local = 'L'
	Empate = 'E'
	Visitante = 'V'
	
	RESULTADO_CHOICES = (
		('L', 'Local'),
		('E', 'Empate'),
		('V', 'Visitante'),
	)

	def __init__(self, arg):
		super(Partido, self).__init__()
		self.arg = arg

	torneo = models.ForeignKey(Torneo)
	numero = models.IntegerField()
	equipo_local = models.ForeignKey(Equipo)
	equipo_visitante = models.ForeignKey(Equipo)
	fecha = models.DateTimeField()
	ganador = models.CharField(max_length=1, choices=RESULTADO_CHOICES)

	def __unicode__(self):
    	return self

class Boleta(object):
	"""Clase que representa los pronosticos (jugadas) de los jugadores"""

	Local = 'L'
	Empate = 'E'
	Visitante = 'V'
	
	RESULTADO_CHOICES = (
		('L', 'Local'),
		('E', 'Empate'),
		('V', 'Visitante'),
	)

	def __init__(self, arg):
		super(Boleta, self).__init__()
		self.arg = arg

	fecha = models.ForeignKey(Fecha)
	ganador = models.CharField(max_length=1, choices=RESULTADO_CHOICES)

	def __unicode__(self):
    	return self