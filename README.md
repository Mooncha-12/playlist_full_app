# Playlist_module
## all_about_playlist
### Класс Song
Класс `Song` представляет собой объект песни, у которого есть два атрибута: `name` и `duration`. 

Методы:
- `__init__(self, name, duration)`: конструктор класса, который принимает два параметра: название песни и ее продолжительность.
- `getDuration(self)`: метод, который возвращает продолжительность песни.
- `getName(self)`: метод, который возвращает название песни.

### Класс Node
Класс `Node` представляет собой узел двусвязного списка, у которого есть три атрибута: `song`, `next` и `previous`.

Методы:
- `__init__(self, song, next=None, previous=None)`: конструктор класса, который принимает три параметра: объект песни, ссылку на следующий узел списка (по умолчанию None) и ссылку на предыдущий узел списка (по умолчанию None).

### Класс DoublyLinkedList
Класс `DoublyLinkedList` представляет собой двусвязный список, у которого есть четыре атрибута: `head`, `tail`, `length` и `current_node_for_doublylinkedlist`.

Методы:
- `__init__(self)`: конструктор класса.
- `addsong(self, song)`: метод, который добавляет новую песню в список.
- `find_node_by_song(self, song)`: метод, который ищет узел по песне.
- `delete_node(self, node)`: метод, который удаляет узел из списка.

### Класс Operation
Класс `Operation` представляет собой объект операции воспроизведения песен из плейлиста.

Методы:
- `__init__(self)`: конструктор класса.
- `add_song(self, song)`: метод, который добавляет новую песню в плейлист.
- `set_current_node(self, node)`: метод, который устанавливает текущий узел списка плейлиста.
- `run(self)`: метод, который запускает воспроизведение песен из плейлиста.
- `play(self)`: метод, который запускает воспроизведение песни из плейлиста.
- `pause(self)`: метод, который приостанавливает воспроизведение песни из плейлиста.
- `next_song(self)`: метод, который переключается на следующую песню из плейлиста.
- `previous_song(self)`: метод, который переключается на предыдущую песню из плейлиста.
- `stop(self)`: метод, который останавливает воспроизведение песен из плейлиста и завершает работу потока воспроизведения.

## basic
## crud.py
### Описание функций для работы с базой данных

Данный код содержит функции для работы с базой данных, используя SQLAlchemy и FastAPI. 

#### Функции для работы с таблицей Playlist

#### get_playlist
Функция `get_playlist` получает объект с указанным идентификатором из таблицы Playlist в базе данных.

#### get_playlist_by_name
Функция `get_playlist_by_name` получает объект Playlist с указанным именем из таблицы Playlist в базе данных.

#### get_playlists
Функция `get_playlists` получает список объектов Playlist из таблицы Playlist в базе данных, начиная с указанного индекса и ограничивая количество результатов указанным лимитом.

#### create_playlist
Функция `create_playlist` создает новый объект Playlist в таблице Playlist в базе данных, используя переданный объект модели PlaylistCreate. Если уже есть объект Playlist в базе данных, то вызывается исключение HTTPException.

#### delete_playlist_by_id
Функция `delete_playlist_by_id` удаляет объект Playlist с указанным идентификатором из таблицы Playlist в базе данных.

### Функции для работы с таблицей Song

#### get_song_by_id
Функция `get_song_by_id` получает объект с указанным идентификатором из таблицы Song в базе данных.

#### get_song_for_delete
Функция `get_song_for_delete` получает объект Song с указанным именем из таблицы Song в базе данных.

#### create_playlist_songs
Функция `create_playlist_songs` создает новый объект Song в таблице Song в базе данных, используя переданный объект модели SongCreate и идентификатор Playlist, который был получен из первого объекта Playlist в таблице Playlist. Если уже есть объект Song с таким же именем, то вызывается исключение HTTPException.

##### delete_song_by_name
Функция `delete_song_by_name` удаляет объект Song с указанным именем из таблицы Song в базе данных.

#### update_song
Функция `update_song` обновляет объект Song с указанным идентификатором в таблице Song в базе данных, используя переданный объект модели SongUpdate. Если объект не найден, то возвращается None.

## main.py

### Модели данных

PlaylistCreate: модель для создания плейлиста с полями name (название плейлиста) и description (описание плейлиста).
Playlist: модель для плейлиста с полями id, name и description.
SongCreate: модель для создания песни с полями name (название песни), duration (продолжительность песни) и playlist_id (ID плейлиста, к которому относится песня).
Song: модель для песни с полями id, name, duration и playlist_id.
SongUpdate: модель для обновления песни с полями name (необязательно) и duration (необязательно).

Функции:

get_db(): функция для получения сессии базы данных. Эта функция используется в качестве зависимости (dependency) в конечных точках, которые требуют доступ к базе данных.

get_player(): функция для создания нового экземпляра двусвязного списка (DoublyLinkedList), который используется для управления плейлистом в режиме воспроизведения.

add_song_for_doublylinkedlist(): вспомогательная функция для добавления песни в двусвязный список.

create_playlist(): конечная точка для создания нового плейлиста.

read_playlist(): конечная точка для чтения списка плейлистов.

read_playlist_by_id(): конечная точка для чтения плейлиста по его ID.

create_song_for_playlist(): конечная точка для создания новой песни в указанном плейлисте. Она также добавляет песню в двусвязный список.

read_song_by_id(): конечная точка для чтения песни по ее ID.

update_song_in_playlist(): конечная точка для обновления информации о песне в указанном плейлисте.

delete_playlist(): конечная точка для удаления плейлиста.

delete_song(): конечная точка для удаления песни из указанного плейлиста и из двусвязного списка. Также проверяет, проигрывается ли песня в данный момент, и возвращает ошибку, если это так.

play(): конечная точка для запуска воспроизведения плейлиста.

pause(): конечная точка для приостановки воспроизведения плейлиста.

next_song(): конечная точка для переключения на следующую песню в плейлисте.

previous_song(): конечная точка для переключения на предыдущую песню в плейлисте.

## models.py

Модель SongBase содержит два поля: name (название песни) и duration (длительность песни).

Модель SongCreate наследуется от SongBase и не добавляет никаких новых полей.

Модель Song наследуется от SongBase и содержит три поля: id (идентификатор песни), playlist_id (идентификатор плейлиста, к которому относится песня) и список songs (список песен).

Модель PlaylistBase содержит одно поле: name (название плейлиста).

Модель PlaylistCreate наследуется от PlaylistBase и также содержит поле name.

Модель Playlist наследуется от PlaylistBase и содержит два поля: id (идентификатор плейлиста) и список songs (список песен).

Также определены модели SongUpdate и SongRequest, которые содержат поля name (название песни) и duration (длительность песни), и которые могут использоваться для обновления и создания объектов типа Song.

Конфигурация классов Song и Playlist содержит параметр orm_mode, который указывает Pydantic на то, что классы должны использоваться для взаимодействия с базой данных с помощью ORM-фреймворков, таких как SQLAlchemy.

## файл sql_app

## database.py

В первой строке определена константа SQLALCHEMY_DATABASE_URL, содержащая адрес базы данных в формате SQLite.

В следующих трех строках создается движок базы данных SQLAlchemy и сессионный конструктор, который используется для создания новых сессий работы с базой данных.

В последней строке создается базовый класс моделей SQLAlchemy с помощью функции declarative_base(). Этот класс используется для определения моделей, которые будут соответствовать таблицам в базе данных.

## shemas.py

Модель "Playlist" содержит поля "id" (уникальный идентификатор плейлиста), "name" (название плейлиста) и список "songs" (список песен, связанных с плейлистом).

Модель "Song" содержит поля "id" (уникальный идентификатор песни), "name" (название песни), "duration" (длительность песни) и "playlist_id" (идентификатор плейлиста, к которому относится песня).

Также определены отношения между таблицами с помощью функции relationship(), которая позволяет получить доступ к связанным данным в другой таблице.

По умолчанию, SQLAlchemy будет использовать имена таблиц, соответствующие именам классов моделей, но в данном коде используется параметр tablename для явного указания имени таблицы в базе данных.

## Прошу прощения за такую документацию, просто очень сильно не успевал по времени
#   p l a y l i s t  
 #   f u l l _ p l a y l i s t  
 