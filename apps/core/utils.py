def can_load_medication_weight(drone_object, medications_json):
    drone_weight_limit = drone_object.weight_limit
    medications_total_weight = 0.0
    for medication in medications_json:
        medications_total_weight += float(medication['weight'])
    return medications_total_weight <= drone_weight_limit


def add_drone_to_medications(drone_object, medications_json):
    for medication in medications_json:
        medication['drone'] = drone_object.serial_number
    return medications_json
