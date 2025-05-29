## Opis etapów zadania
- `env`: Zmienne używane w pliku .yml 
- `Check out the source_repo`: sprawdza dane repozytorium zdefiniowane przez zmienną $GITHUB_WORKSPACE, aby potwierdzić że uruchamiany łańcuch może uzyskać do niego dostęp na zasadach określonych w konfiguracji modułu
- `Docker metadata definitions`: pomaga w tagowaniu obrazów
- `QEMU set-up`, `Buildx set-up`: pozwalają na danym hoście runner-a zainstalować wszystkie niezbędne komponenty do budowania obrazu z wykorzystaniem silnika Buildkit
- `Login to GHCR`, `Login to DockerHub`: logowanie do GHCR oraz DockerHub'a
- `Build image with multi-arch and cache`: zbudowanie obrazu na architektury amd64 i arm64
- `Scan image for vulnerabilities`: przeskanowanie obrazu pod kątem możliwych zagrożeń klasyfikowanych jako krytyczne lub wysokie
- `Push image to GHCR (only if no CRITICAL/HIGH CVEs)`: przesłanie i pobranie danych cache, które pozwalają na przyśpieszenie operacji budowania kolejnych wersji obrazu danej aplikacji
---
