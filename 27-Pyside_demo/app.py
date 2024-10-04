# Dans PySide, il y'à 2 classes à importer: QApplication, QWidget

# QApplication: pour créer l'appication (à utiliser q'une seule fois)
# QWidget: est la classe mère de tous les Widgets

from PySide6.QtCore import Qt
from PySide6.QtWidgets import QApplication, QWidget, QFileDialog
import sys
import os

sys.path.append(os.getcwd())

from mytools.filetool import lecture_fichier_texte,ecriture_fichier_texte



# Utilisation du design crée

from main_ui import Ui_Form

class Main_Window(QWidget, Ui_Form):


    # __init__: gère le design et les différents de la fenêtre
    def __init__(self) -> None:
        super().__init__()

        # Application du design crée dans Designer
        self.setupUi(self)

        # Gestion du button addition
        self.btnAddition.clicked.connect(self.somme)

        # Gestion du bouton lecture fichier
        self.btnLectureFichier.clicked.connect(self.lecture_fichier)

        # Gestion du bouton ecriture fichier
        self.btnEcritureFichier.clicked.connect(self.ecriture_fichier)





    ####### Une fonction pour chaque besoin

    def somme(self):
        nb1 = float(self.lineEditNb1.text())
        nb2 = float(self.lineEditNb2.text())
        s = nb1+nb2
        self.lblAddition.setText(str(s))

    def lecture_fichier(self):
        dialog = QFileDialog()
        resultat = dialog.exec() # renvoie 1: si fichier sélectionné sinon renvoie 0
        if resultat:
            chemin = dialog.selectedFiles()[0]
            contenu = lecture_fichier_texte(chemin)
            self.champTexte.setPlainText(contenu)


    def ecriture_fichier(self):

        dialog = QFileDialog()
        resultat = dialog.exec() # renvoie 1: si fichier sélectionné sinon renvoie 0
        if resultat:
            chemin = dialog.selectedFiles()[0]
            contenu = self.champTexte.toPlainText()
            ecriture_fichier_texte(chemin,contenu)
              




    


# Créer l'application

app = QApplication()

# fenetre = QWidget()
# fenetre.show()

f = Main_Window()
f.show()

app.exec()