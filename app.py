from Connection.Connect import connect

from flask import Flask, render_template, request, flash, url_for
from flask_login import LoginManager, login_user, current_user, login_required, logout_user
from werkzeug.utils import redirect

from Controllers.UserController import UserController
from Models.Users import Users

# создание экземпляра класса Flask
application = Flask(__name__)
# Лучше использовать переменную окружения и более сложный ключ
application.config['SECRET_KEY'] = ('YMK-ymk-otp-22isip')

login_manager = LoginManager(application)

@login_manager.user_loader
def load_user(id):
    try:
        return UserController.show(int(id))
    except (ValueError, TypeError):
        return None
    except Exception as e:
        # Логирование ошибки может быть полезно
        application.logger.error(f"Error loading user {id}: {str(e)}")
        return None
#Маршрут главной страницы
# @application.route('/', methods = ['GET','POST'])
# def home():
#     if request.method == 'POST':
#         login = request.form.get('login')
#         password = request.form.get('password')
#         if UserController.auth(login, password):
#             user = UserController.show_login(login)
#             login_user(user)
#             print('Вы прошли проверку', current_user.login)
#         else:
#             print('Вы ввели неверный логин или пароль')
#     return render_template('login.html')

@application.route('/', methods = ['GET','POST'])
def home():
    if request.method == 'POST':
        login = request.form.get('login')
        password = request.form.get('password')
        if UserController.auth(login, password):
            users = UserController.show_login(login)
            login_user(users)
            print(users)
            print(type(users.role_id))
            if users.role_id.id == 1:
                return redirect('/admin_panel')
            elif users.role_id.id == 2:
                return redirect('/manager_panel')
            elif users.role_id.id == 3:
                return redirect('/clients_panel')
            else:
                print('Вы ввели неверный логин или пароль')
    return render_template('login.html')


#Регистрация
@application.route('/registration',methods=['GET','POST'])
def registration():
    message = ''
    if request.method == 'POST':
        login = request.form.get('login')
        password = request.form.get('password')

        if UserController.registration(login, password):
            return redirect('/clients_panel')
        else:
            message = 'Логин уже занят'

    return  render_template('registation.html', message = message)

@application.route('/logout')
@login_required
def logout():
    logout_user()
    return redirect('/')


@application.route('/admin_panel', methods=['GET', 'POST'])
@login_required
def admin():
    title = "Админ панель"
    if current_user.role_id.id != 1:
        return redirect('/logout')

    if request.method == 'POST':
        try:
            login = request.form.get('login')
            password = request.form.get('password')
            role_id = int(request.form.get('role'))

            UserController.registration(login, password)
            UserController.update(Users.get(Users.login == login).id, role_id=role_id)

            flash('Пользователь успешно добавлен', 'success')
        except Exception as e:
            flash(f'Ошибка при добавлении пользователя: {str(e)}', 'danger')

    users = UserController.get()
    return render_template('admin_panel2.html', title=title, users=users)


@application.route('/user/delete/<int:user_id>', methods=['POST'])
@login_required
def delete_user(user_id):
    if current_user.role_id.id != 1:
        return redirect('/logout')

    try:
        UserController.delete(user_id)
        flash('Пользователь успешно удален', 'success')
    except Exception as e:
        flash(f'Ошибка при удалении пользователя: {str(e)}', 'danger')
    return redirect(url_for('admin'))




if __name__ == "__main__":
    #Запуск web-сервера
    application.run(debug=True)