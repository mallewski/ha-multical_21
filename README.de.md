# Multical 21

Multical-21-Custom-Component für Home Assistant.
![image](https://user-images.githubusercontent.com/6593720/220913633-3daa874f-3ed3-4e39-b827-ec7a1ce1f6dd.png)

**Sprachen:** [English](README.md) | Deutsch | [Français](README.fr.md) | [Español](README.es.md) | [Italiano](README.it.md) | [Polski](README.pl.md) | [Dansk](README.da.md) | [Svenska](README.sv.md) | [Nederlands](README.nl.md)

## Voraussetzungen

Um diese Custom Component zu nutzen, benötigst du einen optischen Lesekopf und verbindest deinen Home-Assistant-Rechner direkt über diesen Lesekopf mit dem Kamstrup-Multical-21-Zähler.
Die Integration funktioniert mit jedem generischen USB-Seriell-Lesekopf – sie ist nicht an eine bestimmte Marke oder einen bestimmten USB-Chip gebunden.
So sieht der optische Lesekopf aus:<br>
![image](https://user-images.githubusercontent.com/6593720/220914030-3ca8bec3-b302-4ed7-a0b8-c4858b0c8120.png)
Ich habe meinen [hier](https://www.aliexpress.com/item/1005004567409202.html?spm=a2g0o.order_list.order_list_main.18.43e81802zaII7n) bestellt.
Du kannst auch [diese Halterung](https://makerworld.com/en/models/490708#profileId-404169) 3D-drucken.

## Installation

### HACS

Diese Komponente kann direkt über HACS installiert werden. Suche in der HACS-Integrationsliste nach „Multical 21“ und klicke auf „Download“.

### Manuell

1. Öffne das Verzeichnis deiner HA-Konfiguration (dort, wo sich `configuration.yaml` befindet).
2. Falls noch kein `custom_components`-Verzeichnis existiert, lege es an.
3. Lade das Verzeichnis `custom_components/multical_21/` aus diesem Repository als ZIP herunter und entpacke es, oder klone das Repository.
4. Kopiere den Ordner `multical_21` in dein `custom_components`-Verzeichnis.
5. Starte Home Assistant neu.
6. Gehe in der HA-Oberfläche zu „Einstellungen“ → „Geräte & Dienste“, klicke auf „Integration hinzufügen“ und suche nach „Multical 21“.

## Die Konfiguration erfolgt über die Oberfläche

Beim Hinzufügen der Integration wirst du nach Folgendem gefragt:

- **Serieller Port** — wähle deinen Lesekopf aus der Liste der erkannten seriellen Geräte, oder gib einen Pfad manuell ein. Die Auswahl bevorzugt automatisch stabile Kennungen; falls du selbst einen Pfad eingibst, bevorzuge `/dev/serial/by-id/...` gegenüber `/dev/ttyUSB1`, da sich Ersteres nicht ändert, wenn USB-Geräte hinzugefügt/entfernt werden oder das System neu startet. Ein `/dev/serial/by-id`-Pfad sieht so aus: `/dev/serial/by-id/usb-FTDI_FT230X_Basic_UART_D307PBVY-if00-port0`.
- **Name** — ein optionaler, frei wählbarer Name, praktisch, wenn du mehr als einen Zähler ausliest.

### Mehrere Zähler

Du kannst die Integration mehrfach hinzufügen — zum Beispiel, wenn du sowohl einen Kalt- als auch einen Warmwasserzähler ausliest. Wiederhole dafür einfach den Schritt „Integration hinzufügen“ für jeden weiteren Lesekopf.

### Den seriellen Port später ändern

Wenn du den USB-Adapter tauschst oder sich dessen Gerätepfad ändert, musst du die Integration nicht löschen und neu einrichten. Öffne den Eintrag der Integration, wähle **Neu konfigurieren** und wähle den neuen Port aus. Entitäten, Verlauf und Automatisierungen bleiben dabei erhalten.

### Optionen

Klicke auf der Integrationsseite auf „Konfigurieren“, um Folgendes anzupassen:

- **Abfrageintervall** (Sekunden, Standard `60`) — manche Zähler enthalten eine Batterie, und die Kommunikation mit dem Zähler wirkt sich auf deren Lebensdauer aus. Erhöhe den Wert, wenn du seltener abfragen möchtest.
- **Timeout beim seriellen Lesen** (Sekunden, Standard `1.0`) — falls die Fehlermeldung `Finished update, No readings from the meter. Please check the IR connection` erscheint, versuche, diesen Wert zu erhöhen. Nachkommastellen sind erlaubt (z. B. `0.5`).
- **Baudrate** (Standard `1200`) — das ist der Protokoll-Standardwert des Multical 21 und muss normalerweise nicht geändert werden. Passe ihn nur an, wenn dein konkreter USB-Adapter eine andere Rate benötigt.

## Logs sammeln

Wenn du ein Problem melden möchtest, füge bitte Logs dieser Komponente bei. Du kannst das Logging dafür in Home Assistant wie folgt aktivieren:
```yaml
logger:
  default: warn
  logs:
    custom_components.multical_21: debug
```
Weitere Infos findest du auf der [Home-Assistant-Logger-Integrationsseite](https://www.home-assistant.io/integrations/logger)
