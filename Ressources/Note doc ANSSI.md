Note doc ANSSI

# Prise de note lecture doc ANSSI  
  
  

### Différent niveaux de durcissement  
  

- MIRE Recommandation de niveau minimal. A mettre en oeuvre systématiquement sur tout le systeme.  
- IRE Recommandation à appliquer dés le niveau intermédiaire. Correspond généralement à des services protégés par plusieurs couches de sécurité de niveau supérieur   
- E Recommandation valide au niveau élevé. Correspond à des systemes hébergeant des données sensibles accessibles depuis des réseaux non authentifiés ou peu contrôlés.  
  

![](https://github.com/StevenDias33/HellFire/blob/master/Ressources/images/Niveaux%20durcissement.png  )
  
  

# Prise de note lecture doc ANSSI

### Différent niveaux de durcissement

-   MIRE Recommandation de niveau minimal. A mettre en oeuvre systématiquement sur tout le systeme.
-   IRE R# Prise de note lecture doc ANSSI


### Différent niveaux de durcissement

- MIRE Recommandation de niveau minimal. A mettre en oeuvre systématiquement sur tout le systeme.
- IRE Recommandation à appliquer dés le niveau intermédiaire. Correspond généralement à des services protégés par plusieurs couches de sécurité de niveau supérieur 
- E Recommandation valide au niveau élevé. Correspond à des systemes hébergeant des données sensibles accessibles depuis des réseaux non authentifiés ou peu contrôlés.

![](https://github.com/StevenDias33/HellFire/blob/master/Ressources/images/Niveaux%20durcissement.png)
## Principes généraux de sécurité et de durcissement

### Principe de minimisation 
 
 C'est un principe qui indique que les systemes conçus et installés doivent éviter les complexités en vue de :

- réduire la surface d'attaque au strict minimum
-  Permettre une mise à jour et un suivi du systeme efficace
-  Rendre l'activité de surveillance des systemes plus accessible, dans la mesure ou le nombre de composant à surveiller est réduit (MIRE)


### Principe de moindre privilège 

Principe qui définit que tout objet ou entité gérée par un systeme ne dispose que des droits strictement nécessaires à son exécution et rien de plus.(RE)

L'objectif est le gain en sécurité et sureté : 

- les conséquences de dysfonctionnements ou vulnérabilités sont limitées aux privilesges octroyés;
- L'altération ou la compromission du systeme nécessitent une escalade de privileges, moins tri-viale et discrete à réaliser dans les cas ou plusieurs couche de protection sont mises en place. 

Utilisation des fonctionnalités de controles d'accés :

-utilisation de fonction de cloisonnement et de controle de privileges(POSIX capabilities, namespaces, filtres seccomp, ou solution à base de conteneurs)

### Principe de défense en profondeur

Le principe de défense en profondeur impose la conception de plusieurs couches de sécurité in- dépendantes et complémentaires en vue de retarder un attaquant dont l’objectif est la compromis- sion du système. Chaque couche de sécurité est donc un point de résistance que l’attaquant doit franchir. La mise en défaut d’une couche s’accompagne de signaux, d’alarmes ou de messages de journalisation permet- tant de détecter une activité suspecte et de pouvoir y réagir. L’étape de rémédiation se trouve aussi facilitée grâce aux informations supplémentaires agrégées sur le contexte de la compromission.

Sous unix et dérivés , la défense en profondeur doit réposeru sur une combinaison de barrieres qu'il faut garder indépendantes les unes des autres, Par exemple :

- Authentification nécessaie avant d'effectuer des opérations, notamment quand elles sont privilégiées;
- Journalisation centralisée d'évènement au niveau systemes et services
- Utilisation préférentielle de services qui implémentent des mécanismes de cloisonnement ou de séparation de privilèges;
- utilisation de mécanismes de prévention d'exploitation


Les services réseau doivent autant que possible être hébergés sur des environnements distincts. Cela évite d'avoir d'autres services potentiellement affectés si l'un d'eux se retrouve compromis sous le même environnement 


### Activité de veille et de maintenance 

- Journalisation de l'activité des services 
- Mise à jour régulieres 


## Configuration matérielle avant installation 

### Réglage général du BIOS 

- Configuration matérielle 
il est conséillé d'appliquer les recommandantions de configuration mentionnées dans la note technique " Recommandations de configuration matérielle de postes clients et serveurs x86" 

### Mode 32 ou 64 bits 

il existe 2 mode sur les distributions GNU/Linux et UNIX:

- le mode protégé (protected mode), cantonné à un adressage virtuel sur 32 bits (4 octets) ; 
- le mode long (long mode), qui permet un adressage plus large sur 64 bits 1 (8 octets).


- Lorsque la machine le supporte, préférer l’installation d’une distribution GNU/Linux en version 64 bits plutôt qu’en version 32 bits.

### Service d'IOMMU (virtualisation entrée/sortie)

L'IOMMU permet de protéger la mémoire du systeme vis-à-vis d'accés arbitraires réalisés par des périphériques. 

l'activation de la fonctionnalité dépendra de la config matérielle et du réglage de l'OS il est possible que linux décide de ne pas initialiser l'IOMMU.

- La directive iommu=force doit être rajoutée à la liste des paramètres du noyau choisi lors du démarrage en plus de celles déjà présentes dans les fichiers de configuration du chargeur de démarrage a (/boot/grub/menu.lst ou /etc/default/grub).

		 #Exemple pour un fichier /etc/default/grub
		'''
		GRUB_CMDLINE_LINUX" iommu=force"

## Installation du système

### Partitionnement 

Il faut préserver des partitions dédiées aux services pouvant générer beaucoup de volumétrie afin d'éviter de saturer les partitions du systeme. 
Il faut adapter l'espace réserver en fonction des cas d'usage.
Exemple un serveur de fichier aura besoin de plus de volumétrie sur /srv ou /var/ftp alors qu'un serveur de log sera plus concerné par le /var/log

Le partitionnement doit permettre de protéger et isoler les différents composants du système de fichier. il est par défaut souvent insatisfaisant: il ne tient pas suffissament compte des options `nosuid` (ignore les bits setuid/setgid) `nodev` (ignore les fichiers spéciaux caractère ou bloc), 
et `noexec`(ignore les droits d'éxécution).

Il faut noter que suivant les systèmes et distributions, certaines des options de montage ne seront pas applicables transitoirement ; par exemple des utilitaires, installeurs ou produits estimeront que les fichiers écrits dans /tmp ou /var peuvent être exécutables. Dans ces cas exceptionnels il est nécessaire d’adapter le partitionnement. Un de ceux les plus fréquemment rencontrés est celui des distributions dérivées de Debian dont le /var/lib/dpkg nécessite des droits d’exécution. Une alternative est d’implémenter une procédure de maintenance durant laquelle les mises à jour sont installées, à l’image de ce que l’on trouve sur d’autres systèmes d’exploitation.

![Partitionnement Type](https://github.com/StevenDias33/HellFire/blob/master/Ressources/images/Partitionnement%20type.png)
### Restriction d'accés sur le dossier /boot 

La partition /boot contient le noyau de démarrage ainsi que le(s) fichier(s) System.map contenant la table des symboles utilisée par celui-ci. Ce fichier est souvent parcouru par différents programmes malveillants afin de construire plus facilement des « exploits » de code noyau. Le partitionnement idéal demande à ce que cette partition ne soit pas montée automatiquement au démarrage (option noauto), car son contenu est inutile en phase d’utilisation normale d’un système. En revanche, son montage ci est indispensable pour réaliser certains évènements critiques d’un point de vue système (pour une mise à jour ou un correctif noyau par exemple).

- Lorsque c'est possible, la partition `/boot` ne doit pas être montée automatiquement. Dans tout les cas, l'accés au dossier `/boot` doit être uniquement autorisé pour l'user `root`

**Attention**
 
  - La modification du montage `/boot` (mesure) demmande d'adapter les outils système à cette configuration partiulière, notamment pour la mise à jour du noyau et du `bootloader`, ce qui nécessite une expertise système pointue lors de son déploiement

L'outil `dpkg` utilisé par les distributions dérivées de Debian peut être configuré pour réaliser des commandes particulières avant ou aprés les commandes d'installation de paquets.

### Choix des paquets à installer

L’installation des paquets est l’étape cruciale qui va déterminer l’ensemble des fichiers qui seront présents sur le système, les services qu’il va rendre ainsi que les paquets qui devront être maintenus dans le temps. 

Il est plus facile d’obtenir une installation minimaliste en retirant tous les paquets présélectionnés, et de ne choisir que ceux nécessaires au contexte d’utilisation. Par exemple, l’exploitation d’un serveur ne requiert pas systématiquement l’installation d’une interface graphique locale (serveur X).

- Le choix des paquets doit conduire à une installation aussi petite que possible se bornant à ne séléctionner que ce qui est nécessaire au besoin. 

Certaines distributions fournissent des "roles" préconfigurés. Il est déconseillé de baser son installation sur ces roles étant donné que les choix des mainteneurs de la distribution ne correspondent pas forcément aux besoins propres, ce qui nécessitera l'installation de paquets supplémentaires.

- Seul les dépôts officiels à jour de la distribution doivent être utilisés.
- Lorsque la distribution fournit plusieurs type de dépôts, la préférence doit aller à ceux contenant des paquets faisant l'objet de mesure de durcissement supplémentaires. Entre deux paquets fournissant le meme services, ceux faisant l'objet de mesure de durcissement (à la compilation, à l'installation ou dans la config par défaut). doivent être privilégiés

### Configuration du chargeur de démarrage 

Pour des raisons équivalentes à la configuration du BIOS, le chargeur de démarrage est un élément important de la chaine de démarrage. 
Les grub désormais sont riches en fonctionnalité, ils permettent d'accéder au systeme de fichiers (eventuellement de modif des données) de démarrer sur des periphs USB ou de changer les option du démarrage du noyau séléctionné 
 
 - Un chargeur de démarrage permetant de protéger le démarrage par mot de passe doit être privilégié. Ce mot de oasse doit empécher un utilisateur quelconque de modifier ses options de configuration. Quand le chargeur de démarrage n'offre pas la possibilité de lui adjoindre un mdp, une mesure technique (de type organisationnelle ) doit être mise en place afin de bloquer tout utilisateur dans ses tentatives de modification du paramétrage.

GRUB et GRUB 2 offrent la possibilité de rajouter un mot de passe de dévérrouillage.

		 
