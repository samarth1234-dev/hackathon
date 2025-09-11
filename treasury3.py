import streamlit as st
import pandas as pd
import numpy as np
from datetime import datetime, timedelta
import matplotlib.pyplot as plt
import matplotlib
matplotlib.use('Agg')  # Use non-interactive backend

# Page configuration
st.set_page_config(
    page_title="Treasury & Debt Instruments Guide",
    page_icon="💰",
    layout="wide",
    initial_sidebar_state="expanded"
)

# Custom CSS
st.markdown("""
<style>
    .main-header {
        font-size: 3rem;
        color: #2c3e50;
        text-align: center;
        margin-bottom: 2rem;
    }
    .sub-header {
        font-size: 2rem;
        color: #34495e;
        margin-top: 2rem;
        margin-bottom: 1rem;
    }
    .info-box {
        background-color: #f8f9fa;
        padding: 1.5rem;
        border-radius: 10px;
        border-left: 5px solid #3498db;
        margin-bottom: 1rem;
    }
    .calculator-box {
        background-color: #e8f4f8;
        padding: 2rem;
        border-radius: 15px;
        box-shadow: 0 4px 6px rgba(0,0,0,0.1);
    }
    .risk-meter {
        height: 30px;
        background: linear-gradient(90deg, #27ae60, #f39c12, #e74c3c);
        border-radius: 15px;
        margin: 10px 0;
    }
    .stProgress > div > div > div > div {
        background-image: linear-gradient(to right, #27ae60, #f39c12, #e74c3c);
    }
</style>
""", unsafe_allow_html=True)

# Sidebar
with st.sidebar:
    st.title("💰 Treasury Navigator")
    st.markdown("---")
    
    section = st.radio(
        "Navigate to:",
        ["🏠 Overview", "📊 Types of Instruments", "🧮 Investment Calculator", 
         "📈 Market Data", "🎓 Learning Center", "📋 Investment Quiz"]
    )
    
    st.markdown("---")
    st.info("""
    **Disclaimer:** This is educational content only. 
    Consult a financial advisor before making investment decisions.
    """)

# Main content
if section == "🏠 Overview":
    st.markdown('<h1 class="main-header">Treasury & Debt Instruments Guide</h1>', unsafe_allow_html=True)
    
    col1, col2 = st.columns([2, 1])
    
    with col1:
        st.markdown("""
        <div class="info-box">
        <h3>What are Treasury & Debt Instruments?</h3>
        <p>Treasury and debt instruments are investment vehicles where you lend money to governments 
        or corporations in exchange for regular interest payments and the return of your principal 
        at maturity. They are generally considered safer than stocks.</p>
        </div>
        """, unsafe_allow_html=True)
    
    with col2:
        st.image("https://images.unsplash.com/photo-1611974789855-9c2a0a7236a3?w=400", 
                caption="Secure Investing", use_column_width=True)
    
    st.markdown("### Key Benefits:")
    
    benefits = [
        {"icon": "🛡️", "title": "Safety", "desc": "Government-backed securities are among the safest investments"},
        {"icon": "💵", "title": "Regular Income", "desc": "Fixed interest payments provide predictable income"},
        {"icon": "📊", "title": "Diversification", "desc": "Helps balance risk in your investment portfolio"},
        {"icon": "💰", "title": "Liquidity", "desc": "Many instruments can be easily bought and sold"}
    ]
    
    cols = st.columns(4)
    for i, benefit in enumerate(benefits):
        with cols[i]:
            st.markdown(f"""
            <div style="text-align: center; padding: 1rem;">
                <span style="font-size: 2.5rem;">{benefit['icon']}</span>
                <h4>{benefit['title']}</h4>
                <p>{benefit['desc']}</p>
            </div>
            """, unsafe_allow_html=True)

elif section == "📊 Types of Instruments":
    st.markdown('<h1 class="main-header">Types of Debt Instruments</h1>', unsafe_allow_html=True)
    
    tab1, tab2, tab3, tab4 = st.tabs(["Government Bonds", "Corporate Bonds", "T-Bills & Notes", "Comparison"])
    
    with tab1:
        st.subheader("Government Bonds")
        col1, col2 = st.columns([2, 1])
        with col1:
            st.markdown("""
            - **Treasury Bonds (T-Bonds)**: Long-term (20-30 years)
            - **Treasury Notes (T-Notes)**: Medium-term (2-10 years)
            - **Treasury Bills (T-Bills)**: Short-term (less than 1 year)
            - **Municipal Bonds**: Issued by state/local governments
            """)
            
            st.markdown("**Features:**")
            st.markdown("""
            - Backed by full faith and credit of the government
            - Generally exempt from state and local taxes
            - Lower risk than corporate bonds
            - Regular interest payments (except T-Bills)
            """)
        
        with col2:
            st.image("https://images.unsplash.com/photo-1586074299757-dc655f18518c?w=300", 
                    caption="Government Securities", use_column_width=True)
    
    with tab2:
        st.subheader("Corporate Bonds")
        col1, col2 = st.columns([2, 1])
        with col1:
            st.markdown("""
            - **Investment Grade**: Higher quality, lower risk
            - **High-Yield (Junk) Bonds**: Higher risk, higher potential return
            - **Convertible Bonds**: Can be converted to stock
            - **Callable Bonds**: Can be redeemed early by issuer
            """)
            
            st.markdown("**Features:**")
            st.markdown("""
            - Higher yields than government bonds
            - Varying levels of risk
            - Subject to corporate default risk
            - Taxable at federal and state levels
            """)
        
        with col2:
            st.image("https://images.unsplash.com/photo-1611974789855-9c2a0a7236a3?w=300", 
                    caption="Corporate Financing", use_column_width=True)
    
    with tab3:
        st.subheader("T-Bills & Short-Term Instruments")
        st.markdown("""
        - **T-Bills**: Maturities from 4 weeks to 52 weeks, sold at discount
        - **Commercial Paper**: Short-term corporate debt (1-270 days)
        - **Certificates of Deposit (CDs)**: Bank-issued, FDIC insured
        - **Money Market Funds**: Pooled short-term investments
        """)
    
    with tab4:
        st.subheader("Instrument Comparison")
        
        comparison_data = {
            'Instrument': ['T-Bills', 'T-Notes', 'T-Bonds', 'Corporate Bonds', 'Municipal Bonds'],
            'Risk Level': ['Very Low', 'Very Low', 'Low', 'Medium-High', 'Low-Medium'],
            'Typical Yield': ['2-4%', '3-5%', '4-6%', '5-8%', '3-6%'],
            'Maturity': ['<1 year', '2-10 years', '20-30 years', '1-30 years', '1-30 years'],
            'Tax Treatment': ['Federal only', 'Federal only', 'Federal only', 'Fully taxable', 'Tax-free*']
        }
        
        df = pd.DataFrame(comparison_data)
        st.dataframe(df, use_container_width=True)
        
        st.caption("*Municipal bond interest is typically exempt from federal taxes and sometimes state taxes")

elif section == "🧮 Investment Calculator":
    st.markdown('<h1 class="main-header">Investment Calculator</h1>', unsafe_allow_html=True)
    
    col1, col2 = st.columns(2)
    
    with col1:
        st.markdown('<div class="calculator-box">', unsafe_allow_html=True)
        st.subheader("Bond Yield Calculator")
        
        principal = st.number_input("Investment Amount ($)", min_value=1000, value=10000, step=1000)
        coupon_rate = st.slider("Annual Coupon Rate (%)", min_value=0.0, max_value=15.0, value=5.0, step=0.1)
        years = st.slider("Years to Maturity", min_value=1, max_value=30, value=10)
        frequency = st.selectbox("Payment Frequency", ["Annual", "Semi-Annual", "Quarterly"])
        
        freq_map = {"Annual": 1, "Semi-Annual": 2, "Quarterly": 4}
        payments_per_year = freq_map[frequency]
        
        # Calculate
        annual_coupon = principal * (coupon_rate / 100)
        total_payments = years * payments_per_year
        payment_amount = annual_coupon / payments_per_year
        total_interest = annual_coupon * years
        
        st.markdown('</div>', unsafe_allow_html=True)
    
    with col2:
        st.markdown('<div class="calculator-box">', unsafe_allow_html=True)
        st.subheader("Results")
        
        st.metric("Annual Coupon Payment", f"${annual_coupon:,.2f}")
        st.metric(f"Each {frequency} Payment", f"${payment_amount:,.2f}")
        st.metric("Total Interest Earned", f"${total_interest:,.2f}")
        st.metric("Total Return", f"${principal + total_interest:,.2f}")
        
        # Create a simple chart with matplotlib
        years_list = list(range(years + 1))
        values = [principal + (annual_coupon * year) for year in years_list]
        
        fig, ax = plt.subplots(figsize=(10, 6))
        ax.plot(years_list, values, marker='o', linewidth=2)
        ax.set_xlabel('Years')
        ax.set_ylabel('Investment Value ($)')
        ax.set_title('Investment Growth Over Time')
        ax.grid(True, linestyle='--', alpha=0.7)
        ax.tick_params(axis='x', which='major', labelsize=10)
        ax.tick_params(axis='y', which='major', labelsize=10)
        
        st.pyplot(fig)
        
        st.markdown('</div>', unsafe_allow_html=True)

elif section == "📈 Market Data":
    st.markdown('<h1 class="main-header">Current Market Data</h1>', unsafe_allow_html=True)
    
    # Simulated market data
    treasury_data = {
        'Instrument': ['13-Week T-Bill', '5-Year T-Note', '10-Year T-Note', '30-Year T-Bond'],
        'Current Yield': [5.32, 4.28, 4.18, 4.35],
        'Previous Yield': [5.28, 4.25, 4.15, 4.32],
        'Change': ['+0.04', '+0.03', '+0.03', '+0.03']
    }
    
    df = pd.DataFrame(treasury_data)
    st.dataframe(df, use_container_width=True)
    
    # Yield curve visualization with matplotlib
    st.subheader("Treasury Yield Curve")
    
    maturities = [0.25, 1, 2, 5, 10, 30]  # years
    yields = [5.32, 5.15, 4.75, 4.28, 4.18, 4.35]  # percentages
    
    fig, ax = plt.subplots(figsize=(10, 6))
    ax.plot(maturities, yields, marker='o', linewidth=2)
    ax.set_xlabel('Maturity (Years)')
    ax.set_ylabel('Yield (%)')
    ax.set_title('Current Yield Curve')
    ax.grid(True, linestyle='--', alpha=0.7)
    
    st.pyplot(fig)
    
    # Historical yield data (simulated)
    st.subheader("Historical 10-Year Treasury Yield")
    
    dates = pd.date_range(end=datetime.today(), periods=365, freq='D')
    historical_yields = 4.0 + 0.5 * np.sin(np.arange(365) / 30) + np.random.normal(0, 0.1, 365)
    
    fig, ax = plt.subplots(figsize=(10, 6))
    ax.plot(dates, historical_yields, linewidth=2)
    ax.set_xlabel('Date')
    ax.set_ylabel('Yield (%)')
    ax.set_title('10-Year Treasury Yield (Last 12 Months)')
    ax.grid(True, linestyle='--', alpha=0.7)
    ax.tick_params(axis='x', rotation=45)
    
    st.pyplot(fig)

elif section == "🎓 Learning Center":
    st.markdown('<h1 class="main-header">Learning Center</h1>', unsafe_allow_html=True)
    
    tab1, tab2, tab3 = st.tabs(["Key Concepts", "Investment Strategies", "Risk Management"])
    
    with tab1:
        st.subheader("Key Bond Concepts")
        
        concepts = [
            {"term": "Yield", "definition": "The annual return on investment, expressed as a percentage"},
            {"term": "Coupon Rate", "definition": "The fixed interest rate paid by the bond"},
            {"term": "Maturity", "definition": "The date when the principal amount is repaid"},
            {"term": "Face Value", "definition": "The amount paid at maturity (typically $1,000 per bond)"},
            {"term": "Duration", "definition": "A measure of interest rate risk sensitivity"}
        ]
        
        for concept in concepts:
            with st.expander(concept["term"]):
                st.write(concept["definition"])
    
    with tab2:
        st.subheader("Investment Strategies")
        
        strategies = [
            "Laddering: Buying bonds with different maturities to manage interest rate risk",
            "Barbell Strategy: Concentrating investments in short-term and long-term bonds",
            "Bullet Strategy: Focusing on bonds that all mature around the same time",
            "Bond Funds: Investing in mutual funds or ETFs that hold diversified bond portfolios"
        ]
        
        for strategy in strategies:
            st.write(f"• {strategy}")
    
    with tab3:
        st.subheader("Understanding Risk")
        
        st.write("**Interest Rate Risk:** When rates rise, bond prices fall")
        st.progress(0.7)
        
        st.write("**Credit Risk:** Risk of issuer defaulting on payments")
        st.progress(0.4)
        
        st.write("**Inflation Risk:** Purchasing power erosion over time")
        st.progress(0.6)
        
        st.write("**Liquidity Risk:** Difficulty selling at fair price")
        st.progress(0.3)

elif section == "📋 Investment Quiz":
    st.markdown('<h1 class="main-header">Investment Knowledge Quiz</h1>', unsafe_allow_html=True)
    
    questions = [
        {
            "question": "What is the primary risk associated with bonds when interest rates rise?",
            "options": ["Default risk", "Interest rate risk", "Inflation risk", "Liquidity risk"],
            "answer": "Interest rate risk"
        },
        {
            "question": "Which type of bond is generally considered the safest?",
            "options": ["Corporate bonds", "Municipal bonds", "Treasury bonds", "High-yield bonds"],
            "answer": "Treasury bonds"
        },
        {
            "question": "What does 'yield' represent in bond investing?",
            "options": ["The bond's price", "The annual return percentage", "The maturity date", "The coupon rate"],
            "answer": "The annual return percentage"
        }
    ]
    
    score = 0
    
    for i, q in enumerate(questions, 1):
        st.subheader(f"Question {i}")
        st.write(q["question"])
        
        user_answer = st.radio(f"Select your answer for Q{i}:", 
                              q["options"], 
                              key=f"q{i}")
        
        if st.button(f"Check Answer {i}", key=f"btn{i}"):
            if user_answer == q["answer"]:
                st.success("Correct! ✅")
                score += 1
            else:
                st.error(f"Incorrect. The correct answer is: {q['answer']}")
    
    if st.button("Calculate Final Score"):
        st.balloons()
        st.success(f"You scored {score} out of {len(questions)}!")
        
        if score == len(questions):
            st.write("🎉 Excellent! You're a bond expert!")
        elif score >= len(questions) // 2:
            st.write("👍 Good job! You have solid knowledge!")
        else:
            st.write("📚 Keep learning! Review the Learning Center section.")

# Footer
st.markdown("---")
st.markdown("""
<div style="text-align: center; color: #7f8c8d;">
    <p>This educational website provides general information about Treasury and Debt Instruments.</p>
    <p>Not financial advice. Always consult with qualified professionals before investing.</p>
    <p>© 2024 Treasury Education Portal</p>
</div>
""", unsafe_allow_html=True)
