from reportlab.lib.colors import HexColor #pip install reportlab
from reportlab.pdfgen.canvas import Canvas
from reportlab.lib.units import cm
from reportlab.pdfbase.ttfonts import TTFont
from reportlab.pdfbase import pdfmetrics
import cv2  #pip install opencv-python
from python.databases.databaseQueries import *
from python.databases.connectToDatabase import connect
from python.path_stuff import get_abs_paths

"""
TeamSoftwareProject (CK, JH, PO'D, CO'D, LdlC, KP)

This python file provides functions and methods to allow us to generate PDFs
"""

pdfmetrics.registerFont(TTFont('Vera', 'Vera.ttf'))
pdfmetrics.registerFont(TTFont('VeraBd', 'VeraBd.ttf'))
line_x_start = 0
line_width = 600


def generatePDF(fileName, title, template):
	"""
	  Function to generate a pdf.

	  @params - filename - name of pdf (includes url to folder)
				title - pdf title
				template - pdf template (***Only have one at the moment)

	"""
	pdf = Canvas(fileName)
	create_header(title, pdf)
	create_footer(pdf)
	#drawMyRuler(pdf)
	if template=="dates":
		stockDates(pdf)
#    resizeImage("location_history.png")
#    pdf.drawImage("modified_location_history.png", line_x_start, 200, width=line_width,
				# preserveAspectRatio=True, mask='auto')
	pdf.save()

def create_header(title, pdf):
	"""
	 Function to create the pdfs header
	 @params title - title of pdf
			 pdf - the pdf canvas
	"""
	pdf.setTitle(title)
	pdf.setFillColor(HexColor("#E9EEF4"))
	path = pdf.beginPath()
	path.moveTo(0*cm,0*cm)
	path.lineTo(0*cm,30*cm)
	path.lineTo(25*cm,30*cm)
	path.lineTo(25*cm,0*cm)
	#this creates a rectangle the size of the sheet
	pdf.drawPath(path,True,True)
	pdf.drawInlineImage(get_abs_paths()['assets'] + "/images/logo.png", 100, 745)
	pdf.setFillColor(HexColor("#080807"))
	pdf.line(0, 725, 850, 725)

def create_footer(pdf):
	"""
	 Function to create the pdfs header
	 @params pdf - the pdf canvas

	"""
	pdf.line(0, 50, 850, 50)
	pdf.setFont('Vera', 12)
	pdf.drawString(30, 30, "SMS - Stock Management Software")


def stockDates(pdf):
	"""
	  template function to display data regarding expiring stock

	"""
	pdf.setFont('VeraBd', 13)
	pdf.drawString(50, 670, "Below is some information regarding the current expiry ")
	pdf.drawString(50, 650, "dates of current stock:")

	total_products = get_total_number_of_products()
	stock_expiring_soon = get_count_of_product_expiring_soon(10)
	final_date = stock_expiring_soon[9]['expiry_date']

	stockNum=0
	for day in stock_expiring_soon:
		stockNum+=day['count']

	text = pdf.beginText(50, 610)
	text.setFont('Vera', 12)

	text.textLine("There are %d products expiring by %s." %(stockNum, final_date))
	text.textLine("That is %.0f%% of the total number of products in stock." % (float(stockNum)/float(total_products)*100.0))
	text.textLine("There are currently %d products currently recorded in the system." %(total_products))
	pdf.drawText(text)
	pdf.setFont('VeraBd', 13)
	pdf.drawString(50, 550, "Below are the number of products expiring on each day:")
	pdf.setFont('VeraBd', 11)
	pdf.drawString(50, 530, "Quantity   Date")

	pdf.line(50, 520, 178, 520)

	text = pdf.beginText(50, 500)
	text.setFont('Vera', 11)
	for day in stock_expiring_soon:
		text.textLine("   %d              %s" %(day['count'], day['expiry_date']))
	pdf.drawText(text)
	pdf.setFont('VeraBd', 13)
	pdf.drawString(50, 340, "Below are some products expiring in the next few days:")
	pdf.setFont('VeraBd', 11)
	pdf.drawString(50, 320, "ID  Location   Expiry-Date          Title")
	pdf.line(50, 310, 300, 310)
	products = get_list_of_product_expiring_soon(10)
	text = pdf.beginText(50, 290)
	text.setFont('Vera', 11)
	for product in products:

		text.textLine("{:2}     {:2}             {}        {:^15}".format(product[0], product[1], product[2], product[3]))
	pdf.drawText(text)


def resizeImage(img_path):
	"""
	 Function to resize the mathlab graphs to fit the pdf
	 @param img_path - path to image of graph

	"""
	img = cv2.imread(img_path, cv2.IMREAD_UNCHANGED)

	#print('Original Dimensions : ',img.shape)
	scale_percent = 60 # percent of original size
	width = int(img.shape[1] * scale_percent / 100)
	height = int(img.shape[0] * scale_percent / 100)
	dim = (width, height)
	# resize image
	resized = cv2.resize(img, dim, interpolation = cv2.INTER_AREA)

	#print('Resized Dimensions : ',resized.shape)
	cv2.imwrite("modified"+img_path, resized)

def drawMyRuler(pdf):
	# Print dimensions on screen to help with drawing
	pdf.drawString(100,810, 'x100')
	pdf.drawString(200,810, 'x200')
	pdf.drawString(300,810, 'x300')
	pdf.drawString(400,810, 'x400')
	pdf.drawString(500,810, 'x500')
	pdf.drawString(10,100, 'y100')
	pdf.drawString(10,200, 'y200')
	pdf.drawString(10,300, 'y300')
	pdf.drawString(10,400, 'y400')
	pdf.drawString(10,500, 'y500')
	pdf.drawString(10,600, 'y600')
	pdf.drawString(10,700, 'y700')
	pdf.drawString(10,800, 'y800')


def generateStockInfo():
	generatePDF(get_abs_paths()['data_store'] + "/StockDates.pdf", "StockDates", "dates")
	return '/data_store/StockDates.pdf'


if __name__ == "__main__":
	generateStockInfo()
