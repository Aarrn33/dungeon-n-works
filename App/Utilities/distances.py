# A class used to create and work with distances
# For instance, it is used to calculate movement speed
class Distance:
    def __init__(self, value: int, unit: str) -> None:
        assert unit in ["m", "ft"], "The unit is not in meters (m) nor in feets (ft) \n Those are the only implemented units for now"
        # The two ifs are used to calculate the value in feet and in meters        
        # We round to a maximum of 3 digits after the decimal part
        if unit == "m":
            self.meters = value
            self.feet = round(self.meter/3.28, 3)
        elif unit == "ft":
            self.feet = value
            self.meters = round(self.feet*3.28, 3)