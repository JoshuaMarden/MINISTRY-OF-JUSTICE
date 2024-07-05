import pytest
from test_2 import *
from test_2_mock_data import *

def test_import_csv(mock_people):
    result = csv_to_dict("mock_people.csv")
    expected = mock_people

    assert result == expected

def test_get_correct_court(mock_people, mock_courts, mock_closest_courts):
    """A *very* broad test so I can check I am returning the 
    correct courts. If I had more time this would be many small
    tests"""


    people = mock_people
    expected = mock_closest_courts

    court_matches = []

    for person in people:

        local_courts = mock_courts

        correct_courts = [court for court in local_courts\
                          if check_court_type(person, court)]


        correct_courts = [filter_court_data(court) for court in correct_courts]

        correct_court = sort_courts(correct_courts)[0]
        correct_court['persons name'] = person["person_name"]
        correct_court['desired court type'] = person["looking_for_court_type"]

        court_matches.append(correct_court)

    result = court_matches
    assert expected == result

