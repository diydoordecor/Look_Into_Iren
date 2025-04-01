import streamlit as st
import pandas as pd

# Set page configuration
st.set_page_config(page_title="Iris Energy Financial Dashboard", layout="wide")

# Custom CSS for IREN branding
st.markdown("""
<style>
    body { font-family: Arial, sans-serif; }
    .stApp { background-color: #FFFFFF; }
    h1, h2, h3, h4 { color: #003087; }
    .stTable { border: 1px solid #E0E0E0; }
</style>
""", unsafe_allow_html=True)

# Sidebar for projection inputs
st.sidebar.header("Projection Inputs")
bitcoin_price = st.sidebar.slider("Bitcoin Price ($)", 50000, 100000, 85000, 1000)
hashrate_q3 = st.sidebar.slider("Hashrate Q3 FY25 (EH/s)", 30.0, 40.0, 35.0, 0.5)
hashrate_q4 = st.sidebar.slider("Hashrate Q4 FY25 (EH/s)", 40.0, 60.0, 45.0, 0.5)

# Historical Data Definitions

## Annual Historical Data (in $M)
df_annual = pd.DataFrame({
    "FY23": [75.5, 0, 75.5, 1.4, -171.9],
    "FY24": [184.1, 3.1, 188.8, 54.7, -29.0],
}, index=[
    "Bitcoin Mining Revenue",
    "AI Cloud Services Revenue",
    "Total Revenue",
    "Adjusted EBITDA",
    "Net Income/Loss",
])
format_dict_annual = {col: "${:.2f}M" for col in df_annual.index}
df_annual_formatted = df_annual.style.format(format_dict_annual).set_properties(**{'text-align': 'center'}).set_table_styles([
    {'selector': 'th', 'props': [('background-color', '#003087'), ('color', 'white')]}
])

## Quarterly Historical Data (in $M)
df_quarterly = pd.DataFrame({
    "Q1 FY25": [49.6, 3.2, 52.8, 2.6, -51.7],
    "Q2 FY25": [113.5, 2.7, 116.2, 62.6, 18.9],
}, index=df_annual.index)
df_quarterly_formatted = df_quarterly.style.format(format_dict_annual).set_properties(**{'text-align': 'center'}).set_table_styles([
    {'selector': 'th', 'props': [('background-color', '#003087'), ('color', 'white')]}
])

# Monthly Data Definitions

## Bitcoin Mining Data
df_bitcoin_jun23_aug23 = pd.DataFrame({
    'Jun-23': [5637, 169, 428, 11683, 5572, 27211, 13011],
    'Jul-23': [5562, 170, 423, 12660, 6552, 29939, 15494],
    'Aug-23': [5493, 168, 410, 11459, 4342, 27937, 10586]
}, index=[
    'Average operating hashrate (PH/s)', 'Renewable energy usage (MW)', 'Bitcoin mined',
    'Mining revenue (US$000)', 'Electricity costs (US$000)', 'Revenue per Bitcoin (US$)',
    'Electricity costs per Bitcoin (US$)'
])

df_bitcoin_sep23_nov23 = pd.DataFrame({
    'Sep-23': [5554, 168, 390, 10278, 5354, 26331, 13717],
    'Oct-23': [5571, 166, 376, 11159, 5868, 29673, 15604],
    'Nov-23': [5551, 164, 369, 13714, 5730, 37155, 15524]
}, index=df_bitcoin_jun23_aug23.index)

df_bitcoin_dec23_feb24 = pd.DataFrame({
    'Dec-23': [5576, 161, 399, 17174, 5926, 43056, 14858],
    'Jan-24': [5642, 163, 341, 14466, 6376, 42436, 18705],
    'Feb-24': [6299, 174, 310, 15212, 6241, 49134, 20158]
}, index=df_bitcoin_jun23_aug23.index)

df_bitcoin_mar_may_24 = pd.DataFrame({
    'Mar-24': [7107, 195, 353, 23705, 7172, 67235, 20343],
    'Apr-24': [8238, 220, 358, 23691, 7002, 66210, 19569],
    'May-24': [9414, 246, 230, 15079, 8167, 65498, 35475]
}, index=df_bitcoin_jun23_aug23.index)

df_bitcoin_jun_aug_24 = pd.DataFrame({
    'Jun-24': [9316, 246, 233, 15490, 9183, 41, 66571, 39466],
    'Jul-24': [9008, 241, 222, 13592, 13674, -19, 61306, 61677],
    'Aug-24': [10940, 246, 245, 14985, 7341, 51, 61150, 29958]
}, index=[
    'Average operating hashrate (PH/s)', 'Renewable energy usage (MW)', 'Bitcoin mined',
    'Mining revenue (US$000)', 'Electricity costs (US$000)', 'Hardware profit margin (%)',
    'Revenue per Bitcoin (US$)', 'Electricity cost per Bitcoin (US$)'
])

df_bitcoin_oct_dec_24 = pd.DataFrame({
    'Oct-24': [19.9, 439, 64165, -18896, 28.2, -8.3, 19.9, 71],
    'Nov-24': [19.7, 379, 86065, -22575, 32.6, -8.6, 24.1, 74],
    'Dec-24': [28.1, 529, 98524, -22799, 52.1, -12.1, 40.1, 77]
}, index=[
    'Average operating hashrate (EH/s)', 'Bitcoin mined (BTC)', 'Revenue (per Bitcoin) ($)',
    'Electricity cost (per Bitcoin) ($)', 'Mining revenue ($m)', 'Electricity costs ($m)',
    'Hardware profit ($m)', 'Hardware profit margin (%)'
])

## AI Cloud Services Data
df_ai_mar_may_24 = pd.DataFrame({
    'Mar-24': [408, 9, 98], 'Apr-24': [581, 7, 99], 'May-24': [892, 16, 98]
}, index=['AI Cloud Services revenue (US$000)', 'Electricity costs (US$000)', 'Hardware profit margin (%)'])

df_ai_jun_aug_24 = pd.DataFrame({
    'Jun-24': [1078, 20, 98], 'Jul-24': [1266, 19, 98], 'Aug-24': [1290, 20, 98]
}, index=df_ai_mar_may_24.index)

df_ai_oct_dec_24 = pd.DataFrame({
    'Oct-24': [1.0, -0.03, 0.9, 97], 'Nov-24': [0.9, -0.05, 0.9, 97], 'Dec-24': [0.8, -0.02, 0.8, 98]
}, index=['AI Cloud Services revenue ($m)', 'Electricity costs ($m)', 'Hardware profit ($m)', 'Hardware profit margin (%)'])

# Processing Functions
def process_bitcoin_df(df):
    df_processed = df.copy()
    if 'Average operating hashrate (PH/s)' in df.index:
        df_processed.loc['Average operating hashrate (EH/s)'] = df_processed.loc['Average operating hashrate (PH/s)'] / 1000
        df_processed = df_processed.drop('Average operating hashrate (PH/s)', axis=0)
    if 'Bitcoin mined' in df.index:
        df_processed.loc['Bitcoin mined (BTC)'] = df_processed.loc['Bitcoin mined']
        df_processed = df_processed.drop('Bitcoin mined', axis=0)
    if 'Mining revenue (US$000)' in df.index:
        df_processed.loc['Mining revenue ($m)'] = df_processed.loc['Mining revenue (US$000)'] / 1000
        df_processed = df_processed.drop('Mining revenue (US$000)', axis=0)
    if 'Electricity costs (US$000)' in df.index:
        df_processed.loc['Electricity costs ($m)'] = df_processed.loc['Electricity costs (US$000)'] / 1000
        df_processed = df_processed.drop('Electricity costs (US$000)', axis=0)
    if 'Revenue per Bitcoin (US$)' in df.index:
        df_processed.loc['Revenue (per Bitcoin) ($)'] = df_processed.loc['Revenue per Bitcoin (US$)']
        df_processed = df_processed.drop('Revenue per Bitcoin (US$)', axis=0)
    if 'Electricity costs per Bitcoin (US$)' in df.index:
        df_processed.loc['Electricity cost (per Bitcoin) ($)'] = df_processed.loc['Electricity costs per Bitcoin (US$)']
        df_processed = df_processed.drop('Electricity costs per Bitcoin (US$)', axis=0)
    return df_processed

def process_ai_df(df):
    df_processed = df.copy()
    if 'AI Cloud Services revenue (US$000)' in df.index:
        df_processed.loc['AI Cloud Services revenue ($m)'] = df_processed.loc['AI Cloud Services revenue (US$000)'] / 1000
        df_processed = df_processed.drop('AI Cloud Services revenue (US$000)', axis=0)
    if 'Electricity costs (US$000)' in df.index:
        df_processed.loc['Electricity costs ($m)'] = df_processed.loc['Electricity costs (US$000)'] / 1000
        df_processed = df_processed.drop('Electricity costs (US$000)', axis=0)
    return df_processed

# Consolidate Monthly Data
df_bitcoin_all = pd.concat([
    process_bitcoin_df(df_bitcoin_jun23_aug23),
    process_bitcoin_df(df_bitcoin_sep23_nov23),
    process_bitcoin_df(df_bitcoin_dec23_feb24),
    process_bitcoin_df(df_bitcoin_mar_may_24),
    process_bitcoin_df(df_bitcoin_jun_aug_24),
    df_bitcoin_oct_dec_24
], axis=1)

df_ai_all = pd.concat([
    process_ai_df(df_ai_mar_may_24),
    process_ai_df(df_ai_jun_aug_24),
    df_ai_oct_dec_24
], axis=1)

# Projection Calculations
mining_rate = 17  # BTC per EH/s per month
ai_revenue_proj = 3  # $M per quarter

# Q3 FY25
bitcoin_mined_q3 = hashrate_q3 * mining_rate * 3
bitcoin_revenue_q3 = (bitcoin_mined_q3 * bitcoin_price) / 1e6
total_revenue_q3 = bitcoin_revenue_q3 + ai_revenue_proj
costs_q3 = (hashrate_q3 / 50) * 89.6
ebitda_q3 = total_revenue_q3 - costs_q3

# Q4 FY25
bitcoin_mined_q4 = hashrate_q4 * mining_rate * 3
bitcoin_revenue_q4 = (bitcoin_mined_q4 * bitcoin_price) / 1e6
total_revenue_q4 = bitcoin_revenue_q4 + ai_revenue_proj
costs_q4 = (hashrate_q4 / 50) * 89.6
ebitda_q4 = total_revenue_q4 - costs_q4

# FY25 Total
total_revenue_fy25 = df_quarterly.loc["Total Revenue"].sum() + total_revenue_q3 + total_revenue_q4
ebitda_fy25 = df_quarterly.loc["Adjusted EBITDA"].sum() + ebitda_q3 + ebitda_q4

df_projections = pd.DataFrame({
    "Q3 FY25": [bitcoin_revenue_q3, ai_revenue_proj, total_revenue_q3, ebitda_q3],
    "Q4 FY25": [bitcoin_revenue_q4, ai_revenue_proj, total_revenue_q4, ebitda_q4],
    "FY25": [
        df_quarterly.loc["Bitcoin Mining Revenue"].sum() + bitcoin_revenue_q3 + bitcoin_revenue_q4,
        df_quarterly.loc["AI Cloud Services Revenue"].sum() + ai_revenue_proj * 2,
        total_revenue_fy25,
        ebitda_fy25,
    ],
}, index=["Bitcoin Mining Revenue", "AI Cloud Services Revenue", "Total Revenue", "Adjusted EBITDA"])
df_projections_formatted = df_projections.style.format(format_dict_annual).set_properties(**{'text-align': 'center'}).set_table_styles([
    {'selector': 'th', 'props': [('background-color', '#003087'), ('color', 'white')]}
])

# Dashboard Layout
st.title("IREN Financial Dashboard")
st.markdown("Explore historical financials and projections.")

tab1, tab2 = st.tabs(["Historical Data", "Projections"])

with tab1:
    st.header("Annual Historical Data")
    st.dataframe(df_annual_formatted)

    st.header("Quarterly Historical Data")
    st.dataframe(df_quarterly_formatted)

    st.header("Monthly Data")

    # Bitcoin Mining
    st.subheader("Bitcoin Mining")
    months_bitcoin = df_bitcoin_all.columns.tolist()
    month_indices = list(range(len(months_bitcoin)))
    slider_bitcoin = st.slider(
        "Select month range for Bitcoin Mining",
        0, len(months_bitcoin) - 1, (0, len(months_bitcoin) - 1),
        help="Slide to select the range of months to display."
    )
    selected_months_bitcoin = months_bitcoin[slider_bitcoin[0]:slider_bitcoin[1] + 1]
    df_bitcoin_display = df_bitcoin_all[selected_months_bitcoin]

    format_dict_bitcoin = {
        'Average operating hashrate (EH/s)': '{:.2f}',
        'Renewable energy usage (MW)': '{:.0f}',
        'Bitcoin mined (BTC)': '{:.0f}',
        'Mining revenue ($m)': '${:.2f}m',
        'Electricity costs ($m)': '${:.2f}m',
        'Hardware profit ($m)': '${:.2f}m',
        'Hardware profit margin (%)': '{:.2f}%',
        'Revenue (per Bitcoin) ($)': '${:,.2f}',
        'Electricity cost (per Bitcoin) ($)': '${:,.2f}',
    }
    st.dataframe(df_bitcoin_display.style.format(format_dict_bitcoin).set_properties(**{'text-align': 'center'}).set_table_styles([
        {'selector': 'th', 'props': [('background-color', '#003087'), ('color', 'white')]}
    ]))

    # AI Cloud Services
    st.subheader("AI Cloud Services")
    months_ai = df_ai_all.columns.tolist()
    month_indices_ai = list(range(len(months_ai)))
    slider_ai = st.slider(
        "Select month range for AI Cloud Services",
        0, len(months_ai) - 1, (0, len(months_ai) - 1),
        help="Slide to select the range of months to display."
    )
    selected_months_ai = months_ai[slider_ai[0]:slider_ai[1] + 1]
    df_ai_display = df_ai_all[selected_months_ai]

    format_dict_ai = {
        'AI Cloud Services revenue ($m)': '${:.2f}m',
        'Electricity costs ($m)': '${:.2f}m',
        'Hardware profit ($m)': '${:.2f}m',
        'Hardware profit margin (%)': '{:.2f}%',
    }
    st.dataframe(df_ai_display.style.format(format_dict_ai).set_properties(**{'text-align': 'center'}).set_table_styles([
        {'selector': 'th', 'props': [('background-color', '#003087'), ('color', 'white')]}
    ]))

with tab2:
    st.header("Projections")
    st.dataframe(df_projections_formatted)

    st.subheader("Total Revenue Comparison")
    revenue_comparison = pd.DataFrame({
        "Period": ["FY23", "FY24", "FY25 (proj)"],
        "Total Revenue": [df_annual.loc["Total Revenue", "FY23"], df_annual.loc["Total Revenue", "FY24"], total_revenue_fy25],
    })
    st.bar_chart(revenue_comparison.set_index("Period"))

    st.subheader("Quarterly Revenue Breakdown")
    periods = ["Q1 FY25", "Q2 FY25", "Q3 FY25 (proj)", "Q4 FY25 (proj)"]
    bitcoin_revenue = [df_quarterly.loc["Bitcoin Mining Revenue", "Q1 FY25"], df_quarterly.loc["Bitcoin Mining Revenue", "Q2 FY25"], bitcoin_revenue_q3, bitcoin_revenue_q4]
    ai_revenue = [df_quarterly.loc["AI Cloud Services Revenue", "Q1 FY25"], df_quarterly.loc["AI Cloud Services Revenue", "Q2 FY25"], ai_revenue_proj, ai_revenue_proj]
    df_stacked = pd.DataFrame({"Period": periods, "Bitcoin Mining": bitcoin_revenue, "AI Cloud Services": ai_revenue})
    st.bar_chart(df_stacked.set_index("Period"))

    st.subheader("Quarterly Adjusted EBITDA")
    ebitda_values = [df_quarterly.loc["Adjusted EBITDA", "Q1 FY25"], df_quarterly.loc["Adjusted EBITDA", "Q2 FY25"], ebitda_q3, ebitda_q4]
    df_ebitda = pd.DataFrame({"Period": periods, "Adjusted EBITDA": ebitda_values})
    st.line_chart(df_ebitda.set_index("Period"))

st.markdown("---")
st.markdown("© 2024 Iris Energy ($IREN) | Data Source: IREN Financial Reports", unsafe_allow_html=True)