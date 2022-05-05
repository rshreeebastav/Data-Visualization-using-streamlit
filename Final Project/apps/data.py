import streamlit as st
import numpy as np
import pandas as pd
from sklearn import datasets

import docx2txt
from PIL import Image
from PIL import Image 
from PyPDF2 import PdfFileReader
import pdfplumber

import streamlit as st
import pandas as pd
import plotly.graph_objects as go
import numpy as np
import plotly.express as px
from PIL import Image
import matplotlib.pyplot as plt
import seaborn as sns
from plotly.subplots import make_subplots
from datetime import datetime


def app(file):
	pdfReader = PdfFileReader(file)
	count = pdfReader.numPages
	all_page_text = ""
	for i in range(count):
		page = pdfReader.getPage(i)
		all_page_text += page.extractText()

	return all_page_text

def app_with_pdfplumber(file):
	with pdfplumber.open(file) as pdf:
	    page = pdf.pages[0]
	    return page.extract_text()

# import fitz  # this is pymupdf

# def read_pdf_with_fitz(file):
# 	with fitz.open(file) as doc:
# 		text = ""
# 		for page in doc:
# 			text += page.getText()
# 		return text 

# Fxn
@st.cache
def load_image(image_file):
	img = Image.open(image_file)
	return img 



def app():
	# st.title("File Upload ")

	menu = ["Home","Dataset","Representation of Data","DocumentFiles","About Data Visualization"]
	choice = st.sidebar.selectbox("Menu",menu)


	if choice == "Home":
		st.subheader("Welcome TO Data Analysis ")
		
		image = Image.open('datascience.jpg')

		st.image(image)
		st.write("Although many groups, organizations, and experts have different ways to approach data analysis, most of them can be distilled into a one-size-fits-all definition. Data analysis is the process of cleaning, changing, and processing raw data, and extracting actionable, relevant information that helps businesses make informed decisions. The procedure helps reduce the risks inherent in decision-making by providing useful insights and statistics, often presented in charts, images, tables, and graphs.")
		# image_file = st.file_uploader("Upload Image",type=['png','jpeg','jpg',"csv"])
		# if image_file is not None:
		
		# 	# To See Details
		# 	# st.write(type(image_file))
		# 	# st.write(dir(image_file))
		# 	file_details = {"Filename":image_file.name,"FileType":image_file.type,"FileSize":image_file.size}
		# 	st.write(file_details)

		# 	img = load_image(image_file)
		# 	# st.image(img,width=250,height=250)


	elif choice == "Dataset":
		st.subheader("Dataset")
		data_file = st.file_uploader("Upload CSV",type=['csv'])
		if st.button("Process"):
			if data_file is not None:
				file_details = {"Filename":data_file.name,"FileType":data_file.type,"FileSize":data_file.size}
				st.write(file_details)

				df = pd.read_csv(data_file)
				st.dataframe(df)
				

	elif choice == "DocumentFiles":
		st.subheader("DocumentFiles")
		docx_file = st.file_uploader("Upload File",type=['txt','docx','pdf'])
		if st.button("Process"):
			if docx_file is not None:
				file_details = {"Filename":docx_file.name,"FileType":docx_file.type,"FileSize":docx_file.size}
				st.write(file_details)
				# Check File Type
				if docx_file.type == "text/plain":
					# raw_text = docx_file.read() # read as bytes
					# st.write(raw_text)
					# st.text(raw_text) # fails
					st.text(str(docx_file.read(),"utf-8")) # empty
					raw_text = str(docx_file.read(),"utf-8") # works with st.text and st.write,used for futher processing
					# st.text(raw_text) # Works
					st.write(raw_text) # works
				elif docx_file.type == "application/pdf":
					# raw_text = read_pdf(docx_file)
					# st.write(raw_text)
					try:
						with pdfplumber.open(docx_file) as pdf:
						    page = pdf.pages[0]
						    st.write(page.extract_text())
					except:
						st.write("None")
					    
					
				elif docx_file.type == "application/vnd.openxmlformats-officedocument.wordprocessingml.document":
				# Use the right file processor ( Docx,Docx2Text,etc)
					raw_text = docx2txt.process(docx_file) # Parse in the uploadFile Class directory
					st.write(raw_text)

	if choice=="About Data Visualization":
		
		image = Image.open('e.jpg')

		st.image(image)
		st.write("Data visualization (often abbreviated data viz) is an interdisciplinary field that deals with the graphic representation of data. It is a particularly efficient way of communicating when the data is numerous as for example a time series. From an academic point of view, this representation can be considered as a mapping between the original data (usually numerical) and graphic elements (for example, lines or points in a chart). The mapping determines how the attributes of these elements vary according to the data. In this light, a bar chart is a mapping of the length of a bar to a magnitude of a variable. Since the graphic design of the mapping can adversely affect the readability of a chart, mapping is a core competency of Data visualization. Data visualization has its roots in the field of statistics and is therefore generally considered a branch of descriptive Statistics. However, because both design skills and statistical and computing skills are required to visualize effectively, it is argued by authors such as Gershon and Page that it is both an art and a science. Research into how people read and misread various types of visualizations is helping to determine what types and features of visualizations are most understandable and effective in conveying information. ")
	else:
		st.subheader("")
		# st.info("Built with Streamlit")
		# st.info("Jesus Saves @JCharisTech")
		# st.text("Jesse E.Agbe(JCharis)")

	if choice=="Representation of Data":
		image = Image.open('Data.jpg')

		st.image(image)
		
	else:
		st.header("")

	if choice=="Representation of Data":			
		st.header('Covid-19 Data Visualization India')

    # ---> Load DataFrame <---
		csv_file = 'D:\\Study material\\Semester 4\\Python Programming-II\\Project\\PSEE\\Final Project\\complete.csv'
		

		file = pd.read_csv(csv_file)

    #---------------------------------------------

		option = st.multiselect(
		 'Select the State :',
		 (file['State']))

    # st.write('You selected:', option)

    #---------------------------------------------

		st.warning("All Graph and Data is only for Confirm Case.")


		state = file['State'] 
		total_case = file['Confirm_Case']

		fig = go.Figure(
		go.Pie(labels = state, values = total_case, hoverinfo = "label + percent", textinfo = "value"))

		st.header("Pie chart of Covid-19, All State of India.")
		st.plotly_chart(fig)

    #----------------------------------------------

		dict2 = {'State': file['State'],
		        'ConfirmCase': file['Confirm_Case']}

		st.header("Bar Graph of Covid-19, All State of India.")
    
		df2 = pd.DataFrame(dict2)
		fig = px.bar(        
		        df2,
		        x = "State",
		        y = "ConfirmCase"
		    )
		st.plotly_chart(fig)

    #------------------------------------------


    #------------------------------------------------    

		df = pd.DataFrame(dict(
		State = file['State'],
		ConfirmCase = file['Confirm_Case']
		))

		st.header("Line Chart of Covid-19, All State of India.")
		fig2 = px.line(        
		    df, #Data Frame
		    x = "State", #Columns from the data frame
		    y = "ConfirmCase",
		)

		fig2.update_traces(line_color = "red")
		st.plotly_chart(fig2)





		
			
# st.header("C R E A T E D   BY   R A H U L    S H R E E B A S T A V")		

if __name__ == '__main__':
	app()