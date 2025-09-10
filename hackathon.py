import streamlit as st
import pandas as pd
import numpy as np

# Set page configuration
st.set_page_config(
    page_title="FinScore - Financial Health Assessment",
    page_icon="📊",
    layout="wide",
    initial_sidebar_state="collapsed"
)

# Custom CSS for styling
st.markdown("""
<style>
    /* Main styles */
    .main-header {
        background: linear-gradient(135deg, #2c3e50 0%, #3498db 100%);
        color: white;
        padding: 2rem;
        border-radius: 0 0 10px 10px;
        box-shadow: 0 4px 6px rgba(0, 0, 0, 0.1);
        margin-bottom: 2rem;
    }
    
    .logo-container {
        display: flex;
        align-items: center;
        justify-content: center;
        gap: 15px;
        margin-bottom: 1rem;
    }
    
    .logo {
        font-size: 2.8rem;
        font-weight: bold;
        color: white;
    }
    
    .tagline {
        font-size: 1.2rem;
        opacity: 0.9;
        text-align: center;
        max-width: 600px;
        margin: 0 auto;
    }
    
    .card {
        background: white;
        border-radius: 12px;
        padding: 25px;
        box-shadow: 0 4px 6px rgba(0, 0, 0, 0.1);
        margin-bottom: 25px;
        border-top: 5px solid #3498db;
    }
    
    .card-header {
        display: flex;
        align-items: center;
        margin-bottom: 20px;
        color: #2c3e50;
    }
    
    .card-title {
        font-size: 1.6rem;
        font-weight: 600;
    }
    
    .status {
        display: inline-block;
        padding: 8px 15px;
        border-radius: 20px;
        font-size: 0.9rem;
        font-weight: 500;
        margin-bottom: 15px;
    }
    
    .status-pending {
        background-color: #ffeaa7;
        color: #d35400;
    }
    
    .status-approved {
        background-color: #d1f7c4;
        color: #27ae60;
    }
    
    .status-rejected {
        background-color: #ffcfd2;
        color: #c0392b;
    }
    
    .stButton>button {
        background-color: #3498db;
        color: white;
        border: none;
        border-radius: 8px;
        padding: 12px 25px;
        font-weight: 500;
        box-shadow: 0 3px 5px rgba(0, 0, 0, 0.1);
    }
    
    .stButton>button:hover {
        background-color: #2c3e50;
        color: white;
    }
    
    .progress-bar {
        height: 12px;
        background-color: #e0e0e0;
        border-radius: 10px;
        overflow: hidden;
        margin-bottom: 15px;
    }
    
    .progress-fill {
        height: 100%;
        background: linear-gradient(135deg, #2c3e50 0%, #3498db 100%);
        border-radius: 10px;
        transition: width 1s ease-in-out;
    }
    
    .factor-container {
        margin: 20px 0;
        padding: 15px;
        background: #f8f9fa;
        border-radius: 8px;
    }
    
    .factor-title {
        font-weight: 600;
        margin-bottom: 10px;
        color: #2c3e50;
    }
    
    .result-container {
        margin-top: 25px;
        padding: 20px;
        border-radius: 8px;
    }
    
    .result-success {
        background-color: #d1f7c4;
        border-left: 5px solid #27ae60;
        color: #145214;
    }
    
    .result-warning {
        background-color: #ffeaa7;
        border-left: 5px solid #f39c12;
        color: #7a5a05;
    }
    
    .result-danger {
        background-color: #ffcfd2;
        border-left: 5px solid #e74c3c;
        color: #8a2c2c;
    }
    
    footer {
        text-align: center;
        padding: 30px;
        margin-top: 50px;
        color: #666;
        font-size: 0.9rem;
        background: white;
        border-radius: 10px 10px 0 0;
        box-shadow: 0 -4px 10px rgba(0, 0, 0, 0.05);
    }
</style>
""", unsafe_allow_html=True)

# Initialize session state variables
if 'completed_assessments' not in st.session_state:
    st.session_state.completed_assessments = {
        'credit': False,
        'tax': False,
        'insurance': False
    }

if 'credit_score' not in st.session_state:
    st.session_state.credit_score = 0

if 'tax_result' not in st.session_state:
    st.session_state.tax_result = {}

if 'insurance_score' not in st.session_state:
    st.session_state.insurance_score = 0

# Header section
st.markdown("""
<div class="main-header">
    <div class="logo-container">
        <div class="logo">FinScore</div>
    </div>
    <div class="tagline">Comprehensive Financial Health Assessment for Inclusive Credit Scoring</div>
</div>
""", unsafe_allow_html=True)

# Main container
col1, col2, col3 = st.columns(3)

# Progress bar
completed_count = sum(st.session_state.completed_assessments.values())
progress_percentage = (completed_count / 3) * 100

st.markdown(f"""
<div class="card">
    <h2>Loan Eligibility Progress</h2>
    <div class="progress-bar">
        <div class="progress-fill" style="width: {progress_percentage}%;"></div>
    </div>
    <div style="display: flex; justify-content: space-between;">
        <span>Assessment Completion</span>
        <span>{progress_percentage:.0f}%</span>
    </div>
</div>
""", unsafe_allow_html=True)

# Credit Assessment Card
with col1:
    with st.container():
        st.markdown("""
        <div class="card">
            <div class="card-header">
                <h2 class="card-title">Credit Assessment</h2>
            </div>
            <p>Calculate your credit score based on payment history, credit utilization, length of credit history, new credit, and credit mix.</p>
        """, unsafe_allow_html=True)
        
        status = "status-approved" if st.session_state.completed_assessments['credit'] else "status-pending"
        st.markdown(f'<p class="status {status}">{"Completed" if st.session_state.completed_assessments["credit"] else "Pending"}</p>', unsafe_allow_html=True)
        
        if st.button("Calculate Credit Score", key="credit_btn"):
            st.session_state.show_credit_modal = True

# Tax Calculation Card
with col2:
    with st.container():
        st.markdown("""
        <div class="card">
            <div class="card-header">
                <h2 class="card-title">Tax Calculation</h2>
            </div>
            <p>Calculate your tax bracket, net vs gross income, and tax obligations.</p>
        """, unsafe_allow_html=True)
        
        status = "status-approved" if st.session_state.completed_assessments['tax'] else "status-pending"
        st.markdown(f'<p class="status {status}">{"Completed" if st.session_state.completed_assessments["tax"] else "Pending"}</p>', unsafe_allow_html=True)
        
        if st.button("Calculate Tax", key="tax_btn"):
            st.session_state.show_tax_modal = True

# Insurance Coverage Card
with col3:
    with st.container():
        st.markdown("""
        <div class="card">
            <div class="card-header">
                <h2 class="card-title">Insurance Coverage</h2>
            </div>
            <p>Review your insurance coverage across health, auto, home, and life policies.</p>
        """, unsafe_allow_html=True)
        
        status = "status-approved" if st.session_state.completed_assessments['insurance'] else "status-pending"
        st.markdown(f'<p class="status {status}">{"Completed" if st.session_state.completed_assessments["insurance"] else "Pending"}</p>', unsafe_allow_html=True)
        
        if st.button("Check Insurance", key="insurance_btn"):
            st.session_state.show_insurance_modal = True

# Credit Assessment Modal
if st.session_state.get('show_credit_modal', False):
    st.markdown("---")
    st.header("Credit Score Calculation")
    st.write("Enter your financial information to calculate your credit score (300-850 range)")
    
    with st.expander("Payment History (35%)", expanded=True):
        st.write("Your track record of making timely payments")
        payment_history = st.slider("On-time payment percentage (0-100%)", 0, 100, 95, key="ph_slider")
    
    with st.expander("Credit Utilization (30%)", expanded=True):
        st.write("Your outstanding balances relative to your total credit limits")
        credit_utilization = st.slider("Credit utilization ratio (0-100%)", 0, 100, 25, key="cu_slider")
    
    with st.expander("Length of Credit History (15%)", expanded=True):
        st.write("How long you've had credit accounts")
        credit_history = st.slider("Credit history length (in years)", 0, 50, 5, key="ch_slider")
    
    with st.expander("New Credit (10%)", expanded=True):
        st.write("Recent credit inquiries and new accounts")
        new_credit = st.slider("Number of new credit accounts in past year", 0, 20, 2, key="nc_slider")
    
    with st.expander("Credit Mix (10%)", expanded=True):
        st.write("Variety of credit types (credit cards, mortgage, auto loans, etc.)")
        credit_mix = st.slider("Number of different credit types", 0, 10, 3, key="cm_slider")
    
    if st.button("Calculate Credit Score", key="calc_credit"):
        # Calculate individual factor scores
        payment_score = (payment_history / 100) * 35 * 10
        utilization_score = (1 - min(credit_utilization, 100) / 100) * 30 * 10
        history_score = (min(credit_history, 30) / 30) * 15 * 10
        new_credit_score = (1 - min(new_credit, 10) / 10) * 10 * 10
        mix_score = (min(credit_mix, 5) / 5) * 10 * 10
        
        # Calculate total score (300-850 range)
        total_score = 300 + payment_score + utilization_score + history_score + new_credit_score + mix_score
        total_score = round(min(max(total_score, 300), 850))
        
        # Determine rating
        if total_score >= 800:
            rating = "Excellent"
            rating_color = "#27ae60"
            result_class = "result-success"
        elif total_score >= 740:
            rating = "Very Good"
            rating_color = "#2ecc71"
            result_class = "result-success"
        elif total_score >= 670:
            rating = "Good"
            rating_color = "#f39c12"
            result_class = "result-warning"
        elif total_score >= 580:
            rating = "Fair"
            rating_color = "#e67e22"
            result_class = "result-warning"
        else:
            rating = "Poor"
            rating_color = "#e74c3c"
            result_class = "result-danger"
        
        # Display results
        st.markdown(f"""
        <div class="result-container {result_class}">
            <h3>Credit Score Results</h3>
            <div style="font-size: 2.5rem; font-weight: bold; color: {rating_color}; margin: 15px 0;">
                {total_score}
            </div>
            <div style="color: {rating_color}; font-weight: bold; font-size: 1.2rem; margin-bottom: 15px;">
                {rating}
            </div>
        </div>
        """, unsafe_allow_html=True)
        
        # Mark as completed
        st.session_state.completed_assessments['credit'] = True
        st.session_state.credit_score = total_score
        st.session_state.show_credit_modal = False
        st.rerun()
    
    if st.button("Close", key="close_credit"):
        st.session_state.show_credit_modal = False
        st.rerun()

# Tax Calculation Modal
if st.session_state.get('show_tax_modal', False):
    st.markdown("---")
    st.header("Tax Calculation")
    
    annual_income = st.number_input("Annual Gross Income ($)", min_value=0.0, value=50000.0, step=1000.0)
    filing_status = st.selectbox("Filing Status", ["Single", "Married Filing Jointly", "Head of Household"])
    deductions = st.number_input("Total Deductions ($)", min_value=0.0, value=12500.0, step=1000.0)
    
    if st.button("Calculate Tax", key="calc_tax"):
        taxable_income = annual_income - deductions
        
        # Simplified tax brackets for demonstration
        if filing_status == "Single":
            if taxable_income <= 11000:
                tax_bracket = '10%'
                tax_amount = taxable_income * 0.1
            elif taxable_income <= 44725:
                tax_bracket = '12%'
                tax_amount = 1100 + (taxable_income - 11000) * 0.12
            elif taxable_income <= 95375:
                tax_bracket = '22%'
                tax_amount = 5147 + (taxable_income - 44725) * 0.22
            else:
                tax_bracket = '24%+'
                tax_amount = 16290 + (taxable_income - 95375) * 0.24
        elif filing_status == "Married Filing Jointly":
            if taxable_income <= 22000:
                tax_bracket = '10%'
                tax_amount = taxable_income * 0.1
            elif taxable_income <= 89450:
                tax_bracket = '12%'
                tax_amount = 2200 + (taxable_income - 22000) * 0.12
            elif taxable_income <= 190750:
                tax_bracket = '22%'
                tax_amount = 10294 + (taxable_income - 89450) * 0.22
            else:
                tax_bracket = '24%+'
                tax_amount = 32580 + (taxable_income - 190750) * 0.24
        else:  # Head of Household
            if taxable_income <= 15700:
                tax_bracket = '10%'
                tax_amount = taxable_income * 0.1
            elif taxable_income <= 59850:
                tax_bracket = '12%'
                tax_amount = 1570 + (taxable_income - 15700) * 0.12
            elif taxable_income <= 95350:
                tax_bracket = '22%'
                tax_amount = 6868 + (taxable_income - 59850) * 0.22
            else:
                tax_bracket = '24%+'
                tax_amount = 14678 + (taxable_income - 95350) * 0.24
        
        net_income = annual_income - tax_amount
        
        st.session_state.tax_result = {
            'gross_income': annual_income,
            'taxable_income': taxable_income,
            'tax_bracket': tax_bracket,
            'tax_amount': tax_amount,
            'net_income': net_income
        }
        
        st.markdown(f"""
        <div class="result-container result-success">
            <h3>Tax Calculation Results</h3>
            <p><strong>Gross Income:</strong> ${annual_income:,.2f}</p>
            <p><strong>Taxable Income:</strong> ${taxable_income:,.2f}</p>
            <p><strong>Tax Bracket:</strong> {tax_bracket}</p>
            <p><strong>Estimated Tax:</strong> ${tax_amount:,.2f}</p>
            <p><strong>Net Income:</strong> ${net_income:,.2f}</p>
        </div>
        """, unsafe_allow_html=True)
        
        # Mark as completed
        st.session_state.completed_assessments['tax'] = True
        st.session_state.show_tax_modal = False
        st.rerun()
    
    if st.button("Close", key="close_tax"):
        st.session_state.show_tax_modal = False
        st.rerun()

# Insurance Modal
if st.session_state.get('show_insurance_modal', False):
    st.markdown("---")
    st.header("Insurance Coverage")
    
    health_insurance = st.selectbox("Health Insurance Coverage", 
                                   ["No Coverage", "Basic Coverage", "Comprehensive Coverage"])
    auto_insurance = st.selectbox("Auto Insurance Coverage", 
                                 ["No Coverage", "Liability Only", "Full Coverage"])
    home_insurance = st.selectbox("Home Insurance Coverage", 
                                 ["No Coverage", "Renters Insurance", "Homeowners Insurance"])
    life_insurance = st.selectbox("Life Insurance Coverage", 
                                 ["No Coverage", "Term Life", "Whole Life"])
    
    if st.button("Evaluate Coverage", key="calc_insurance"):
        coverage_score = 0
        recommendations = []
        
        # Evaluate health insurance
        if health_insurance == 'No Coverage':
            recommendations.append('Consider getting health insurance to protect against medical costs')
        elif health_insurance == 'Basic Coverage':
            coverage_score += 25
        else:
            coverage_score += 35
        
        # Evaluate auto insurance
        if auto_insurance == 'No Coverage':
            recommendations.append('Auto insurance is legally required in most states')
        elif auto_insurance == 'Liability Only':
            coverage_score += 15
        else:
            coverage_score += 20
        
        # Evaluate home insurance
        if home_insurance == 'No Coverage':
            recommendations.append('Consider getting home/renters insurance to protect your property')
        elif home_insurance == 'Renters Insurance':
            coverage_score += 15
        else:
            coverage_score += 25
        
        # Evaluate life insurance
        if life_insurance == 'No Coverage':
            recommendations.append('Consider life insurance if you have dependents')
        elif life_insurance == 'Term Life':
            coverage_score += 15
        else:
            coverage_score += 20
        
        if coverage_score >= 70:
            result_class = "result-success"
        elif coverage_score >= 40:
            result_class = "result-warning"
        else:
            result_class = "result-danger"
        
        recommendations_html = ''
        if recommendations:
            recommendations_html = '<h4>Recommendations:</h4><ul>'
            for rec in recommendations:
                recommendations_html += f'<li>{rec}</li>'
            recommendations_html += '</ul>'
        
        st.markdown(f"""
        <div class="result-container {result_class}">
            <h3>Insurance Coverage Results</h3>
            <p><strong>Coverage Score:</strong> {coverage_score}/100</p>
            {recommendations_html}
        </div>
        """, unsafe_allow_html=True)
        
        # Mark as completed
        st.session_state.completed_assessments['insurance'] = True
        st.session_state.insurance_score = coverage_score
        st.session_state.show_insurance_modal = False
        st.rerun()
    
    if st.button("Close", key="close_insurance"):
        st.session_state.show_insurance_modal = False
        st.rerun()

# Loan Eligibility Result
st.markdown("---")
st.header("Loan Eligibility Result")

if st.button("Check Eligibility", key="check_eligibility", disabled=completed_count < 3):
    credit_score = st.session_state.credit_score
    annual_income = st.session_state.tax_result.get('gross_income', 0) if st.session_state.tax_result else 0
    
    eligible = True
    reasons = []
    
    if credit_score < 580:
        eligible = False
        reasons.append('Credit score is too low (below 580)')
    elif credit_score < 670:
        reasons.append('Credit score is fair, which may result in higher interest rates')
    
    if annual_income < 30000:
        reasons.append('Income is relatively low, which may limit loan amount')
    
    if eligible:
        st.markdown(f"""
        <div class="result-container result-success">
            <h3>Congratulations! You are eligible for a loan.</h3>
            <p>Based on your financial assessment, you meet our criteria for loan approval.</p>
            <p>Next steps: A loan officer will contact you to discuss options and amounts.</p>
            {"<p>Notes: <ul>" + "".join([f"<li>{reason}</li>" for reason in reasons]) + "</ul></p>" if reasons else ""}
        </div>
        """, unsafe_allow_html=True)
    else:
        st.markdown(f"""
        <div class="result-container result-danger">
            <h3>Currently not eligible for a loan.</h3>
            <p>Reasons:</p>
            <ul>
                {"".join([f"<li>{reason}</li>" for reason in reasons])}
            </ul>
            <p>Please work on improving these areas and check back later.</p>
        </div>
        """, unsafe_allow_html=True)

# Footer
st.markdown("""
<footer>
    <p>FinScore - Alternative Credit Scoring for Financial Inclusion</p>
    <p>DSS INNOVATERS - Digital Dawn Track | Providing financial assistance to the masses</p>
    <p>Team: Divyanshu, Sukrit Pal, Shaurya Jha, Samarth Singh</p>
</footer>
""", unsafe_allow_html=True)
