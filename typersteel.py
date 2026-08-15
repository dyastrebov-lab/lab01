"""CLI-приветствие на базе typer."""

import typer

def main(
    name: str,
    lastname: str = typer.Option("", help="Фамилия пользователя."),
    
    # --formal / -f переключает регистр обращения на официальный
    formal: bool = typer.Option(False, "--formal", "-f", help="Использовать формальное приветствие."),
):
    """
    Приветствует пользователя по имени
    """
    if formal:
        print(f"Добрый день, {name} {lastname}!")
    else:
        print(f"Привет, {name}!")

if __name__ == "__main__":
    typer.run(main)
