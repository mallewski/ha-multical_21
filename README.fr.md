# Multical 21

Composant personnalisé Multical 21 pour Home Assistant.
![image](https://user-images.githubusercontent.com/6593720/220913633-3daa874f-3ed3-4e39-b827-ec7a1ce1f6dd.png)

**Langues :** [English](README.md) | [Deutsch](README.de.md) | Français | [Español](README.es.md) | [Italiano](README.it.md) | [Polski](README.pl.md) | [Dansk](README.da.md) | [Svenska](README.sv.md) | [Nederlands](README.nl.md)

## Prérequis

Pour utiliser ce composant personnalisé, vous aurez besoin d'un œil optique et de connecter directement votre machine Home Assistant, via cet œil optique, au compteur Kamstrup Multical 21.
L'intégration fonctionne avec n'importe quelle tête de lecture optique USB-série générique — elle n'est liée à aucune marque ni puce USB spécifique.
Voici à quoi ressemble l'œil optique :<br>
![image](https://user-images.githubusercontent.com/6593720/220914030-3ca8bec3-b302-4ed7-a0b8-c4858b0c8120.png)
Je l'ai commandé [ici](https://www.aliexpress.com/item/1005004567409202.html?spm=a2g0o.order_list.order_list_main.18.43e81802zaII7n)
Vous pouvez également imprimer en 3D [ce support](https://makerworld.com/en/models/490708#profileId-404169)

## Installation

### HACS

Ce composant peut être installé directement via HACS. Recherchez « Multical 21 » dans la liste des intégrations HACS et cliquez sur « Download ».

### Manuelle

1. Ouvrez le répertoire de votre configuration HA (là où se trouve `configuration.yaml`).
2. Si vous n'avez pas de répertoire `custom_components`, créez-le.
3. Téléchargez le répertoire `custom_components/multical_21/` de ce dépôt sous forme de ZIP et extrayez-le, ou clonez le dépôt.
4. Copiez le dossier `multical_21` dans votre répertoire `custom_components`.
5. Redémarrez Home Assistant.
6. Dans l'interface HA, allez dans « Paramètres » → « Appareils et services », cliquez sur « Ajouter une intégration » et recherchez « Multical 21 ».

## La configuration se fait depuis l'interface

Lors de l'ajout de l'intégration, on vous demandera :

- **Port série** — choisissez votre tête de lecture dans la liste des périphériques série détectés, ou saisissez un chemin manuellement. Le sélecteur privilégie automatiquement les identifiants stables ; si vous saisissez vous-même un chemin, préférez `/dev/serial/by-id/...` à `/dev/ttyUSB1`, car le premier ne change pas lors de l'ajout/retrait de périphériques USB ou d'un redémarrage du système. Un chemin `/dev/serial/by-id` ressemble à ceci : `/dev/serial/by-id/usb-FTDI_FT230X_Basic_UART_D307PBVY-if00-port0`.
- **Nom** — un nom convivial optionnel, utile si vous relevez plusieurs compteurs.

### Plusieurs compteurs

Vous pouvez ajouter l'intégration plusieurs fois — par exemple si vous relevez à la fois un compteur d'eau froide et un compteur d'eau chaude. Il suffit de répéter l'étape « Ajouter une intégration » pour chaque tête de lecture supplémentaire.

### Changer le port série ultérieurement

Si vous remplacez l'adaptateur USB, ou si son chemin d'accès change, vous n'avez pas besoin de supprimer puis réajouter l'intégration. Ouvrez l'entrée de l'intégration, choisissez **Reconfigurer**, puis sélectionnez le nouveau port. Vos entités, l'historique et vos automatisations restent intacts.

### Options

Cliquez sur « Configurer » dans la page des intégrations pour ajuster :

- **Intervalle de scan** (secondes, défaut `60`) — certains compteurs contiennent une pile, et communiquer avec le compteur a un impact sur son autonomie. Augmentez cette valeur si vous souhaitez interroger le compteur moins souvent.
- **Délai d'expiration de lecture série** (secondes, défaut `1.0`) — si vous obtenez l'erreur `Finished update, No readings from the meter. Please check the IR connection`, essayez d'augmenter cette valeur. Les nombres décimaux sont autorisés (par ex. `0.5`).
- **Débit en bauds** (défaut `1200`) — il s'agit de la valeur par défaut du protocole du Multical 21 et elle n'a normalement pas besoin d'être modifiée. Ne l'ajustez que si votre adaptateur USB spécifique nécessite un débit différent.

## Collecter les journaux

Si vous souhaitez signaler un problème, merci de joindre les journaux de ce composant. Vous pouvez activer la journalisation pour ce composant en configurant le logger dans Home Assistant comme suit :
```yaml
logger:
  default: warn
  logs:
    custom_components.multical_21: debug
```
Plus d'informations sur la [page de l'intégration logger de Home Assistant](https://www.home-assistant.io/integrations/logger)
