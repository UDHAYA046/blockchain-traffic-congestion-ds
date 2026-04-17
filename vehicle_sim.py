import random
import time

locations = ["L1", "L2", "L3", "L4", "L5"]

def generate_vehicle_data(vehicle_id):
    return {
        "vehicle_id": f"V{vehicle_id}",
        "location_id": random.choice(locations),
        "timestamp": int(time.time()),
        "speed": random.randint(20, 80)
    }

def simulate_traffic(density="low"):
    if density == "low":
        num_vehicles = 5
    elif density == "medium":
        num_vehicles = 15
    else:
        num_vehicles = 30

    return [generate_vehicle_data(i) for i in range(num_vehicles)]

if __name__ == "__main__":
    data = simulate_traffic("medium")
    for d in data:
        print(d)