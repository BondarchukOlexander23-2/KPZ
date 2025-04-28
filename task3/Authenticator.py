import threading


class Authenticator:
    _instance = None
    _lock = threading.Lock()

    def __new__(cls):
        if cls._instance is None:
            with cls._lock:
                if cls._instance is None:
                    cls._instance = super().__new__(cls)
                    cls._instance._initialized = False
        return cls._instance

    def __init__(self):
        if not self._initialized:
            self._users = {}
            self._initialized = True

    def add_user(self, username, password):
        self._users[username] = password

    def authenticate(self, username, password):
        return self._users.get(username) == password

    def __str__(self):
        return f"Аутентифікатор з {len(self._users)} користувачами"



if __name__ == "__main__":
    auth1 = Authenticator()
    auth2 = Authenticator()

    print(f"auth1 це auth2: {auth1 is auth2}")

    auth1.add_user("admin", "secret123")
    auth1.add_user("user1", "password1")

    print(f"Auth1 перевірка: {auth1.authenticate('admin', 'secret123')}")  # True
    print(f"Auth2 перевірка: {auth2.authenticate('user1', 'password1')}")  # True
    print(f"Auth2 невірний логін: {auth2.authenticate('admin', 'wrong')}")  # False


    def test_singleton():
        auth = Authenticator()
        print(f"Потік {threading.current_thread().name}: {auth}")

    threads = []
    for i in range(5):
        thread = threading.Thread(target=test_singleton)
        threads.append(thread)
        thread.start()

    for thread in threads:
        thread.join()