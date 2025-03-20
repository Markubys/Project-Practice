```mermaid
C4Context
title System Context diagram for 3D Typing Trainer Project

Person(user, "User", "Пользователь тренажёра, обучающийся слепому набору текста")

Enterprise_Boundary(b1, "ProjectBoundary") {

    System(game, "3D Typing Trainer (Godot)", "3D-игра для тренировки навыков слепого набора текста")
    System(web, "Web Dashboard (Dash)", "Веб-интерфейс для просмотра статистики и прогресса пользователей")
    System(django, "Django REST API", "Серверное приложение для обработки запросов и работы с базой данных")
    SystemDb(database, "SQLite Database", "Хранит данные о пользователях и их прогрессе")

}

Rel(user, game, "Использует для тренировки")
Rel(game, django, "Отправляет результаты и получает тексты заданий")
Rel(web, django, "Запрашивает статистику")
Rel(django, database, "Читает и записывает данные")

