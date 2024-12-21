from ex_1 import AutoBase, DecoratorOptions


class Audi(AutoBase):
    def __init__(self, name, description, cost_base):
        super().__init__(name, description, cost_base)


class ClimateControl(DecoratorOptions):
    def __init__(self, auto_property, title):
        super().__init__(auto_property, title)

        self.name = auto_property.name + ". Комфортный"
        self.description = f"{auto_property.description}. {title}. Климат-контроль"

    def get_cost(self):
        return self.auto_property.get_cost() + 25.99


class SportPackage(DecoratorOptions):
    def __init__(self, auto_property, title):
        super().__init__(auto_property, title)

        self.name = auto_property.name + ". Быстрый"
        self.description = f"{auto_property.description}. {title}. Спортивный обвес и улучшенная подвеска"

    def get_cost(self):
        return self.auto_property.get_cost() + 30.99



if __name__ == "__main__":
    # Новый автомобиль Audi
    audi = Audi("Audi A4", "Базовая комплектация", 899.0)
    print(audi)

    # Audi с климат-контролем
    audi_with_climate = ClimateControl(audi, "Температурный режим")
    print(f"\n{audi_with_climate}")

    # Audi с климат-контролем и спортивным пакетом
    audi_sport = SportPackage(audi_with_climate, "Снаряжение")
    print(f"\n{audi_sport}")
