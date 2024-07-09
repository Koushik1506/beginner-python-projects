import requests

city = input("Enter city to proceed with: ").capitalize()
try:
    info = requests.get(f"http://api.weatherapi.com/v1/current.json?key=fa8202fb2db346fc8a6124127240907&q={city}&aqi=no")
    w_info = info.json()
    dic_keys = []
    for keys in w_info.keys():
        dic_keys.append(keys)
    choice = input("Enter Option to Proceed\n1.Location Details\n2.Current Weather Details\n")
    match choice:
        case "1":
            for location_details in w_info[f"{dic_keys[0]}"]:
                print(f"{location_details} : {w_info[f"{dic_keys[0]}"][f"{location_details}"]}")

        case "2":
            for weather_details in w_info[f"{dic_keys[1]}"]:
                print(f"{weather_details} : {w_info[f"{dic_keys[1]}"][f"{weather_details}"]}")
except requests.ConnectionError as error:
    print(error)
