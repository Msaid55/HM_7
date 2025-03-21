# 📝 Мой веб-сайт для резюме
Это современный и профессиональный веб-сайт для резюме, который интегрируется с GitHub API для автоматической загрузки и отображения данных профиля пользователя. Веб-сайт разработан с использованием Flask на бэкенде и служит отличной платформой для демонстрации вашего профессионального опыта, проектов и навыков, актуальных данных напрямую из вашего профиля GitHub.

Этот сайт идеально подходит для разработчиков, позволяя поддерживать актуальность резюме и автоматически отображать последние изменения в ваших репозиториях и других профессиональных достижениях.

---

## 📸 Скриншот

![Скриншот резюме](screenshot.png)

---

## 🛠 Установка

1. **Клонировать репозиторий:**
   ``
клонирование bash git https://github.com/your-username/your-repository-name.git
   укажите имя вашего репозитория
## Установленные зависимости
Проект использует несколько внешних библиотек, которые можно установить с помощью pip. Для этого в корневой папке проекта выполните следующую команду:
```bash
pip install -r requirements.txt
```

## Создайте и активируйте виртуальную среду:

```bash
python -m venv venv
.\venv\Scripts\Activate
```

## Шаги для создания персонального токена доступа на GitHub
Следуйте шагам ниже для создания токена на GitHub:Следуйте шагам ниже для создания токена на GitHub:
1. Войдите в свою учетную запись GitHub
Перейдите на [GitHub](https://github.com) и войдите в свою учетную запись.
2. Откройте настройки разработчика
3. В правом верхнем углу любой страницы GitHub нажмите на изображение своего профиля.
4. В выпадающем меню выберите **Settings** (Настройки).
5. В левой части экрана прокрутите вниз и нажмите **Developer settings** (Настройки разработчика).
6.  В меню **Developer settings** выберите **Personal access tokens** (Персональные токены доступа).
7. Затем выберите **Tokens (classic)** в разделе **Personal access tokens**.
8. Нажмите **Generate new token** (Создать новый токен), чтобы создать токен.
9. получить ваш токен 


## Создайте файл .env:

удар
GITHUB_TOKEN=ваш_github_token
GITHUB_USERNAME=ваш_github_username

## Запустите приложение:


запустите bash flask

## Посетите сайт:
удар
Перейдите по ссылке http://127.0.0.1:5000

## 📚 Использование
Домашняя страница: Отображает информацию о вашем профиле на GitHub и репозиториях.
Кнопка обновления: Обновляет резюме с использованием последних данных GitHub без перезагрузки страницы.
Строка поиска: Фильтрует репозитории по названию.

## 📜 Лицензия
Этот проект лицензирован по лицензии MIT - подробности смотрите в файле ЛИЦЕНЗИИ.