class Converter:
    """
    Class providing static methods for unit conversions.
    """

    @staticmethod
    def kg_to_lbs(x: float) -> float:
        """
        Convert kilograms to pounds.
        """
        result = x * 2.205
        return result

    @staticmethod
    def lbs_to_kg(x: float) -> float:
        """
        Convert pounds to kilograms.
        """
        result = x / 2.205
        return result

    @staticmethod
    def km_to_miles(x: float) -> float:
        """
        Convert kilometers to miles.
        """
        result = x / 1.609
        return result

    @staticmethod
    def miles_to_km(x: float) -> float:
        """
        Convert miles to kilometers.
        """
        result = x * 1.609
        return result
