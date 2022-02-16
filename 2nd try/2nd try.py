"""Assignment 10

Contact Tracing App
	- Create a python program that will read QRCode using your webcam
	- You may use any online QRCode generator to create QRCode
	- All personal data are in QRCode 
	- You may decide which personal data to include
	- All data read from QRCode should be stored in a text file including the date and time it was read

Note: 
	- Search how to generate QRCode
	- Search how to read QRCode using webcam
	- Search how to create and write to text file
	- Your source code should be in github before Feb 19
	- Create a demo of your program (1-2 min) and send it directly to my messenger. """

# lagay ko lng references and guide ko para madali ko mabalikan: 
# https://www.geeksforgeeks.org/webcam-qr-code-scanner-using-opencv/
# https://medium.com/@stasinskipawel/create-and-read-qr-code-with-python-in-3-minutes-opencv-and-qrcode-38ecc3a6258a
# https://www.programiz.com/python-programming/file-operation

# qr generator used
# https://goqr.me/#


#1st try, d pa tapos, tinesting lng ung cv2 module, gumawa ng sample qr code, nadedetect na dapat ng webcam ung qr
#2nd try, writes all information from scanned qrs to a txt file 


import cv2

def qr_scanning():
    counter = 0
    cam = cv2.VideoCapture(0)
    detector = cv2.QRCodeDetector()
    while True:
        _, img = cam.read()
        data, bbox, _ = detector.detectAndDecode(img)
        if data:
            person = data
            print("--- QR Code scanned ---\n" + person + "\n") 
            counter = write_txt(person, counter)
        cv2.imshow("QR Scanner", img)    
        if cv2.waitKey(1) == ord("Q"):
            break
    cam.release()
    cv2.destroyAllWindows()


def write_txt(person, counter_in_write):
    try:
        if counter_in_write  == 0:
            file = open("file2.txt","w")
            file.write(person + "\n\n")
            counter_in_write  =+ 1
        else:
            file = open("file2.txt","a")
            file.write(person + "\n\n")
        return counter_in_write   

    finally:
        file.close()

qr_scanning()





