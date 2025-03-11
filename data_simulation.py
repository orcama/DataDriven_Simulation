import numpy as np
import matplotlib.pyplot as plt
import seaborn as sns
from queue import Queue
from pymongo import MongoClient

def get_data_from_db():
    # Koneksi ke MongoDB
    client = MongoClient("mongodb+srv://anharinizam:UPvln2zIzmH0m1Pq@database1.nom1v.mongodb.net/?retryWrites=true&w=majority&appName=Database1")
    db = client["Online_retail"]  # Ganti dengan nama database yang diinginkan
    collection = db["mycollection"]  # Ganti dengan nama koleksi yang diinginkan
    
    # Mengambil data dari database
    data = list(collection.find({}, {"_id": 0}))  # Menghilangkan field _id
    return data

def queue_simulation(num_requests=100, service_rate=2, arrival_rate=1):
    queue = Queue()
    wait_times = []
    time = 0
    
    for _ in range(num_requests):
        time += np.random.exponential(1 / arrival_rate)
        queue.put(time)
        
        if not queue.empty():
            start_service = queue.get()
            service_time = np.random.exponential(1 / service_rate)
            wait_times.append(service_time)
    
    return wait_times

def performance_analysis(wait_times):
    mean_wait = np.mean(wait_times)
    median_wait = np.median(wait_times)
    print(f"Rata-rata waktu tunggu: {mean_wait:.2f} detik")
    print(f"Median waktu tunggu: {median_wait:.2f} detik")
    
    plt.figure(figsize=(10, 5))
    sns.histplot(wait_times, bins=20, kde=True)
    plt.xlabel("Waktu Tunggu")
    plt.ylabel("Frekuensi")
    plt.title("Distribusi Waktu Tunggu")
    plt.show()

def optimize_parameters():
    best_service_rate = None
    best_mean_wait = float("inf")
    
    for service_rate in np.arange(1, 5, 0.5):
        wait_times = queue_simulation(service_rate=service_rate)
        mean_wait = np.mean(wait_times)
        if mean_wait < best_mean_wait:
            best_mean_wait = mean_wait
            best_service_rate = service_rate
    
    print(f"Optimasi: Laju pelayanan terbaik: {best_service_rate} dengan waktu tunggu rata-rata {best_mean_wait:.2f} detik")

def plot_additional_insights(wait_times):
    plt.figure(figsize=(10, 5))
    plt.plot(wait_times, marker='o', linestyle='-')
    plt.xlabel("Index Request")
    plt.ylabel("Waktu Tunggu")
    plt.title("Perubahan Waktu Tunggu Per Request")
    plt.show()

if __name__ == "__main__":
    data = get_data_from_db()
    print(f"Data yang diambil dari database: {len(data)} records")
    
    wait_times = queue_simulation()
    performance_analysis(wait_times)
    optimize_parameters()
    plot_additional_insights(wait_times)
