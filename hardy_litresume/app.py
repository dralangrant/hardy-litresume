import streamlit as st
import streamlit.components.v1 as components
import abt, skl, exp, edu
    
PAGES = {
"About Me": abt,
"Experience": exp,
"Skills & Accomplishments": skl,
"Education": edu
}

pic = 'https://media-exp1.licdn.com/dms/image/C5603AQFmDxcAQifEhw/profile-displayphoto-shrink_400_400/0/1631820862744?e=1637193600&v=beta&t=n-bEqGYwfKWhklNJwH-TDn67uqI_r5sHohi9D50Y8qI'

st.sidebar.image(pic, width=180, output_format='auto')
st.sidebar.title('David Hardy | Tampa, FL')
selection = st.sidebar.radio("", list(PAGES.keys()))
st.sidebar.header('My Contact Info')
st.sidebar.write('(225) 610-8522')
st.sidebar.markdown('<a href="mailto:dhardy314@gmail.com">Email Me</a>', unsafe_allow_html=True)
st.sidebar.write('[LinkedIn Profile](https://www.linkedin.com/in/david-hardy77/)')
st.sidebar.markdown("<a href='https://drive.google.com/file/d/1l-BlMZealft-cWYFS4KuVRH_WV01lC9F/view?usp=sharing' download='https://drive.google.com/file/d/1l-BlMZealft-cWYFS4KuVRH_WV01lC9F/view?usp=sharing' target='_blank'><button>The Res Dispenser</button></a>", unsafe_allow_html=True)

st.title('David Hardy')
st.header('Sales | Service | Business Development')
st.markdown('Tampa, FL | (225) 610-8522 | <a href="mailto:dhardy314@gmail.com">dhardy314@gmail.com</a> | <a href="https://www.linkedin.com/in/david-hardy77/" target="_blank">LinkedIn</a>', unsafe_allow_html=True)

page = PAGES[selection]
page.app()