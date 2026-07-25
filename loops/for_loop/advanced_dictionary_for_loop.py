people = {
    "weka": {
        "dart": 90,
        "python": 80,
        "Js": 50,
    },
    "ahmed": {
        "dart": 50,
        "python": 100,
        "Js": 20,
    },
    "aly": {
        "dart": 80,
        "python": 80,
        "Js": 60,
    }
}

for main_key, main_value in people.items():
    print(f"{main_key} progress:")
    for child_key, child_value in main_value.items():
        print(f"- {child_key} -> {child_value}")