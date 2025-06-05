[![Lang en](https://img.shields.io/badge/lang-en-blue?style=flat)](https://github.com/ian-ani/bluesky_sh/blob/main/README.md)
[![Lang es](https://img.shields.io/badge/lang-es-red?style=flat)](https://github.com/ian-ani/bluesky_sh/blob/main/README.es.md)

## Table of contents

- [About the project](#About-the-project)
- [Built with](#Built-with)
- [Usage](#Usage)
- [Docker](#Docker)
- [To Do](#To-Do)

## About the project

Made with **Python** to interact with [Bluesky](https://docs.bsky.app/docs/get-started) from a shell.  
Tested on **Windows 10** and **Linux** (``python:3.12.7-alpine``).

## Built with

- os
- getpass
- atproto

## Usage

1. By only using the files in **/app/src**, running from **main.py**. In this case, the files **Dockerfile** and
**docker-compose.yml** aren't necessary.
2. Through **Docker**, but in this case, you will need all the files.

## Docker

1. Run the container:

```sh
docker-compose run --name bluesky_txt python_app sh
```

2. Run the program:

```sh
python main.py
```

3. Exit the shell:

```sh
exit
```

## To-Do

- Search user by **did** and related features.