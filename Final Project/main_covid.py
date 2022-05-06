import streamlit as st
from multiapp import MultiApp
from apps import home, data, model # import your app modules here

st.set_page_config(page_title = "Covid-19", page_icon=":earth_africa:", layout="wide")
st.title('WELCOME TO DATA VISUALIZATION')
with st.container():
    st.write("---")
st.subheader('COVId_19')
app = MultiApp()

st.markdown("")

# Add all your application here
app.add_app("Home", home.app)
app.add_app("Data", data.app)
app.add_app("Model", model.app)


# with st.container():
#     left_column, right_column = st.columns(2)

#     with left_column:
#         st.info("color")
#     with right_column:
#         st.warning("red")

# The main app
app.run()
