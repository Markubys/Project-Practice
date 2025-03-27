import dash
from dash import dcc, html
from dash.dependencies import Input, Output
import requests

# Создаем Dash-приложение
app = dash.Dash(__name__, suppress_callback_exceptions=True)

app.layout = html.Div([
    html.H1("Прогресс пользователей"),
    dcc.Dropdown(id='user-dropdown', placeholder="Выберите пользователя"),
    html.Div(id='progress-data')
])

# Callback для загрузки списка пользователей
@app.callback(
    Output('user-dropdown', 'options'),
    [Input('user-dropdown', 'id')]
)
def fetch_users(_):
    response = requests.get('http://localhost:8000/users/')  # Замените на URL вашего API
    if response.status_code == 200:
        users = response.json()
        return [{'label': user['username'], 'value': user['id']} for user in users]
    return []

# Callback для отображения прогресса пользователя
@app.callback(
    Output('progress-data', 'children'),
    [Input('user-dropdown', 'value')]
)
def display_progress(user_id):
    if not user_id:
        return "Выберите пользователя."
    
    response = requests.get(f'http://localhost:8000/progress/?user={user_id}')
    if response.status_code == 200:
        progress_list = response.json()
        if not progress_list:
            return "Нет данных о прогрессе."
        
        return html.Ul([
            html.Li(f"Уровень: {p['level']}, Точность: {p['accuracy']}%, Скорость: {p['speed']} CPM") if user_id == p['user'] else None for p in progress_list
        ])
    return "Ошибка загрузки данных."

if __name__ == '__main__':
    app.run_server(debug=True)