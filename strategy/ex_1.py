from abc import ABC, abstractmethod


class StrategySort(ABC):

    def __init__(self, title: str) -> None:
        self.title = title

    @abstractmethod
    def sort(self, array: list) -> None:
        raise NotImplementedError


class InsertionSort(StrategySort):
    """Сортировка вставками"""

    def __init__(self):
        super().__init__("Сортировка вставками")

    def sort(self, array: list) -> None:
        for i in range(1, len(array)):
            key = array[i]
            j = i - 1
            while j >= 0 and key < array[j]:
                array[j + 1] = array[j]
                j -= 1
            array[j + 1] = key

class SelectionSort(StrategySort):
    """Сортировка выбором"""

    def __init__(self):
        super().__init__("Сортировка выбором")

    def sort(self, array: list) -> None:
        for i in range(len(array)):
            min_idx = i
            for j in range(i + 1, len(array)):
                if array[j] < array[min_idx]:
                    min_idx = j
            array[i], array[min_idx] = array[min_idx], array[i]


class BubbleSort(StrategySort):
    def __init__(self) -> None:
        super().__init__("Сортировка пузырьком")

    def sort(self, array: list) -> None:
        n = len(array)
        for i in range(n):
            for j in range(0, n - i - 1):
                if array[j] > array[j + 1]:
                    array[j], array[j + 1] = array[j + 1], array[j]


class Context:

    def __init__(self, strategy: StrategySort, array: list) -> None:
        self._strategy = strategy
        self._array = array

    @property
    def strategy(self) -> StrategySort:
        return self._strategy

    @strategy.setter
    def strategy(self, strategy: StrategySort) -> None:
        self._strategy = strategy

    def sort(self) -> None:
        self._strategy.sort(self._array)

    def print_array(self) -> None:
        print(f"{self.strategy.title}: {self._array}")


if __name__ == "__main__":
    arr1 = [31, 15, 10, 2, 4, 2, 14, 23, 12, 66]
    arr2 = [1, 5, 10, 2, 4, 12, 14, 23, 12, 66]
    arr3 = [64, 34, 25, 12, 22, 11, 90]

    # Сортировка пузырьком
    context = Context(BubbleSort(), arr3)
    context.sort()
    context.print_array()

    # Сортировка выбором
    context = Context(SelectionSort(), arr1)
    context.sort()
    context.print_array()

    # Сортировка вставками
    context = Context(InsertionSort(), arr2)
    context.sort()
    context.print_array()