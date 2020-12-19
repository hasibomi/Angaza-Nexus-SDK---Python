import requests
from typing import Any, Dict
from. base import Base


class Angaza(Base):
    def get_usage_data(self, unit_number: int, from_when_dt: str, to_when_dt: str = None, sample_type: str=None, offset: int=0) -> Dict[str, Any]:
        """
        Retrieve a unit's usage data samples that have been previously recorded with Angaza.
        Filter by sample time. Restricted to a one month maximum range per request.

        Args:
            unit_number (int): Angaza-unique unit identifier.
            from_when_dt (str): ISO-formatted UTC datetime of first sample that should be returned.
                All samples from that time forward will be returned.
            to_when_dt (str): ISO-formatted UTC datetime of last sample that should be returned.
                No samples newer than to_when_dt will be returned.
            sample_type (str): Corresponds to a unique sample type, for example, battery voltage for a particular product.
                Sample types must be specified with Angaza.
            offset (int): Starting position in logical sequence of results returned by query. 

        Returns:
            Dict[str, Any]
        """

        url = self.url('usage_data')
        params = {
            'offset': offset,
            'unit_number': unit_number,
            'from_when_dt': from_when_dt
        }

        if to_when_dt is not None:
            params['to_when_dt'] = to_when_dt

        if sample_type is not None:
            params['type'] = sample_type

        request = requests.get(url, auth=(self._username, self._password), params=params)

        return request.json()
