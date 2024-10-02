from time import sleep

class User:
    def __init__(self, nickname: str, password, age: int):
        self.nickname = nickname
        self.password = hash(password)
        self.age = age


    def __str__(self):
        return f'{self.nickname}'

    def __eq__(self, other):
        return other.nickname == self.nickname

    def get_info(self):
        return self.nickname, self.password





class Video:
    def __init__(self, title: str, duration, time_now=0, adult_mode=False):
        self.title = title
        self.duration = duration
        self.time_now = time_now
        self.adult_mode = adult_mode

    def __str__(self):
        return self.title


class UrTube:
    def __init__(self):
        self.users = []
        self.videos = []
        self.current_user = None

    def log_in(self, nickname, password):

        for user in self.users:
            if (nickname, hash(password)) == user.get_info():
                self.current_user = user
                return

        print(f'Такого пользователя не существует')


    def register(self, nickname, password, age):
        new_user = User(nickname, password, age)
        if new_user not in self.users:
            self.users.append(new_user)
            UrTube.log_in(self, nickname, password)
        else:
            print(f'Пользователь с ником {nickname} уже существует!')


    def log_out(self):
        self.current_user = None

    def add(self, *new_videos):
        for new_video in new_videos:
            for video in self.videos:
                if new_video.title == video.title:
                    print('такое видео уже существует')
                    break
            else:
                self.videos.append(new_video)


    def get_videos(self, key_word):
        names_of_videos = []
        for video in self.videos:
            if key_word.lower() in video.title.lower():
                names_of_videos.append(video.title)
        return names_of_videos

    def watch_video(self, title):
        film = None
        for video in self.videos:
            if title == video.title:
                film = video
                break

        if film is None:
            pass
        else:
            if self.current_user is None:
                print('Войдите в аккаунт, чтобы смотреть видео')
            else:
                if self.current_user.age < 18 and film.adult_mode is True:
                    print('Вам нет 18 лет, пожалуйста покиньте страницу')
                else:
                    for time in range(film.time_now, film.duration):
                        print(f'{time + 1}', end=' ')
                        sleep(0.1)
                    print(f'Конец видео')














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





