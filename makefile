# Nom du fichier généré
README.md: guessinggame.sh
	@echo "# Guessing Game Project" > README.md
	@echo "" >> README.md
	@echo "## Date et heure d'exécution" >> README.md
	@echo "\`\`\`" >> README.md
	@date "+%Y-%m-%d %H:%M:%S" >> README.md
	@echo "\`\`\`" >> README.md
	@echo "" >> README.md
	@echo "## Nombre de lignes de code dans guessinggame.sh" >> README.md
	@echo "\`\`\`" >> README.md
	@wc -l < guessinggame.sh >> README.md
	@echo "\`\`\`" >> README.md
	@echo "" >> README.md
	@echo "## Site GitHub Pages" >> README.md
	@echo "La seconde URL est : [Votre Site GitHub Pages](https://<votre-utilisateur>.github.io/<votre-repository>/)" >> README.md

# Commande pour nettoyer les fichiers générés
clean:
	rm -f README.md
