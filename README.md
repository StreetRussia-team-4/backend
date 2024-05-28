Запуск бекнда локально в контейнере.
Из дериктории с файлом Dockerfile-dev выполнить команды:

```sudo docker build -f Dockerfile-dev -t rust .```

```sudo docker run --name rust -p 8000:8000 rust```

API будет доступно на локалхосте 8000 порту http://127.0.0.1:8000/

http://127.0.0.1:8000/swagger/ - документация