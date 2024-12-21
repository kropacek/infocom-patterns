from ex_1 import Microwave, Drive, Power, Notification,handle_drive_event, handle_power_event, handle_notification_event

class MicrowaveWithCooking(Microwave):

    def cook(self):
        self._notification.start()
        self._power.set_power(1200)
        self._drive.turn_right()
        self._drive.turn_right()
        self._drive.turn_left()
        self._power.set_power(800)
        self._drive.turn_right()
        self._drive.stop()
        self._notification.stop()


if __name__ == "__main__":
    # Создаем компоненты
    drive = Drive()
    power = Power()
    notification = Notification()

    # Подписываем обработчики событий
    drive.drive_event.subscribe(handle_drive_event)
    power.power_event.subscribe(handle_power_event)
    notification.notification_event.subscribe(handle_notification_event)

    microwave = MicrowaveWithCooking(drive, power, notification)

    print("Приготовление:")
    microwave.cook()
