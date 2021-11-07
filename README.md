# Projet-2-daar

le but de ce projet et d'indexer des cvs dans Elasticsearch en passant par deux point essentielle: 
- Indexe des données du CV dans l’instance Elasticsearch lors de son ajout.
- La recherche en se basant sur des terme

Un utilisateur a la possibilité d’uploader des CVs en format PDF seulement.
on a gérer  deux configurations  : une partie DEV à était realiser par Python elle log sur la console et une partie Prod qui log sur Kibana.

Partie Dev :
Nous avons creer un folder CV qui contien tout les PDF qu'on veut les indexer et faire la recherche sur, ensuite on a ecrit un programme qui permet d'ouvrir et de lire ce folder extraire ses informations en meta et les mettre dans un dictionnaire puis transformer le contenue en JSON . nous avons ensuite utiliser la methode index() pour indexer cette data et nous avons  afficher le resultat sur la console, une fois qu'on ait eu le résultat de la data indexer  sur la console on fais le search on visualisons le résultat du search par nombres de Hits (tapper le mots recherché ===> nombre d'occurence est : ...)

Partie Prod :
maintenant si on veut visualiser le resultat sur kibana, on doit d'abbord installer puis  elasticsearch  en tappant sur le cmd de bin (elasticsearch), ensuite installer et et lancer kibana sur cmd de bin en tappant (kibana)  une fois il demarre, on ouvre l'interface: "http://localhost:5601" puis sur devtools en ecris la commande
 (GET pdf/_doc/0  pour le cv1  ou GET pdf/_doc/0  pour le cv1 ) si on veut afficher l'indexation du repertoire CV qui contient deux cvs donc deux id différent (0 et 1) on peut avoir autant de cv qu'on veut donc autant d'id qu'on veut

 la meme chose si on veut visualiser sur kibana le resultat de recherche sur ce qu'on a indexer, on ecris 
 GET pdf/_search
