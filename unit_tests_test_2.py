"""Unit tests for second test"""
from test_2 import *
from test_2_mock_data import *

def test_import_csv(mock_people):
    """check import people from csv works"""
    result = csv_to_dict("mock_people.csv")
    expected = mock_people

    assert result == expected

def test_get_correct_court(mock_people, mock_courts, mock_closest_courts):
    """A *very* broad test so I can check I am returning the 
    correct courts. If I had more time this would be many small
    tests"""


    local_mock_people = mock_people
    expected = mock_closest_courts

    mock_court_matches = []

    for mock_person in local_mock_people:

        mock_local_courts = mock_courts

        mock_correct_courts = [court for court in mock_local_courts\
                          if check_court_type(mock_person, court)]


        mock_correct_courts = [filter_court_data(court) for court in mock_correct_courts]

        mock_correct_court = sort_courts(mock_correct_courts)[0]
        mock_correct_court['persons name'] =\
            mock_person["person_name"]
        mock_correct_court['desired court type'] =\
            mock_person["looking_for_court_type"]

        mock_court_matches.append(mock_correct_court)

    result = mock_court_matches
    assert expected == result
