#!/usr/bin/env python
# -*- coding: utf-8 -*-

# SERVEUR WEB - AFFICHAGE FIXE

# Importation des modules nécessaires
from flask import Flask

# Instanciation du serveur
serveur_web = Flask(__name__)

# Définit le texte à afficher selon le chemin de l'URL
@serveur_web.route('/')		# page racine
def racine() :
	return "Bonjour, vous êtes bien connecté à la Raspberry !!"
	
@serveur_web.route('/test/')	# page test
def test() :
	return "Changement de page... En construction"
	
# PROGRAMME PRINCIPAL
if __name__ == '__main__' :
	serveur_web.debug = False
	serveur_web.run(host="0.0.0.0")
