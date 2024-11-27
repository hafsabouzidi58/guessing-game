#!/bin/bash

# Fonction pour demander à l'utilisateur de deviner le nombre de fichiers
function play_game {
    local file_count=$(ls -1 | wc -l) # Compte le nombre de fichiers dans le répertoire actuel
    local user_guess=-1 # Initialisation de la réponse de l'utilisateur
    
    echo "Bienvenue dans le jeu de devinettes !"
    echo "Combien de fichiers se trouvent dans le répertoire actuel ? Essayez de deviner."

    # Boucle jusqu'à ce que l'utilisateur trouve le bon nombre
    while [[ $user_guess -ne $file_count ]]; do
        # Demande à l'utilisateur une estimation
        read -p "Votre estimation : " user_guess
        
        # Vérifie si l'entrée est un nombre
        if [[ ! $user_guess =~ ^[0-9]+$ ]]; then
            echo "Veuillez entrer un nombre valide."
            continue
        fi

        # Comparaison de l'estimation avec le nombre réel de fichiers
        if [[ $user_guess -lt $file_count ]]; then
            echo "Trop bas ! Essayez encore."
        elif [[ $user_guess -gt $file_count ]]; then
            echo "Trop élevé ! Essayez encore."
        else
            echo "Félicitations ! Vous avez trouvé : il y a exactement $file_count fichiers."
        fi
    done
}

# Appel de la fonction
play_game
