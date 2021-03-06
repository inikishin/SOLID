# Open-Closed (OCP) — принцип открытости/закрытости

Программные сущности должны быть открыты для расширения, но закрыты для изменения.

Это принцип изначально был описан Бертраном Мейером и основывался на том, что однажды написанный класс не должен никаким образом изменяться. Если вам требуются изменения, создайте класс-наследник и пишите код в нём. Вы можете переопределить реализацию или изменить интерфейс — главное, чтобы это не затрагивало существующий код.

Позднее была сформулирована полиморфная версия этого принципа: вы можете дописывать код или переопределять в наследниках любые участки класса, если это не изменяет его интерфейс. Идеальной можно считать ситуацию, когда вам вообще не требуется изменять класс, чтобы добавить ему новую возможность. Важно понимать, что речь идёт не о запрете на рефакторинг, истребление багов или оптимизацию. Вы должны оставлять нетронутой именно логику работы программы.

Допустим, вам нужно написать код, который умеет находить фильм в базе данных по набору параметров. Вы, вдохновившись SRP, выделили две сущности и написали следующую структуру:

Можете ли вы научить этот класс работать с ElasticSearch, не внося изменения в код модуля «Поиск фильмов»? Вряд ли. Они тесно связаны. Хоть код и не работает напрямую с базой данных, он зависит от методов, которые есть в соседнем классе. Если и дальше продолжить придерживаться выбранной архитектуры, то после изменения и расширения модуля он будет зависеть уже от двух классов.

Нарушение OCP зачастую влечёт за собой нарушение SRP и наоборот. Если код открыт к изменениям, то правки в одном модуле приведут к правкам в другом и правило «весь код, который меняется по какой-то одной причине, должен быть сгруппирован» перестаёт соблюдаться.

Как сделать код, который будет работать независимо от того, какое хранилище выполняет поиск? Используйте интерфейсы или абстрактные классы.

Неважно, кто именно будет работать за интерфейсом: база данных, ES, файловая система, внешний API или кэш. Вы сможете добавить нужный модуль, просто написав его реализацию и передав в конструктор класса, который занимается фильтрацией. Изменять код больше не придётся, а значит, вы уменьшите риск что-то нечаянно повредить в уже работающей системе.

Стоит заметить, что в Python нет интерфейсов как таковых. Утиная типизация позволяет вам использовать любой объект, у которого реализованы подходящие атрибуты и методы. Для усиления контроля над реализацией в Python используются абстрактные классы. Важно учитывать, что в отличие от более строгих языков, вы не можете зафиксировать в классах сигнатуру методов.

С точки зрения Python такая запись совершенно не вызывает подозрений, несмотря на то, что метод превратился в атрибут.

```python
class A(abc.ABC):
     @abc.abstractmethod
     def a(self, x):
         pass

class C(A):
     a = 13

c = C() 
```
