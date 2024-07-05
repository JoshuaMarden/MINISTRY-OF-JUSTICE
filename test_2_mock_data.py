"""Mock data for unit tests testing second assessment task"""
import pytest

@pytest.fixture
def mock_courts():
    """mock courts from api"""
    return [
        {
            "name": "Close Tribunal",
            "lat": 51.5063346382936,
            "lon": -0.0261344650867725,
            "number": None,
            "cci_code": None,
            "magistrate_code": None,
            "slug": "mock_court",
            "types": ["Tribunal"],
            "dx_number": "1.1",
            "distance": 0.02,
        },
        {
            "name": "Distant Tribunal",
            "lat": 51.5063346382936,
            "lon": -0.0261344650867725,
            "number": None,
            "cci_code": None,
            "magistrate_code": None,
            "slug": "mock_court",
            "types": ["Tribunal"],
            "dx_number": "1.2",
            "distance": 100,
        },
        {
            "name": "Close Crown Court",
            "lat": 51.5063346382936,
            "lon": -0.0261344650867725,
            "number": None,
            "cci_code": None,
            "magistrate_code": None,
            "slug": "mock_court",
            "types": ["Crown Court"],
            "dx_number": "1.1",
            "distance": 0.01,
        },
        {
            "name": "Distant Crown Court",
            "lat": 51.5063346382936,
            "lon": -0.0261344650867725,
            "number": None,
            "cci_code": None,
            "magistrate_code": None,
            "slug": "mock_court",
            "types": ["Crown Court"],
            "dx_number": "1.2",
            "distance": 99,
        },
        {
            "name": "Mcdonalds",
            "lat": 51.5063346382936,
            "lon": -0.0261344650867725,
            "number": None,
            "cci_code": None,
            "magistrate_code": None,
            "slug": "mock_court",
            "types": ["Kangaroo Court"],
            "dx_number": "-100",
            "distance": 38,
        }
    ]

@pytest.fixture
def mock_people():
    """mock people from CSV"""
    return [
        {
            'person_name': 'Captain Birdseye',
            'home_postcode': 'ATS34',
            'looking_for_court_type': 'Crown Court'
        },
        {
            'person_name': 'JD Weatherspoons',
            'home_postcode': '1NPU8',
            'looking_for_court_type': 'Tribunal'
        }
    ]

@pytest.fixture
def mock_closest_courts():
    """mock people from CSV"""
    return [
    {'desired court type': 'Crown Court',
    'distance': 0.01,
    'dx_number': '1.1',
    'name': 'Close Crown Court',
    'persons name': 'Captain Birdseye'},

    {'desired court type': 'Tribunal',
    'distance': 0.02,
    'dx_number': '1.1',
    'name': 'Close Tribunal',
    'persons name': 'JD Weatherspoons'}
    ]