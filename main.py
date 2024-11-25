from http.server import BaseHTTPRequestHandler, HTTPServer
from src.config import file_contact_html  # Импортируется путь к файлу contacts.html

hostName = "localhost"  # Имя хоста, на котором будет запущен сервер
serverPort = 8080  # Порт, на котором будет работать сервер


class MyServer(BaseHTTPRequestHandler):
    """
    Класс для обработки входящих запросов от клиентов.
    Наследуется от BaseHTTPRequestHandler.
    """

    def do_GET(self):
        """Метод для обработки входящих GET-запросов."""

        self.send_response(200)  # Отправляем ответ с кодом состояния 200 (OK)
        self.send_header("Content-type", "text/html")  # Устанавливаем тип контента как HTML
        self.end_headers()  # Завершаем формирование заголовков ответа

        with open(file_contact_html, encoding='utf-8') as f:  # Открываем файл contacts.html
            content = f.read()  # Читаем содержимое файла

        self.wfile.write(bytes(content, "utf-8"))  # Отправляем содержимое файла в виде байтов

    def do_POST(self):
        """Метод для обработки входящих POST-запросов."""

        content_length = int(self.headers['Content-Length'])  # Получаем длину тела запроса
        post_data = self.rfile.read(content_length)  # Читаем данные из тела запроса

        print(post_data)  # Выводим полученные данные в консоль

        response = f"Received POST data: {post_data.decode('utf-8')}"  # Формируем строку ответа
        print(response)  # Выводим ответ в консоль


if __name__ == "__main__":
    # Инициализация веб-сервера с указанными хостом и портом
    webServer = HTTPServer((hostName, serverPort), MyServer)

    print(f"Server started http://{hostName}:{serverPort}")  # Сообщение о старте сервера

    try:
        # Бесконечный цикл ожидания и обработки входящих запросов
        webServer.serve_forever()
    except KeyboardInterrupt:
        # Обработка прерывания (Ctrl+C)
        pass

    # Остановка и закрытие сервера
    webServer.server_close()
    print("Server stopped.")  # Сообщение об остановке сервера

print(1)