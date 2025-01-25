# HRS - Hermes Revision System

Современная и эффективная система контроля версий, написанная на Python.

[![PyPI version](https://badge.fury.io/py/hermes-revision-system.svg)](https://badge.fury.io/py/hermes-revision-system)
[![Python Version](https://img.shields.io/pypi/pyversions/hermes-revision-system.svg)](https://pypi.org/project/hermes-revision-system/)
[![License: MIT](https://img.shields.io/badge/License-MIT-yellow.svg)](https://opensource.org/licenses/MIT)

## Возможности

- 📦 Базовые операции контроля версий (init, add, commit, status)
- 🌳 Ветвление и слияние (branch, checkout, merge)
- 🏷️ Теги для маркировки важных версий
- 🔄 Система хуков для автоматизации
- 📚 Управление подмодулями
- 📝 Стэш для временного сохранения изменений
- 📊 Визуализация структуры репозитория и истории коммитов
- 🌐 Работа с удаленными репозиториями
- 🚫 Система игнорирования файлов

## Требования

- Python 3.8 или выше
- Graphviz (для визуализации)

## Установка

### Через pip

```bash
pip install hermes-revision-system
```

### Установка Graphviz

#### Windows
```bash
winget install graphviz
```

#### macOS
```bash
brew install graphviz
```

#### Linux
```bash
sudo apt-get install graphviz  # Debian/Ubuntu
sudo dnf install graphviz      # Fedora
sudo pacman -S graphviz       # Arch Linux
```

## Использование

После установки команда `hrs` станет доступна глобально.

### Основные команды

```bash
# Инициализация репозитория
hrs init

# Добавление файлов
hrs add <files>

# Создание коммита
hrs commit -m "commit message"

# Просмотр статуса
hrs status

# История коммитов
hrs log
```

### Работа с ветками

```bash
# Создание ветки
hrs branch <name>

# Список веток
hrs branches

# Переключение веток
hrs checkout <branch>

# Слияние веток
hrs merge <branch> -m "merge message"

# Удаление ветки
hrs delete-branch <name>
```

### Теги

```bash
# Создание тега
hrs tag create <name> -m "message"

# Список тегов
hrs tag list

# Удаление тега
hrs tag delete <name>

# Переключение на тег
hrs tag checkout <name>
```

### Временное хранилище (stash)

```bash
# Сохранение изменений
hrs stash save -m "message"

# Список сохраненных изменений
hrs stash list

# Применение и удаление последнего stash
hrs stash pop

# Применение без удаления
hrs stash apply <index>

# Удаление stash
hrs stash drop <index>

# Очистка всего stash
hrs stash clear
```

### Визуализация

```bash
# Граф структуры директорий
hrs graph tree output.png                    # Сохранить в файл
hrs graph tree -c                            # Вывести в консоль
hrs graph tree -c --ignore "__pycache__"     # С игнорированием файлов

# Граф истории коммитов
hrs graph history output.png                 # Сохранить в файл
hrs graph history -f svg output.svg          # В формате SVG
hrs graph history -n 10 output.png           # Ограничить количество коммитов
```

### Удаленные репозитории

```bash
# Добавление удаленного репозитория
hrs remote add <name> <url>

# Список удаленных репозиториев
hrs remote list

# Отправка изменений
hrs push <remote> <branch>

# Получение изменений
hrs pull <remote> <branch>

# Загрузка информации
hrs fetch <remote>

# Клонирование репозитория
hrs clone <url> [destination]
```

### Игнорирование файлов

```bash
# Добавление паттерна
hrs ignore add "*.pyc"

# Удаление паттерна
hrs ignore remove "*.pyc"

# Список игнорируемых паттернов
hrs ignore list

# Создание стандартного .hrsignore
hrs ignore init
```

## Разработка

1. Клонируйте репозиторий
```bash
git clone https://github.com/SomeMedic/hermes-revision-system.git
cd hermes-revision-system
```

2. Создайте виртуальное окружение
```bash
python -m venv venv
source venv/bin/activate  # Linux/macOS
venv\Scripts\activate     # Windows
```

3. Установите зависимости для разработки
```bash
pip install -e ".[dev]"
```

4. Запустите тесты
```bash
pytest
```

## Лицензия

MIT License. См. файл [LICENSE](LICENSE) для подробностей. 