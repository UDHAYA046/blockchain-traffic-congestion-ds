import time
import os

from congestion import (
    detect_congestion,
    print_results,
    print_table_header,
    print_table_row,
    print_summary_report,
    export_results_csv,
    export_performance_csv
)
from vehicle_sim import simulate_traffic
from web3_client import send_batch_to_blockchain, get_record


def validate_data(record):
    required_fields = ["vehicle_id", "location_id", "timestamp", "speed"]
    return all(field in record for field in required_fields)


def batch_data(records, batch_size=5):
    return [records[i:i+batch_size] for i in range(0, len(records), batch_size)]


def send_to_blockchain(batch):
    print("\n📡 Sending batch to blockchain...")
    return send_batch_to_blockchain(batch)


def run_pipeline_for_level(level):
    print(f"\n{'#' * 20} RUNNING {level.upper()} TRAFFIC {'#' * 20}\n")

    data = simulate_traffic(level)
    valid_data = [d for d in data if validate_data(d)]
    batches = batch_data(valid_data)

    all_records = []
    all_latencies = []

    start_time = time.time()

    for batch in batches:
        batch_metrics = send_to_blockchain(batch)
        all_records.extend(batch)
        all_latencies.extend(batch_metrics["batch_latencies"])

    end_time = time.time()

    # Congestion detection
    results = detect_congestion(all_records)
    print_results(results)

    # Evaluation
    total_time = end_time - start_time
    throughput = len(all_records) / total_time if total_time > 0 else 0
    avg_latency = sum(all_latencies) / len(all_latencies) if all_latencies else 0

    print("\n📊 Performance Metrics:\n")
    print(f"Total Time: {total_time:.4f} sec")
    print(f"Throughput: {throughput:.2f} records/sec")
    print(f"Average Latency: {avg_latency:.4f} sec")

    # Summary block
    print_summary_report(level, all_records, results)

    # CSV exports
    export_results_csv(level, results)

    congested_locations = [r["location"] for r in results if r["status"] == "CONGESTED"]

    return {
        "level": level,
        "total_vehicles": len(all_records),
        "total_time": total_time,
        "throughput": throughput,
        "avg_latency": avg_latency,
        "congested_locations": congested_locations
    }


if __name__ == "__main__":
    print("🚦 RSU Node Started...\n")

    # Fresh CSV for each full run
    for file_name in ["results.csv", "performance_metrics.csv"]:
        if os.path.exists(file_name):
            os.remove(file_name)

    performance_rows = []

    # Load comparison: low, medium, high
    for level in ["low", "medium", "high"]:
        row = run_pipeline_for_level(level)
        performance_rows.append(row)

    # Results table
    print_table_header()
    for row in performance_rows:
        results_like = [{"location": loc, "status": "CONGESTED"} for loc in row["congested_locations"]]
        print_table_row(
            row["level"],
            row["total_vehicles"],
            row["total_time"],
            row["throughput"],
            row["avg_latency"],
            results_like
        )

    # Export performance table
    export_performance_csv(performance_rows)

    # Blockchain readback proof
    print("\n📦 Blockchain Readback Proof:")
    get_record(0)

    print("\n✅ CSV files created:")
    print(" - results.csv")
    print(" - performance_metrics.csv")

    print("\n📸 Screenshot Checklist:")
    print("1. Blockchain transactions with latency")
    print("2. Congestion analysis with alerts")
    print("3. Performance table + summary")