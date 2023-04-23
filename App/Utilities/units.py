# A class for all units used
class Unit:
    def __init__(self, value: float, unit: str) -> None:
        self.unit = unit
        self.value = value


# A class used to create and work with distances
# For instance, it is used to calculate movement speed
class Distance(Unit):
    def __init__(self, value: float, unit: str) -> None:
        assert unit in [
            "m", "ft"], "The unit is not in meters (m) nor in feets (ft) \n Those are the only implemented units for now"
        # The two ifs are used to calculate the value in feet and in meters
        # We round to a maximum of 3 digits after the decimal part
        if unit == "m":
            self.meters = value
            self.feet = round(self.meter/3.28, 3)
        elif unit == "ft":
            self.feet = value
            self.meters = round(self.feet*3.28, 3)
        super().__init__(value, unit)
        self.unit = self.unit

# A class used to work with angles (in degrees)


class Angle(Unit):
    def __init__(self, value: float) -> None:
        super().__init__(value, "°")
        self.value = self.value
