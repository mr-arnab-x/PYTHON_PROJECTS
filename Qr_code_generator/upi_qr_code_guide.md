
# Generating and Displaying UPI QR Codes

This guide provides step-by-step instructions for generating UPI QR codes using Python.

## Step 1: Install Required Libraries

Before you begin, make sure to install the necessary Python libraries.

```bash
pip install qrcode[pil]
pip install pillow
```

- **qrcode[pil]**: This is the library used to generate QR codes.
- **Pillow**: This library (often imported as `PIL`) is used for image processing and handling.

## Step 2: Write the Python Script

Below is the Python script that generates and displays UPI QR codes for PhonePe and Google Pay.

```python
import qrcode  # Import the qrcode library to generate QR codes

# Prompt the user to enter their UPI ID
upi_id = input("Enter Your UPI ID Here - ")

# Create the UPI payment URL for PhonePe with a merchant code (mc)
phonepe_url = f"upi://pay?pa={upi_id}&pn=Recipient%20Name&mc=1234"

# Create the UPI payment URL for Google Pay with a merchant code (mc)
googlepay_url = f"upi://pay?pa={upi_id}&pn=Recipient%20Name&mc=1234"

# Generate QR codes for the PhonePe and Google Pay URLs
phonepe_qr = qrcode.make(phonepe_url)
googlepay_qr = qrcode.make(googlepay_url)

# Save the generated QR codes as image files
phonepe_qr.save('phonepe_qr.png')  # Saves the PhonePe QR code as 'phonepe_qr.png'
googlepay_qr.save('googlepay_qr.png')  # Saves the Google Pay QR code as 'googlepay_qr.png'

# Display the generated QR codes on the screen
phonepe_qr.show()  # Opens the PhonePe QR code image
googlepay_qr.show()  # Opens the Google Pay QR code image
```

## Step 3: Running the Script

1. **Run the script**: Execute the Python script in your terminal or IDE.
2. **Input UPI ID**: The script will prompt you to enter your UPI ID.
3. **View QR Codes**: The script will generate two QR codes (one for PhonePe and one for Google Pay) and display them.

## Step 4: Save and Use the QR Codes

- The QR codes are saved as `phonepe_qr.png` and `googlepay_qr.png` in the same directory where the script is located.
- You can use these images for payments or share them with others for transactions.
