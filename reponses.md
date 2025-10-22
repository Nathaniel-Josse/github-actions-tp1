3. Le répertoire .github/workflows permet de configurer le workflow de GitHub Actions.
8. Sur l'onglet Actions, on constate que le workflow défini a bien run, avec le Hello World.
10. Après commit et push, on constate que les deux workflows se sont exécutés. Le workflow ajouté a setup le projet.
11. En pushant une erreur intentionnelle, le workflow de test retourne une erreur, comme attendu.
12. En corrigeant l'erreur intentionnelle, les tests passent de nouveau.