
class Event:
    def __init__(self):
        self.subscribers = []

    def subscribe(self, callback):
        self.subscribers.append(callback)

    def notify(self, *args, **kwargs):
        for callback in self.subscribers:
            callback(*args, **kwargs)


class Drive:
    def __init__(self):
        self.twist = "Исходная позиция"
        self.drive_event = Event()

    def turn_left(self):
        self.twist = "Поворот налево"
        self.drive_event.notify(self.twist)

    def turn_right(self):
        self.twist = "Поворот направо"
        self.drive_event.notify(self.twist)

    def stop(self):
        self.twist = "Стоп"
        self.drive_event.notify(self.twist)


class Power:
    def __init__(self):
        self.power = 0
        self.power_event = Event()

    def set_power(self, level):
        self.power = level
        self.power_event.notify(self.power)


class Notification:
    def __init__(self):
        self.message = ""
        self.notification_event = Event()

    def start(self):
        self.message = "Операция началась"
        self.notification_event.notify(self.message)

    def stop(self):
        self.message = "Операция завершена"
        self.notification_event.notify(self.message)


class Microwave:
    def __init__(self, drive, power, notification):
        self._drive = drive
        self._power = power
        self._notification = notification

    def defrost(self):
        self._notification.start()
        self._power.set_power(1000)
        self._drive.turn_right()
        self._drive.turn_right()
        self._power.set_power(500)
        self._drive.stop()
        self._drive.turn_left()
        self._drive.turn_left()
        self._power.set_power(200)
        self._drive.stop()
        self._notification.stop()


def handle_drive_event(twist: str) -> None:
    print(f"Привод: {twist}")

def handle_power_event(power: str) -> None:
    print(f"Мощность: {power}W")

def handle_notification_event(message: str) -> None:
    print(f"Оповещение: {message}")


if __name__ == "__main__":
    # Создаем компоненты
    drive = Drive()
    power = Power()
    notification = Notification()

    # Подписываем обработчики событий
    drive.drive_event.subscribe(handle_drive_event)
    power.power_event.subscribe(handle_power_event)
    notification.notification_event.subscribe(handle_notification_event)

    # Создаем фасад
    microwave = Microwave(drive, power, notification)

    # Используем микроволновку
    print("Разморозка:")
    microwave.defrost()
