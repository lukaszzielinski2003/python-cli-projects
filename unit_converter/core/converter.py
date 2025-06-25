class Converter:
    """
    Class providing static methods for unit conversions.
    """

    @staticmethod
    def kg_to_lbs(x: float) -> float:
        """
        Convert Kilograms to Pounds.
        """
        result = x * 2.205
        return result

    @staticmethod
    def lbs_to_kg(x: float) -> float:
        """
        Convert Pounds to Kilograms.
        """
        result = x / 2.205
        return result

    @staticmethod
    def km_to_miles(x: float) -> float:
        """
        Convert Kilometers to Miles.
        """
        result = x / 1.609
        return result

    @staticmethod
    def miles_to_km(x: float) -> float:
        """
        Convert Miles to Kilometers.
        """
        result = x * 1.609
        return result
    
    @staticmethod
    def cel_to_far(x: float) -> float:
        """
        Convert Celsius to Fahrenheit
        """
        result = (x * 9/5) + 32
        return result

    @staticmethod
    def far_to_cel(x: float) -> float:
        """
        Convert Fahrenheit to Celsius.
        """
        result = (x - 32) * 5/9
        return result