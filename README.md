### Decoding-MRZ-Barcodes-using-Python-OpenCV-pytesseract

The Machine Readable Zone (MRZ) barcode refers to the TD1 and TD3 format (2 or 3 lines) found on most travel passports, passport cards, some driver's licenses and ID cards. The MRZ code includes the owner's personal information. The MRZ is the red marked region on the image below. 

![alt text](https://github.com/lucynwosu/Decoding-MRZ-Barcodes-using-Python-OpenCV-pytesseract/blob/master/examples/220px-Mrp_image.gif)

The aim of this project is to extract all personal information data from the MRZ like:

**Firstname<br> 
Lastname<br>
Passport number<br>
Nationality<br>
Sex<br>
Date of birth<br>
Expiration date<br>
Personal number<br>
Document type<br>
Country of issuance<br>**

The project includes the following steps:
1. Detecting MRZ Region on Image - OpenCV
2. Reading encoded information on MRZ - python passport eye (pytesseract, OCR)

To run: 
Clone repo and run code from root folder on Terminal
python main.py --images <examples/image>

