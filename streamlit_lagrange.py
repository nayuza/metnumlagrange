import streamlit as st
import numpy as np
import matplotlib.pyplot as plt

# Anggota Kelompok
st.title("📊 Aplikasi Interpolasi Lagrange")
st.markdown("""
### Anggota Kelompok:
- 22.11.5098 Muhamad Rifan Kurniawan  
- 22.11.5073 M. Nasyid Yunitian Rizal  
- 22.11.5099 Sofyan  
""")
st.write("---")

# Fungsi Lagrange
def lagrange_basis(x_values, i, x):
    """Fungsi untuk menghitung basis polinom Lagrange L_i(x) untuk titik i."""
    n = len(x_values)
    basis = 1
    for j in range(n):
        if j != i:
            basis *= (x - x_values[j]) / (x_values[i] - x_values[j])
    return basis

def interpolasi_lagrange(x_values, y_values, x):
    """Fungsi untuk interpolasi Lagrange."""
    n = len(x_values)
    y = 0
    for i in range(n):
        y += y_values[i] * lagrange_basis(x_values, i, x)
    return y

# Input Data
st.header("🔢 Input Data")
num_points = st.number_input("Jumlah Titik Data", min_value=2, value=3, step=1, help="Masukkan jumlah titik data untuk interpolasi.")
x_values = []
y_values = []

st.subheader("Masukkan Titik Data")
cols = st.columns(2)
for i in range(num_points):
    x = cols[0].number_input(f"x{i}", key=f"x{i}", help=f"Masukkan nilai x{i}.")
    y = cols[1].number_input(f"y{i}", key=f"y{i}", help=f"Masukkan nilai y{i}.")
    x_values.append(x)
    y_values.append(y)

x_target = st.number_input("Masukkan nilai x untuk interpolasi", help="Masukkan nilai x yang ingin dihitung nilai interpolasinya.")

# Hitung Interpolasi
if st.button("Hitung Interpolasi"):
    try:
        y_target = interpolasi_lagrange(x_values, y_values, x_target)
        st.success(f"Nilai interpolasi pada x = {x_target} adalah y = {y_target:.4f}")

        # Visualisasi
        st.header("📈 Visualisasi Interpolasi")
        x_plot = np.linspace(min(x_values) - 1, max(x_values) + 1, 500)
        y_plot = [interpolasi_lagrange(x_values, y_values, xi) for xi in x_plot]

        plt.figure(figsize=(10, 6))
        plt.plot(x_plot, y_plot, label="Polinom Interpolasi", color="blue", linewidth=2)
        plt.scatter(x_values, y_values, color="red", label="Titik Data", zorder=5)
        plt.axvline(x_target, color="green", linestyle="--", label=f"x = {x_target}", zorder=5)
        plt.scatter(x_target, y_target, color="orange", label=f"Interpolasi (y = {y_target:.4f})", zorder=5)
        plt.xlabel("x", fontsize=12)
        plt.ylabel("y", fontsize=12)
        plt.title("Interpolasi Lagrange", fontsize=16, fontweight="bold")
        plt.legend(fontsize=10)
        plt.grid(True)
        st.pyplot(plt)

    except Exception as e:
        st.error(f"Terjadi kesalahan: {e}")