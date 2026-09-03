# Multical 21

Brugerdefineret Multical 21-komponent til Home Assistant.
![image](https://user-images.githubusercontent.com/6593720/220913633-3daa874f-3ed3-4e39-b827-ec7a1ce1f6dd.png)

**Sprog:** [English](README.md) | [Deutsch](README.de.md) | [Français](README.fr.md) | [Español](README.es.md) | [Italiano](README.it.md) | [Polski](README.pl.md) | Dansk | [Svenska](README.sv.md) | [Nederlands](README.nl.md)

## Krav

For at bruge denne brugerdefinerede komponent skal du bruge et optisk øje og forbinde din Home Assistant-maskine direkte, via dette optiske øje, til Kamstrup Multical 21-måleren.
Integrationen fungerer med ethvert generisk USB-til-seriel optisk læsehoved — den er ikke bundet til et bestemt mærke eller en bestemt USB-chip.
Sådan ser det optiske øje ud:<br>
![image](https://user-images.githubusercontent.com/6593720/220914030-3ca8bec3-b302-4ed7-a0b8-c4858b0c8120.png)
Jeg bestilte mit [her](https://www.aliexpress.com/item/1005004567409202.html?spm=a2g0o.order_list.order_list_main.18.43e81802zaII7n)
Du kan også 3D-printe [denne montering](https://makerworld.com/en/models/490708#profileId-404169)

## Installation

### HACS

Denne komponent kan installeres direkte via HACS. Søg efter "Multical 21" på HACS' integrationsliste, og klik på "Download".

### Manuel

1. Åbn mappen med din HA-konfiguration (der hvor du finder `configuration.yaml`).
2. Hvis du ikke har en `custom_components`-mappe, skal du oprette den.
3. Download mappen `custom_components/multical_21/` fra dette repository som en ZIP-fil, og pak den ud — eller klon repositoryet.
4. Kopiér mappen `multical_21` ind i din `custom_components`-mappe.
5. Genstart Home Assistant.
6. Gå i HA-brugerfladen til "Indstillinger" → "Enheder og tjenester", klik på "Tilføj integration", og søg efter "Multical 21".

## Konfigurationen foregår i brugerfladen

Når du tilføjer integrationen, bliver du spurgt om:

- **Seriel port** — vælg dit læsehoved fra listen over fundne serielle enheder, eller indtast en sti manuelt. Vælgeren foretrækker automatisk stabile identifikatorer; hvis du selv indtaster en sti, så foretræk `/dev/serial/by-id/...` frem for `/dev/ttyUSB1`, da den første ikke ændres, når USB-enheder tilføjes/fjernes, eller systemet genstartes. En `/dev/serial/by-id`-sti ser sådan ud: `/dev/serial/by-id/usb-FTDI_FT230X_Basic_UART_D307PBVY-if00-port0`.
- **Navn** — et valgfrit, letforståeligt navn, praktisk hvis du aflæser mere end én måler.

### Flere målere

Du kan tilføje integrationen mere end én gang — for eksempel hvis du aflæser både en koldt- og en varmtvandsmåler. Gentag blot trinnet "Tilføj integration" for hvert ekstra læsehoved.

### Skift af seriel port senere

Hvis du udskifter USB-adapteren, eller dens enhedssti ændres, behøver du ikke slette og gentilføje integrationen. Åbn integrationens post, vælg **Rekonfigurér**, og vælg den nye port. Dine enheder, historik og automatiseringer bevares.

### Indstillinger

Tryk på "Konfigurér" på integrationssiden for at justere:

- **Scanningsinterval** (sekunder, standard `60`) — nogle målere indeholder et batteri, og kommunikation med måleren påvirker batteriets levetid. Øg denne værdi, hvis du vil forespørge sjældnere.
- **Timeout for seriel læsning** (sekunder, standard `1.0`) — hvis du får fejlen `Finished update, No readings from the meter. Please check the IR connection`, kan du prøve at øge denne værdi. Decimaltal er tilladt (fx `0.5`).
- **Baudrate** (standard `1200`) — dette er Multical 21's protokolstandard og skal normalt ikke ændres. Justér kun, hvis din specifikke USB-adapter kræver en anden hastighed.

## Indsamling af logs

Når du vil rapportere et problem, bedes du vedhæfte logs fra denne komponent. Du kan aktivere logning for komponenten ved at konfigurere loggeren i Home Assistant som følger:
```yaml
logger:
  default: warn
  logs:
    custom_components.multical_21: debug
```
Mere information findes på [Home Assistants side om logger-integrationen](https://www.home-assistant.io/integrations/logger)
