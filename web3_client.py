from web3 import Web3
import json
import time

# Connect to local Hardhat blockchain
w3 = Web3(Web3.HTTPProvider("http://127.0.0.1:8545"))
print("Connected:", w3.is_connected())

# Replace this if you redeploy after restarting hardhat node
contract_address = Web3.to_checksum_address("0x5fbdb2315678afecb367f032d93f642f64180aa3")

# Load ABI
with open("TrafficLogABI.json", "r") as f:
    abi = json.load(f)

# Create contract object
contract = w3.eth.contract(address=contract_address, abi=abi)

# Use first account from Hardhat node
account = w3.eth.accounts[0]


def get_total_records():
    total = contract.functions.getTotalRecords().call()
    print("📊 Total Records on Blockchain:", total)
    return total


def get_record(index):
    try:
        record = contract.functions.records(index).call()
        print(f"📦 Record {index}: {record}")
        return record
    except Exception as e:
        print(f"❌ Error reading record {index}: {e}")
        return None


def send_batch_to_blockchain(batch):
    latencies = []

    for record in batch:
        try:
            start = time.time()

            tx_hash = contract.functions.addRecord(
                record["vehicle_id"],
                record["location_id"],
                record["timestamp"],
                record["speed"]
            ).transact({'from': account})

            receipt = w3.eth.wait_for_transaction_receipt(tx_hash)

            end = time.time()
            latency = end - start
            latencies.append(latency)

            print(
                f"✅ Stored: {record['vehicle_id']} | "
                f"Latency: {latency:.4f} sec | "
                f"Tx: {receipt.transactionHash.hex()}"
            )

        except Exception as e:
            print(f"❌ Error storing {record['vehicle_id']}: {e}")

    total_records = get_total_records()

    avg_latency = sum(latencies) / len(latencies) if latencies else 0
    print(f"📊 Average Batch Latency: {avg_latency:.4f} sec")

    return {
        "batch_avg_latency": avg_latency,
        "batch_latencies": latencies,
        "blockchain_total_records": total_records
    }