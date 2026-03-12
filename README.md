# Neutron Transport Energy Audit
This repository contains a Monte Carlo Neutron Transport Simulation, with CodeCarbon emission tracking implemented in the final module.  
The simulation calculates the transmission, absortbtion and reflection rates of a given number of neutrons incident onto a slab of material of given thickness.  
The implementation of CodeCarbon results in a 5 lines of emissions data for each number of incident neutrons inside each material (water, lead and graphite).  
The emissions data from each line represents the energy consumption from running the simulation across 15 distinct slab thicknesses, run in parallel across 15 CPU threads.  

## Hardware & Environment
To produce the CSV files inside Data folder, the following specifications were used:
- CPU: AMD Ryzen 7 PRO 5875U with Radeon Graphics (16 Threads / 8 Cores)
- Available RAM : 14.795 GB
- Location: Manchester
- 
## Installation & Execution

### 1. Clone the Repository
```bash
git clone https://github.com/YourUsername/GSoC_Neutron_Transport_Energy_Audit.git
cd GSoC_Neutron_Transport_Energy_Audit
````
### 2. Set up Virtual Environment
```bash
python -m venv .venv
source .venv/bin/activate  # On Windows: .venv\Scripts\activate
````
### 3. Install Dependencies
```bash
pip install -r requirements.txt
````
### 4. Run the Neutron Transport Simulation
Ensure the notebook kernel is set to your `.venv.`
Open Neutron_Transport_Simulation.ipynb in VSCode/Jupyter and run all cells.
### 5. Process Raw CodeCarbon Logs
To obtain the total emissions / energy consumption metrics
```bash
python process_codecarbon_logs.py
````
