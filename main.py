# from flask import Flask
# import socket
# import psutil
# import os

# app = Flask(__name__)

# def get_ip_address():
#     hostname = socket.gethostname()
#     ip_address = socket.gethostbyname(hostname)
#     return ip_address

# def get_battery_charge():
#     battery = psutil.sensors_battery()
#     if battery is not None:
#         return battery.percent
#     else:
#         return None

# def get_first_photo_in_downloads():
#     downloads_path = os.path.expanduser("~/Downloads")  # Get the path to the Downloads folder
#     files = os.listdir(downloads_path)  # List all files in the Downloads folder

#     # Filter out only image files (you can add more extensions as needed)
#     image_files = [f for f in files if f.lower().endswith(('.png', '.jpg', '.jpeg', '.gif'))]

#     if image_files:
#         first_photo_path = os.path.join(downloads_path, image_files[0])
#         return first_photo_path
#     else:
#         return None

# def ff():
#     final_charge = get_battery_charge()
#     first_photo = get_first_photo_in_downloads()
#     if final_charge is not None:
#         return f"Final Battery Charge: {final_charge}%, First Photo: {first_photo}"
#     else:
#         return "<img src={first_photo}/>"

# @app.route('/')
# def home():
#     return ff()
# if __name__ == "__main__":
#     app.run(debug=True)

# from flask import Flask, render_template
# import os

# app = Flask(__name__)

# def get_first_photo_in_downloads():
#     downloads_path = os.path.expanduser("~/Downloads")  # Get the path to the Downloads folder
#     files = os.listdir(downloads_path)  # List all files in the Downloads folder

#     # Filter out only image files (you can add more extensions as needed)
#     image_files = [f for f in files if f.lower().endswith(('.png', '.jpg', '.jpeg', '.gif'))]

#     if image_files:
#         first_photo_path = os.path.join(downloads_path, image_files[0])
#         return first_photo_path
#     else:
#         return None

# @app.route('/')
# def home():
#     first_photo_path = get_first_photo_in_downloads()
#     return render_template("index.html", first_photo_path=first_photo_path)

# if __name__ == "__main__":
#     app.run(debug=True)

# from flask import Flask, render_template, request
# from geopy.geocoders import Nominatim

# app = Flask(__name__)

# def get_current_location(ip_address):
#     geolocator = Nominatim(user_agent="my_app")
#     try:
#         location = geolocator.geocode(ip_address)
#         return location
#     except Exception as e:
#         print(f"Error getting location: {str(e)}")
#         return None

# @app.route('/')
# @app.route('/home')
# def home():
#     ip_address = request.remote_addr  # Get the IP address from the request
#     location = get_current_location(ip_address)
#     if location:
#         return render_template("index.html", location=location)
#     else:
#         return "Location not found."

# if __name__ == "__main__":
#     app.run(debug=True)

# from flask import Flask, render_template

# app = Flask(__name__)

# @app.route('/')
# def home():
#     return render_template("index.html")

# if __name__ == "__main__":
#     app.run(debug=True)

# from flask import Flask, render_template
# import requests

# app = Flask(__name__)

# def get_location_from_ip():
#     try:
#         # Get public IP address of the user
#         response = requests.get('https://api.ipify.org?format=json')
#         data = response.json()
#         print(data)
#         ip_address = data['ip']

#         # Use a geolocation service to get the approximate location based on the IP address
#         response = requests.get(f'http://ip-api.com/json/{ip_address}')
#         data = response.json()

#         # Extract relevant location information
#         country = data['country']
#         city = data['city']
#         latitude = data['lat']
#         longitude = data['lon']

#         return {
#             'country': country,
#             'city': city,
#             'latitude': latitude,
#             'longitude': longitude
#         }
#     except Exception as e:
#         print(f"Error getting location: {e}")
#         return None

from flask import Flask, render_template
import os

app = Flask(__name__)

def power_off():
    if os.name == 'posix':  # For Unix-based systems
        print("Shutting down Unix-based system.")
        return os.system('sudo shutdown -h now')  # Execute the shutdown command with superuser privileges
    elif os.name == 'nt':  # For Windows
        print("Shutting down Windows system.")
        return os.system('shutdown /s /t 1')  # Execute the shutdown command
    else:
        print("Power off command is not supported on this platform.")
        return "Power off command is not supported on this platform."

@app.route('/')
@app.route('/home')
def home():
    return render_template("index.html")  # Render the index.html template

@app.route('/shutdown')
def shutdown():
    result = power_off()
    return f"Shutting down... Result: {result}"

if __name__ == "__main__":
    app.run(debug=True)




