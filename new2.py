import streamlit as st
import pandas as pd
import numpy as np
from datetime import datetime, timedelta

# Page configuration
st.set_page_config(
    page_title="PlanGuru Budgeting",
    page_icon="📊",
    layout="wide",
    initial_sidebar_state="expanded"
)

# Custom CSS
st.markdown("""
<style>
    .main-header {
        font-size: 3rem;
        color: #1E3A8A;
        text-align: center;
    }
    .sub-header {
        font-size: 1.5rem;
        color: #3B82F6;
        border-bottom: 2px solid #3B82F6;
        padding-bottom: 0.2rem;
        margin-top: 2rem;
    }
    .budget-card {
        background-color: #F0F9FF;
        border-radius: 0.5rem;
        padding: 1.5rem;
        box-shadow: 0 4px 6px rgba(0, 0, 0, 0.1);
        margin-bottom: 1rem;
    }
    .positive-value {
        color: #059669;
        font-weight: bold;
    }
    .negative-value {
        color: #DC2626;
        font-weight: bold;
    }
</style>
""", unsafe_allow_html=True)

# App header
st.markdown('<h1 class="main-header">📊 PlanGuru Budgeting</h1>', unsafe_allow_html=True)
st.markdown("### Strategic Financial Planning for Emerging Companies")

# Introduction
st.write("""
Creating and sticking to a realistic budget is vital for your organization's financial health, 
but it can be challenging for emerging companies. PlanGuru helps you manage cash flow, 
make projections months in advance, and divide your assets strategically.
""")

# Sidebar for navigation
st.sidebar.title("Navigation")
app_mode = st.sidebar.selectbox("Choose a section", 
                               ["Dashboard", "Budget Creation", "Cash Flow Management", 
                                "Financial Projections", "Asset Allocation"])

# Sample data generation functions
def generate_income_data():
    dates = pd.date_range(start='2023-01-01', end='2023-12-31', freq='M')
    data = {
        'Month': dates.strftime('%B'),
        'Revenue': [50000, 52000, 48000, 55000, 60000, 65000, 70000, 75000, 80000, 85000, 90000, 95000],
        'Expenses': [45000, 46000, 47000, 48000, 49000, 50000, 51000, 52000, 53000, 54000, 55000, 56000],
        'Profit': [5000, 6000, 1000, 7000, 11000, 15000, 19000, 23000, 27000, 31000, 35000, 39000]
    }
    return pd.DataFrame(data)

def generate_cash_flow_data():
    dates = pd.date_range(start='2023-01-01', periods=12, freq='M')
    data = {
        'Month': dates.strftime('%B'),
        'Cash In': [45000, 47000, 43000, 50000, 55000, 60000, 65000, 70000, 75000, 80000, 85000, 90000],
        'Cash Out': [40000, 41000, 42000, 43000, 44000, 45000, 46000, 47000, 48000, 49000, 50000, 51000],
        'Net Cash Flow': [5000, 6000, 1000, 7000, 11000, 15000, 19000, 23000, 27000, 31000, 35000, 39000]
    }
    return pd.DataFrame(data)

def generate_asset_allocation_data():
    data = {
        'Category': ['Operations', 'Marketing', 'R&D', 'Salaries', 'Infrastructure', 'Emergency Fund'],
        'Percentage': [40, 15, 10, 25, 7, 3],
        'Amount': [200000, 75000, 50000, 125000, 35000, 15000]
    }
    return pd.DataFrame(data)

# Dashboard
if app_mode == "Dashboard":
    st.markdown('<h2 class="sub-header">Financial Overview</h2>', unsafe_allow_html=True)
    
    # Key metrics
    col1, col2, col3, col4 = st.columns(4)
    with col1:
        st.metric("Total Revenue", "$756,000", "12%")
    with col2:
        st.metric("Total Expenses", "$586,000", "8%")
    with col3:
        st.metric("Net Profit", "$170,000", "22%")
    with col4:
        st.metric("Cash Flow", "$189,000", "15%")
    
    # Income and expenses chart
    st.markdown("### Income vs Expenses")
    income_df = generate_income_data()
    
    chart_data = pd.DataFrame({
        'Month': income_df['Month'],
        'Revenue': income_df['Revenue'],
        'Expenses': income_df['Expenses']
    })
    
    st.bar_chart(chart_data.set_index('Month'))
    
    # Profit trend
    st.markdown("### Profit Trend")
    st.line_chart(income_df.set_index('Month')['Profit'])

# Budget Creation
elif app_mode == "Budget Creation":
    st.markdown('<h2 class="sub-header">Create Your Budget</h2>', unsafe_allow_html=True)
    
    st.write("Plan and allocate your financial resources for the upcoming period.")
    
    col1, col2 = st.columns([2, 1])
    
    with col1:
        with st.form("budget_form"):
            st.subheader("Budget Details")
            budget_name = st.text_input("Budget Name", "Q3 2023 Budget")
            budget_period = st.selectbox("Budget Period", ["Monthly", "Quarterly", "Annual"])
            budget_amount = st.number_input("Total Budget Amount ($)", min_value=0, value=100000, step=1000)
            
            st.subheader("Expense Categories")
            categories = st.text_area("Enter expense categories (one per line)", "Operations\nMarketing\nR&D\nSalaries\nInfrastructure\nEmergency Fund")
            
            submitted = st.form_submit_button("Create Budget")
            if submitted:
                st.success(f"Budget '{budget_name}' created successfully!")
    
    with col2:
        st.markdown("### Budget Tips")
        st.info("""
        - Be realistic about your income and expenses
        - Include a contingency fund (5-10%)
        - Review past spending patterns
        - Align budget with business goals
        - Monitor and adjust regularly
        """)

# Cash Flow Management
elif app_mode == "Cash Flow Management":
    st.markdown('<h2 class="sub-header">Cash Flow Management</h2>', unsafe_allow_html=True)
    
    cash_flow_df = generate_cash_flow_data()
    
    col1, col2 = st.columns(2)
    
    with col1:
        st.subheader("Monthly Cash Flow")
        cash_flow_chart_data = pd.DataFrame({
            'Month': cash_flow_df['Month'],
            'Cash In': cash_flow_df['Cash In'],
            'Cash Out': cash_flow_df['Cash Out']
        })
        st.bar_chart(cash_flow_chart_data.set_index('Month'))
    
    with col2:
        st.subheader("Net Cash Flow")
        net_cash_data = pd.DataFrame({
            'Month': cash_flow_df['Month'],
            'Net Cash Flow': cash_flow_df['Net Cash Flow']
        })
        st.bar_chart(net_cash_data.set_index('Month'))
    
    # Cash flow projections
    st.subheader("Cash Flow Projections")
    projection_months = st.slider("Projection Period (months)", 3, 24, 12)
    
    # Simple projection calculation
    last_cash_flow = cash_flow_df['Net Cash Flow'].iloc[-1]
    projected = [last_cash_flow * (1 + i * 0.05) for i in range(projection_months)]
    months = [f"Month {i+1}" for i in range(projection_months)]
    
    projection_data = pd.DataFrame({
        'Month': months,
        'Projected Cash Flow': projected
    })
    st.line_chart(projection_data.set_index('Month'))

# Financial Projections
elif app_mode == "Financial Projections":
    st.markdown('<h2 class="sub-header">Financial Projections</h2>', unsafe_allow_html=True)
    
    st.write("Forecast your company's financial performance based on historical data and growth assumptions.")
    
    col1, col2 = st.columns(2)
    
    with col1:
        st.subheader("Revenue Projection")
        growth_rate = st.slider("Expected Monthly Growth Rate (%)", 0.0, 10.0, 2.5, step=0.5) / 100
        
        # Generate projection data
        months = 12
        current_revenue = 95000  # Last month's revenue from sample data
        projected_revenue = [current_revenue * ((1 + growth_rate) ** i) for i in range(months)]
        projection_months = [f"Month {i+1}" for i in range(months)]
        
        revenue_data = pd.DataFrame({
            'Month': projection_months,
            'Projected Revenue': projected_revenue
        })
        st.line_chart(revenue_data.set_index('Month'))
    
    with col2:
        st.subheader("Expense Projection")
        expense_growth = st.slider("Expected Monthly Expense Growth (%)", 0.0, 10.0, 1.5, step=0.5) / 100
        
        # Generate projection data
        current_expense = 56000  # Last month's expense from sample data
        projected_expense = [current_expense * ((1 + expense_growth) ** i) for i in range(months)]
        
        expense_data = pd.DataFrame({
            'Month': projection_months,
            'Projected Expenses': projected_expense
        })
        st.line_chart(expense_data.set_index('Month'))
    
    # Profit projection
    st.subheader("Profit Projection")
    projected_profit = [projected_revenue[i] - projected_expense[i] for i in range(months)]
    
    profit_data = pd.DataFrame({
        'Month': projection_months,
        'Projected Profit': projected_profit
    })
    st.line_chart(profit_data.set_index('Month'))

# Asset Allocation
elif app_mode == "Asset Allocation":
    st.markdown('<h2 class="sub-header">Strategic Asset Allocation</h2>', unsafe_allow_html=True)
    
    st.write("Divide your assets strategically across different business functions.")
    
    asset_df = generate_asset_allocation_data()
    
    col1, col2 = st.columns(2)
    
    with col1:
        st.subheader("Current Allocation")
        st.dataframe(asset_df)
    
    with col2:
        st.subheader("Allocation Visualization")
        allocation_data = pd.DataFrame({
            'Category': asset_df['Category'],
            'Percentage': asset_df['Percentage']
        })
        st.bar_chart(allocation_data.set_index('Category'))
    
    # Asset allocation adjustment
    st.subheader("Adjust Asset Allocation")
    
    total_budget = st.number_input("Total Budget Amount ($)", min_value=0, value=500000, step=1000)
    
    cols = st.columns(6)
    allocations = {}
    
    with cols[0]:
        operations = st.slider("Operations (%)", 0, 100, 40, key="ops")
        allocations["Operations"] = operations
    with cols[1]:
        marketing = st.slider("Marketing (%)", 0, 100, 15, key="mkt")
        allocations["Marketing"] = marketing
    with cols[2]:
        rnd = st.slider("R&D (%)", 0, 100, 10, key="rnd")
        allocations["R&D"] = rnd
    with cols[3]:
        salaries = st.slider("Salaries (%)", 0, 100, 25, key="sal")
        allocations["Salaries"] = salaries
    with cols[4]:
        infrastructure = st.slider("Infrastructure (%)", 0, 100, 7, key="inf")
        allocations["Infrastructure"] = infrastructure
    with cols[5]:
        emergency = st.slider("Emergency (%)", 0, 100, 3, key="emg")
        allocations["Emergency"] = emergency
    
    total_percentage = sum(allocations.values())
    
    if total_percentage != 100:
        st.error(f"Total allocation must be 100%. Current total: {total_percentage}%")
    else:
        st.success("Allocation percentages are valid!")
        
        # Show allocation amounts
        st.subheader("Allocation Amounts")
        for category, percentage in allocations.items():
            amount = total_budget * (percentage / 100)
            st.write(f"{category}: ${amount:,.2f} ({percentage}%)")

# Footer
st.markdown("---")
st.markdown("""
<div style='text-align: center'>
    <p>PlanGuru Budgeting • Financial Planning for Emerging Companies</p>
    <p>© 2023 PlanGuru. All rights reserved.</p>
</div>
""", unsafe_allow_html=True)
