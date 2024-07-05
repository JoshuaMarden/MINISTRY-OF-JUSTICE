import csv
import requests
from pprint import pprint
# A team of analysts wish to discover how far people are travelling to their nearest
# desired court. We have provided you with a small test dataset so you can find out if
# it is possible to give the analysts the data they need to do this. The data is in
# `people.csv` and contains the following columns:
# - person_name
# - home_postcode
# - looking_for_court_type

# The courts and tribunals finder API returns a list of the 10 nearest courts to a
# given postcode. The output is an array of objects in JSON format. The API is
# accessed by including the postcode of interest in a URL. For example, accessing
# https://www.find-court-tribunal.service.gov.uk/search/results.json?postcode=E144PU gives
# the 10 nearest courts to the postcode E14 4PU. Visit the link to see an example of
# the output.

# Below is the first element of the JSON array from the above API call. We only want the
# following keys from the json:
# - name
# - dx_number
# - distance
# dx_number is not always returned and the "types" field can be empty.


# Use this API and the data in people.csv to determine how far each person's nearest
# desired court is. Generate an output (of whatever format you feel is appropriate)
# showing, for each person:
# - name
# - type of court desired
# - home postcode
# - nearest court of the right type
# - the dx_number (if available) of the nearest court of the right type
# - the distance to the nearest court of the right type


def csv_to_dict(file_path: str) -> list[dict]:
    """returns csv as a list of dicts"""
    with open(file_path, mode='r', newline='', encoding='utf-8') as csv_file:
        reader = csv.DictReader(csv_file)
        return [row for row in reader]

def courts_for_postcode(postcode: str) -> list[dict]:
    """Takes a postcode and returns list of local courts"""
    url = f"https://www.find-court-tribunal.service.gov.uk/search/results.json?postcode={
        postcode}"

    response = requests.get(url)
    if response.status_code == 200:
        body = response.json()

    return body

def check_court_type(person: dict, court: dict) -> bool:
    """checks if a persons desired court matches the given court"""
    return True if person.get('looking_for_court_type')\
        in court['types'] else False

def filter_court_data(court: dict) -> dict:
    """filters extraneous K:V pairs from a court dictionary"""
    desired_keys = ["dx_number", "distance", "name"]

    clean_dict = {}
    for key, value in court.items():
        if key in desired_keys:
            clean_dict[key] = value

    if desired_keys[0] not in court:
        clean_dict[desired_keys[0]] = "N/A"

    return clean_dict


def sort_courts(courts: list[dict]) -> list[dict]:
    """sorts list of court dict so closest are at the top"""
    sort_key = "distance"
    return sorted(courts, key=lambda x: x[sort_key])




if __name__ == "__main__":

    people = csv_to_dict("people.csv")

    court_matches = []

    for person in people:

        local_courts = courts_for_postcode(person["home_postcode"])

        # Please forgive the nesting, this is a devlopment area for me.
        correct_courts = [court for court in local_courts\
                          if check_court_type(person, court)]


        correct_courts = [filter_court_data(court) for court in correct_courts]

        correct_court = sort_courts(correct_courts)[0]
        correct_court['persons name'] = person["person_name"]
        correct_court['desired court type'] = person["looking_for_court_type"]

        court_matches.append(correct_court)

    for court in court_matches:
        print("---")
        pprint(court)
