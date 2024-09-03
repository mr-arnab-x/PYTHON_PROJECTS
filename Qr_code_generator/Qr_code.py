import qrcode  # Import the qrcode library to generate QR codes

# Prompt the user to enter their UPI ID
upi_id = input("Enter Your UPI ID Here - ")

#   upi://pay?pa=UPI_ID&pn=NAME&am=AMOUNT&cu=CURRENCY&tn=MASSAGE

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
