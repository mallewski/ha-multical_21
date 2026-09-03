# Multical 21

Componente personalizzato Multical 21 per Home Assistant.
![image](https://user-images.githubusercontent.com/6593720/220913633-3daa874f-3ed3-4e39-b827-ec7a1ce1f6dd.png)

**Lingue:** [English](README.md) | [Deutsch](README.de.md) | [Français](README.fr.md) | [Español](README.es.md) | Italiano | [Polski](README.pl.md) | [Dansk](README.da.md) | [Svenska](README.sv.md) | [Nederlands](README.nl.md)

## Requisiti

Per usare questo componente personalizzato, ti serve un occhio ottico e devi collegare la tua macchina con Home Assistant direttamente, tramite tale occhio ottico, al contatore Kamstrup Multical 21.
L'integrazione funziona con qualsiasi testina di lettura ottica USB-seriale generica — non è legata a una marca o a un chip USB specifico.
Ecco come si presenta l'occhio ottico:<br>
![image](https://user-images.githubusercontent.com/6593720/220914030-3ca8bec3-b302-4ed7-a0b8-c4858b0c8120.png)
L'ho ordinato [qui](https://www.aliexpress.com/item/1005004567409202.html?spm=a2g0o.order_list.order_list_main.18.43e81802zaII7n)
Puoi anche stampare in 3D [questo supporto](https://makerworld.com/en/models/490708#profileId-404169)

## Installazione

### HACS

Questo componente può essere installato direttamente tramite HACS. Cerca "Multical 21" nell'elenco delle integrazioni HACS e clicca su "Download".

### Manuale

1. Apri la directory della tua configurazione HA (dove trovi `configuration.yaml`).
2. Se non hai una directory `custom_components`, creala.
3. Scarica la directory `custom_components/multical_21/` di questo repository come ZIP ed estraila, oppure clona il repository.
4. Copia la cartella `multical_21` nella tua directory `custom_components`.
5. Riavvia Home Assistant.
6. Nell'interfaccia di HA vai su "Impostazioni" → "Dispositivi e servizi", clicca su "Aggiungi integrazione" e cerca "Multical 21".

## La configurazione avviene dall'interfaccia

Durante l'aggiunta dell'integrazione ti verrà chiesto:

- **Porta seriale** — scegli la tua testina di lettura dall'elenco dei dispositivi seriali rilevati, oppure inserisci un percorso manualmente. Il selettore preferisce automaticamente identificatori stabili; se inserisci tu stesso un percorso, preferisci `/dev/serial/by-id/...` a `/dev/ttyUSB1`, poiché il primo non cambia quando vengono aggiunti/rimossi dispositivi USB o quando il sistema viene riavviato. Un percorso `/dev/serial/by-id` è simile a questo: `/dev/serial/by-id/usb-FTDI_FT230X_Basic_UART_D307PBVY-if00-port0`.
- **Nome** — un nome descrittivo facoltativo, utile se leggi più di un contatore.

### Più contatori

Puoi aggiungere l'integrazione più di una volta — ad esempio se leggi sia un contatore dell'acqua fredda sia uno dell'acqua calda. Basta ripetere il passaggio "Aggiungi integrazione" per ogni testina di lettura aggiuntiva.

### Cambiare la porta seriale in seguito

Se sostituisci l'adattatore USB, o il suo percorso dispositivo cambia, non è necessario eliminare e riaggiungere l'integrazione. Apri la voce dell'integrazione, scegli **Riconfigura** e seleziona la nuova porta. Le tue entità, la cronologia e le automazioni restano intatte.

### Opzioni

Premi "Configura" nella pagina delle integrazioni per regolare:

- **Intervallo di scansione** (secondi, predefinito `60`) — alcuni contatori contengono una batteria, e comunicare con il contatore ne influenza la durata. Aumenta questo valore se vuoi interrogarlo meno spesso.
- **Timeout di lettura seriale** (secondi, predefinito `1.0`) — se ottieni l'errore `Finished update, No readings from the meter. Please check the IR connection`, prova ad aumentare questo valore. Sono ammessi numeri decimali (es. `0.5`).
- **Velocità in baud** (predefinito `1200`) — è il valore predefinito del protocollo del Multical 21 e normalmente non deve essere modificato. Cambialo solo se il tuo specifico adattatore USB richiede una velocità diversa.

## Raccogliere i log

Se vuoi segnalare un problema, aggiungi per favore i log di questo componente. Puoi abilitare il logging per questo componente configurando il logger in Home Assistant così:
```yaml
logger:
  default: warn
  logs:
    custom_components.multical_21: debug
```
Maggiori informazioni nella [pagina dell'integrazione logger di Home Assistant](https://www.home-assistant.io/integrations/logger)
