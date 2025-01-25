from enum import Enum

class Colors(Enum):
    BLACK = "\033[30m"
    RED = "\033[31m"
    GREEN = "\033[32m"
    YELLOW = "\033[33m"
    BLUE = "\033[34m"
    MAGENTA = "\033[35m"
    CYAN = "\033[36m"
    WHITE = "\033[37m"
    RESET = "\033[0m"

    def apply(self, text: str) -> str:
        """
        Returns text with color
        """

        return f'{self.value}{text}{Colors.RESET.value}'

    def __call__(self, text: str) -> None:
        """
        Prints text with color
        """

        print(
            f'{self.value}{text}{Colors.RESET.value}'
        )
