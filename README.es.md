# Multical 21

Componente personalizado Multical 21 para Home Assistant.
![image](https://user-images.githubusercontent.com/6593720/220913633-3daa874f-3ed3-4e39-b827-ec7a1ce1f6dd.png)

**Idiomas:** [English](README.md) | [Deutsch](README.de.md) | [Français](README.fr.md) | Español | [Italiano](README.it.md) | [Polski](README.pl.md) | [Dansk](README.da.md) | [Svenska](README.sv.md) | [Nederlands](README.nl.md)

## Requisitos

Para usar este componente personalizado, necesitarás un ojo óptico y conectar tu equipo con Home Assistant directamente, a través de dicho ojo óptico, al medidor Kamstrup Multical 21.
La integración funciona con cualquier cabezal de lectura óptico USB-serie genérico — no está ligada a una marca ni a un chip USB en concreto.
Así es como se ve el ojo óptico:<br>
![image](https://user-images.githubusercontent.com/6593720/220914030-3ca8bec3-b302-4ed7-a0b8-c4858b0c8120.png)
Yo lo pedí [aquí](https://www.aliexpress.com/item/1005004567409202.html?spm=a2g0o.order_list.order_list_main.18.43e81802zaII7n)
También puedes imprimir en 3D [este soporte](https://makerworld.com/en/models/490708#profileId-404169)

## Instalación

### HACS

Este componente puede instalarse directamente a través de HACS. Busca "Multical 21" en la lista de integraciones de HACS y haz clic en "Download".

### Manual

1. Abre el directorio de tu configuración de HA (donde se encuentra `configuration.yaml`).
2. Si no tienes un directorio `custom_components`, créalo.
3. Descarga el directorio `custom_components/multical_21/` de este repositorio como ZIP y extráelo, o clona el repositorio.
4. Copia la carpeta `multical_21` en tu directorio `custom_components`.
5. Reinicia Home Assistant.
6. En la interfaz de HA, ve a "Ajustes" → "Dispositivos y servicios", haz clic en "Añadir integración" y busca "Multical 21".

## La configuración se realiza desde la interfaz

Al añadir la integración se te pedirá:

- **Puerto serie** — elige tu cabezal de lectura de la lista de dispositivos serie detectados, o escribe una ruta manualmente. El selector prioriza automáticamente identificadores estables; si introduces tú mismo una ruta, prefiere `/dev/serial/by-id/...` en lugar de `/dev/ttyUSB1`, ya que el primero no cambia al añadir/quitar dispositivos USB o al reiniciar el sistema. Una ruta `/dev/serial/by-id` tiene este aspecto: `/dev/serial/by-id/usb-FTDI_FT230X_Basic_UART_D307PBVY-if00-port0`.
- **Nombre** — un nombre descriptivo opcional, útil si lees más de un medidor.

### Varios medidores

Puedes añadir la integración más de una vez — por ejemplo, si lees tanto un medidor de agua fría como uno de agua caliente. Simplemente repite el paso "Añadir integración" para cada cabezal de lectura adicional.

### Cambiar el puerto serie más adelante

Si cambias el adaptador USB, o su ruta de dispositivo cambia, no necesitas eliminar y volver a añadir la integración. Abre la entrada de la integración, elige **Reconfigurar** y selecciona el nuevo puerto. Tus entidades, historial y automatizaciones se mantienen intactos.

### Opciones

Pulsa "Configurar" en la página de integraciones para ajustar:

- **Intervalo de escaneo** (segundos, por defecto `60`) — algunos medidores contienen una pila, y comunicarse con el medidor afecta a su duración. Aumenta este valor si quieres consultarlo con menos frecuencia.
- **Tiempo de espera de lectura serie** (segundos, por defecto `1.0`) — si obtienes el error `Finished update, No readings from the meter. Please check the IR connection`, intenta aumentar este valor. Se permiten números decimales (p. ej. `0.5`).
- **Velocidad en baudios** (por defecto `1200`) — es el valor por defecto del protocolo del Multical 21 y normalmente no hace falta cambiarlo. Ajústalo solo si tu adaptador USB concreto necesita una velocidad distinta.

## Recopilar registros

Si quieres reportar un problema, añade por favor los registros de este componente. Puedes activar el registro para este componente configurando el logger en Home Assistant así:
```yaml
logger:
  default: warn
  logs:
    custom_components.multical_21: debug
```
Más información en la [página de la integración logger de Home Assistant](https://www.home-assistant.io/integrations/logger)
