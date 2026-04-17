# 🚦 Blockchain-Enabled Distributed Traffic Congestion Detection System

## 📌 Project Overview
This project implements a **distributed traffic congestion detection system** using **Vehicle-to-Roadside Unit (V2RSU) communication** and **blockchain technology**.

The system simulates real-time vehicular data, securely stores it using a blockchain-based smart contract, and detects congestion based on vehicle density in different locations. It demonstrates how **distributed systems and decentralized storage** can be applied to intelligent transportation systems.

---

## 🎯 Objectives
- To design a **distributed system** for traffic monitoring  
- To ensure **secure and tamper-proof data storage** using blockchain  
- To simulate **real-time vehicle-to-RSU communication**  
- To detect congestion based on **vehicle density thresholds**  
- To evaluate system performance using **latency, throughput, and scalability**

---

## 🧠 System Architecture


Vehicle Simulation → RSU Node → Blockchain (Smart Contract)
                                ↓
                        Congestion Detection
                                ↓
                        Alerts + Metrics


---

## ⚙️ Modules Description

### 1. 🚗 Vehicle Simulation (`vehicle_sim.py`)
- Generates dummy traffic data
- Simulates vehicles under:
  - Low load
  - Medium load
  - High load
- Fields:
  - Vehicle ID
  - Location ID
  - Timestamp
  - Speed

---

### 2. 📡 RSU Node (`rsu_node.py`)
- Acts as a roadside unit
- Collects and batches vehicle data
- Sends data to blockchain
- Triggers congestion detection
- Handles:
  - Data validation
  - Batch processing

---

### 3. 🔗 Blockchain Layer
#### Smart Contract (`contracts/TrafficLog.sol`)
- Stores traffic data immutably
- Ensures:
  - Data integrity
  - No tampering
  - Transparency

#### Deployment Script (`scripts/deploy.js`)
- Deploys contract to local blockchain (Hardhat)

---

### 4. 🌐 Web3 Client (`web3_client.py`)
- Connects Python to blockchain
- Sends transactions
- Measures:
  - Transaction latency
- Provides:
  - Blockchain readback verification

---

### 5. 🚦 Congestion Detection (`congestion.py`)
- Analyzes vehicle density per location
- Uses threshold-based logic:
  - If vehicles > threshold → CONGESTED
- Generates:
  - Alerts
  - Location-wise results

---

## 📊 Performance Evaluation

### Metrics Used

| Metric | Description |
|------|------------|
| Transaction Latency | Time taken to store data on blockchain |
| Throughput | Records processed per second |
| Scalability | Performance under different traffic loads |
| Data Integrity | Ensured via blockchain immutability |

---

### ⚠️ Note on Accuracy
Congestion detection is **rule-based (threshold-based)**, not ML-based.  
Therefore, traditional accuracy metrics are not applicable.

Correctness is logically validated using predefined thresholds.

---

## 📈 Experimental Results

System tested under 3 scenarios:

| Load | Vehicles | Time(s) | Throughput | Avg Latency | Congestion |
|------|--------|--------|------------|------------|-----------|
| Low | 5 | ~0.22 | ~21 rec/s | ~0.04s | None |
| Medium | 15 | ~0.57 | ~26 rec/s | ~0.03s | Partial |
| High | 30 | ~1.32 | ~22 rec/s | ~0.04s | Multiple |

---

## 📁 Output Files

- `results.csv` → congestion analysis results  
- `performance_metrics.csv` → system performance data  

---

## 🔍 Key Features

- ✅ Distributed system architecture  
- ✅ Blockchain-based secure storage  
- ✅ Real-time congestion detection  
- ✅ Multi-load simulation (low, medium, high)  
- ✅ Transaction latency tracking  
- ✅ Throughput calculation  
- ✅ CSV-based reporting  
- ✅ Blockchain data verification  

---

## 🚀 How to Run

### 1. Start Blockchain : npx hardhat node
### 2. Deploy Smart Contract : npx hardhat run scripts/deploy.js --network localhost
### 3. Run System : python rsu_node.py


---

## 🛠️ Technologies Used

- Python  
- Web3.py  
- Ethereum (Hardhat)  
- Node.js  
- Solidity  

---

## 📌 Project Type
Simulation-based Distributed Systems Project

---

## 👨‍💻 Team Members

-  BL.EN.U4CSE23122 : Gangam Sai Samarth  
-  BL.EN.U4CSE23134 : Maytrai Sharma  
-  BL.EN.U4CSE23150 : S.Udhaya Sankari  
-  BL.EN.U4CSE23152 : Saswat Subhankar  

---

## 🏫 Institution

Amrita Vishwa Vidyapeetham  

---

## 🎓 Course

Distributed Systems   

---

## 👩‍🏫 Faculty Guide

Meena Belwal

---

## 📌 Conclusion

This project demonstrates how **blockchain and distributed systems** can be combined to create a secure, scalable, and reliable traffic monitoring system. The simulation validates the feasibility of decentralized traffic data management and real-time congestion detection.

---

## 🔮 Future Work

- Integration with real V2X hardware  
- Machine learning-based congestion prediction  
- Smart traffic signal control  
- Cloud + edge deployment  

---

## 📦 Note

This is a **simulation-based implementation** intended to validate system design and feasibility. Real-world deployment would require integration with physical RSUs and vehicular communication systems.

---

