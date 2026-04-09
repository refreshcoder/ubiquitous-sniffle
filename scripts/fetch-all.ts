import { execSync } from "child_process";

async function main() {
  console.log("Fetching China market data using Python script...");
  try {
    execSync("python3 scripts/fetch_china_data.py", { stdio: "inherit" });
    console.log("Successfully fetched and generated data for China edition.");
  } catch (error) {
    console.error("Failed to run python script:", error);
    process.exit(1);
  }
}

main().catch(console.error);
