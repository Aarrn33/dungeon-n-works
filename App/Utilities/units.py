# A class for all units used
class Unit:
    def __init__(self, value: float, unit: str):
        self.unit = unit
        self.value = value


# A class used to create and work with distances
# For instance, it is used to calculate movement speed
class Distance(Unit):
    def __init__(self, value: float, unit: str):
        assert unit in [
            "m", "ft"], "The unit is not in meters (m) nor in feets (ft) \n Those are the only implemented units for now"
        # The two ifs are used to calculate the value in feet and in meters
        # We round to a maximum of 3 digits after the decimal part
        if unit == "m":
            self.meters = value
            self.feet = round(self.meters/3.28, 3)
        elif unit == "ft":
            self.feet = value
            self.meters = round(self.feet*3.28, 3)
        super().__init__(value, unit)

# A class used to work with angles (in degrees)


class Angle(Unit):
    def __init__(self, value: float, unit: str):
        assert unit in [
            "°"], "The unit is not in degrees (°) \n This is the only implemented unit for now"
        super().__init__(value, unit)


class Weight(Unit):
    def __init__(self, value: float, unit: str):
        assert unit in [
            "kg", "lb"], "The unit is not in kilograms (kg) nor in pounds (lb) \n Those are the only implemented units for now"
        if unit == "kg":
            self.kilograms = value
            self.pounds = round(self.kilograms*2.21, 3)
        elif unit == "ft":
            self.pounds = value
            self.kilograms = round(self.pounds/2.21, 3)
        super().__init__(value, unit)
