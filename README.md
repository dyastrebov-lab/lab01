<div align="center">
  <a href="https://github.com/dyastrebov-lab/lab01">
    <img src="https://socialify.git.ci/dyastrebov-lab/lab01/image?language=1&owner=1&name=1&stargazers=1&theme=Light" alt="lab01" width="640" />
  </a>
</div>

<div align="center">

![Last commit](https://img.shields.io/github/last-commit/dyastrebov-lab/lab01)
![Repo Size](https://img.shields.io/github/repo-size/dyastrebov-lab/lab01)
![License](https://img.shields.io/github/license/dyastrebov-lab/lab01)
![Python](https://img.shields.io/static/v1?logo=python&logoColor=fff&label=&message=Python&color=363939&style=flat)
![Git](https://img.shields.io/static/v1?logo=git&logoColor=fff&label=&message=Git&color=363939&style=flat)
![GnuPG](https://img.shields.io/static/v1?logo=gnuprivacyguard&logoColor=fff&label=&message=GnuPG&color=363939&style=flat)

</div>

В работе рассмотрена система обмена данными на примере `git`. В ходе работы были получены базовые навыки для произведения `commit`-ов, публикации изменений в удаленный репозиторий, обновления данных для них, разрешений конфликтов и т.д.

**Что отработано:** инициализация репозитория, SSH/GPG, ветвление, Pull Request, разрешение конфликта через `rebase`

**Стек:** Git, GitHub CLI, Python 3.14.4, typer, GnuPG

***

### Требования

- Python 3.14.4
- git 2.53.0
- gh 2.46.0
- gpg (GnuPG) 2.4.8

### Установка

```bash
git clone git@github.com:dyastrebov-lab/lab01.git
cd lab01
python3 -m venv .venv
source .venv/bin/activate
pip install -r requirements.txt
```

### Использование

```bash
python3 typersteel.py Danil
```
```
Привет, Danil!
```

```bash
python3 typersteel.py Danil --lastname Yastrebov --formal
```
```
Добрый день, Danil Yastrebov!
```

```bash
python3 typersteel.py --help
```
```                                                                            
 Приветствует пользователя по имени                                             
                                                                                
╭─ Arguments ──────────────────────────────────────────────────────────────────╮
│ *    name      <str>  [required]                                             │
╰──────────────────────────────────────────────────────────────────────────────╯
╭─ Options ────────────────────────────────────────────────────────────────────╮
│ --lastname          <str>  Фамилия пользователя.                             │
│ --formal    -f             Использовать формальное приветствие.              │
│ --help                     Show this message and exit.                       │
╰──────────────────────────────────────────────────────────────────────────────╯
```
***

### Структура

```
└── lab01
    ├── CODE_OF_CONDUCT.md
    ├── CONTRIBUTING.md
    ├── LICENSE.md
    ├── NOTICE.md
    ├── README.md
    ├── requirements.txt
    ├── SECURITY.md
    └── typersteel.py
```
***

### Соответствие требованиям

- Все коммиты подписаны GPG (`git commit -S`), на GitHub — статус **Verified**
- История разбита на атомарные коммиты
- Изменения вливаются через Pull Request: `patch1 → master`, `patch2 → master`
- Конфликт слияния разрешён через `git rebase` с публикацией `--force-with-lease`
- Все операции выполнены из терминала, включая работу с GitHub через `gh`
- Репозиторий содержит `.gitignore`, `LICENSE.md`, `NOTICE.md`, `SECURITY.md`,
  `CODE_OF_CONDUCT.md`, `CONTRIBUTING.md`

***

### Лицензия

Apache License 2.0 — см. [LICENSE.md](LICENSE.md) и [NOTICE.md](NOTICE.md).



