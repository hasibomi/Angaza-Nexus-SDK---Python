class Base:
    __rooturl = 'https://payg.angazadesign.com/nexus'
    __version = 'v1'
    __url = str()
    _username = str()
    _password = str()

    def __init__(self) -> None:
        self.__url = '{}/{}'.format(
            self.__rooturl,
            self.__version
        )

    def set_auth(self, username: str, password: str):
        self._username = username
        self._password = password

    def url(self, url: str) -> str:
        return '{}/{}'.format(self.__url, url)

