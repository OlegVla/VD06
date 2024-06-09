
from flask import render_template, request, redirect, url_for
from app import app
posts = []
@app.route("/", methods=["GET", "POST"])

def index():
    #Использует метод POST , так как информация будет отправляться.
    # Request method сравнивает данные с HTTP запросом.
    if request.method == 'POST':
    #функция request.form извлекает значение из соответствующих полей
        title = request.form.get('title')
        content = request.form.get('content')
        title1 = request.form.get('title1')
        content1 = request.form.get('content1')
        #создаёт условие для проверки наличия данных в полях title и content

        if title and content:
            posts.append({'title': title, 'content': content, 'title1': title1, 'content1': content1})
        #использует для обновления страницы и предотвращения повторной отправки формы.
            return redirect(url_for('index'))

        #возвращает отрендеренный шаблон с переданными данными постов

    return render_template('blog.html', posts=posts)
    print(posts)