# Фабричный метод (Factory Method) в Python

## Описание паттерна Фабричный метод

**Фабричный метод** — это порождающий паттерн проектирования, который определяет интерфейс для создания объекта, позволяя подклассам решать, какой тип создавать. Этот паттерн делегирует создание объектов производным классам, обеспечивая гибкость и расширяемость системы.

### Применимость

- Когда заранее неизвестны типы и зависимости объектов, с которыми должен работать ваш код.
- Фабричный метод отделяет код производства продуктов от остального кода, который эти продукты использует. Это позволяет расширять код производства, не изменяя основной.
- Когда пользователи должны иметь возможность расширять части вашего фреймворка или библиотеки, переопределяя методы создания объектов.
- Когда необходимо экономить системные ресурсы, повторно используя уже созданные объекты вместо порождения новых.

### Преимущества и недостатки

**Преимущества:**
- Избавляет класс от привязки к конкретным классам продуктов.
- Выделяет код производства продуктов в одно место, упрощая поддержку.
- Упрощает добавление новых продуктов в программу.
- Реализует принцип открытости/закрытости.

**Недостатки:**
- Может привести к созданию больших параллельных иерархий классов, так как для каждого класса продукта нужно создать свой подкласс создателя.

---

## Сущности паттерна

1. **Интерфейс продукта** (`Notification`): Определяет общий интерфейс для всех уведомлений.
2. **Конкретные продукты**:
   - `EmailNotification`: Реализует отправку уведомлений по электронной почте.
   - `SMSNotification`: Реализует отправку уведомлений по SMS.
3. **Базовая фабрика** (`AbstractNotificationFactory`): Определяет метод для создания уведомлений.
4. **Конкретные фабрики**:
   - `EmailNotificationFactory`: Создает экземпляры `EmailNotification`.
   - `SMSNotificationFactory`: Создает экземпляры `SMSNotification`.
5. **Клиент**: Использует фабрики для получения уведомлений и отправки сообщений.

---


### Клиентский код

- `notify_user`: Использует фабрику для получения уведомления и отправки сообщения.

```python
def notify_user(factory: NotificationFactory, message: str, username: str) -> None:
    notification = factory.create_notification()
    notification.send(username, message)


if __name__ == "__main__":
    username = "Yeblan"
    message = f"Hello, {username}"

    email_factory = EmailNotificationFactory()
    sms_factory = SmsNotificationFactory()

    notify_user(email_factory, message, username)
    notify_user(sms_factory, message, username)

```