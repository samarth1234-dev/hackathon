import streamlit as st
import pandas as pd
import numpy as np
import matplotlib.pyplot as plt
import yfinance as yf
from datetime import datetime, timedelta
import time

# Set page configuration
st.set_page_config(
    page_title="InvestWise - Start Your Investment Journey",
    page_icon="📈",
    layout="wide",
    initial_sidebar_state="expanded"
)

# Custom CSS
st.markdown("""
<style>
    .main-header {
        font-size: 3rem;
        color: #1f77b4;
        text-align: center;
        margin-bottom: 2rem;
    }
    .sub-header {
        font-size: 1.8rem;
        color: #2c3e50;
        border-bottom: 2px solid #1f77b4;
        padding-bottom: 0.5rem;
        margin-top: 2rem;
        margin-bottom: 1rem;
    }
    .feature-box {
        background-color: #f8f9fa;
        border-radius: 10px;
        padding: 1.5rem;
        margin-bottom: 1.5rem;
        box-shadow: 0 4px 6px rgba(0, 0, 0, 0.1);
    }
    .risk-low {
        background-color: #d4edda;
        padding: 15px;
        border-radius: 5px;
    }
    .risk-medium {
        background-color: #fff3cd;
        padding: 15px;
        border-radius: 5px;
    }
    .risk-high {
        background-color: #f8d7da;
        padding: 15px;
        border-radius: 5px;
    }
    .investment-card {
        border-left: 5px solid #1f77b4;
        padding: 15px;
        margin: 10px 0;
        background-color: #f8f9fa;
        border-radius: 5px;
    }
</style>
""", unsafe_allow_html=True)

# Initialize session state variables
if 'quiz_completed' not in st.session_state:
    st.session_state.quiz_completed = False
if 'risk_profile' not in st.session_state:
    st.session_state.risk_profile = None
if 'mock_portfolio' not in st.session_state:
    st.session_state.mock_portfolio = {}
if 'portfolio_value' not in st.session_state:
    st.session_state.portfolio_value = 10000  # Starting with $10,000 mock money

# Navigation
st.sidebar.title("InvestWise Navigation")
page = st.sidebar.radio("Go to", ["Home", "Investment Guides", "Risk Assessment", "Mock Portfolio"])

# Home Page
if page == "Home":
    st.markdown('<h1 class="main-header">InvestWise: Start Your Investment Journey</h1>', unsafe_allow_html=True)
    st.markdown("""
    <div style='text-align: center; font-size: 1.2rem; margin-bottom: 2rem;'>
        Overcoming investment fears through education and practice
    </div>
    """, unsafe_allow_html=True)
    
    col1, col2, col3 = st.columns(3)
    
    with col1:
        st.markdown("""
        <div class='feature-box'>
            <h3>📚 Educational Guides</h3>
            <p>Learn about different investment options with our beginner-friendly guides.</p>
        </div>
        """, unsafe_allow_html=True)
    
    with col2:
        st.markdown("""
        <div class='feature-box'>
            <h3>📊 Risk Assessment</h3>
            <p>Take our quiz to understand your risk tolerance and get personalized recommendations.</p>
        </div>
        """, unsafe_allow_html=True)
    
    with col3:
        st.markdown("""
        <div class='feature-box'>
            <h3>💼 Mock Portfolio</h3>
            <p>Practice investing with virtual money before risking your real capital.</p>
        </div>
        """, unsafe_allow_html=True)
    
    st.markdown("---")
    
    st.markdown("""
    ## Why People Avoid Investing
    
    Many people hesitate to invest due to:
    - Fear of losing money
    - Lack of knowledge about where to start
    - Confusion about complex financial products
    - Belief that investing is only for the wealthy
    
    ## How InvestWise Helps
    
    Our platform is designed to:
    - Provide clear, simple explanations of investment concepts
    - Help you understand your risk tolerance
    - Allow you to practice without financial risk
    - Build confidence in your investment decisions
    """)

# Investment Guides Page
elif page == "Investment Guides":
    st.markdown('<h1 class="main-header">Investment Guides</h1>', unsafe_allow_html=True)
    
    investment_type = st.selectbox("Choose an investment type to learn about:", 
                                  ["Mutual Funds", "SIPs (Systematic Investment Plans)", "Stocks", "Gold", "Fixed Deposits"])
    
    if investment_type == "Mutual Funds":
        st.markdown('<div class="sub-header">Mutual Funds</div>', unsafe_allow_html=True)
        st.markdown("""
        <div class='investment-card'>
            <h3>What are Mutual Funds?</h3>
            <p>Mutual funds pool money from many investors to purchase a diversified portfolio of stocks, bonds, or other securities.</p>
            
            <h3>Key Benefits:</h3>
            <ul>
                <li><strong>Diversification:</strong> Spread risk across many investments</li>
                <li><strong>Professional Management:</strong> Experienced fund managers make decisions</li>
                <li><strong>Accessibility:</strong> Start with relatively small amounts</li>
                <li><strong>Liquidity:</strong> Generally easy to buy and sell</li>
            </ul>
            
            <h3>Types of Mutual Funds:</h3>
            <ul>
                <li><strong>Equity Funds:</strong> Invest primarily in stocks</li>
                <li><strong>Debt Funds:</strong> Invest in fixed-income securities like bonds</li>
                <li><strong>Hybrid Funds:</strong> Mix of equity and debt investments</li>
                <li><strong>Index Funds:</strong> Track a specific market index</li>
            </ul>
            
            <h3>Considerations:</h3>
            <ul>
                <li>All mutual funds charge fees (expense ratios)</li>
                <li>Past performance doesn't guarantee future results</li>
                <li>Different funds have different risk levels</li>
            </ul>
        </div>
        """, unsafe_allow_html=True)
        
    elif investment_type == "SIPs (Systematic Investment Plans)":
        st.markdown('<div class="sub-header">Systematic Investment Plans (SIPs)</div>', unsafe_allow_html=True)
        st.markdown("""
        <div class='investment-card'>
            <h3>What are SIPs?</h3>
            <p>SIPs allow you to invest a fixed amount regularly (usually monthly) in a mutual fund scheme.</p>
            
            <h3>Key Benefits:</h3>
            <ul>
                <li><strong>Discipline:</strong> Encourages regular investing habits</li>
                <li><strong>Rupee Cost Averaging:</strong> Buy more units when prices are low, fewer when prices are high</li>
                <li><strong>Affordability:</strong> Start with as little as ₹500 per month</li>
                <li><strong>Power of Compounding:</strong> Regular investments grow over time</li>
            </ul>
            
            <h3>How SIPs Work:</h3>
            <p>When you invest through a SIP, a fixed amount is deducted from your bank account periodically and used to purchase units of a mutual fund at the current Net Asset Value (NAV).</p>
            
            <h3>Example:</h3>
            <p>If you invest ₹5,000 monthly through a SIP for 20 years with an assumed 12% annual return, you could accumulate approximately ₹50 lakhs from a total investment of ₹12 lakhs.</p>
            
            <h3>Considerations:</h3>
            <ul>
                <li>SIPs don't guarantee profits</li>
                <li>Market fluctuations will affect your returns</li>
                <li>Long-term commitment typically yields better results</li>
            </ul>
        </div>
        """, unsafe_allow_html=True)
        
    elif investment_type == "Stocks":
        st.markdown('<div class="sub-header">Stocks</div>', unsafe_allow_html=True)
        st.markdown("""
        <div class='investment-card'>
            <h3>What are Stocks?</h3>
            <p>Stocks represent ownership shares in a company. When you buy a stock, you become a partial owner of that company.</p>
            
            <h3>Key Benefits:</h3>
            <ul>
                <li><strong>High Return Potential:</strong> Historically, stocks have offered higher returns than many other investments</li>
                <li><strong>Ownership:</strong> Share in the company's growth and profits</li>
                <li><strong>Liquidity:</strong> Generally easy to buy and sell on stock exchanges</li>
                <li><strong>Dividends:</strong> Some companies share profits with shareholders</li>
            </ul>
            
            <h3>Types of Stocks:</h3>
            <ul>
                <li><strong>Blue-Chip Stocks:</strong> Large, established companies with stable performance</li>
                <li><strong>Growth Stocks:</strong> Companies expected to grow faster than the market</li>
                <li><strong>Value Stocks:</strong> Stocks that appear undervalued relative to their fundamentals</li>
                <li><strong>Dividend Stocks:</strong> Companies that regularly pay dividends</li>
            </ul>
            
            <h3>Considerations:</h3>
            <ul>
                <li>Higher potential returns come with higher risk</li>
                <li>Stock prices can be volatile in the short term</li>
                <li>Requires research or professional advice</li>
                <li>Diversification is important to manage risk</li>
            </ul>
        </div>
        """, unsafe_allow_html=True)
        
    elif investment_type == "Gold":
        st.markdown('<div class="sub-header">Gold</div>', unsafe_allow_html=True)
        st.markdown("""
        <div class='investment-card'>
            <h3>Gold as an Investment</h3>
            <p>Gold has been a valued investment for centuries, serving as a hedge against inflation and currency fluctuations.</p>
            
            <h3>Key Benefits:</h3>
            <ul>
                <li><strong>Inflation Hedge:</strong> Tends to maintain value during inflationary periods</li>
                <li><strong>Safe Haven:</strong> Often performs well during economic uncertainty</li>
                <li><strong>Portfolio Diversification:</strong> Low correlation with stocks and bonds</li>
                <li><strong>Tangible Asset:</strong> Physical gold can be held directly</li>
            </ul>
            
            <h3>Ways to Invest in Gold:</h3>
            <ul>
                <li><strong>Physical Gold:</strong> Jewellery, coins, and bars</li>
                <li><strong>Gold ETFs:</strong> Exchange-Traded Funds that track gold prices</li>
                <li><strong>Sovereign Gold Bonds (SGBs):</strong> Government securities denominated in grams of gold</li>
                <li><strong>Gold Mutual Funds:</strong> Funds that invest in gold-related assets</li>
            </ul>
            
            <h3>Considerations:</h3>
            <ul>
                <li>Physical gold requires secure storage</li>
                <li>Does not generate regular income like dividends or interest</li>
                <li>Prices can be volatile in the short term</li>
                <li>Making charges reduce returns on jewellery investments</li>
            </ul>
        </div>
        """, unsafe_allow_html=True)
        
    elif investment_type == "Fixed Deposits":
        st.markdown('<div class="sub-header">Fixed Deposits</div>', unsafe_allow_html=True)
        st.markdown("""
        <div class='investment-card'>
            <h3>What are Fixed Deposits?</h3>
            <p>Fixed Deposits (FDs) are investment instruments offered by banks and NBFCs where you deposit a lump sum for a fixed period at a predetermined interest rate.</p>
            
            <h3>Key Benefits:</h3>
            <ul>
                <li><strong>Safety:</strong> Among the safest investment options available</li>
                <li><strong>Guaranteed Returns:</strong> Fixed interest rate regardless of market conditions</li>
                <li><strong>Flexible Tenures:</strong> Choose from 7 days to 10 years</li>
                <li><strong>Loan Facility:</strong> Can avail loans against FDs</li>
            </ul>
            
            <h3>Types of Fixed Deposits:</h3>
            <ul>
                <li><strong>Regular FDs:</strong> Standard fixed deposits with fixed tenure and interest</li>
                <li><strong>Tax-Saving FDs:</strong> Eligible for tax deduction under Section 80C with 5-year lock-in</li>
                <li><strong>Senior Citizen FDs:</strong> Higher interest rates for investors above 60 years</li>
                <li><strong>Corporate FDs:</strong> Offered by companies, typically with higher rates but more risk</li>
            </ul>
            
            <h3>Considerations:</h3>
            <ul>
                <li>Returns may be lower than inflation, reducing purchasing power</li>
                <li>Premature withdrawal may attract penalties</li>
                <li>Interest is taxable as per your income tax slab</li>
                <li>Not all FDs are equally safe (bank FDs are safer than corporate FDs)</li>
            </ul>
        </div>
        """, unsafe_allow_html=True)

# Risk Assessment Quiz Page
elif page == "Risk Assessment":
    st.markdown('<h1 class="main-header">Investment Risk Assessment</h1>', unsafe_allow_html=True)
    
    if not st.session_state.quiz_completed:
        st.info("Answer these questions to understand your risk profile and get personalized investment recommendations.")
        
        with st.form("risk_quiz"):
            st.subheader("1. What is your investment time horizon?")
            time_horizon = st.radio("", 
                                   ("Less than 2 years", "2-5 years", "5-10 years", "More than 10 years"),
                                   key="time_horizon")
            
            st.subheader("2. What is your primary investment goal?")
            goal = st.radio("",
                           ("Preserve capital", "Generate regular income", "Balance growth and safety", "Maximize long-term growth"),
                           key="goal")
            
            st.subheader("3. How would you react to a 20% decline in your investment value in a short period?")
            reaction = st.radio("",
                               ("Sell all investments to avoid further loss", 
                                "Sell some investments and move to safer options",
                                "Hold investments and wait for recovery",
                                "Invest more to take advantage of lower prices"),
                               key="reaction")
            
            st.subheader("4. What percentage of your income are you willing to invest?")
            income_percentage = st.radio("",
                                        ("Less than 10%", "10-20%", "20-30%", "More than 30%"),
                                        key="income_percentage")
            
            st.subheader("5. How familiar are you with investment concepts?")
            familiarity = st.radio("",
                                  ("Not familiar at all", 
                                   "Somewhat familiar", 
                                   "Moderately familiar", 
                                   "Very familiar"),
                                  key="familiarity")
            
            submitted = st.form_submit_button("Submit Answers")
            
            if submitted:
                # Calculate risk score (simplified)
                score = 0
                
                # Time horizon scoring
                if time_horizon == "Less than 2 years":
                    score += 1
                elif time_horizon == "2-5 years":
                    score += 2
                elif time_horizon == "5-10 years":
                    score += 3
                else:
                    score += 4
                
                # Goal scoring
                if goal == "Preserve capital":
                    score += 1
                elif goal == "Generate regular income":
                    score += 2
                elif goal == "Balance growth and safety":
                    score += 3
                else:
                    score += 4
                
                # Reaction scoring
                if reaction == "Sell all investments to avoid further loss":
                    score += 1
                elif reaction == "Sell some investments and move to safer options":
                    score += 2
                elif reaction == "Hold investments and wait for recovery":
                    score += 3
                else:
                    score += 4
                
                # Income percentage scoring
                if income_percentage == "Less than 10%":
                    score += 1
                elif income_percentage == "10-20%":
                    score += 2
                elif income_percentage == "20-30%":
                    score += 3
                else:
                    score += 4
                
                # Familiarity scoring
                if familiarity == "Not familiar at all":
                    score += 1
                elif familiarity == "Somewhat familiar":
                    score += 2
                elif familiarity == "Moderately familiar":
                    score += 3
                else:
                    score += 4
                
                # Determine risk profile
                if score <= 10:
                    risk_profile = "Conservative"
                elif score <= 15:
                    risk_profile = "Moderately Conservative"
                elif score <= 20:
                    risk_profile = "Moderate"
                else:
                    risk_profile = "Aggressive"
                
                st.session_state.quiz_completed = True
                st.session_state.risk_profile = risk_profile
                st.session_state.risk_score = score
                
                st.success("Assessment completed! Your risk profile is: **{}**".format(risk_profile))
                st.experimental_rerun()
    
    else:
        st.success("Your investment risk profile: **{}**".format(st.session_state.risk_profile))
        
        if st.session_state.risk_profile == "Conservative":
            st.markdown("""
            <div class='risk-low'>
                <h3>Recommended Investment Approach</h3>
                <p>As a conservative investor, you prioritize capital preservation over high returns. Your portfolio should focus on stability and lower-risk investments.</p>
                
                <h4>Suggested Allocation:</h4>
                <ul>
                    <li>60% Fixed Income (Fixed Deposits, Debt Funds)</li>
                    <li>20% Gold (SGBs, Gold ETFs)</li>
                    <li>15% Large-Cap Equity (Blue-chip stocks, Index funds)</li>
                    <li>5% Cash equivalents</li>
                </ul>
                
                <h4>Recommended Investments:</h4>
                <ul>
                    <li>Bank Fixed Deposits</li>
                    <li>Debt Mutual Funds</li>
                    <li>Sovereign Gold Bonds (SGBs)</li>
                    <li>Large-Cap Index Funds</li>
                    <li>Liquid Funds for emergency corpus</li>
                </ul>
            </div>
            """, unsafe_allow_html=True)
            
        elif st.session_state.risk_profile == "Moderately Conservative":
            st.markdown("""
            <div class='risk-medium'>
                <h3>Recommended Investment Approach</h3>
                <p>As a moderately conservative investor, you're willing to accept some risk for potentially higher returns while still emphasizing capital preservation.</p>
                
                <h4>Suggested Allocation:</h4>
                <ul>
                    <li>50% Fixed Income (Fixed Deposits, Debt Funds)</li>
                    <li>20% Equity (Large-cap and Blue-chip stocks)</li>
                    <li>15% Gold (SGBs, Gold ETFs)</li>
                    <li>15% Hybrid or Balanced Funds</li>
                </ul>
                
                <h4>Recommended Investments:</h4>
                <ul>
                    <li>Bank Fixed Deposits</li>
                    <li>Debt Mutual Funds</li>
                    <li>Large-Cap Mutual Funds</li>
                    <li>Sovereign Gold Bonds (SGBs)</li>
                    <li>Balanced Advantage Funds</li>
                </ul>
            </div>
            """, unsafe_allow_html=True)
            
        elif st.session_state.risk_profile == "Moderate":
            st.markdown("""
            <div class='risk-medium'>
                <h3>Recommended Investment Approach</h3>
                <p>As a moderate investor, you seek a balance between growth and safety, willing to accept moderate risk for potentially higher returns.</p>
                
                <h4>Suggested Allocation:</h4>
                <ul>
                    <li>40% Equity (Diversified across market caps)</li>
                    <li>30% Fixed Income (Debt Funds, Corporate Bonds)</li>
                    <li>15% Gold (Gold ETFs, SGBs)</li>
                    <li>15% International Equity or Sector Funds</li>
                </ul>
                
                <h4>Recommended Investments:</h4>
                <ul>
                    <li>Multi-Cap Mutual Funds</li>
                    <li>Corporate Bond Funds</li>
                    <li>Gold ETFs</li>
                    <li>PPF or NPS for tax efficiency</li>
                    <li>International Equity Funds</li>
                </ul>
            </div>
            """, unsafe_allow_html=True)
            
        else:  # Aggressive
            st.markdown("""
            <div class='risk-high'>
                <h3>Recommended Investment Approach</h3>
                <p>As an aggressive investor, you're comfortable with higher risk in pursuit of potentially higher returns, with a long-term investment horizon.</p>
                
                <h4>Suggested Allocation:</h4>
                <ul>
                    <li>60% Equity (Across market caps with mid/small cap focus)</li>
                    <li>20% Sectoral or Thematic Funds</li>
                    <li>10% International Equity</li>
                    <li>10% Alternative Investments (REITs, InvITs)</li>
                </ul>
                
                <h4>Recommended Investments:</h4>
                <ul>
                    <li>Flexi-Cap and Small-Cap Mutual Funds</li>
                    <li>Sectoral Funds (IT, Pharma, Infrastructure)</li>
                    <li>International Equity Funds</li>
                    <li>Direct Equity (for experienced investors)</li>
                    <li>REITs and InvITs</li>
                </ul>
            </div>
            """, unsafe_allow_html=True)
        
        if st.button("Retake Quiz"):
            st.session_state.quiz_completed = False
            st.session_state.risk_profile = None
            st.experimental_rerun()

# Mock Portfolio Page
elif page == "Mock Portfolio":
    st.markdown('<h1 class="main-header">Mock Investment Portfolio</h1>', unsafe_allow_html=True)
    
    st.info("Practice investing with virtual money. Start with ₹10,000 to build your portfolio.")
    
    col1, col2 = st.columns([2, 1])
    
    with col1:
        st.subheader("Your Portfolio Value: ₹{:.2f}".format(st.session_state.portfolio_value))
        
        # Display current portfolio
        if st.session_state.mock_portfolio:
            st.subheader("Your Investments")
            portfolio_data = []
            total_value = 0
            
            for ticker, details in st.session_state.mock_portfolio.items():
                current_price = yf.Ticker(ticker + ".NS").history(period="1d")["Close"].iloc[-1]
                current_value = current_price * details["quantity"]
                profit_loss = current_value - details["invested_amount"]
                profit_loss_pct = (profit_loss / details["invested_amount"]) * 100
                total_value += current_value
                
                portfolio_data.append({
                    "Asset": ticker,
                    "Quantity": details["quantity"],
                    "Avg Price": details["avg_price"],
                    "Current Price": current_price,
                    "Invested Amount": details["invested_amount"],
                    "Current Value": current_value,
                    "P/L": profit_loss,
                    "P/L %": profit_loss_pct
                })
            
            df = pd.DataFrame(portfolio_data)
            st.dataframe(df.style.format({
                "Avg Price": "₹{:.2f}",
                "Current Price": "₹{:.2f}",
                "Invested Amount": "₹{:.2f}",
                "Current Value": "₹{:.2f}",
                "P/L": "₹{:.2f}",
                "P/L %": "{:.2f}%"
            }))
            
            # Update portfolio value
            st.session_state.portfolio_value = total_value + (st.session_state.portfolio_value - sum([d["invested_amount"] for d in st.session_state.mock_portfolio.values()]))
            
        else:
            st.info("You haven't made any investments yet. Use the form to add investments to your portfolio.")
    
    with col2:
        st.subheader("Add Investment")
        
        with st.form("add_investment"):
            asset_type = st.selectbox("Asset Type", ["Stock", "ETF", "Mutual Fund"])
            
            if asset_type == "Stock":
                ticker = st.text_input("Stock Symbol (e.g., RELIANCE, TCS, INFY)").upper()
            elif asset_type == "ETF":
                ticker = st.text_input("ETF Symbol (e.g., NIFTYBEES, GOLDBEES)").upper()
            else:
                ticker = st.text_input("Mutual Fund Name")  # This would need a different approach
            
            quantity = st.number_input("Quantity", min_value=1, value=1)
            
            submitted = st.form_submit_button("Add to Portfolio")
            
            if submitted:
                if ticker:
                    try:
                        # Get current price
                        stock = yf.Ticker(ticker + ".NS")
                        hist = stock.history(period="1d")
                        current_price = hist["Close"].iloc[-1]
                        
                        investment_amount = current_price * quantity
                        
                        if investment_amount > st.session_state.portfolio_value:
                            st.error("Insufficient funds for this investment!")
                        else:
                            if ticker in st.session_state.mock_portfolio:
                                # Update existing holding
                                existing = st.session_state.mock_portfolio[ticker]
                                total_quantity = existing["quantity"] + quantity
                                total_invested = existing["invested_amount"] + investment_amount
                                avg_price = total_invested / total_quantity
                                
                                st.session_state.mock_portfolio[ticker] = {
                                    "quantity": total_quantity,
                                    "avg_price": avg_price,
                                    "invested_amount": total_invested
                                }
                            else:
                                # Add new holding
                                st.session_state.mock_portfolio[ticker] = {
                                    "quantity": quantity,
                                    "avg_price": current_price,
                                    "invested_amount": investment_amount
                                }
                            
                            # Deduct from available cash
                            st.session_state.portfolio_value -= investment_amount
                            st.success("Added {} shares of {} to portfolio".format(quantity, ticker))
                            st.experimental_rerun()
                    
                    except:
                        st.error("Could not fetch data for {}. Please check the symbol.".format(ticker))
                else:
                    st.error("Please enter a valid symbol")
    
    # Portfolio analysis
    if st.session_state.mock_portfolio:
        st.subheader("Portfolio Analysis")
        
        # Pie chart of allocations
        labels = []
        sizes = []
        
        for ticker, details in st.session_state.mock_portfolio.items():
            current_price = yf.Ticker(ticker + ".NS").history(period="1d")["Close"].iloc[-1]
            current_value = current_price * details["quantity"]
            labels.append(ticker)
            sizes.append(current_value)
        
        # Add cash position
        labels.append("Cash")
        sizes.append(st.session_state.portfolio_value - sum(sizes))
        
        fig, ax = plt.subplots()
        ax.pie(sizes, labels=labels, autopct='%1.1f%%', startangle=90)
        ax.axis('equal')
        st.pyplot(fig)
        
        # Performance chart (simplified)
        st.subheader("Portfolio Performance Over Time")
        
        # This would ideally track historical performance
        st.info("Performance tracking would require storing historical data. In a full implementation, this would show your portfolio's growth over time.")
        
        # Reset portfolio button
        if st.button("Reset Portfolio"):
            st.session_state.mock_portfolio = {}
            st.session_state.portfolio_value = 10000
            st.experimental_rerun()

# Footer
st.markdown("---")
st.markdown("""
<div style='text-align: center;'>
    <p>Disclaimer: This platform is for educational purposes only. Investments in real markets carry risks. Past performance is not indicative of future results.</p>
    <p>Consult with a qualified financial advisor before making investment decisions.</p>
</div>
""", unsafe_allow_html=True)
