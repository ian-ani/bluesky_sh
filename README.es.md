[![Lang en](https://img.shields.io/badge/lang-en-blue?style=flat)](https://github.com/ian-ani/bluesky_sh/blob/main/README.md)
[![Lang es](https://img.shields.io/badge/lang-es-red?style=flat)](https://github.com/ian-ani/bluesky_sh/blob/main/README.es.md)

## Tabla de contenidos

- [Acerca de este repositorio](#Acerca-de-este-repositorio)
- [Hecho con](#Hecho-con)
- [Uso](#Uso)
- [Docker](#Docker)
- [Por hacer](#Por-hacer)

## Acerca de este repositorio

Programa creado con **Python** para interactuar con [Bluesky](https://docs.bsky.app/docs/get-started) desde la consola.  
Probado con **Windows 10** y **Linux** (``python:3.12.7-alpine``).

## Hecho con

- os
- getpass
- atproto

## Uso

Se puede usar de dos maneras:

1. Usando solo los archivos ubicados en **/app/src**, iniciando desde **main.py**. En este caso, los archivos **Dockerfile** y 
**docker-compose.yml** no serán necesarios.
2. Mediante el uso de **Docker**, en tal caso, sí se necesitará tener todos los archivos.

## Docker

1. Para iniciar el contenedor:

```sh
docker-compose run --name bluesky_txt python_app sh
```

2. Para iniciar el programa:

```sh
python main.py
```

3. Para salir del shell:

```sh
exit
```
## Por hacer

- Buscar un usuario mediante un **did** y funciones relacionadas.