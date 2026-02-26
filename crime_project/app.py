import streamlit as st
import services
import model
import pandas as pd
from datetime import date
import plotly.express as px

st.set_page_config(page_title="Crime Intelligence System",layout="wide")

st.title("🚔 Crime Pattern Analysis & Prediction System")

menu=st.sidebar.radio("Navigation",
["Dashboard","Add Record","Manage Data","Analytics","Prediction","Hotspots"])

df=services.get_data()

# ---------------- DASHBOARD ----------------
if menu=="Dashboard":

    st.subheader("System Overview")

    if len(df)==0:
        st.warning("No crime records available")
    else:
        c1,c2,c3=st.columns(3)
        c1.metric("Total Crimes",len(df))
        c2.metric("Locations",df["location"].nunique())
        c3.metric("Crime Types",df["crime_type"].nunique())

        fig=px.histogram(df,x="crime_type",color="crime_type")
        st.plotly_chart(fig,use_container_width=True)

# ---------------- ADD ----------------
elif menu=="Add Record":

    st.subheader("Insert Crime Record")

    d=st.date_input("Date",date.today())
    c=st.text_input("Crime Type")
    lat=st.number_input("Latitude")
    lon=st.number_input("Longitude")
    loc=st.text_input("Location")

    if st.button("Save"):
        services.add_crime(str(d),c,lat,lon,loc)
        st.success("Record Saved")

# ---------------- MANAGE ----------------
elif menu=="Manage Data":

    st.subheader("Database Records")

    if len(df)==0:
        st.info("No data")
    else:
        st.dataframe(df,use_container_width=True)

        id_del=st.number_input("Enter ID to delete",step=1)

        if st.button("Delete Record"):
            services.remove(id_del)
            st.success("Deleted")

# ---------------- ANALYTICS ----------------
elif menu=="Analytics":

    st.subheader("Crime Trends")

    if len(df)==0:
        st.warning("No data")
    else:
        df["date"]=pd.to_datetime(df["date"])

        trend=df.groupby(df["date"].dt.date).size()

        st.line_chart(trend)

        pie=px.pie(df,names="crime_type")
        st.plotly_chart(pie)

# ---------------- PREDICTION ----------------
elif menu=="Prediction":

    st.subheader("Crime Prediction Panel")

    lat=st.number_input("Latitude",value=13.0)
    lon=st.number_input("Longitude",value=80.0)
    month=st.slider("Month",1,12)

    if st.button("Predict Crime"):
        crime,risk=model.predict(lat,lon,month)

        st.success(f"Prediction: {crime}")
        st.error(f"Risk Level: {risk}")

# ---------------- MAP ----------------
elif menu=="Hotspots":

    st.subheader("Crime Hotspot Map")

    if len(df)==0:
        st.warning("No data")
    else:
        st.map(df[["latitude","longitude"]])
