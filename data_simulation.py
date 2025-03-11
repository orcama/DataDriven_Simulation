import pandas as pd
import numpy as np
import matplotlib.pyplot as plt
import seaborn as sns
from datetime import datetime

# Load dataset
file_path = "/Users/afif/Documents/Semester6/Pemodelan dan Simulasi Data/Tugas3/Training_dataset.csv"
df = pd.read_csv(file_path)

# Explore dataset
print("Informasi dataset:")
print(df.info())

print("\nStatistik deskriptif:")
print(df.describe(include='all'))

print("\nJumlah nilai null per kolom:")
print(df.isnull().sum())

print("\nLima baris pertama dataset:")
print(df.head())

# Convert time-related columns to datetime format
time_columns = ['Arrival_Time', 'Start_Time', 'Finish_Time']
for col in time_columns:
    df[col] = pd.to_datetime(df[col], errors='coerce')

# Convert Wait_Time to timedelta
df['Wait_Time'] = pd.to_timedelta(df['Wait_Time'], errors='coerce')

# Step 2: Implement Queueing Simulation
class QueueSimulation:
    def __init__(self, df):
        self.df = df
        self.df['Service_Time'] = (self.df['Finish_Time'] - self.df['Start_Time']).dt.total_seconds()
    
    def simulate_queue(self):
        avg_wait_time = self.df['Wait_Time'].dt.total_seconds().mean()
        avg_service_time = self.df['Service_Time'].mean()
        avg_queue_length = self.df['Queue_Length'].mean()
        return avg_wait_time, avg_service_time, avg_queue_length

# Step 3: Performance Analysis & Visualization
def plot_performance(df):
    plt.figure(figsize=(12, 6))
    sns.histplot(df['Wait_Time'].dt.total_seconds(), bins=30, kde=True)
    plt.xlabel('Wait Time (seconds)')
    plt.ylabel('Frequency')
    plt.title('Distribution of Customer Wait Times')
    plt.show()

# Step 4: Modify Parameters and Optimize
def modify_parameters(df, new_service_time_factor=1.2):
    df['Optimized_Service_Time'] = df['Service_Time'] / new_service_time_factor
    return df

# Step 5: Plot Additional Insights
def plot_additional_insights(df):
    plt.figure(figsize=(12, 6))
    avg_wait_time_per_day = df.groupby('Day')['Wait_Time'].mean().dt.total_seconds()
    avg_wait_time_per_day.plot(kind='bar', color='skyblue', edgecolor='black')
    
    plt.xlabel('Day of the Week')
    plt.ylabel('Average Wait Time (seconds)')
    plt.title('Average Wait Time per Day')
    plt.xticks(rotation=45)
    plt.grid(axis='y', linestyle='--', alpha=0.7)
    
    plt.show()

# Execute Simulation
queue_sim = QueueSimulation(df)
avg_wait_time, avg_service_time, avg_queue_length = queue_sim.simulate_queue()
print(f'Average Wait Time: {avg_wait_time:.2f} seconds')
print(f'Average Service Time: {avg_service_time:.2f} seconds')
print(f'Average Queue Length: {avg_queue_length:.2f}')

# Visualizations
plot_performance(df)
df = modify_parameters(df)
plot_additional_insights(df)