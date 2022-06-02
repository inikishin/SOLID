# Dependency Inversion — принцип инверсии зависимостей

Модули верхних уровней не должны зависеть от модулей нижних уровней. Оба типа модулей должны зависеть от абстракций.

Абстракции не должны зависеть от деталей. Детали должны зависеть от абстракций.

Принцип инверсии зависимостей предлагает избавиться от использования конструкторов явно заданных классов. Вместо этого высокоуровневый модуль должен объявить интерфейс, в котором он нуждается. Это даст ему возможность пользоваться любым из низкоуровневых модулей, реализовавших его требования.

Этот принцип похож на принцип открытости/закрытости. Отличие в том, что OCP определяет, как вам стоит подходить к проектированию одного модуля, а DIP — как упростить связи между несколькими модулями.

Вернёмся к проблеме прямой зависимости, рассмотренной в OCP.

```python
class View:
    def __init__(self):
        self.data = RemoteStorage().get_data(id=24)

class RemoteStorage:
    def __init__(self):
        self.session = HTTPSession()
    
    def get_data(self, **params): 
        response = self.session.request(params['id'])
        return response.data

class HTTPSession:
    def __init__(self):
        ...

    def request(self, pk):
        return ... 
```

Высокоуровневый класс View создаёт экземпляр класса RemoteStorage, который, в свою очередь, создаёт экземпляр класса HTTPSession. У такого кода есть несколько проблем:
* Изменения в HTTPSession.request могут заставить вас вносить изменения в RemoteStorage и View.
* Вы не можете заменить RemoteStorage на LocalStorage или другую реализацию, не изменив класс.
* Вы не сможете протестировать свой код, не выполнив код из связаных классов.

* Теперь применим к этому коду принцип инверсии зависимостей, добавив абстрактные классы между связями.

```python
class View:
    def __init__(self, storage: AbstractStorage):
        self.data = storage().get_data(id=24)

class AbstractStorage(ABC):
    @abstractmethod
    def get_data(self, **params): 
        pass

class RemoteStorage(AbstractStorage):
    def __init__(self, session: AbstractSession):
        self.session = session()
    
    def get_data(self, **params): 
        response = self.session.request(params['id'])
        return response.data

class AbstractSession(ABC):
    @abstractmethod
    def request(pk):
        pass

class HTTPSession(AbstractSession):
    ... 
```

Для уменьшения связности вы можете пользоваться паттерном Composition Root, реализовав единую точку, в которой вы будете создавать и группировать объекты для модуля. Или вместо того, чтобы вручную создавать объекты, использовать DI-контейнеры.
