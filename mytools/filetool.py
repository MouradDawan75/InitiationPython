
# Fonction de lecture d'un fichier texte

def lecture_fichier_texte(chemin:str) -> str:
    """Fonction de lecture d'un fichier texte.

    Args:
        chemin (str): Il faut fournir le chemin complet du fichier à lire. Ex: c:\\dossier\\test.txt

    Returns:
        str: renvoie le contenu du fichier.
    """

    try:

        with open(chemin,'r',encoding='utf-8') as flux:
            contenu = flux.read()

        return contenu

    except:
        print('Chemin inavlide........')


# Fonction d'écriture dans fichier texte

def ecriture_fichier_texte(chemin:str, contenu:str, mode_append:bool = False) -> None:
    """Fonction d'écriture dans un fichier texte.

    Args:
        chemin (str): Il faut fournir le chemin complet du fichier à lire. Ex: c:\\dossier\\test.txt
        contenu (str): Contenu à insérer dans le fichier
        mode_append (bool, optional): Pour insérer le contenu à la suite dans le fichier, mettre ce paramètre à True
    """
  

    mode_acces = 'w'

    if mode_append:
        mode_acces = 'a'
        contenu = '\n'+contenu

    try:
        with open(chemin, mode_acces, encoding='utf-8') as flux:
            flux.write(contenu)

    except:
        print('Chemin invalide.............')
