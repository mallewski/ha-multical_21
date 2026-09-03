# Multical 21

Niestandardowa integracja Multical 21 dla Home Assistant.
![image](https://user-images.githubusercontent.com/6593720/220913633-3daa874f-3ed3-4e39-b827-ec7a1ce1f6dd.png)

**Języki:** [English](README.md) | [Deutsch](README.de.md) | [Français](README.fr.md) | [Español](README.es.md) | [Italiano](README.it.md) | Polski | [Dansk](README.da.md) | [Svenska](README.sv.md) | [Nederlands](README.nl.md)

## Wymagania

Aby korzystać z tej niestandardowej integracji, potrzebujesz głowicy optycznej i musisz połączyć komputer z Home Assistant bezpośrednio, za jej pośrednictwem, z licznikiem Kamstrup Multical 21.
Integracja działa z dowolną generyczną głowicą optyczną USB-szeregową — nie jest przywiązana do konkretnej marki ani konkretnego chipu USB.
Tak wygląda głowica optyczna:<br>
![image](https://user-images.githubusercontent.com/6593720/220914030-3ca8bec3-b302-4ed7-a0b8-c4858b0c8120.png)
Zamówiłem swoją [tutaj](https://www.aliexpress.com/item/1005004567409202.html?spm=a2g0o.order_list.order_list_main.18.43e81802zaII7n)
Możesz też wydrukować w 3D [ten uchwyt](https://makerworld.com/en/models/490708#profileId-404169)

## Instalacja

### HACS

Tę komponentę można zainstalować bezpośrednio przez HACS. Wyszukaj „Multical 21” na liście integracji HACS i kliknij „Download”.

### Ręczna

1. Otwórz katalog swojej konfiguracji HA (tam, gdzie znajduje się `configuration.yaml`).
2. Jeśli nie masz katalogu `custom_components`, utwórz go.
3. Pobierz katalog `custom_components/multical_21/` z tego repozytorium jako ZIP i rozpakuj go, albo sklonuj repozytorium.
4. Skopiuj folder `multical_21` do katalogu `custom_components`.
5. Uruchom ponownie Home Assistant.
6. W interfejsie HA przejdź do „Ustawienia” → „Urządzenia i usługi”, kliknij „Dodaj integrację” i wyszukaj „Multical 21”.

## Konfiguracja odbywa się w interfejsie

Podczas dodawania integracji zostaniesz zapytany o:

- **Port szeregowy** — wybierz swoją głowicę z listy wykrytych urządzeń szeregowych albo wpisz ścieżkę ręcznie. Selektor automatycznie preferuje stabilne identyfikatory; jeśli wpisujesz ścieżkę samodzielnie, preferuj `/dev/serial/by-id/...` zamiast `/dev/ttyUSB1`, ponieważ ta pierwsza się nie zmienia przy dodawaniu/usuwaniu urządzeń USB ani po restarcie systemu. Ścieżka `/dev/serial/by-id` wygląda tak: `/dev/serial/by-id/usb-FTDI_FT230X_Basic_UART_D307PBVY-if00-port0`.
- **Nazwa** — opcjonalna, przyjazna nazwa, przydatna jeśli odczytujesz więcej niż jeden licznik.

### Wiele liczników

Możesz dodać integrację więcej niż raz — na przykład jeśli odczytujesz zarówno licznik zimnej, jak i ciepłej wody. Po prostu powtórz krok „Dodaj integrację” dla każdej kolejnej głowicy.

### Zmiana portu szeregowego później

Jeśli wymienisz adapter USB albo zmieni się jego ścieżka urządzenia, nie musisz usuwać i ponownie dodawać integracji. Otwórz wpis integracji, wybierz **Rekonfiguruj** i wskaż nowy port. Twoje encje, historia i automatyzacje pozostaną nienaruszone.

### Opcje

Naciśnij „Konfiguruj” na stronie integracji, aby dostosować:

- **Interwał odpytywania** (sekundy, domyślnie `60`) — niektóre liczniki mają baterię, a komunikacja z licznikiem wpływa na jej żywotność. Zwiększ tę wartość, jeśli chcesz odpytywać rzadziej.
- **Limit czasu odczytu szeregowego** (sekundy, domyślnie `1.0`) — jeśli pojawia się błąd `Finished update, No readings from the meter. Please check the IR connection`, spróbuj zwiększyć tę wartość. Dozwolone są liczby dziesiętne (np. `0.5`).
- **Szybkość transmisji** (domyślnie `1200`) — to domyślna wartość protokołu Multical 21 i zwykle nie trzeba jej zmieniać. Zmień ją tylko, jeśli Twój konkretny adapter USB wymaga innej szybkości.

## Zbieranie logów

Jeśli chcesz zgłosić problem, dołącz logi z tej komponenty. Możesz włączyć logowanie dla niej, konfigurując logger w Home Assistant w następujący sposób:
```yaml
logger:
  default: warn
  logs:
    custom_components.multical_21: debug
```
Więcej informacji znajdziesz na [stronie integracji logger w Home Assistant](https://www.home-assistant.io/integrations/logger)
