3. Le répertoire .github/workflows permet de configurer le workflow de GitHub Actions.
8. Sur l'onglet Actions, on constate que le workflow défini a bien run, avec le Hello World.
10. Après commit et push, on constate que les deux workflows se sont exécutés. Le workflow ajouté a setup le projet.
11. En pushant une erreur intentionnelle, le workflow de test retourne une erreur, comme attendu.
12. En corrigeant l'erreur intentionnelle, les tests passent de nouveau.
14. Après le push, on constate que les tests ont été run sur la matrice des versions de Python que nous avons donné. Chaque test a donc été lancé en Python 3.8, 3.9, et 3.10.
_Remarque : Les workflows exécutés ont toujours été uniquement ceux de la branche en default._
18. On remarque que dans une nouvelle branche, les workflows ne sont pas exécutés.
19. Après avoir poussé ces modifications, le Workflow de badge a run mais ne semble pas avoir affecté correctement le README.
24. Après avoir ajouté le workflow de Docker, le build Docker a fonctionné en s'étant bien lancé.
27. Après avoir ajouté le workflow evaluate, il renvoie l'erreur suivante : Error: This request has been automatically failed because it uses a deprecated version of `actions/upload-artifact: v3`. Learn more: https://github.blog/changelog/2024-04-16-deprecation-notice-v3-of-the-artifact-actions/ . Le résultat attendu est probablement une réussite de l'évaluation.
30. Le workflow a de nouveau planté pour la même raison que 27. Le résultat attendu est probablement une variation des réussites et échecs du workflow selon les stats reçues.
33. On constate que le Workflow manuel peut être lancé directement depuis GitHub Actions.
36. Dans l'onglet Releases, le tag apparaît désormais.
38. On constate que cela renvoie la même erreur que 27. Le résultat attendu est probablement une constatation de la doc ?