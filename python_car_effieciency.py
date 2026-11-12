from collections import OrderedDict
import matplotlib.pyplot as plt


# ============================================================
# CAR DATABASE
# ============================================================

cars = {
    "Mahindra Thar Roxx": {
        "fuel_type": "Diesel",
        "tank": 57,
        "mileage": 15.20,
        "weight": 1900,
        "max_passengers": 5,
        "max_luggage": 100,      # Project limit - replace with actual value
        "max_speed": 200         # Project input limit - replace if required
    },

    "Tata Sierra": {
        "fuel_type": "Petrol",
        "tank": 50,
        "mileage": 14.00,
        "weight": 1750,
        "max_passengers": 5,
        "max_luggage": 100,
        "max_speed": 200
    },

    "Maruti Suzuki Victoris": {
        "fuel_type": "Petrol",
        "tank": 45,
        "mileage": 21.18,
        "weight": 1200,
        "max_passengers": 5,
        "max_luggage": 100,
        "max_speed": 200
    },

    "Hyundai Creta": {
        "fuel_type": "Petrol",
        "tank": 50,
        "mileage": 17.40,
        "weight": 1450,
        "max_passengers": 5,
        "max_luggage": 100,
        "max_speed": 200
    },

    "Kia Seltos": {
        "fuel_type": "Petrol",
        "tank": 50,
        "mileage": 17.00,
        "weight": 1450,
        "max_passengers": 5,
        "max_luggage": 100,
        "max_speed": 200
    },

    "Toyota Innova Hycross": {
        "fuel_type": "Petrol Hybrid",
        "tank": 52,
        "mileage": 23.24,
        "weight": 1700,
        "max_passengers": 7,
        "max_luggage": 100,
        "max_speed": 200
    },

    "Tata Curvv": {
        "fuel_type": "Petrol",
        "tank": 44,
        "mileage": 14.00,
        "weight": 1500,
        "max_passengers": 5,
        "max_luggage": 100,
        "max_speed": 200
    },

    "Tata Nexon": {
        "fuel_type": "Petrol",
        "tank": 44,
        "mileage": 17.44,
        "weight": 1300,
        "max_passengers": 5,
        "max_luggage": 100,
        "max_speed": 200
    },

    "Mahindra XUV 3XO": {
        "fuel_type": "Petrol",
        "tank": 42,
        "mileage": 18.20,
        "weight": 1400,
        "max_passengers": 5,
        "max_luggage": 100,
        "max_speed": 200
    },

    "Maruti Suzuki Swift": {
        "fuel_type": "Petrol",
        "tank": 37,
        "mileage": 24.80,
        "weight": 900,
        "max_passengers": 5,
        "max_luggage": 100,
        "max_speed": 200
    },

    "Maruti Suzuki Baleno": {
        "fuel_type": "Petrol",
        "tank": 37,
        "mileage": 22.35,
        "weight": 960,
        "max_passengers": 5,
        "max_luggage": 100,
        "max_speed": 180
    },

    "Maruti Suzuki Brezza": {
        "fuel_type": "Petrol",
        "tank": 48,
        "mileage": 20.51,
        "weight": 1150,
        "max_passengers": 5,
        "max_luggage": 100,
        "max_speed": 180
    },

    "Maruti Suzuki Dzire": {
        "fuel_type": "Petrol",
        "tank": 37,
        "mileage": 24.80,
        "weight": 950,
        "max_passengers": 5,
        "max_luggage": 100,
        "max_speed": 180
    },

    "Maruti Suzuki Ertiga": {
        "fuel_type": "Petrol",
        "tank": 45,
        "mileage": 20.51,
        "weight": 1150,
        "max_passengers": 7,
        "max_luggage": 120,
        "max_speed": 180
    },

    "Maruti Suzuki Grand Vitara": {
        "fuel_type": "Petrol Hybrid",
        "tank": 45,
        "mileage": 21.11,
        "weight": 1250,
        "max_passengers": 5,
        "max_luggage": 100,
        "max_speed": 180
    },

    "Maruti Suzuki Fronx": {
        "fuel_type": "Petrol",
        "tank": 37,
        "mileage": 21.79,
        "weight": 970,
        "max_passengers": 5,
        "max_luggage": 100,
        "max_speed": 180
    },

    "Maruti Suzuki Wagon R": {
        "fuel_type": "Petrol",
        "tank": 32,
        "mileage": 24.35,
        "weight": 850,
        "max_passengers": 5,
        "max_luggage": 80,
        "max_speed": 160
    },

    "Maruti Suzuki Alto K10": {
        "fuel_type": "Petrol",
        "tank": 27,
        "mileage": 24.39,
        "weight": 760,
        "max_passengers": 5,
        "max_luggage": 70,
        "max_speed": 145
    },

    "Maruti Suzuki Celerio": {
        "fuel_type": "Petrol",
        "tank": 32,
        "mileage": 25.24,
        "weight": 825,
        "max_passengers": 5,
        "max_luggage": 70,
        "max_speed": 150
    },

    "Maruti Suzuki XL6": {
        "fuel_type": "Petrol",
        "tank": 45,
        "mileage": 20.97,
        "weight": 1200,
        "max_passengers": 6,
        "max_luggage": 100,
        "max_speed": 180
    },


    "Hyundai Venue": {
        "fuel_type": "Petrol",
        "tank": 45,
        "mileage": 18.27,
        "weight": 1100,
        "max_passengers": 5,
        "max_luggage": 100,
        "max_speed": 180
    },

    "Hyundai Exter": {
        "fuel_type": "Petrol",
        "tank": 37,
        "mileage": 19.40,
        "weight": 1000,
        "max_passengers": 5,
        "max_luggage": 80,
        "max_speed": 165
    },

    "Hyundai Verna": {
        "fuel_type": "Petrol",
        "tank": 45,
        "mileage": 18.60,
        "weight": 1300,
        "max_passengers": 5,
        "max_luggage": 100,
        "max_speed": 200
    },

    "Hyundai i20": {
        "fuel_type": "Petrol",
        "tank": 37,
        "mileage": 20.35,
        "weight": 1050,
        "max_passengers": 5,
        "max_luggage": 80,
        "max_speed": 180
    },

    "Hyundai Alcazar": {
        "fuel_type": "Petrol",
        "tank": 50,
        "mileage": 17.50,
        "weight": 1600,
        "max_passengers": 7,
        "max_luggage": 120,
        "max_speed": 190
    },


    "Tata Punch": {
        "fuel_type": "Petrol",
        "tank": 37,
        "mileage": 18.97,
        "weight": 1100,
        "max_passengers": 5,
        "max_luggage": 80,
        "max_speed": 170
    },

    "Tata Altroz": {
        "fuel_type": "Petrol",
        "tank": 37,
        "mileage": 19.33,
        "weight": 1050,
        "max_passengers": 5,
        "max_luggage": 80,
        "max_speed": 175
    },

    "Tata Tiago": {
        "fuel_type": "Petrol",
        "tank": 35,
        "mileage": 19.00,
        "weight": 950,
        "max_passengers": 5,
        "max_luggage": 70,
        "max_speed": 165
    },

    "Tata Tigor": {
        "fuel_type": "Petrol",
        "tank": 35,
        "mileage": 19.28,
        "weight": 1000,
        "max_passengers": 5,
        "max_luggage": 80,
        "max_speed": 165
    },

    "Tata Harrier": {
        "fuel_type": "Diesel",
        "tank": 50,
        "mileage": 16.80,
        "weight": 1700,
        "max_passengers": 5,
        "max_luggage": 120,
        "max_speed": 190
    },

    "Tata Safari": {
        "fuel_type": "Diesel",
        "tank": 50,
        "mileage": 16.30,
        "weight": 1800,
        "max_passengers": 7,
        "max_luggage": 120,
        "max_speed": 190
    },


    "Mahindra Scorpio N": {
        "fuel_type": "Diesel",
        "tank": 57,
        "mileage": 15.42,
        "weight": 1900,
        "max_passengers": 7,
        "max_luggage": 120,
        "max_speed": 165
    },

    "Mahindra XUV700": {
        "fuel_type": "Diesel",
        "tank": 60,
        "mileage": 17.00,
        "weight": 1800,
        "max_passengers": 7,
        "max_luggage": 120,
        "max_speed": 190
    },

    "Mahindra Bolero Neo": {
        "fuel_type": "Diesel",
        "tank": 50,
        "mileage": 17.29,
        "weight": 1600,
        "max_passengers": 7,
        "max_luggage": 120,
        "max_speed": 140
    },

    "Mahindra Thar": {
        "fuel_type": "Diesel",
        "tank": 57,
        "mileage": 15.20,
        "weight": 1800,
        "max_passengers": 4,
        "max_luggage": 80,
        "max_speed": 165
    },

    "Mahindra Bolero": {
        "fuel_type": "Diesel",
        "tank": 60,
        "mileage": 16.00,
        "weight": 1650,
        "max_passengers": 7,
        "max_luggage": 120,
        "max_speed": 135
    },


    "Kia Sonet": {
        "fuel_type": "Petrol",
        "tank": 45,
        "mileage": 18.60,
        "weight": 1200,
        "max_passengers": 5,
        "max_luggage": 100,
        "max_speed": 180
    },

    "Kia Carens Clavis": {
        "fuel_type": "Petrol",
        "tank": 45,
        "mileage": 18.40,
        "weight": 1550,
        "max_passengers": 7,
        "max_luggage": 120,
        "max_speed": 180
    },

    "Kia Syros": {
        "fuel_type": "Petrol",
        "tank": 45,
        "mileage": 18.00,
        "weight": 1250,
        "max_passengers": 5,
        "max_luggage": 100,
        "max_speed": 180
    },


    "Toyota Urban Cruiser Hyryder": {
        "fuel_type": "Petrol Hybrid",
        "tank": 45,
        "mileage": 21.12,
        "weight": 1250,
        "max_passengers": 5,
        "max_luggage": 100,
        "max_speed": 175
    }
}


# ============================================================
# ORDERED DICTIONARY
# ============================================================

# Every calculation is stored in the order it was performed.
previous_results = OrderedDict()


# ============================================================
# INPUT VALIDATION
# ============================================================

def get_float(prompt, minimum=None, maximum=None):

    while True:

        try:
            value = float(input(prompt))

            if minimum is not None and value < minimum:
                print(f"Invalid input. Value must be at least {minimum}.")
                continue

            if maximum is not None and value > maximum:
                print(f"Invalid input. Value must not exceed {maximum}.")
                continue

            return value

        except ValueError:
            print("Invalid input. Please enter a number.")


def get_int(prompt, minimum=None, maximum=None):

    while True:

        try:
            value = int(input(prompt))

            if minimum is not None and value < minimum:
                print(f"Invalid input. Value must be at least {minimum}.")
                continue

            if maximum is not None and value > maximum:
                print(f"Invalid input. Value must not exceed {maximum}.")
                continue

            return value

        except ValueError:
            print("Invalid input. Please enter a whole number.")


def get_choice(prompt, choices):

    choices_lower = [choice.lower() for choice in choices]

    while True:

        value = input(prompt).strip().lower()

        if value in choices_lower:
            return value

        print("Invalid input.")
        print("Choose from:", ", ".join(choices))


# ============================================================
# FUEL EFFICIENCY CALCULATION
# ============================================================

def calculate_efficiency(
    car,
    passengers,
    luggage,
    speed,
    driving_condition,
    ac,
    service,
    road
):

    factor = 1.0


    # --------------------------------------------------------
    # PASSENGER LOAD
    # --------------------------------------------------------

    if passengers >= 4:
        factor -= 0.05

    elif passengers >= 2:
        factor -= 0.02


    # --------------------------------------------------------
    # LUGGAGE
    # --------------------------------------------------------

    if luggage > 100:
        factor -= 0.05

    elif luggage > 50:
        factor -= 0.02


    # --------------------------------------------------------
    # DRIVING CONDITION
    # --------------------------------------------------------

    if driving_condition == "city":
        factor -= 0.15

    elif driving_condition == "highway":
        factor += 0.05

    elif driving_condition == "mixed":
        factor -= 0.05


    # --------------------------------------------------------
    # SPEED
    # --------------------------------------------------------

    if speed > 100:
        factor -= 0.10

    elif speed < 40:
        factor -= 0.05


    # --------------------------------------------------------
    # AC
    # --------------------------------------------------------

    if ac == "on":
        factor -= 0.05


    # --------------------------------------------------------
    # SERVICE CONDITION
    # --------------------------------------------------------

    if service == "average":
        factor -= 0.05

    elif service == "poor":
        factor -= 0.10


    # --------------------------------------------------------
    # ROAD CONDITION
    # --------------------------------------------------------

    if road == "average":
        factor -= 0.05

    elif road == "poor":
        factor -= 0.10


    # Prevent efficiency factor from becoming zero/negative

    factor = max(factor, 0.10)


    adjusted_mileage = car["mileage"] * factor

    return adjusted_mileage


# ============================================================
# COMPLETE CALCULATION
# ============================================================

def calculate_result(
    car,
    fuel,
    distance,
    passengers,
    luggage,
    speed,
    driving_condition,
    fuel_price,
    driving_time,
    ac,
    service,
    road
):

    adjusted_mileage = calculate_efficiency(
        car,
        passengers,
        luggage,
        speed,
        driving_condition,
        ac,
        service,
        road
    )


    fuel_consumed = distance / adjusted_mileage

    remaining_fuel = fuel - fuel_consumed

    driving_range = fuel * adjusted_mileage

    fuel_cost = fuel_consumed * fuel_price

    cost_per_km = fuel_cost / distance

    calculated_travel_time = distance / speed


    # --------------------------------------------------------
    # FUEL STATUS
    # --------------------------------------------------------

    if remaining_fuel < 0:
        status = "Insufficient"

    elif remaining_fuel < car["tank"] * 0.20:
        status = "Low"

    else:
        status = "Sufficient"


    # --------------------------------------------------------
    # STORE RESULTS IN ORDERED DICTIONARY
    # --------------------------------------------------------

    result = OrderedDict([

        ("Adjusted Efficiency",
         round(adjusted_mileage, 2)),

        ("Fuel Consumed",
         round(fuel_consumed, 2)),

        ("Remaining Fuel",
         round(max(remaining_fuel, 0), 2)),

        ("Driving Range",
         round(driving_range, 2)),

        ("Fuel Cost",
         round(fuel_cost, 2)),

        ("Cost per km",
         round(cost_per_km, 2)),

        ("Calculated Travel Time",
         round(calculated_travel_time, 2)),

        ("User Entered Driving Time",
         round(driving_time, 2)),

        ("Fuel Status",
         status)
    ])


    return result


# ============================================================
# CONDITION GRAPH
# ============================================================

def plot_condition_analysis(
    car,
    car_name,
    passengers,
    luggage,
    speed,
    driving_condition,
    ac,
    service,
    road
):

    labels = []
    efficiencies = []


    # --------------------------------------------------------
    # FUNCTION TO ADD A CONDITION TO GRAPH
    # --------------------------------------------------------

    def add_case(
        label,
        passenger_value,
        luggage_value,
        speed_value,
        driving_value,
        ac_value,
        service_value,
        road_value
    ):

        efficiency = calculate_efficiency(

            car,

            passenger_value,

            luggage_value,

            speed_value,

            driving_value,

            ac_value,

            service_value,

            road_value
        )

        labels.append(label)
        efficiencies.append(efficiency)


    # --------------------------------------------------------
    # USER'S ACTUAL CONDITION
    # --------------------------------------------------------

    user_efficiency = calculate_efficiency(

        car,
        passengers,
        luggage,
        speed,
        driving_condition,
        ac,
        service,
        road
    )


    add_case(

        "USER CASE",

        passengers,
        luggage,
        speed,
        driving_condition,
        ac,
        service,
        road
    )


    # --------------------------------------------------------
    # DRIVING CONDITIONS
    # --------------------------------------------------------

    for condition in ["city", "mixed", "highway"]:

        add_case(

            f"Driving: {condition.title()}",

            passengers,
            luggage,
            speed,

            condition,

            ac,
            service,
            road
        )


    # --------------------------------------------------------
    # SERVICE CONDITIONS
    # --------------------------------------------------------

    for condition in ["good", "average", "poor"]:

        add_case(

            f"Service: {condition.title()}",

            passengers,
            luggage,
            speed,

            driving_condition,

            ac,

            condition,

            road
        )


    # --------------------------------------------------------
    # ROAD CONDITIONS
    # --------------------------------------------------------

    for condition in ["good", "average", "poor"]:

        add_case(

            f"Road: {condition.title()}",

            passengers,
            luggage,
            speed,

            driving_condition,

            ac,
            service,

            condition
        )


    # --------------------------------------------------------
    # AC
    # --------------------------------------------------------

    for ac_condition in ["off", "on"]:

        add_case(

            f"AC: {ac_condition.upper()}",

            passengers,
            luggage,
            speed,

            driving_condition,

            ac_condition,

            service,
            road
        )


    # --------------------------------------------------------
    # PASSENGER LOAD
    # --------------------------------------------------------

    passenger_cases = [

        ("Passengers: 0",
         0),

        ("Passengers: 2",
         min(2, car["max_passengers"])),

        (f"Passengers: {car['max_passengers']}",
         car["max_passengers"])
    ]


    for label, passenger_count in passenger_cases:

        add_case(

            label,

            passenger_count,

            luggage,
            speed,

            driving_condition,

            ac,
            service,
            road
        )


    # --------------------------------------------------------
    # LUGGAGE LOAD
    # --------------------------------------------------------

    luggage_cases = [

        ("Luggage: 0 kg",
         0),

        ("Luggage: 50 kg",
         min(50, car["max_luggage"])),

        (f"Luggage: {car['max_luggage']} kg",
         car["max_luggage"])
    ]


    for label, luggage_weight in luggage_cases:

        add_case(

            label,

            passengers,

            luggage_weight,

            speed,

            driving_condition,

            ac,
            service,
            road
        )


    # --------------------------------------------------------
    # SPEED
    # --------------------------------------------------------

    speed_cases = [40, 60, 80, 100, 120]


    for test_speed in speed_cases:

        if test_speed <= car["max_speed"]:

            add_case(

                f"Speed: {test_speed} km/h",

                passengers,
                luggage,

                test_speed,

                driving_condition,

                ac,
                service,
                road
            )


    # --------------------------------------------------------
    # REMOVE DUPLICATE LABELS
    # --------------------------------------------------------

    unique_data = OrderedDict()


    for label, efficiency in zip(
        labels,
        efficiencies
    ):

        if label not in unique_data:
            unique_data[label] = efficiency


    labels = list(unique_data.keys())

    efficiencies = list(unique_data.values())


    # --------------------------------------------------------
    # CALCULATE DEVIATION FROM USER CASE
    # --------------------------------------------------------

    deviations = []


    for efficiency in efficiencies:

        deviation = (
            (efficiency - user_efficiency)
            / user_efficiency
        ) * 100

        deviations.append(deviation)


    # --------------------------------------------------------
    # DISPLAY TABLE
    # --------------------------------------------------------

    print("\n")
    print("=" * 70)
    print("          CONDITION-WISE FUEL EFFICIENCY ANALYSIS")
    print("=" * 70)

    for label, efficiency, deviation in zip(
        labels,
        efficiencies,
        deviations
    ):

        sign = "+" if deviation >= 0 else ""

        print(

            f"{label:<32}"

            f"{efficiency:>7.2f} km/L   "

            f"({sign}{deviation:.2f}% vs user case)"
        )

    print("=" * 70)


    # --------------------------------------------------------
    # GRAPH
    # --------------------------------------------------------

    plt.figure(figsize=(13, 10))


    bars = plt.barh(
        labels,
        efficiencies
    )


    # User-selected efficiency

    plt.axvline(

        user_efficiency,

        linestyle="--",

        linewidth=2,

        label=f"User Case = {user_efficiency:.2f} km/L"
    )


    # Rated vehicle efficiency

    plt.axvline(

        car["mileage"],

        linestyle=":",

        linewidth=2,

        label=f"Rated Efficiency = {car['mileage']:.2f} km/L"
    )


    plt.xlabel(
        "Fuel Efficiency (km/L)"
    )

    plt.ylabel(
        "Condition"
    )

    plt.title(

        f"Fuel Efficiency Variation\n"
        f"{car_name}"
    )


    plt.grid(
        axis="x",
        linestyle=":",
        alpha=0.5
    )


    plt.legend()


    # --------------------------------------------------------
    # ADD VALUES + DEVIATION TO BARS
    # --------------------------------------------------------

    for bar, efficiency, deviation in zip(
        bars,
        efficiencies,
        deviations
    ):

        sign = "+" if deviation >= 0 else ""

        plt.text(

            bar.get_width() + 0.05,

            bar.get_y()
            + bar.get_height() / 2,

            f"{efficiency:.2f} "
            f"({sign}{deviation:.1f}%)",

            va="center"
        )


    plt.tight_layout()

    plt.show()


# ============================================================
# DISPLAY A SAVED CALCULATION
# ============================================================

def display_saved_calculation(calculation_id):

    if calculation_id not in previous_results:

        print("\nCalculation not found.")

        return


    data = previous_results[calculation_id]


    print("\n")
    print("=" * 65)

    print(
        f"        STORED CALCULATION: {calculation_id}"
    )

    print("=" * 65)


    # --------------------------------------------------------
    # INPUTS
    # --------------------------------------------------------

    print("\nVehicle / Input Data")

    print("-" * 65)


    for key, value in data["Inputs"].items():

        print(
            f"{key:<28}: {value}"
        )


    # --------------------------------------------------------
    # RESULTS
    # --------------------------------------------------------

    print("\nCalculated Results")

    print("-" * 65)


    for key, value in data["Results"].items():

        print(
            f"{key:<28}: {value}"
        )


    print("=" * 65)


# ============================================================
# SHOW PREVIOUS CALCULATIONS
# ============================================================

def show_previous_calculations():

    if not previous_results:

        print("\nNo previous calculations stored.")

        return


    print("\n")
    print("=" * 65)

    print("                STORED CALCULATIONS")

    print("=" * 65)


    for calculation_id, data in previous_results.items():

        print(

            calculation_id,

            "->",

            data["Inputs"]["Car"],

            "|",

            data["Results"]["Adjusted Efficiency"],

            "km/L"
        )


    calculation_id = input(

        "\nEnter calculation ID "
        "(example: Calculation 1), "
        "or press Enter to cancel: "

    ).strip()


    if calculation_id:

        display_saved_calculation(
            calculation_id
        )


# ============================================================
# MAIN PROGRAM
# ============================================================

calculation_number = 1


while True:

    print("\n")
    print("=" * 65)

    print(
        "       CAR FUEL EFFICIENCY & DRIVING RANGE"
    )

    print("=" * 65)


    # --------------------------------------------------------
    # CAR SELECTION
    # --------------------------------------------------------

    print("\nAvailable Cars:")


    car_list = list(cars.keys())


    for i, car_name in enumerate(
        car_list,
        1
    ):

        print(
            i,
            ".",
            car_name
        )


    choice = get_int(

        f"\nSelect car number (1-{len(car_list)}): ",

        1,

        len(car_list)
    )


    car_name = car_list[
        choice - 1
    ]


    car = cars[car_name]


    # --------------------------------------------------------
    # DISPLAY VEHICLE INFORMATION
    # --------------------------------------------------------

    print("\nSelected Car:", car_name)

    print(
        "Fuel Type:",
        car["fuel_type"]
    )

    print(
        "Tank Capacity:",
        car["tank"],
        "L"
    )

    print(
        "Rated Efficiency:",
        car["mileage"],
        "km/L"
    )

    print(
        "Maximum Passengers:",
        car["max_passengers"]
    )

    print(
        "Project Luggage Limit:",
        car["max_luggage"],
        "kg"
    )


    # --------------------------------------------------------
    # USER INPUTS
    # --------------------------------------------------------

    fuel = get_float(

        f"\nInitial Fuel Level "
        f"(0-{car['tank']} L): ",

        0,

        car["tank"]
    )


    distance = get_float(

        "Distance to Travel (km): ",

        0.01
    )


    passengers = get_int(

        f"Number of Passengers "
        f"(0-{car['max_passengers']}): ",

        0,

        car["max_passengers"]
    )


    luggage = get_float(

        f"Luggage Weight "
        f"(0-{car['max_luggage']} kg): ",

        0,

        car["max_luggage"]
    )


    speed = get_float(

        f"Average Speed "
        f"(1-{car['max_speed']} km/h): ",

        1,

        car["max_speed"]
    )


    driving_condition = get_choice(

        "Driving Condition "
        "(City/Highway/Mixed): ",

        ["city", "highway", "mixed"]
    )


    fuel_price = get_float(

        "Fuel Price (₹/L): ",

        0.01
    )


    driving_time = get_float(

        "Driving Time (hours): ",

        0.01
    )


    ac = get_choice(

        "AC Usage (ON/OFF): ",

        ["on", "off"]
    )


    service = get_choice(

        "Vehicle Service Condition "
        "(Good/Average/Poor): ",

        ["good", "average", "poor"]
    )


    road = get_choice(

        "Road Condition "
        "(Good/Average/Poor): ",

        ["good", "average", "poor"]
    )


    # --------------------------------------------------------
    # CALCULATE USER-SPECIFIED RESULT
    # --------------------------------------------------------

    result = calculate_result(

        car,

        fuel,

        distance,

        passengers,

        luggage,

        speed,

        driving_condition,

        fuel_price,

        driving_time,

        ac,

        service,

        road
    )


    # --------------------------------------------------------
    # STORE ALL INPUTS IN ORDERED DICTIONARY
    # --------------------------------------------------------

    calculation_id = (
        f"Calculation {calculation_number}"
    )


    input_data = OrderedDict([

        ("Car", car_name),

        ("Fuel Type", car["fuel_type"]),

        ("Initial Fuel", f"{fuel} L"),

        ("Distance", f"{distance} km"),

        ("Passengers", passengers),

        ("Luggage", f"{luggage} kg"),

        ("Average Speed", f"{speed} km/h"),

        ("Driving Condition",
         driving_condition.title()),

        ("Fuel Price", f"₹{fuel_price}/L"),

        ("Driving Time Entered",
         f"{driving_time} hours"),

        ("AC", ac.upper()),

        ("Service Condition",
         service.title()),

        ("Road Condition",
         road.title())
    ])


    # --------------------------------------------------------
    # STORE EVERYTHING
    # --------------------------------------------------------

    previous_results[calculation_id] = OrderedDict([

        ("Inputs", input_data),

        ("Results", result)
    ])


    calculation_number += 1


    # --------------------------------------------------------
    # DISPLAY FINAL RESULT
    # --------------------------------------------------------

    print("\n")
    print("=" * 55)

    print(
        "             CALCULATION RESULT"
    )

    print("=" * 55)


    print(

        "Adjusted Fuel Efficiency :",

        result["Adjusted Efficiency"],

        "km/L"
    )


    print(

        "Fuel Consumed            :",

        result["Fuel Consumed"],

        "L"
    )


    print(

        "Remaining Fuel           :",

        result["Remaining Fuel"],

        "L"
    )


    print(

        "Estimated Driving Range  :",

        result["Driving Range"],

        "km"
    )


    print(

        "Fuel Cost                : ₹",

        result["Fuel Cost"]
    )


    print(

        "Cost per km              : ₹",

        result["Cost per km"]
    )


    print(

        "Calculated Travel Time   :",

        result["Calculated Travel Time"],

        "hours"
    )


    print(

        "Fuel Status              :",

        result["Fuel Status"]
    )


    print("=" * 55)


    # --------------------------------------------------------
    # GENERATE GRAPH
    # --------------------------------------------------------

    print(
        "\nGenerating condition-wise "
        "efficiency graph..."
    )


    plot_condition_analysis(

        car,

        car_name,

        passengers,

        luggage,

        speed,

        driving_condition,

        ac,

        service,

        road
    )


    # --------------------------------------------------------
    # NEXT ACTION
    # --------------------------------------------------------

    print("\nWhat would you like to do next?")

    print("1. New Calculation")

    print("2. Retrieve Previous Calculation")

    print("3. Exit")


    next_action = get_choice(

        "Enter choice (1/2/3): ",

        ["1", "2", "3"]
    )


    if next_action == "1":

        continue


    elif next_action == "2":

        show_previous_calculations()


        repeat = get_choice(

            "\nDo you want to make "
            "a new calculation? (Yes/No): ",

            ["yes", "no"]
        )


        if repeat == "yes":

            continue

        else:

            print("\nProgram ended.")

            break


    else:

        print("\nProgram ended.")

        break
