# Правила внесения изменений

## Окружение

```bash
python3 -m venv .venv
source .venv/bin/activate
pip install -r requirements.txt
```

## Ветвление

- `master` — основная ветка, прямые коммиты нежелательны
- `patch*` — ветки для правок, вливаются через Pull Request

## Коммиты

- Атомарные: одно логическое изменение — один коммит
- Обязательная GPG-подпись: `git commit -S`
- Формат сообщения: `<тип>: <описание>` в повелительном наклонении
- Типы: `feat`, `fix`, `docs`, `style`, `refactor`, `chore`

## Pull Request

1. Ветка от актуального `master`
2. Проверить работоспособность кода перед публикацией
3. `gh pr create --base master --head <ветка>`
4. Конфликты разрешать через `git rebase`, публиковать `--force-with-lease`
