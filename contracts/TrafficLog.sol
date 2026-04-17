// SPDX-License-Identifier: MIT
pragma solidity ^0.8.0;

contract TrafficLog {

    struct Record {
        string vehicle_id;
        string location_id;
        uint timestamp;
        uint speed;
    }

    Record[] public records;

    function addRecord(
        string memory vehicle_id,
        string memory location_id,
        uint timestamp,
        uint speed
    ) public {
        records.push(Record(vehicle_id, location_id, timestamp, speed));
    }

    function getTotalRecords() public view returns (uint) {
        return records.length;
    }
}