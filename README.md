# **UTS INTEGRASI DATA**
**Data Matching**

Tugas ini dibangun untuk mendeteksi anomali pada data Pengadaan Barang/Jasa (PBJ) menggunakan pendekatan klasifikasi berbobot. Dimulai dari pre-processing dan pelabelan berbasis kemiripan nama paket, dilanjutkan klasifikasi dengan Weighted Scoring dan XGBoost, hingga visualisasi anomali anggaran dan metode pengadaan.


**Disusun Oleh**
| Nama | Chayun Fadila |
|------|---------------|
| **NRP** | **602624211** |

## ⚙️ Konfigurasi & Bobot

> - `Nama Paket = 0.50` → identitas utama paket, paling dominan
> - `Uraian Pekerjaan = 0.35` → detail teknis, membedakan paket yg namanya mirip tapi isinya beda
> - `Metode Pengadaan = 0.15` → konteks prosedural, penting tapi bukan penentu utama

| Kolom | Bobot | Alasan |
|---|---|---|
| **Nama Paket** | **50%** | Identitas utama paket pengadaan. Jika nama mirip → kemungkinan besar paket serupa |
| **Uraian Pekerjaan** | **35%** | Detail teknis yang membedakan paket bermakna sama vs berbeda konteks |
| **Metode Pengadaan** | **15%** | Konteks prosedural. Dua paket bisa mirip walau metode berbeda, tapi tetap relevan |
