import { execSync } from "child_process";
import { dirname, resolve } from "path";
import { fileURLToPath } from "url";

const __filename = fileURLToPath(import.meta.url);
const __dirname = dirname(__filename);

async function main() {
  console.log("Fetching China market data using Python script...");
  try {
    const scriptPath = resolve(__dirname, "fetch_china_data.py");
    execSync(`python3 ${scriptPath}`, { stdio: "inherit" });
    console.log("Successfully fetched and generated data for China edition.");
  } catch (error) {
    console.error("Failed to run python script:", error);
    process.exit(1);
  }
}

main().catch(console.error);
