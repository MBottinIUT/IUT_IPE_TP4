#!/usr/bin/env python
# encoding: utf-8
from __future__ import unicode_literals

"""
Module IPE - TPs Raspberry
auteurs : Noms des etudiants
Etablissement : IUT de Rennes - Dpt GEII
Date : 31.07.2018 21:53:31 Paris, Madrid

Commentaires : 
"""
# RECUPERATION DES PREVISIONS METEO DE LA VILLE DE RENNES

# Importation des modules nécessaires
import pywapi
from pprint import pprint

# Récupération des prévisions météo de la ville 'Rennes' depuis weather.com
previsions_meteo = pywapi.get_weather_from_weather_com("FRXX0114")

# Affichage des prévisions météo dans le terminal dans un format plus convivial
pprint(previsions_meteo)
	
