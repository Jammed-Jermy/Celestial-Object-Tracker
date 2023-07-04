#############################################################################################################################################################################################################
THIS PROGRAM IS NOT FINISHED YET, I WILL BE UPDATING THE NEW VERISONS OF THE PROGRAM, SOME FEATURES MAY NOT WORK
############################################################################################################################################################################################################
# Celestial Object Tracker

This project is a Python program that allows you to track and obtain information about celestial objects such as the Sun, Moon, planets, and more. It utilizes the `ephem` module to perform calculations and provide accurate data.

## Prerequisites

Before running this program, make sure you have the following modules installed:

- `ephem`
- `math`
- `webbrowser`
- `time`
- `datetime`
- `pandas`

You can install these modules using pip:

```
pip install ephem math webbrowser pandas
```

## Getting Started

To use this program, follow the steps below:

1. Clone the repository or download the source code.
2. Open the Python file (`celestial_object_tracker.py`) in a text editor or an IDE.

## Setting Up Your Observer's Location

In the code, you will find placeholders for the coordinates of your observer's location. Replace the `'enter_cordinates'` placeholders with the latitude and longitude of your desired location. Make sure to provide the coordinates in decimal degrees format.

Example:
```python
observer.lon = '12.3456'  # Replace with the actual longitude
observer.lat = '34.5678'  # Replace with the actual latitude
```

## Running the Program

To run the program, execute the Python script (`celestial_object_tracker.py`) using the Python interpreter. You can do this by running the following command in your terminal or command prompt:

```
python celestial_object_tracker.py
```

Once the program starts, you will be presented with a menu of options. Choose the desired option by entering the corresponding number.

- Option 1: Check Position - Enter the name of a celestial body to obtain its current position.
- Option 2: Track Position - Track the position of a celestial body for a specific duration.
- Option 3: Sunset Time - Calculate and display the time until sunset.
- Option 4: Sunrise Time - Calculate and display the time until sunrise.
- Option 5: All Planets Visibility - Show a table with the visibility of all planets.
- Option 6: Exit - Terminate the program.

Follow the prompts and provide the necessary inputs to retrieve the desired information.

## Contributing

Contributions to this project are not accepted at the moment.

## License

This project is not licensed.

---

Feel free to customize and modify the code according to your specific requirements.
