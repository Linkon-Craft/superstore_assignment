import streamlit as st
import numpy as np
import pandas as pd
import plotly.express as px
from pandasql import sqldf



st.title("Data Vizualization App")
st.set_page_config(page_title="Data Viz App", layout="wide")

with st.expander("Data Preview"): 
    data = pd.read_excel("sample_-_superstore.xls", engine='xlrd')


    st.write(data)

    st.write("Rows:", data.shape[0])
    st.write("Columns:", data.shape[1])

    st.subheader("Column Data Types")
    st.dataframe(data.dtypes)


    st.subheader("Statistical Summary")
    st.dataframe(data.describe())

count_order, count_product_id, count_customer, total_sales,tot_qua, net_rev,total_profit = st.columns(7)

with count_order:
    st.metric("Total Orders", data["Order ID"].nunique())
with count_product_id:
    st.metric("Total Products", data["Product ID"].nunique())  
with count_customer:
    st.metric("Total Customers", data["Customer ID"].nunique())
with total_sales:
    st.metric("Total Sales", f"${data['Sales'].sum():,.2f}")
with tot_qua:   
    st.metric("Total Quantity", f"{data['Quantity'].sum():,.0f}")   
with net_rev:   
    data["Net Revenue"] = (data["Sales"] * data["Quantity"]) - (data["Discount"]* data["Sales"] * data["Quantity"])
    st.metric("Net Revenue", f"{data['Net Revenue'].sum():,.2f}")
with total_profit:
    st.metric("Total Profit", f"${data['Profit'].sum():,.2f}")








first_column, middle_column, last_column = st.columns(3)

with first_column:
    tab1, tab2, tab3 = st.tabs(["Tab 1", "Tab 2", "Tab 3"])

    with tab1:
        st.header("Data Visualization")
        st.subheader("Ship Mode CLass Distribution")
        ShipMode = data['Ship Mode'].value_counts()
        st.bar_chart(ShipMode)

        mode_tab1, mode_tab2, mode_tab3 =  st.tabs(["sales_by_Cats", "cat_by_profit", "Sales_by_Sub-category"])

        with mode_tab1:
            st.subheader("Sales by Category")
            sales_by_category = data.groupby("Category")["Sales"].sum()
            st.bar_chart(sales_by_category)

        with mode_tab2:
            st.subheader("Product by category")
            cat_by_prof = data.groupby("Category")["Profit"].sum()
            st.bar_chart(cat_by_prof)
        
        with mode_tab3:
            st.subheader("Sales by Sub-Category")
            sub_sales = data.groupby("Sub-Category")["Sales"].sum().sort_values(ascending=False)
            st.bar_chart(sub_sales.head(10))

    with tab2:
        st.header("Regional Performance Analysis")
        
        s_tab1, s_tab2 =  st.tabs(["sales_by_reg", "reg_by_profit"])

        with s_tab1:
            st.subheader("Sales by Region")
            sale_region = data.groupby("Region")["Sales"].sum().sort_values(ascending=False)
            st.bar_chart(sale_region)

        with s_tab2:
            st.subheader("Profit by Region")
            region_profit = data.groupby("Region")["Profit"].sum()
            st.bar_chart(region_profit)


with middle_column:
    st.header("Time Series Analysis")
    st.subheader("Monthly Sales Trend")
    data["Order Date"] = pd.to_datetime(data["Order Date"])

    sales_over_time = data.groupby(data["Order Date"].dt.to_period("M"))["Sales"].sum()
    sales_over_time.index = sales_over_time.index.to_timestamp()

    st.line_chart(sales_over_time)

    sales_table = sales_over_time.reset_index()
    sales_table.columns = ["Month", "Total Sales"]

    sales_table["Month"] = sales_table["Month"].dt.strftime("%Y %b")


    st.subheader("Monthly Sales Table")
    st.dataframe(sales_table)
    


    st.subheader("Monthly Profit trend")
    data["Order Date"] = pd.to_datetime(data["Order Date"])

    profit_over_time = data.groupby(data["Order Date"].dt.to_period("M"))["Profit"].sum()
    profit_over_time.index = profit_over_time.index.to_timestamp()

    st.line_chart(profit_over_time)


    st.subheader("Monthly profit Table")
    profit_table = profit_over_time.reset_index()
    profit_table.columns = ["Month", "Total Profit"]

    profit_table["Month"] = profit_table["Month"].dt.strftime("%Y %b")

    st.dataframe(profit_table)

with last_column:
    st.header(" Segment & Ship mode Trends")
    # Streamlit Method
    # segment_summary = (
    # data.groupby("Segment")
    #   .size()
    #   .reset_index(name="Sales")
    # )

    # segment_summary["Percentage"] = (
    #     segment_summary["Sales"] / segment_summary["Sales"].sum() * 100
    # ).round(2).concat('%')

    # segment_summary = segment_summary.sort_values("Sales", ascending=False)

    # st.subheader("Sales by Segment")
    # st.dataframe(segment_summary)
    
    st.subheader("How customer type affect sales")
    query = """
    SELECT
        Segment,
        SUM(Sales) AS Total_Sales,
        ROUND(SUM(Sales) * 100.0 / (SELECT SUM(Sales) FROM data), 2) || '%' AS Percentage
    FROM data
    GROUP BY Segment
    ORDER BY Sales DESC
    """
    result = sqldf(query)

    st.dataframe(result)
    st.bar_chart(
    result.set_index("Segment")["Total_Sales"]
    )

    st.subheader("Profit ratio from customer type")
    profit_query = """
    SELECT
        Segment,
        SUM(Profit) As Total_Profit,
        ROUND(SUM(Profit) * 100.0 / (SELECT SUM(Profit) FROM data), 2) || '%' AS Percentage
    FROM data
    GROUP BY Segment
    ORDER BY Profit DESC
    """

    query_result = sqldf(profit_query)
    st.dataframe(query_result)
    st.bar_chart(
        query_result.set_index("Segment")["Total_Profit"]
    )



        
