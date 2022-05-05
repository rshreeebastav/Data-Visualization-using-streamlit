import streamlit as st
from PIL import Image
from PIL import Image 
@st.cache
def load_image(image_file):
	img = Image.open(image_file)
	return img 

def app():
    st.write("""
       About COVID_19
    """)
    video1 = open("coronovirus.mp4","rb")
    st.video(video1)
    # st.title('Home')
    
    st.write("The COVID-19 pandemic in India is a part of the worldwide pandemic of coronavirus disease 2019 (COVID-19) caused by severe acute respiratory syndrome coronavirus 2 (SARS-CoV-2). As of 14 April 2022, according to official figures, India has the second-highest number of confirmed cases in the world (after the United States of America) with 43,038,016 reported cases of COVID-19 infection and the third-highest number of COVID-19 deaths (after the United States and Brazil) at 521,736] deaths. ")
    st.write("The first cases of COVID-19 in India were reported on 30 January 2020 in three towns of Kerala, among three Indian medical students who had returned from Wuhan, the epicenter of the pandemic. Lockdowns were announced in Kerala on 23 March, and in the rest of the country on 25 March. On 10 June, India's recoveries exceeded active cases for the first time. Infection rates started to drop in September, along with the number of new and active cases. Daily cases peaked mid-September with over 90,000 cases reported per-day, dropping to below 15,000 in January 2021.[13] A second wave beginning in March 2021 was much more devastating than the first, with shortages of vaccines, hospital beds, oxygen cylinders and other medical supplies in parts of the country.[13] By late April, India led the world in new and active cases. ")
    st.write("India began its vaccination programme on 16 January 2021 with AstraZeneca vaccine (Covishield) and the indigenous Covaxin. Later, Sputnik V and the Moderna vaccine was approved for emergency use too. As of 8 January 2022, the country had administered over 1.5 billion vaccine doses. On 21 October 2021, at 9:47 AM according to the Co-WIN portal, India crossed 100 crore (1 billion) doses. ")
    image = Image.open('corona.jpg')
    st.image(image)
    st.subheader("To prevent the spread of COVID-19:")
    st.write("Maintain a safe distance from others (at least 1 metre), even if they don’t appear to be sick.")
    st.write("Wear a mask in public, especially indoors or when physical distancing is not possible.")
    st.write("Choose open, well-ventilated spaces over closed ones. Open a window if indoors.")
    st.write("Clean your hands often. Use soap and water, or an alcohol-based hand rub.")
    st.write("Get vaccinated when it’s your turn. Follow local guidance about vaccination.")
    st.write("Cover your nose and mouth with your bent elbow or a tissue when you cough or sneeze.")
    st.write("Stay home if you feel unwell.")
    st.subheader("Click here to get more Information of corona Virus")
    st.write("https://en.wikipedia.org/wiki/COVID-19")
    st.header("C R E A T E D BY R A H U L S H R E E B A S T A V")


    
