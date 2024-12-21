
class AutoBase:
    def __init__(self, name, description, cost_base):
        self.name = name
        self.description = description
        self.cost_base = cost_base

    def get_cost(self):
        return self.cost_base

    def __str__(self):
        return f"Ваш автомобиль: {self.name}\nОписание: {self.description}\nСтоимость: {self.get_cost()}"


class Renault(AutoBase):
    def __init__(self, name, description, cost_base):
        super().__init__(name, description, cost_base)

    def get_cost(self):
        return self.cost_base * 1.18


class DecoratorOptions(AutoBase):
    def __init__(self, auto_property: AutoBase, title: str) -> None:
        self.auto_property = auto_property
        self.title = title



class MediaNAV(DecoratorOptions):

    def __init__(self, auto_property, title):
        super().__init__(auto_property, title)

        self.name = auto_property.name + ". Современный"
        self.description = f"{auto_property.description}. {title}. Обновленная мультимедийная система"

    def get_cost(self):
        return self.auto_property.get_cost() + 15.99




class SystemSecurity(DecoratorOptions):
    def __init__(self, auto_property, title):
        super().__init__(auto_property, title)

        self.name = auto_property.name + ". Повышенной безопасности"
        self.description = (f"{auto_property.description}. {title}. Передние подушки безопасности и система стабилизации"
                            f", ESP - система динамической стабилизации автомобиля")

    def get_cost(self):
        return self.auto_property.get_cost() + 20.99


if __name__ == "__main__":
    # Базовый автомобиль
    renault = Renault("Renault Logan", "Стандартная комплектация", 499.0)
    print(renault)

    # Автомобиль с мультимедийной системой
    renault_with_media = MediaNAV(renault, "Навигация")
    print(f"\n{renault_with_media}")

    # Автомобиль с мультимедийной системой и системой безопасности
    renault_full = SystemSecurity(renault_with_media, "Безопасность")
    print(f"\n{renault_full}")
