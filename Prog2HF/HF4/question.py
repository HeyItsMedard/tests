from abc import abstractmethod, ABC


class Question(ABC):
    def __init__(self, text) -> None:
        self.text = text

    @abstractmethod
    def ask(self) -> bool:
        """Print question, read answer from user, and return whether it is correct."""
        pass

    # The order is important!
    @classmethod
    @abstractmethod
    def create_question(cls) -> "Question":
        """Prompt user for question information and return a new Question object."""
        pass

    @abstractmethod
    def __repr__(self) -> str:
        """Return a string representation of the question.

        This should be a valid Python expression that can be evaluated to recreate the question.
        """
        pass


class TrueFalseQuestion(Question):
    """Answer can be 'True' or 'False'."""
    def __init__(self, text, correct_answer) -> None:
        super().__init__(text)
        self.correct_answer = correct_answer.lower() == 'true'

    def ask(self) -> bool:
        print(self.text)
        user_input = input("Enter 'True' or 'False': ").strip().lower()
        return user_input == str(self.correct_answer).lower()

    @classmethod
    def create_question(cls) -> "Question":
        text = input("Enter the True/False question text: ")
        correct_answer = input("Is the correct answer 'True' or 'False'? ").strip()
        return cls(text, correct_answer)

    def __repr__(self) -> str:
        return f"{self.__class__.__name__}('{self.text}', '{'True' if self.correct_answer else 'False'}')"


class MultipleChoiceQuestion(Question):
    """There are given answer options to choose from.
    Only 1 option is correct."""
    def __init__(self, text, options, correct_option) -> None:
        super().__init__(text)
        self.options = options
        self.correct_option = correct_option

    def ask(self) -> bool:
        print(self.text)
        for i, option in enumerate(self.options):
            print(f"{i + 1}. {option}")
        user_input = input("Enter the number of the correct option: ")
        return int(user_input) == self.correct_option

    @classmethod
    def create_question(cls) -> "Question":
        text = input("Enter the Multiple Choice question text: ")
        options = input("Enter the answer options separated by commas: ").split(',')
        options = [option.strip() for option in options]
        correct_option = int(input("Enter the number of the correct option: "))
        return cls(text, options, correct_option)

    def __repr__(self) -> str:
        return f"{self.__class__.__name__}('{self.text}', {self.options}, {self.correct_option})"

class NumericQuestion(Question):
    """The answer is a number (maybe rational).
    Set a tolerance value at creation."""
    def __init__(self, text, correct_answer, tolerance) -> None:
        super().__init__(text)
        self.correct_answer = correct_answer
        self.tolerance = tolerance

    def ask(self) -> bool:
        print(self.text)
        user_input = input("Enter a number: ")
        try:
            user_answer = float(user_input)
            return abs(user_answer - self.correct_answer) <= self.tolerance
        except ValueError:
            return False

    @classmethod
    def create_question(cls) -> "Question":
        text = input("Enter the Numeric question text: ")
        correct_answer = float(input("Enter the correct numeric answer: "))
        tolerance = float(input("Enter the tolerance value for the answer: "))
        return cls(text, correct_answer, tolerance)

    def __repr__(self) -> str:
        return f"{self.__class__.__name__}('{self.text}', {self.correct_answer}, {self.tolerance})"
