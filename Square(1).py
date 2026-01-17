class Square:
    def __init__(self, length=5):
        # We set the property (self.length) to trigger the setter's validation logic immediately
        self.length = length
        self.ch = '*'

    @property
    def length(self):
        return self._length

    @length.setter
    def length(self, value):
        # Uses abs() for cleaner logic
        self._length = abs(value)

    # Area Calculation: s^2
    def calc_area(self):
        return self._length ** 2

    # Perimeter Calculation: 4s
    def calc_perimeter(self):
        return self._length * 4

    def __str__(self):
        # Pythonic optimization: Multiply strings instead of looping
        # 1. Create one row: self.ch * self._length
        # 2. Add a newline
        # 3. Multiply that whole row by the number of rows (self._length)
        row = (self.ch * self._length) + "\n"
        return row * self._length
