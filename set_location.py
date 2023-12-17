import requests

headers = {
    'user-agent': 'Mozilla/5.0 (Macintosh; Intel Mac OS X 10_11_6) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/56.0.2924.87 Safari/537.36',
}

def get_state_id(state):
    response = requests.get("https://cdn-api.co-vin.in/api/v2/admin/location/states", headers=headers)
    states_data = response.json()["states"]
    for state_data in states_data:
        if state_data["state_name"].lower() == state.lower():
            return state_data["state_id"]

def get_district_id(state_id, district):
    response = requests.get("https://cdn-api.co-vin.in/api/v2/admin/location/districts/{}".format(state_id), headers=headers)
    districts_data = response.json()["districts"]
    for district_data in districts_data:
        if district_data["district_name"].lower() == district.lower():
            return district_data["district_id"]

if __name__ == '__main__':
    state = input("Enter state name: ")
    district = input("Enter district name: ")
    state_id = get_state_id(state)
    district_id = get_district_id(state_id, district)
    if district_id:
        with open("location.txt", "w") as file:
            file.write(str(district_id))
    else:
        print("Invalid input!")
