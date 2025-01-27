### Hexlet tests and linter status:
[![Actions Status](https://github.com/RatiborM/python-project-50/workflows/hexlet-check/badge.svg)](https://github.com/RatiborM/python-project-50/actions)
[![Maintainability](https://api.codeclimate.com/v1/badges/acd05649de1fc98c22bc/maintainability)](https://codeclimate.com/github/RatiborM/python-project-50/maintainability)
[![Test Coverage](https://api.codeclimate.com/v1/badges/acd05649de1fc98c22bc/test_coverage)](https://codeclimate.com/github/RatiborM/python-project-50/test_coverage)

# Gendiff: Найти различия между файлами

Gendiff — это мощный CLI-инструмент для поиска различий между файлами. Он поддерживает различные форматы и предоставляет результаты в стильном, простом или JSON формате.

---

## 🚀 Возможности

- Легкое сравнение JSON и YAML файлов.
- Поддержка нескольких форматов вывода: Stylish, Plain и JSON.
- Легкий и удобный CLI-инструмент.

---

## 📦 Установка

### Шаг 1: Установите зависимости
```bash
make install
```

### Шаг 2: Соберите проект
```bash
make build
```

### Шаг 3: Установите пакет
```bash
make package-install
```

---

## 🛠️ Использование

### Показать справку
```bash
gendiff -h
```

### Сравнить два файла (по умолчанию: Stylish формат)
```bash
gendiff tests/fixtures/file1.json tests/fixtures/file2.json
```

### Сравнить два файла в Plain формате
```bash
gendiff --format plain tests/fixtures/file1.yml tests/fixtures/file2.yml
```



### Сравнить два файла в JSON формате
```bash
gendiff --format json tests/fixtures/file1.json tests/fixtures/file2.json
```

---

## 🧹 Очистка

Для полного удаления проекта выполните:
```bash
rm -rf .
```

## Демонстрация

### `Вывод справки через флаг -h`

[![asciicast](https://asciinema.org/a/Lh27JDsBGNTUTWyEm97xgjGsi.svg)](https://asciinema.org/a/Lh27JDsBGNTUTWyEm97xgjGsi)


### `Два файла (по умолчанию stylish)`
[![asciicast](https://asciinema.org/a/NN8aXZ3TKZ0xpWDNissRI95O2.svg)](https://asciinema.org/a/NN8aXZ3TKZ0xpWDNissRI95O2)

### `Два файла в plain-формате`
[![asciicast](https://asciinema.org/a/np1ppxfh5GZFqG0oX3iOkVI1h.svg)](https://asciinema.org/a/np1ppxfh5GZFqG0oX3iOkVI1h)

### `Два файла в JSON-формате`
[![asciicast](https://asciinema.org/a/Ux7IUUChVAGZd1gqtqWjl9Oye.svg)](https://asciinema.org/a/Ux7IUUChVAGZd1gqtqWjl9Oye)
## 📖 Лицензия
Этот проект лицензирован на условиях лицензии MIT.
