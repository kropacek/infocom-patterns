from abc import ABC, abstractmethod

class HaircutProcess(ABC):

    def template_method(self) -> None:
        self.prepare_tools()
        self.cut_hair()
        self.clean_up()

    def prepare_tools(self) -> None:
        print("Подготовка инструментов: ножницы, расческа, машинка для стрижки.")

    def clean_up(self) -> None:
        print("Очистка инструментов и уборка рабочего места.")

    @abstractmethod
    def cut_hair(self)  -> None:
        raise NotImplementedError


class MenHaircut(HaircutProcess):
    def cut_hair(self):
        print("Выполняем мужскую стрижку: выравнивание боков и укладка волос.")


class WomenHaircut(HaircutProcess):
    def cut_hair(self):
        print("Выполняем женскую стрижку: укорачивание длины и создание слоя.")


if __name__ == "__main__":
    # Мужская стрижка
    men_haircut = MenHaircut()
    print("Мужская стрижка:")
    men_haircut.template_method()

    # Женская стрижка
    women_haircut = WomenHaircut()
    print("\nЖенская стрижка:")
    women_haircut.template_method()
