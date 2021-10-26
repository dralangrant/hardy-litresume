import streamlit as st

def peacock():
    st.subheader('Peacock Alley Remodeling | Tampa, FL')
    st.write('**Sales Consultant | May 2021 - Present**')
    st.markdown('''
    * I assess the wants, needs, and budgets of new leads in order to offer an appropriate solution, considering variables like design, materials, and labor.
    * I work with each client to build a custom scope of work that I oversee through installation.
    * Most of my time is spent finding and converting new opportunities, prioritizing my schedule and current projects, and maintaining rapport with my customers.
    * Exceeded my first month revenue goal of $60k to generate over $124k
    ''')

def french_mkt():
    st.subheader('French Market Bistro | Baton Rouge, LA')
    st.write('**Server | Oct 2020 - May 2021**')
    st.markdown('''
    * Created long-term customer relationships that contributed to an overall sales growth of $240,000 annually.
    * Managed the restaurant’s opening and closing procedures according to service industry standards
    * Provided elite level service to guests in a fine dining atmosphere to ensure customer satisfaction and increase customer loyalty.
    ''')

def rum_house():
    st.subheader('The Rum House | Baton Rouge, LA')
    st.write('**Bartender | Aug 2018 - Mar 2020**')
    st.markdown('''
    * Consistently led front of house sales bringing in over $310,000 in company revenue.
    * Assisted management to facilitate effective inventory management and supply ordering.
    * Capitalized on opportunities to upsell special food and beverage options, driving revenue and increasing restaurant profits.
    ''')

def perf_pltr():
    st.subheader('The Perfect Platter Catering Co. | Baton Rouge, LA')
    st.write('**Business Development Manager | Aug 2016 - Aug 2018**')
    st.markdown('''
    * Coordinated business-to-business sales and marketing strategies producing over $245,000 in new business.
    * Developed lasting relationships with existing customers and established new accounts with various local companies.
    * Served as marketing coordinator with responsibilities that included but were not limited to market outreach, promo design, and social media management.
    ''')

def levee():
    st.subheader('The Levee Bar | Baton Rouge, LA')
    st.write('**Owner / Operator | Jun 2014 - Aug 2016**')
    st.markdown('''
    * Acquired failing bar alongside business partner and turned the business profitable in less than two years by implementing new accounting, marketing, and employee training strategies generating $820,000 in annual sales.
    * Oversaw all daily operations and managerial duties including cash management and bookkeeping.
    * Innovatively created a grassroots marketing campaign that integrated interactive social media practices generating new customer business and loyalty.
    * Initiated a complete staff overhaul and developed an upgraded new-hire training program improving overall employee efficiency.
    * After establishing a profitable and sustainable business, sold restaurant for a profit through negotiation efforts.
    ''')

def app():
    st.header('**Work Experience**')
    peacock()
    french_mkt()
    rum_house()
    perf_pltr()
    levee()
