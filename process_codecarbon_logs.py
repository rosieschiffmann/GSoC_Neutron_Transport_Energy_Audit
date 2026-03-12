import pandas as pd
import os

# Load your CodeCarbon log file
log_file = r"Energy_Audit_CodeCarbon_Log.csv"
df = pd.read_csv(log_file)

# Calculate Time & Emissions
total_duration_sec = df['duration'].sum()
total_emissions_kg = df['emissions'].sum()

# Calculate Energy Consumption (kWh) per Component
total_cpu_energy = df['cpu_energy'].sum()
total_gpu_energy = df['gpu_energy'].sum()
total_ram_energy = df['ram_energy'].sum()
total_combined_energy = df['energy_consumed'].sum()
total_water_liters = df['water_consumed'].sum()

# Calculate Average Power Draw (Watts)
avg_cpu_power = df['cpu_power'].mean()
avg_gpu_power = df['gpu_power'].mean()
avg_ram_power = df['ram_power'].mean()

# Save summary to a CSV for your records
summary_df = pd.DataFrame({
    'Duration (s)': [total_duration_sec],
    'Emissions (kg)': [total_emissions_kg],
    'Water Consumed (L)': [total_water_liters],
    'CPU Energy (kWh)': [total_cpu_energy],
    'RAM Energy (kWh)': [total_ram_energy],
    'Total Energy (kWh)': [total_combined_energy],
    'Avg CPU Power (W)': [avg_cpu_power],
    'Avg RAM Power (W)': [avg_ram_power]
})

# Print the summary to the console
print("--- GreenMetaData Energy Audit Summary ---")
print(summary_df.to_string(index=False))

dir_name = os.path.dirname(log_file)
base_name = os.path.basename(log_file)
filename = f"Total_{base_name}"
output_path = os.path.join(dir_name, filename)
summary_df.to_csv(output_path, index=False)
