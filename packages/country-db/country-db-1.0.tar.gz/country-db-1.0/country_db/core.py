import json
import os
from typing import Optional, Dict, Any, List


class CountryDB:
    def __init__(self):
        self._data = self._load_data()
        self._field_mapping = {
            'name': 'CountryName',
            'alpha2_code': 'Alpha2Code',
            'alpha3_code': 'Alpha3Code',
            'numeric_code': 'NumericCode',
            'continent': 'Continent',
            'capital': 'Capital',
            'region_name': 'RegionName',
            'region_code': 'RegionCode',
            'subregion_name': 'SubRegionName',
            'subregion_code': 'SubRegionCode',
            'top_level_domain': 'TopLevelDomain',
            'calling_code': 'CallingCode',
            'currency_code': 'CurrencyCode',
            'currency_numeric_code': 'CurrencyNumericCode',
            'currency_symbol': 'CurrencySymbol',
            'currency_name': 'CurrencyName',
            'flag_emoji': 'FlagEmoji',
            'flag_unicode': 'FlagUnicode'
        }

    def _load_data(self) -> List[Dict[str, Any]]:
        """Load country data from JSON file."""
        data_file = os.path.join(os.path.dirname(__file__), 'data', 'country.json')
        with open(data_file, 'r', encoding='utf-8') as f:
            return json.load(f)

    def get(self, **kwargs) -> List[Dict[str, Any]]:
        """
        Get country information based on provided parameters.

        Args:
            **kwargs: One or more search parameters (e.g., name="India", alpha2_code="IN")
                     See _field_mapping for all supported parameters.

        Returns:
            List[Dict[str, Any]]: List of country information dictionaries that match the criteria.
            Returns an empty list if no matches are found.

        Raises:
            ValueError: If no search parameter is provided or if an invalid parameter is used
        """
        if not kwargs:
            raise ValueError("At least one search parameter must be provided")

        results = []
        for param, value in kwargs.items():
            if param not in self._field_mapping:
                raise ValueError(f"Invalid parameter: {param}")

            field_name = self._field_mapping[param]
            results = [
                country for country in self._data
                if str(country.get(field_name, '')).lower() == str(value).lower()
            ]
            break  # Only use the first parameter for searching

        return results
