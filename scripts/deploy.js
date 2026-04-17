async function main() {
  const TrafficLog = await ethers.getContractFactory("TrafficLog");
  const contract = await TrafficLog.deploy();

  await contract.waitForDeployment();

  console.log("Contract deployed to:", await contract.getAddress());
}

main().catch((error) => {
  console.error(error);
  process.exitCode = 1;
});