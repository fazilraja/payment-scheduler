from protocols import TermProtocol, TermUnitProtocol, FrequencyProtocol
from typing import Union, Dict

class TermUnit(TermUnitProtocol):
    """Protocol of Term Unit Representation"""
    def __init__(self, name: str, code: str) -> None:
        self.name = name
        self.code = code

    def __str__(self) -> str:
        return f"{self.code} - {self.name}"

class Term(TermProtocol):
    """Financial Term Class"""
    
    #gets paid every 7 weeks
    quantity: int #7
    unit: TermUnit #week

    #string to TermUnit map
    CODE_TO_TERM_MAP: Dict[str, TermUnit] = {
        "DAY": TermUnit("day", "d"),
        "WEEK": TermUnit("week", "w"),
        "MONTH": TermUnit("month", "m"),
        "YEAR": TermUnit("year", "y"),
    }

    #lenient = false - if the unit code is not in the map, raise an error
    def __init__(
            self, quantity: int, unit: Union[TermUnit, str], lenient: bool = False
    ) -> None:
        if isinstance(unit, str):                           
            unit = self.CODE_TO_TERM_MAP.get(unit, None)
            if unit is None:
                if lenient:
                    self.unit = TermUnit(unit, unit)
                else:
                    raise ValueError(f"Invalid unit code: {unit}")
        self.quantity = quantity
        self.unit = unit

    
    #create a Term object from a string
    @classmethod
    def from_str(cls, string: str, lenient: bool = False) -> "Term":
        quantity, unit_code = string.split()
        return cls(int(quantity), unit_code, lenient)

    #display the Term object to a string
    def __str__(self) -> str:
        return f"{self.quantity} {self.unit.code}"

    #convert the Term object to a float
    def __float__(self) -> float:
        if self.unit.code == "d":
            return self.quantity / 365.0
        elif self.unit.code == "w":
            return self.quantity / 52.0
        elif self.unit.code == "m":
            return self.quantity / 12.0
        elif self.unit.code == "y":
            return self.quantity
        else:
            raise ValueError(f"Invalid unit code: {self.unit.code}")

    def __repr__(self) -> str:
         return f"Term({self.quantity}, {self.unit.code})"

    def __hash__(self) -> int:
        val = self.quantity + self.unit.code
        return hash(val)

    def __add__(self, other: "Term") -> "Term":
        if self.unit.code != other.unit.code:
            raise ValueError("Cannot add terms with different units.")
        return Term(self.quantity + other.quantity, self.unit)

    def __sub__(self, other: "Term") -> "Term":
        if self.unit.code != other.unit.code:
            raise ValueError("Cannot subtract terms with different units.")
        if self.quantity < other.quantity:
            raise ValueError("Cannot subtract terms with a larger quantity.")
        return Term(self.quantity - other.quantity, self.unit)

    def __mul__(self, other: int) -> "Term":
        return Term(self.quantity * other, self.unit)

    def __floordiv__(self, other: int) -> "Term":
        return Term(self.quantity // other, self.unit)

    def __mod__(self, other: int) -> "Term":
        return Term(self.quantity % other, self.unit)

    def __truediv__(self, other: int) -> "Term":
        return Term(self.quantity / other, self.unit)

    def __eq__(self, other: "Term") -> bool:
        return self.quantity == other.quantity and self.unit.code == other.unit.code

    def __gt__(self, other: "Term") -> bool:
        return self.quantity > other.quantity and self.unit.code > other.unit.code

    def __ge__(self, other: "Term") -> bool:
        return self.quantity >= other.quantity and self.unit.code >= other.unit.code

    def __lt__(self, other: "Term") -> bool:
        return self.quantity < other.quantity and self.unit.code < other.unit.code

    def __le__(self, other: "Term") -> bool:
        return self.quantity <= other.quantity and self.unit.code <= other.unit.code

    #take in a new unit (string or termunit) and change the unit of the term object
    def change_unit(
            self, new_unit: Union[TermUnit, str], lenient: bool = False
    ) -> None:
        if isinstance(new_unit, str):
            new_unit = self.CODE_TO_TERM_MAP.get(new_unit.upper())
            if not new_unit:
                if lenient:
                    return
                raise ValueError(f"Unknown term unit code: {new_unit}")
        self.unit = new_unit

    #take in a new unit (string or termunit) and return a new term object with the new unit
    def change_unit_copy(self, new_unit: Union[TermUnit, str], lenient: bool) -> "Term":
        new_term = self.__class__(self.quantity, self.unit)
        new_term.change_unit(new_unit, lenient)
        return new_term
    

class Frequency(FrequencyProtocol):
    def __init__(self, name: str, term: "Term", numerical: float) -> None:
        self.name = name
        self.term = term
        self.numerical = numerical

    def __eq__(self, other: "Frequency") -> bool:
        return str(self) == str(other)
    
    def year_fraction(self) -> float:
        return 1 / self.numerical

    def __str__(self) -> str:
        return f"{self.name} ({self.numerical} {self.term})"