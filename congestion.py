from collections import defaultdict
import csv


def detect_congestion(records, threshold=3):
    traffic_map = defaultdict(int)

    for r in records:
        key = r["location_id"]
        traffic_map[key] += 1

    results = []

    for location, count in traffic_map.items():
        status = "CONGESTED" if count > threshold else "CLEAR"
        results.append({
            "location": location,
            "vehicle_count": count,
            "status": status
        })

    return results


def print_results(results):
    print("\n🚦 Congestion Analysis:\n")
    for r in results:
        print(f"Location {r['location']} → {r['vehicle_count']} vehicles → {r['status']}")
        if r["status"] == "CONGESTED":
            print(f"⚠️ ALERT: Congestion detected at {r['location']}")


def print_table_header():
    print("\n" + "=" * 110)
    print(
        f"{'Load':<10}{'Vehicles':<12}{'Time(s)':<12}"
        f"{'Throughput':<18}{'Avg Latency(s)':<18}{'Congested Locations':<40}"
    )
    print("=" * 110)


def print_table_row(level, total, total_time, throughput, avg_latency, results):
    congested = [r["location"] for r in results if r["status"] == "CONGESTED"]
    print(
        f"{level:<10}{total:<12}{total_time:<12.4f}"
        f"{throughput:<18.2f}{avg_latency:<18.4f}{str(congested):<40}"
    )


def print_summary_report(level, all_records, results):
    congested_locations = [r["location"] for r in results if r["status"] == "CONGESTED"]

    print("\n📄 Summary Report:")
    print(f"Traffic Level: {level}")
    print(f"Total Vehicles: {len(all_records)}")
    print(f"Congested Locations: {congested_locations if congested_locations else 'None'}")


def export_results_csv(level, results, filename="results.csv"):
    with open(filename, "a", newline="") as f:
        writer = csv.writer(f)

        # If file is empty, write header
        if f.tell() == 0:
            writer.writerow(["Traffic Level", "Location", "Vehicle Count", "Status"])

        for r in results:
            writer.writerow([level, r["location"], r["vehicle_count"], r["status"]])


def export_performance_csv(rows, filename="performance_metrics.csv"):
    with open(filename, "w", newline="") as f:
        writer = csv.writer(f)
        writer.writerow([
            "Traffic Level",
            "Total Vehicles",
            "Total Time (sec)",
            "Throughput (records/sec)",
            "Average Latency (sec)",
            "Congested Locations"
        ])

        for row in rows:
            writer.writerow([
                row["level"],
                row["total_vehicles"],
                f"{row['total_time']:.4f}",
                f"{row['throughput']:.2f}",
                f"{row['avg_latency']:.4f}",
                ", ".join(row["congested_locations"]) if row["congested_locations"] else "None"
            ])