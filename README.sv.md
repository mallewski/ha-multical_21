# Multical 21

Anpassad Multical 21-komponent för Home Assistant.
![image](https://user-images.githubusercontent.com/6593720/220913633-3daa874f-3ed3-4e39-b827-ec7a1ce1f6dd.png)

**Språk:** [English](README.md) | [Deutsch](README.de.md) | [Français](README.fr.md) | [Español](README.es.md) | [Italiano](README.it.md) | [Polski](README.pl.md) | [Dansk](README.da.md) | Svenska | [Nederlands](README.nl.md)

## Krav

För att använda den här anpassade komponenten behöver du ett optiskt öga och ansluta din Home Assistant-dator direkt, via detta optiska öga, till Kamstrup Multical 21-mätaren.
Integrationen fungerar med vilket generiskt USB-seriellt optiskt läshuvud som helst — den är inte knuten till ett visst märke eller en viss USB-krets.
Så här ser det optiska ögat ut:<br>
![image](https://user-images.githubusercontent.com/6593720/220914030-3ca8bec3-b302-4ed7-a0b8-c4858b0c8120.png)
Jag beställde mitt [här](https://www.aliexpress.com/item/1005004567409202.html?spm=a2g0o.order_list.order_list_main.18.43e81802zaII7n)
Du kan även 3D-skriva ut [det här fästet](https://makerworld.com/en/models/490708#profileId-404169)

## Installation

### HACS

Den här komponenten kan installeras direkt via HACS. Sök efter "Multical 21" i HACS integrationslista och klicka på "Download".

### Manuell

1. Öppna mappen för din HA-konfiguration (där du hittar `configuration.yaml`).
2. Om du inte har någon `custom_components`-mapp, skapa en.
3. Ladda ner mappen `custom_components/multical_21/` från det här repositoryt som en ZIP-fil och packa upp den, eller klona repositoryt.
4. Kopiera mappen `multical_21` till din `custom_components`-mapp.
5. Starta om Home Assistant.
6. Gå i HA-gränssnittet till "Inställningar" → "Enheter och tjänster", klicka på "Lägg till integration" och sök efter "Multical 21".

## Konfigurationen sker i gränssnittet

När du lägger till integrationen blir du ombedd att ange:

- **Seriell port** — välj ditt läshuvud från listan över upptäckta seriella enheter, eller skriv in en sökväg manuellt. Väljaren föredrar automatiskt stabila identifierare; om du själv skriver in en sökväg bör du föredra `/dev/serial/by-id/...` framför `/dev/ttyUSB1`, eftersom den förstnämnda inte ändras när USB-enheter läggs till/tas bort eller systemet startas om. En `/dev/serial/by-id`-sökväg ser ut så här: `/dev/serial/by-id/usb-FTDI_FT230X_Basic_UART_D307PBVY-if00-port0`.
- **Namn** — ett valfritt, lättöverskådligt namn, praktiskt om du läser av mer än en mätare.

### Flera mätare

Du kan lägga till integrationen mer än en gång — till exempel om du läser av både en kallvatten- och en varmvattenmätare. Upprepa bara steget "Lägg till integration" för varje ytterligare läshuvud.

### Byta seriell port senare

Om du byter USB-adapter, eller om dess enhetssökväg ändras, behöver du inte ta bort och lägga till integrationen på nytt. Öppna integrationens post, välj **Konfigurera om**, och välj den nya porten. Dina entiteter, historik och automatiseringar bevaras.

### Alternativ

Tryck på "Konfigurera" på integrationssidan för att justera:

- **Avsökningsintervall** (sekunder, standard `60`) — vissa mätare innehåller ett batteri, och kommunikation med mätaren påverkar batteriets livslängd. Öka värdet om du vill fråga av mätaren mer sällan.
- **Timeout för seriell läsning** (sekunder, standard `1.0`) — om du får felet `Finished update, No readings from the meter. Please check the IR connection`, prova att öka detta värde. Decimaltal är tillåtna (t.ex. `0.5`).
- **Baudhastighet** (standard `1200`) — detta är Multical 21:s standardvärde för protokollet och behöver normalt inte ändras. Justera det bara om din specifika USB-adapter kräver en annan hastighet.

## Samla in loggar

Om du vill rapportera ett problem, bifoga gärna loggar från den här komponenten. Du kan aktivera loggning för komponenten genom att konfigurera loggern i Home Assistant enligt följande:
```yaml
logger:
  default: warn
  logs:
    custom_components.multical_21: debug
```
Mer information finns på [Home Assistants sida för logger-integrationen](https://www.home-assistant.io/integrations/logger)
