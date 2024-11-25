# Function to calculate the total payment based on purchase amount
def calculate_payment(jlh_pembelian):
    # Check the conditions for the discount
    if jlh_pembelian >= 1000000:  # Greater than 1jt
        discount = 0.5
    elif jlh_pembelian >= 500000:  # Greater than 500rb
        discount = 0.25
    else:  # Less than 500rb
        discount = 0.05
    
    # Calculate discount and final amount to be paid
    potongan = jlh_pembelian * discount
    jumlah_bayar = jlh_pembelian - potongan
    
    return jumlah_bayar

# Main part of the program
if __name__ == "__main__":
    # Input purchase amount
    jlh_pembelian = float(input("Masukkan Jumlah Pembelian: "))
    
    # Calculate the total payment after applying the discount
    jumlah_bayar = calculate_payment(jlh_pembelian)
    
    # Output the final amount
    print(f"Jumlah Bayar: {jumlah_bayar}")