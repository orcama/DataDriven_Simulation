import pandas as pd
from pymongo import MongoClient

def insert_data_from_csv(file_path):
    # Koneksi ke MongoDB (pastikan MongoDB sudah berjalan)
    client = MongoClient("mongodb+srv://anharinizam:UPvln2zIzmH0m1Pq@database1.nom1v.mongodb.net/?retryWrites=true&w=majority&appName=Database1")
    db = client["Online_retail"]  # Ganti dengan nama database yang diinginkan
    collection = db["mycollection"]  # Ganti dengan nama koleksi yang diinginkan

    # Membaca dataset dari CSV
    df = pd.read_csv(file_path)

    # Konversi DataFrame ke dalam format dictionary
    data = df.to_dict(orient="records")
    
    # Memasukkan data ke dalam koleksi
    result = collection.insert_many(data)
    print(f"Data berhasil dimasukkan, total: {len(result.inserted_ids)} records")

if __name__ == "__main__":
    file_path = "/Users/afif/Documents/Semester6/Pemodelan dan Simulasi Data/Tugas3/online_retail.csv"  # Ganti dengan path dataset yang sesuai
    insert_data_from_csv(file_path)
