from time import sleep


class User:
    def __init__(self, nickname: str, password: int, age: int):
        self.nickname = nickname
        self.password = password
        self.age = age

    def __str__(self):
        return self.nickname


class Video:
    """
    title(заголовок, строка), duration(продолжительность, секунды), time_now(секунда остановки (изначально 0)),
    adult_mode(ограничение по возрасту, bool (False по умолчанию)
    """
    def __init__(self, title: str, duration: int, time_now=0, adult_mode: bool = False):
        self.title = title
        self.duration = duration
        self.time_now = time_now
        self.adult_mode = adult_mode

    def __eq__(self, other):
        return self.title == other.title

    def __contains__(self, item):
        return item in self.title


class UrTube:
    """
    users(список объектов User), videos(список объектов Video), current_user(текущий пользователь, User)
    """
    def __init__(self):
        self.users = []
        self.videos = []
        self.current_user = None

    def __repr__(self):
        return self

    def register(self, nickname, password, age):
        password = hash(password)
        """
        Метод register, который принимает три аргумента: nickname, password, age, и добавляет пользователя в список,
        если пользователя не существует (с таким же nickname). Если существует, выводит на экран:
        "Пользователь {nickname} уже существует". После регистрации, вход выполняется автоматически.
        """
        for user in self.users:
            if user.nickname == nickname:
                print(f"Пользователь {nickname} уже существует")
                return

        new_user = User(nickname, password, age)
        self.users.append(new_user)
        self.current_user = new_user

    def log_in(self, nickname, password):
        """
        Метод log_in, который принимает на вход аргументы: nickname, password и пытается найти пользователя в users
        с такими же логином и паролем. Если такой пользователь существует, то current_user меняется на найденного.
        WARNING! password передаётся в виде строки, а сравнивается по хэшу.
        :param nickname:
        :param password:
        :return:
        """
        for user in self.users:
            if user.nickname == nickname and user.password == password:
                self.current_user = user

    def log_out(self):
        """
        Метод log_out для сброса текущего пользователя на None
        :return:
        """
        self.current_user = None

    def add(self, *args):
        """
        Метод add, который принимает неограниченное кол-во объектов класса Video и все добавляет в videos, если
        с таким же названием видео ещё не существует. В противном случае ничего не происходит.
        :param args:
        :return:
        """
        for video in args:
            if video not in self.videos:
                self.videos.append(video)

    def get_videos(self, search):
        list_video = []
        """
        Метод get_videos, который принимает поисковое слово и возвращает список названий всех видео, содержащих
        поисковое слово. Следует учесть, что слово 'UrbaN' присутствует в строке 'Urban the best' (не учитывать регистр)
        :return:
        """
        for video in self.videos:
            if search.upper() in video.title.upper():
                list_video.append(video.title)
        return list_video

    def watch_video(self, title):
        """
        Метод watch_video, который принимает название фильма, если не находит точного совпадения(вплоть до пробела),
        то ничего не воспроизводится, если же находит - ведётся отчёт в консоль на какой секунде ведётся просмотр.
        После текущее время просмотра данного видео сбрасывается.
        Для паузы между выводами секунд воспроизведения можно использовать функцию sleep из модуля time.
        Воспроизводить видео можно только тогда, когда пользователь вошёл в UrTube. В противном случае выводить
        в консоль надпись: "Войдите в аккаунт, чтобы смотреть видео"
        Если видео найдено, следует учесть, что пользователю может быть отказано в просмотре, т.к. есть ограничения 18+.
        Должно выводиться сообщение: "Вам нет 18 лет, пожалуйста покиньте страницу"
        После воспроизведения нужно выводить: "Конец видео"
        :return:
        """
        if self.current_user is None:
            print("Войдите в аккаунт, чтобы смотреть видео")
            return

        for j in self.videos:
            if j.title == title:
                if self.current_user.age < 18:
                    print("Вам нет 18 лет, пожалуйста покиньте страницу")
                    return

                for i in range(1, j.duration + 1):
                    print(i, end=' ')
                    sleep(1)
                    j.time_now += 1
                j.time_now = 0
                print("Конец видео")


if __name__ == '__main__':
    ur = UrTube()
    v1 = Video('Лучший язык программирования 2024 года', 200)
    v2 = Video('Для чего девушкам парень программист?', 10, adult_mode=True)

    # Добавление видео
    ur.add(v1, v2)

    # Проверка поиска
    print(ur.get_videos('лучший'))
    print(ur.get_videos('ПРОГ'))

    # Проверка на вход пользователя и возрастное ограничение
    ur.watch_video('Для чего девушкам парень программист?')
    ur.register('vasya_pupkin', 'lolkekcheburek', 13)
    ur.watch_video('Для чего девушкам парень программист?')
    ur.register('urban_pythonist', 'iScX4vIJClb9YQavjAgF', 25)
    ur.watch_video('Для чего девушкам парень программист?')

    # Проверка входа в другой аккаунт
    ur.register('vasya_pupkin', 'F8098FM8fjm9jmi', 55)
    print(ur.current_user)

    # Попытка воспроизведения несуществующего видео
    ur.watch_video('Лучший язык программирования 2024 года!')
