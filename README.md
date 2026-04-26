# 👾 Alien Invasion

Космический шутер на Python + Pygame. Уничтожай флоты пришельцев, 
набирай очки и побей свой рекорд.

## 🎮 Геймплей
- Управляй кораблём и отстреливай пришельцев
- С каждым уровнем флот становится быстрее
- 3 жизни — не дай пришельцам добраться до земли
- Рекорд сохраняется в течение сессии

## 🕹️ Управление
| Клавиша | Действие |
|---------|----------|
| ← → | Движение корабля |
| Пробел | Выстрел |
| Q | Выход из игры |
| Play | Начать игру |

## 🛠️ Установка

### Требования
- Python 3.12+
- Pygame

### Запуск
```bash
git clone https://github.com/AlekseyMigitka/alien-invasion.git
cd alien-invasion
python3 -m venv venv
source venv/bin/activate
pip install -r requirements.txt
python3 alien_invasion.py
```

## 🗂️ Структура проекта

alien-invasion/
├── images/              # Спрайты корабля и пришельцев
├── alien_invasion.py    # Главный файл, игровой цикл
├── settings.py          # Все настройки игры
├── ship.py              # Класс корабля игрока
├── alien.py             # Класс пришельца
├── bullet.py            # Класс снаряда
├── button.py            # Класс кнопки Play
├── game_stats.py        # Статистика (счёт, жизни, уровень)
├── scoreboard.py        # Отображение счёта на экране
└── requirements.txt     # Зависимости проекта

## 📄 Лицензия
MIT