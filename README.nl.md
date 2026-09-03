# Multical 21

Aangepaste Multical 21-component voor Home Assistant.
![image](https://user-images.githubusercontent.com/6593720/220913633-3daa874f-3ed3-4e39-b827-ec7a1ce1f6dd.png)

**Talen:** [English](README.md) | [Deutsch](README.de.md) | [Français](README.fr.md) | [Español](README.es.md) | [Italiano](README.it.md) | [Polski](README.pl.md) | [Dansk](README.da.md) | [Svenska](README.sv.md) | Nederlands

## Vereisten

Om deze aangepaste component te gebruiken, heb je een optisch oog nodig en verbind je jouw Home Assistant-machine rechtstreeks, via dit optische oog, met de Kamstrup Multical 21-meter.
De integratie werkt met elke generieke USB-naar-serieel optische leeskop — ze is niet gebonden aan een specifiek merk of een specifieke USB-chip.
Zo ziet het optische oog eruit:<br>
![image](https://user-images.githubusercontent.com/6593720/220914030-3ca8bec3-b302-4ed7-a0b8-c4858b0c8120.png)
Ik heb de mijne [hier](https://www.aliexpress.com/item/1005004567409202.html?spm=a2g0o.order_list.order_list_main.18.43e81802zaII7n) besteld
Je kunt ook [deze houder](https://makerworld.com/en/models/490708#profileId-404169) 3D-printen

## Installatie

### HACS

Deze component kan rechtstreeks via HACS geïnstalleerd worden. Zoek naar "Multical 21" in de HACS-integratielijst en klik op "Download".

### Handmatig

1. Open de map van je HA-configuratie (waar je `configuration.yaml` vindt).
2. Als je nog geen `custom_components`-map hebt, maak er dan een aan.
3. Download de map `custom_components/multical_21/` uit deze repository als ZIP en pak deze uit, of kloon de repository.
4. Kopieer de map `multical_21` naar je `custom_components`-map.
5. Herstart Home Assistant.
6. Ga in de HA-interface naar "Instellingen" → "Apparaten en diensten", klik op "Integratie toevoegen" en zoek naar "Multical 21".

## De configuratie gebeurt via de interface

Bij het toevoegen van de integratie wordt je het volgende gevraagd:

- **Seriële poort** — kies je leeskop uit de lijst met gedetecteerde seriële apparaten, of typ een pad handmatig in. De kiezer geeft automatisch de voorkeur aan stabiele identifiers; als je zelf een pad invoert, geef dan de voorkeur aan `/dev/serial/by-id/...` boven `/dev/ttyUSB1`, omdat het eerste niet verandert wanneer USB-apparaten worden toegevoegd/verwijderd of het systeem opnieuw opstart. Een `/dev/serial/by-id`-pad ziet er zo uit: `/dev/serial/by-id/usb-FTDI_FT230X_Basic_UART_D307PBVY-if00-port0`.
- **Naam** — een optionele, herkenbare naam, handig als je meer dan één meter uitleest.

### Meerdere meters

Je kunt de integratie meer dan één keer toevoegen — bijvoorbeeld als je zowel een koud- als een warmwatermeter uitleest. Herhaal gewoon de stap "Integratie toevoegen" voor elke extra leeskop.

### De seriële poort later wijzigen

Als je de USB-adapter vervangt, of het apparaatpad ervan verandert, hoef je de integratie niet te verwijderen en opnieuw toe te voegen. Open de integratie, kies **Herconfigureren** en selecteer de nieuwe poort. Je entiteiten, geschiedenis en automatiseringen blijven behouden.

### Opties

Klik op "Configureren" op de integratiepagina om het volgende aan te passen:

- **Scaninterval** (seconden, standaard `60`) — sommige meters bevatten een batterij, en communiceren met de meter heeft invloed op de batterijduur. Verhoog deze waarde als je minder vaak wilt uitlezen.
- **Time-out voor serieel lezen** (seconden, standaard `1.0`) — als je de foutmelding `Finished update, No readings from the meter. Please check the IR connection` krijgt, probeer dan deze waarde te verhogen. Decimale getallen zijn toegestaan (bijv. `0.5`).
- **Baudrate** (standaard `1200`) — dit is de protocolstandaard van de Multical 21 en hoeft normaal gesproken niet gewijzigd te worden. Pas dit alleen aan als jouw specifieke USB-adapter een andere snelheid vereist.

## Logs verzamelen

Als je een probleem wilt melden, voeg dan a.u.b. logs van deze component toe. Je kunt logging voor deze component inschakelen door de logger in Home Assistant als volgt te configureren:
```yaml
logger:
  default: warn
  logs:
    custom_components.multical_21: debug
```
Meer informatie vind je op de [pagina van de Home Assistant logger-integratie](https://www.home-assistant.io/integrations/logger)
