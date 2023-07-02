import asyncio
import src.gui.gui  # Подставьте правильный путь к файлу gui.py

async def main():
    # Здесь можно добавить другую асинхронную логику, если необходимо
    # ...

    # Запуск GUI
    src.gui.gui.main()  # Подставьте правильное имя функции запуска GUI

if __name__ == "__main__":
    asyncio.run(main())