import streamlit as st
import pandas as pd
import numpy as np
import plotly.express as px
import plotly.graph_objects as go
from datetime import datetime, timedelta

# Page configuration
st.set_page_config(
    page_title="Capital Compass - Advanced Financial Dashboard", 
    layout="wide",
    page_icon="💹",
    initial_sidebar_state="collapsed"
)

# Initialize theme state
if "dark_mode" not in st.session_state:
    st.session_state.dark_mode = False

# Create toggle button using Streamlit columns for positioning
col1, col2, col3 = st.columns([6, 1, 1])
with col3:
    if st.button("🌙 Dark" if not st.session_state.dark_mode else "☀️ Light", 
                 help="Toggle dark/light mode"):
        st.session_state.dark_mode = not st.session_state.dark_mode
        st.rerun()

# Professional Images Integration
hero_image_url = "https://images.unsplash.com/photo-1551288049-bebda4e38f71?ixlib=rb-4.0.3&auto=format&fit=crop&w=1000&q=80"
dashboard_image_url = "https://images.unsplash.com/photo-1460925895917-afdab827c52f?ixlib=rb-4.0.3&auto=format&fit=crop&w=800&q=80"
analytics_image_url = "https://plus.unsplash.com/premium_photo-1682310156923-3f4a463610f0?q=80&w=912&auto=format&fit=crop&ixlib=rb-4.1.0&ixid=M3wxMjA3fDB8MHxwaG90by1wYWdlfHx8fGVufDB8fHx8fA%3D%3D"
calculator_image_url = "https://images.unsplash.com/photo-1554224155-6726b3ff858f?ixlib=rb-4.0.3&auto=format&fit=crop&w=800&q=80"

# Apply CSS based on theme state
if st.session_state.dark_mode:
    # Professional Dark theme CSS with enhanced navigation dashboard
    st.markdown(f"""
    <style>
        @import url('https://fonts.googleapis.com/css2?family=Inter:wght@300;400;500;600;700;800&display=swap');
        
        /* Hide Streamlit elements */
        #MainMenu {{visibility: hidden;}}
        footer {{visibility: hidden;}}
        header {{visibility: hidden;}}
        
        /* Smooth scrolling */
        html {{
            scroll-behavior: smooth;
            scroll-padding-top: 100px;
        }}
        
        /* Dark theme styling */
        .stApp {{
            background: linear-gradient(135deg, #0f0f23 0%, #1a1a2e 50%, #16213e 100%);
            color: white;
            font-family: 'Inter', sans-serif;
        }}
        
        /* Glassmorphism Navigation Dashboard Styling */
        .nav-dashboard {{
            background: rgba(45, 55, 72, 0.7);
            backdrop-filter: blur(10px);
            border: 1px solid rgba(255, 255, 255, 0.1);
            border-radius: 16px;
            padding: 15px;
            margin: 15px auto 25px auto;
            max-width: 1000px;
            box-shadow: 0 8px 32px rgba(0, 0, 0, 0.3);
            position: relative;
            z-index: 100;
        }}
        
        .nav-title {{
            font-family: 'Inter', sans-serif;
            font-size: 1.1rem;
            font-weight: 600;
            text-align: center;
            color: #ffffff;
            margin-bottom: 15px;
            letter-spacing: 0.02em;
            text-transform: uppercase;
        }}
        
        .nav-grid {{
            display: grid;
            grid-template-columns: repeat(auto-fit, minmax(130px, 1fr));
            gap: 10px;
        }}
        
        .nav-link {{
            display: flex;
            flex-direction: column;
            align-items: center;
            justify-content: center;
            padding: 12px 10px;
            background: rgba(55, 65, 81, 0.5);
            color: #e5e7eb;
            text-decoration: none;
            border-radius: 12px;
            font-family: 'Inter', sans-serif;
            font-weight: 500;
            font-size: 0.85rem;
            text-align: center;
            transition: all 0.3s ease;
            border: 1px solid rgba(255, 255, 255, 0.1);
            min-height: 40px;
            cursor: pointer;
            box-shadow: 0 4px 6px rgba(0, 0, 0, 0.2);
        }}
        
        .nav-link:hover {{
            background: linear-gradient(145deg, #4F46E5, #8B5CF6);
            color: white;
            text-decoration: none;
            transform: translateY(-3px);
            box-shadow: 0 6px 15px rgba(79, 70, 229, 0.4);
        }}
        
        .nav-link:active {{
            transform: translateY(0px);
        }}
        
        .nav-icon {{
            font-size: 1.2rem;
            margin-bottom: 5px;
        }}
        
        /* Main title styling */
        .main-title {{
            font-family: 'Inter', sans-serif;
            font-size: 3.8rem;
            font-weight: 800;
            text-align: center;
            background: linear-gradient(135deg, #4F46E5, #8B5CF6, #EC4899);
            -webkit-background-clip: text;
            -webkit-text-fill-color: transparent;
            margin: 10px 0 15px 0;
            letter-spacing: -0.02em;
            text-shadow: 0 2px 10px rgba(0, 0, 0, 0.3);
        }}
        
        .subtitle {{
            text-align: center;
            font-family: 'Inter', sans-serif;
            font-size: 1.4rem;
            color: #e2e8f0;
            margin-bottom: 15px;
            font-weight: 500;
        }}
        
        .tagline {{
            text-align: center;
            font-family: 'Inter', sans-serif;
            font-size: 1.1rem;
            color: #cbd5e0;
            margin-bottom: 50px;
            font-weight: 400;
            font-style: italic;
        }}
        
        /* Hero section styling */
        .hero-section {{
            display: flex;
            align-items: center;
            justify-content: space-between;
            margin: 40px auto 80px auto;
            max-width: 1200px;
            padding: 50px 30px;
            background: rgba(45, 55, 72, 0.6);
            border-radius: 24px;
            border: 1px solid rgba(255, 255, 255, 0.1);
            gap: 50px;
            box-shadow: 0 25px 50px rgba(0, 0, 0, 0.3);
            backdrop-filter: blur(10px);
        }}
        
        .hero-content {{
            flex: 1;
            max-width: 500px;
        }}
        
        .hero-image {{
            flex: 1;
            max-width: 500px;
        }}
        
        .hero-image img {{
            width: 100%;
            height: 320px;
            object-fit: cover;
            border-radius: 20px;
            box-shadow: 0 20px 40px rgba(0, 0, 0, 0.5);
        }}
        
        .hero-title {{
            font-size: 2.2rem;
            font-weight: 700;
            color: #ffffff;
            margin-bottom: 25px;
            line-height: 1.3;
        }}
        
        .hero-desc {{
            font-size: 1.1rem;
            line-height: 1.7;
            color: #cbd5e0;
            margin-bottom: 30px;
        }}
        
        .badge-container {{
            display: flex;
            gap: 12px;
            flex-wrap: wrap;
        }}
        
        .badge {{
            padding: 10px 18px;
            border-radius: 25px;
            font-size: 0.9rem;
            font-weight: 600;
            color: white;
            box-shadow: 0 4px 8px rgba(0, 0, 0, 0.2);
            backdrop-filter: blur(10px);
        }}
        
        .badge-primary {{ background: linear-gradient(145deg, #4F46E5, #3730a3); }}
        .badge-success {{ background: linear-gradient(145deg, #10B981, #059669); }}
        .badge-warning {{ background: linear-gradient(145deg, #F59E0B, #D97706); }}
        
        /* Tools section header */
        .tools-header {{
            text-align: center;
            margin: 80px auto 50px auto;
            max-width: 800px;
        }}
        
        .tools-main-title {{
            font-family: 'Inter', sans-serif;
            font-size: 3rem;
            font-weight: 800;
            background: linear-gradient(135deg, #4F46E5, #8B5CF6);
            -webkit-background-clip: text;
            -webkit-text-fill-color: transparent;
            margin-bottom: 25px;
        }}
        
        .tools-subtitle {{
            font-family: 'Inter', sans-serif;
            font-size: 1.3rem;
            color: #cbd5e0;
            margin-bottom: 50px;
            line-height: 1.6;
        }}
        
        /* Professional tool cards with enhanced spacing */
        .tools-grid {{
            display: grid;
            grid-template-columns: repeat(3, 1fr);
            gap: 30px;
            max-width: 1300px;
            margin: 0 auto;
            padding: 0 30px;
        }}
        
        .tool-card {{
            background: linear-gradient(145deg, rgba(45, 55, 72, 0.8), rgba(31, 41, 55, 0.8));
            border: 1px solid rgba(255, 255, 255, 0.1);
            border-radius: 20px;
            padding: 30px;
            text-align: left;
            box-shadow: 0 15px 30px rgba(0, 0, 0, 0.3);
            transition: all 0.3s ease;
            min-height: 240px;
            display: flex;
            flex-direction: column;
            scroll-margin-top: 140px;
            position: relative;
            overflow: hidden;
            backdrop-filter: blur(10px);
        }}
        
        .tool-card::before {{
            content: '';
            position: absolute;
            top: 0;
            left: 0;
            width: 100%;
            height: 5px;
            background: linear-gradient(90deg, #4F46E5, #8B5CF6);
            opacity: 0.8;
        }}
        
        .tool-card:hover {{
            box-shadow: 0 20px 40px rgba(0, 0, 0, 0.4);
            transform: translateY(-7px);
            border-color: rgba(255, 255, 255, 0.2);
        }}
        
        .tool-card:target {{
            border-color: #4F46E5;
            box-shadow: 0 0 30px rgba(79, 70, 229, 0.6);
            animation: highlight 2s ease-in-out;
        }}
        
        @keyframes highlight {{
            0% {{ box-shadow: 0 0 30px rgba(79, 70, 229, 0.8); }}
            50% {{ box-shadow: 0 0 40px rgba(79, 70, 229, 0.7); }}
            100% {{ box-shadow: 0 0 30px rgba(79, 70, 229, 0.6); }}
        }}
        
        .tool-title {{
            font-family: 'Inter', sans-serif;
            font-size: 1.5rem;
            font-weight: 700;
            color: #ffffff;
            margin-bottom: 15px;
            line-height: 1.4;
        }}
        
        .tool-desc {{
            font-family: 'Inter', sans-serif;
            font-size: 1rem;
            color: #cbd5e0;
            line-height: 1.6;
            margin-bottom: 20px;
            flex-grow: 1;
        }}
        
        .tool-button {{
            display: inline-flex;
            align-items: center;
            justify-content: center;
            padding: 12px 24px;
            background: linear-gradient(145deg, #4F46E5, #3730a3);
            color: white;
            text-decoration: none;
            border-radius: 12px;
            font-family: 'Inter', sans-serif;
            font-weight: 600;
            font-size: 1rem;
            transition: all 0.3s ease;
            align-self: flex-start;
            box-shadow: 0 4px 10px rgba(79, 70, 229, 0.3);
            gap: 8px;
        }}
        
        .tool-button:hover {{
            background: linear-gradient(145deg, #3730a3, #312e81);
            text-decoration: none;
            color: white;
            transform: translateY(-2px);
            box-shadow: 0 6px 15px rgba(79, 70, 229, 0.4);
        }}
        
        /* Professional info sections */
        .features-section {{
            background: rgba(45, 55, 72, 0.7);
            border: 1px solid rgba(255, 255, 255, 0.1);
            border-radius: 24px;
            padding: 40px;
            margin: 70px auto;
            max-width: 1100px;
            box-shadow: 0 20px 40px rgba(0, 0, 0, 0.3);
            backdrop-filter: blur(10px);
        }}
        
        .features-title {{
            font-family: 'Inter', sans-serif;
            font-size: 2.4rem;
            font-weight: 700;
            text-align: center;
            background: linear-gradient(135deg, #4F46E5, #8B5CF6);
            -webkit-background-clip: text;
            -webkit-text-fill-color: transparent;
            margin-bottom: 40px;
        }}
        
        .features-list {{
            display: grid;
            grid-template-columns: repeat(auto-fit, minmax(300px, 1fr));
            gap: 25px;
        }}
        
        .feature-item {{
            background: linear-gradient(145deg, rgba(55, 65, 81, 0.7), rgba(45, 55, 72, 0.7));
            padding: 25px;
            border-radius: 16px;
            border-left: 5px solid #4F46E5;
            box-shadow: 0 8px 20px rgba(0, 0, 0, 0.2);
            transition: transform 0.3s ease;
            backdrop-filter: blur(10px);
        }}
        
        .feature-item:hover {{
            transform: translateY(-5px);
        }}
        
        .feature-title {{
            font-weight: 700;
            color: #ffffff;
            font-size: 1.2rem;
            margin-bottom: 12px;
        }}
        
        .feature-desc {{
            color: #d1d5db;
            font-size: 1rem;
            line-height: 1.6;
        }}
        
        .info-section {{
            background: rgba(45, 55, 72, 0.7);
            border: 1px solid rgba(255, 255, 255, 0.1);
            border-radius: 20px;
            padding: 35px;
            margin: 70px auto;
            text-align: center;
            color: #e2e8f0;
            font-family: 'Inter', sans-serif;
            max-width: 1000px;
            box-shadow: 0 15px 35px rgba(0, 0, 0, 0.3);
            backdrop-filter: blur(10px);
        }}
        
        /* Image showcase section */
        .showcase-section {{
            margin: 80px auto;
            max-width: 1300px;
            padding: 0 30px;
        }}
        
        .showcase-title {{
            font-family: 'Inter', sans-serif;
            font-size: 2.4rem;
            font-weight: 700;
            text-align: center;
            background: linear-gradient(135deg, #4F46E5, #8B5CF6);
            -webkit-background-clip: text;
            -webkit-text-fill-color: transparent;
            margin-bottom: 20px;
        }}
        
        .showcase-subtitle {{
            font-family: 'Inter', sans-serif;
            font-size: 1.1rem;
            text-align: center;
            color: #cbd5e0;
            margin-bottom: 50px;
            line-height: 1.6;
        }}
        
        .showcase-grid {{
            display: grid;
            grid-template-columns: repeat(auto-fit, minmax(350px, 1fr));
            gap: 35px;
        }}
        
        .showcase-item {{
            background: linear-gradient(145deg, rgba(45, 55, 72, 0.8), rgba(31, 41, 55, 0.8));
            border: 1px solid rgba(255, 255, 255, 0.1);
            border-radius: 20px;
            padding: 25px;
            text-align: center;
            box-shadow: 0 20px 40px rgba(0, 0, 0, 0.3);
            transition: transform 0.3s ease;
            overflow: hidden;
            backdrop-filter: blur(10px);
        }}
        
        .showcase-item:hover {{
            transform: translateY(-7px);
        }}
        
        .showcase-item img {{
            width: 100%;
            height: 220px;
            object-fit: cover;
            border-radius: 16px;
            margin-bottom: 20px;
            transition: transform 0.3s ease;
        }}
        
        .showcase-item:hover img {{
            transform: scale(1.05);
        }}
        
        .showcase-caption {{
            font-family: 'Inter', sans-serif;
            font-size: 1rem;
            color: #cbd5e0;
            line-height: 1.6;
        }}
        
        /* Responsive design */
        @media (max-width: 1200px) {{
            .tools-grid {{
                grid-template-columns: repeat(2, 1fr);
                gap: 25px;
            }}
            .hero-section {{
                flex-direction: column;
                text-align: center;
                padding: 40px 25px;
            }}
            .nav-grid {{
                grid-template-columns: repeat(4, 1fr);
            }}
        }}
        
        @media (max-width: 900px) {{
            .main-title {{
                font-size: 3rem;
            }}
            .tools-grid {{
                grid-template-columns: 1fr;
                max-width: 600px;
            }}
            .tool-card {{
                min-height: 220px;
            }}
            .nav-grid {{
                grid-template-columns: repeat(3, 1fr);
            }}
            .features-list {{
                grid-template-columns: 1fr;
            }}
        }}
        
        @media (max-width: 600px) {{
            .nav-grid {{
                grid-template-columns: repeat(2, 1fr);
            }}
            .main-title {{
                font-size: 2.5rem;
            }}
            .tools-main-title {{
                font-size: 2.2rem;
            }}
            .hero-title {{
                font-size: 1.8rem;
            }}
            .showcase-grid {{
                grid-template-columns: 1fr;
            }}
        }}
        
        @media (max-width: 480px) {{
            .nav-grid {{
                grid-template-columns: 1fr;
            }}
            .badge {{
                padding: 8px 14px;
                font-size: 0.8rem;
            }}
        }}
    </style>
    """, unsafe_allow_html=True)
    
else:
    # Professional Light theme CSS with enhanced navigation dashboard
    st.markdown(f"""
    <style>
        @import url('https://fonts.googleapis.com/css2?family=Inter:wght@300;400;500;600;700;800&display=swap');
        
        /* Hide Streamlit elements */
        #MainMenu {{visibility: hidden;}}
        footer {{visibility: hidden;}}
        header {{visibility: hidden;}}
        
        /* Smooth scrolling */
        html {{
            scroll-behavior: smooth;
            scroll-padding-top: 100px;
        }}
        
        /* Professional light theme styling */
        .stApp {{
            background: linear-gradient(180deg, #f8fafc 0%, #e2e8f0 100%);
            color: #1a202c;
            font-family: 'Inter', sans-serif;
        }}
        
        /* Glassmorphism Navigation Dashboard Styling */
        .nav-dashboard {{
            background: rgba(255, 255, 255, 0.8);
            backdrop-filter: blur(10px);
            border: 1px solid rgba(255, 255, 255, 0.2);
            border-radius: 16px;
            padding: 15px;
            margin: 15px auto 25px auto;
            max-width: 1000px;
            box-shadow: 0 8px 32px rgba(0, 0, 0, 0.1);
            position: relative;
            z-index: 100;
        }}
        
        .nav-title {{
            font-family: 'Inter', sans-serif;
            font-size: 1.1rem;
            font-weight: 600;
            text-align: center;
            color: #2d3748;
            margin-bottom: 15px;
            letter-spacing: 0.02em;
            text-transform: uppercase;
        }}
        
        .nav-grid {{
            display: grid;
            grid-template-columns: repeat(auto-fit, minmax(130px, 1fr));
            gap: 10px;
        }}
        
        .nav-link {{
            display: flex;
            flex-direction: column;
            align-items: center;
            justify-content: center;
            padding: 12px 10px;
            background: rgba(247, 250, 252, 0.5);
            color: #4a5568;
            text-decoration: none;
            border-radius: 12px;
            font-family: 'Inter', sans-serif;
            font-weight: 500;
            font-size: 0.85rem;
            text-align: center;
            transition: all 0.3s ease;
            border: 1px solid rgba(255, 255, 255, 0.2);
            min-height: 40px;
            cursor: pointer;
            box-shadow: 0 4px 6px rgba(0, 0, 0, 0.05);
        }}
        
        .nav-link:hover {{
            background: linear-gradient(145deg, #4F46E5, #8B5CF6);
            color: white;
            text-decoration: none;
            transform: translateY(-3px);
            box-shadow: 0 6px 15px rgba(79, 70, 229, 0.2);
        }}
        
        .nav-link:active {{
            transform: translateY(0px);
        }}
        
        .nav-icon {{
            font-size: 1.2rem;
            margin-bottom: 5px;
        }}
        
        /* Main title styling */
        .main-title {{
            font-family: 'Inter', sans-serif;
            font-size: 3.8rem;
            font-weight: 800;
            text-align: center;
            background: linear-gradient(135deg, #4F46E5, #8B5CF6, #EC4899);
            -webkit-background-clip: text;
            -webkit-text-fill-color: transparent;
            margin: 10px 0 15px 0;
            letter-spacing: -0.02em;
        }}
        
        .subtitle {{
            text-align: center;
            font-family: 'Inter', sans-serif;
            font-size: 1.4rem;
            color: #4a5568;
            margin-bottom: 15px;
            font-weight: 500;
        }}
        
        .tagline {{
            text-align: center;
            font-family: 'Inter', sans-serif;
            font-size: 1.1rem;
            color: #718096;
            margin-bottom: 50px;
            font-weight: 400;
            font-style: italic;
        }}
        
        /* Hero section styling */
        .hero-section {{
            display: flex;
            align-items: center;
            justify-content: space-between;
            margin: 40px auto 80px auto;
            max-width: 1200px;
            padding: 50px 30px;
            background: rgba(255, 255, 255, 0.9);
            border-radius: 24px;
            border: 1px solid rgba(255, 255, 255, 0.2);
            box-shadow: 0 25px 50px rgba(0, 0, 0, 0.1);
            gap: 50px;
            backdrop-filter: blur(10px);
        }}
        
        .hero-content {{
            flex: 1;
            max-width: 500px;
        }}
        
        .hero-image {{
            flex: 1;
            max-width: 500px;
        }}
        
        .hero-image img {{
            width: 100%;
            height: 320px;
            object-fit: cover;
            border-radius: 20px;
            box-shadow: 0 20px 40px rgba(0, 0, 0, 0.15);
        }}
        
        .hero-title {{
            font-size: 2.2rem;
            font-weight: 700;
            color: #2d3748;
            margin-bottom: 25px;
            line-height: 1.3;
        }}
        
        .hero-desc {{
            font-size: 1.1rem;
            line-height: 1.7;
            color: #4a5568;
            margin-bottom: 30px;
        }}
        
        .badge-container {{
            display: flex;
            gap: 12px;
            flex-wrap: wrap;
        }}
        
        .badge {{
            padding: 10px 18px;
            border-radius: 25px;
            font-size: 0.9rem;
            font-weight: 600;
            color: white;
            box-shadow: 0 4px 8px rgba(0, 0, 0, 0.1);
            backdrop-filter: blur(10px);
        }}
        
        .badge-primary {{ background: linear-gradient(145deg, #4F46E5, #3730a3); }}
        .badge-success {{ background: linear-gradient(145deg, #10B981, #059669); }}
        .badge-warning {{ background: linear-gradient(145deg, #F59E0B, #D97706); }}
        
        /* Tools section header */
        .tools-header {{
            text-align: center;
            margin: 80px auto 50px auto;
            max-width: 800px;
        }}
        
        .tools-main-title {{
            font-family: 'Inter', sans-serif;
            font-size: 3rem;
            font-weight: 800;
            background: linear-gradient(135deg, #4F46E5, #8B5CF6);
            -webkit-background-clip: text;
            -webkit-text-fill-color: transparent;
            margin-bottom: 25px;
        }}
        
        .tools-subtitle {{
            font-family: 'Inter', sans-serif;
            font-size: 1.3rem;
            color: #4a5568;
            margin-bottom: 50px;
            line-height: 1.6;
        }}
        
        /* Professional tool cards with enhanced spacing */
        .tools-grid {{
            display: grid;
            grid-template-columns: repeat(3, 1fr);
            gap: 30px;
            max-width: 1300px;
            margin: 0 auto;
            padding: 0 30px;
        }}
        
        .tool-card {{
            background: linear-gradient(145deg, rgba(255, 255, 255, 0.9), rgba(247, 250, 252, 0.9));
            border: 1px solid rgba(255, 255, 255, 0.2);
            border-radius: 20px;
            padding: 30px;
            text-align: left;
            box-shadow: 0 15px 30px rgba(0, 0, 0, 0.08);
            transition: all 0.3s ease;
            min-height: 240px;
            display: flex;
            flex-direction: column;
            scroll-margin-top: 140px;
            position: relative;
            overflow: hidden;
            backdrop-filter: blur(10px);
        }}
        
        .tool-card::before {{
            content: '';
            position: absolute;
            top: 0;
            left: 0;
            width: 100%;
            height: 5px;
            background: linear-gradient(90deg, #4F46E5, #8B5CF6);
            opacity: 0.8;
        }}
        
        .tool-card:hover {{
            box-shadow: 0 20px 40px rgba(0, 0, 0, 0.15);
            transform: translateY(-7px);
            border-color: rgba(255, 255, 255, 0.3);
        }}
        
        .tool-card:target {{
            border-color: #4F46E5;
            box-shadow: 0 0 30px rgba(79, 70, 229, 0.3);
            animation: highlight 2s ease-in-out;
        }}
        
        @keyframes highlight {{
            0% {{ box-shadow: 0 0 30px rgba(79, 70, 229, 0.4); }}
            50% {{ box-shadow: 0 0 40px rgba(79, 70, 229, 0.3); }}
            100% {{ box-shadow: 0 0 30px rgba(79, 70, 229, 0.3); }}
        }}
        
        .tool-title {{
            font-family: 'Inter', sans-serif;
            font-size: 1.5rem;
            font-weight: 700;
            color: #2d3748;
            margin-bottom: 15px;
            line-height: 1.4;
        }}
        
        .tool-desc {{
            font-family: 'Inter', sans-serif;
            font-size: 1rem;
            color: #718096;
            line-height: 1.6;
            margin-bottom: 20px;
            flex-grow: 1;
        }}
        
        .tool-button {{
            display: inline-flex;
            align-items: center;
            justify-content: center;
            padding: 12px 24px;
            background: linear-gradient(145deg, #4F46E5, #3730a3);
            color: white;
            text-decoration: none;
            border-radius: 12px;
            font-family: 'Inter', sans-serif;
            font-weight: 600;
            font-size: 1rem;
            transition: all 0.3s ease;
            align-self: flex-start;
            box-shadow: 0 4px 10px rgba(79, 70, 229, 0.2);
            gap: 8px;
        }}
        
        .tool-button:hover {{
            background: linear-gradient(145deg, #3730a3, #312e81);
            text-decoration: none;
            color: white;
            transform: translateY(-2px);
            box-shadow: 0 6px 15px rgba(79, 70, 229, 0.3);
        }}
        
        /* Professional info sections */
        .features-section {{
            background: rgba(255, 255, 255, 0.9);
            border: 1px solid rgba(255, 255, 255, 0.2);
            border-radius: 24px;
            padding: 40px;
            margin: 70px auto;
            max-width: 1100px;
            box-shadow: 0 20px 40px rgba(0, 0, 0, 0.08);
            backdrop-filter: blur(10px);
        }}
        
        .features-title {{
            font-family: 'Inter', sans-serif;
            font-size: 2.4rem;
            font-weight: 700;
            text-align: center;
            background: linear-gradient(135deg, #4F46E5, #8B5CF6);
            -webkit-background-clip: text;
            -webkit-text-fill-color: transparent;
            margin-bottom: 40px;
        }}
        
        .features-list {{
            display: grid;
            grid-template-columns: repeat(auto-fit, minmax(300px, 1fr));
            gap: 25px;
        }}
        
        .feature-item {{
            background: linear-gradient(145deg, rgba(247, 250, 252, 0.7), rgba(237, 242, 247, 0.7));
            padding: 25px;
            border-radius: 16px;
            border-left: 5px solid #4F46E5;
            box-shadow: 0 8px 20px rgba(0, 0, 0, 0.05);
            transition: transform 0.3s ease;
            backdrop-filter: blur(10px);
        }}
        
        .feature-item:hover {{
            transform: translateY(-5px);
        }}
        
        .feature-title {{
            font-weight: 700;
            color: #2d3748;
            font-size: 1.2rem;
            margin-bottom: 12px;
        }}
        
        .feature-desc {{
            color: #4a5568;
            font-size: 1rem;
            line-height: 1.6;
        }}
        
        .info-section {{
            background: rgba(255, 255, 255, 0.9);
            border: 1px solid rgba(255, 255, 255, 0.2);
            border-radius: 20px;
            padding: 35px;
            margin: 70px auto;
            text-align: center;
            color: #4a5568;
            font-family: 'Inter', sans-serif;
            max-width: 1000px;
            box-shadow: 0 15px 35px rgba(0, 0, 0, 0.08);
            backdrop-filter: blur(10px);
        }}
        
        /* Image showcase section */
        .showcase-section {{
            margin: 80px auto;
            max-width: 1300px;
            padding: 0 30px;
        }}
        
        .showcase-title {{
            font-family: 'Inter', sans-serif;
            font-size: 2.4rem;
            font-weight: 700;
            text-align: center;
            background: linear-gradient(135deg, #4F46E5, #8B5CF6);
            -webkit-background-clip: text;
            -webkit-text-fill-color: transparent;
            margin-bottom: 20px;
        }}
        
        .showcase-subtitle {{
            font-family: 'Inter', sans-serif;
            font-size: 1.1rem;
            text-align: center;
            color: #718096;
            margin-bottom: 50px;
            line-height: 1.6;
        }}
        
        .showcase-grid {{
            display: grid;
            grid-template-columns: repeat(auto-fit, minmax(350px, 1fr));
            gap: 35px;
        }}
        
        .showcase-item {{
            background: linear-gradient(145deg, rgba(255, 255, 255, 0.9), rgba(247, 250, 252, 0.9));
            border: 1px solid rgba(255, 255, 255, 0.2);
            border-radius: 20px;
            padding: 25px;
            text-align: center;
            box-shadow: 0 20px 40px rgba(0, 0, 0, 0.08);
            transition: transform 0.3s ease;
            overflow: hidden;
            backdrop-filter: blur(10px);
        }}
        
        .showcase-item:hover {{
            transform: translateY(-7px);
        }}
        
        .showcase-item img {{
            width: 100%;
            height: 220px;
            object-fit: cover;
            border-radius: 16px;
            margin-bottom: 20px;
            transition: transform 0.3s ease;
        }}
        
        .showcase-item:hover img {{
            transform: scale(1.05);
        }}
        
        .showcase-caption {{
            font-family: 'Inter', sans-serif;
            font-size: 1rem;
            color: #4a5568;
            line-height: 1.6;
        }}
        
        /* Responsive design */
        @media (max-width: 1200px) {{
            .tools-grid {{
                grid-template-columns: repeat(2, 1fr);
                gap: 25px;
            }}
            .hero-section {{
                flex-direction: column;
                text-align: center;
                padding: 40px 25px;
            }}
            .nav-grid {{
                grid-template-columns: repeat(4, 1fr);
            }}
        }}
        
        @media (max-width: 900px) {{
            .main-title {{
                font-size: 3rem;
            }}
            .tools-grid {{
                grid-template-columns: 1fr;
                max-width: 600px;
            }}
            .tool-card {{
                min-height: 220px;
            }}
            .nav-grid {{
                grid-template-columns: repeat(3, 1fr);
            }}
            .features-list {{
                grid-template-columns: 1fr;
            }}
        }}
        
        @media (max-width: 600px) {{
            .nav-grid {{
                grid-template-columns: repeat(2, 1fr);
            }}
            .main-title {{
                font-size: 2.5rem;
            }}
            .tools-main-title {{
                font-size: 2.2rem;
            }}
            .hero-title {{
                font-size: 1.8rem;
            }}
            .showcase-grid {{
                grid-template-columns: 1fr;
            }}
        }}
        
        @media (max-width: 480px) {{
            .nav-grid {{
                grid-template-columns: 1fr;
            }}
            .badge {{
                padding: 8px 14px;
                font-size: 0.8rem;
            }}
        }}
    </style>
    """, unsafe_allow_html=True)

# Compact Navigation Dashboard with internal anchor links
st.markdown("""
<div class="nav-dashboard">
    <h3 class="nav-title"> Quick Access to Financial Tools </h3>
    <div class="nav-grid">
        <a href="#sip-calculator" class="nav-link"><span class="nav-icon">📈</span>SIP Calculator</a>
        <a href="#credit-score" class="nav-link"><span class="nav-icon">💳</span>Credit Score</a>
        <a href="#tax-calculator" class="nav-link"><span class="nav-icon">📊</span>Tax Calculator</a>
        <a href="#emi-calculator" class="nav-link"><span class="nav-icon">🏠</span>EMI Calculator</a>
        <a href="#expense-tracker" class="nav-link"><span class="nav-icon">💰</span>Expense Tracker</a>
        <a href="#retirement-planner" class="nav-link"><span class="nav-icon">🏖️</span>Retirement Planner</a>
        <a href="#stock-market" class="nav-link"><span class="nav-icon">📈</span>Stock Market</a>
    </div>
</div>
""", unsafe_allow_html=True)

# Header section
st.markdown("""
<h1 class="main-title">Capital Compass</h1>
<p class="subtitle"><strong>All your financial solutions in one place</strong></p>
<p class="tagline">"Where Smart Money Decisions Begin"</p>
""", unsafe_allow_html=True)

# Hero section with professional image
st.markdown(f"""
<div class="hero-section">
    <div class="hero-content">
        <h2 class="hero-title">Professional Financial Management Made Simple</h2>
        <p class="hero-desc">
            Experience the power of comprehensive financial planning with our suite of professional-grade calculators and tools. 
            Designed for accuracy, built for professionals, trusted by thousands.
        </p>
        <div class="badge-container">
            <span class="badge badge-primary">Enterprise Ready</span>
            <span class="badge badge-success">Bank-Grade Security</span>
            <span class="badge badge-warning">Real-time Analytics</span>
        </div>
    </div>
    <div class="hero-image">
        <img src="{hero_image_url}" alt="Professional Financial Dashboard" />
    </div>
</div>
""", unsafe_allow_html=True)

# Enhanced description section
st.markdown("""
<div class="features-section">
    <h2 class="features-title">What Makes Capital Compass Unique?</h2>
    <div class="features-list">        
        <div class="feature-item">
            <div class="feature-title"><strong>Lightning Fast</strong></div>
            <div class="feature-desc">Get instant results with our optimized calculation engine - no waiting, no delays</div>
        </div>
        <div class="feature-item">
            <div class="feature-title"><strong>Mobile-First Design</strong></div>
            <div class="feature-desc">Perfect experience across all devices with responsive, touch-friendly interfaces</div>
        </div>
        <div class="feature-item">
            <div class="feature-title"><strong>Personalized Insights</strong></div>
            <div class="feature-desc">Smart recommendations based on your financial profile and Indian market conditions</div>
        </div>
        <div class="feature-item">
            <div class="feature-title"><strong>Interactive Visualizations</strong></div>
            <div class="feature-desc">Beautiful charts and graphs that make complex financial data easy to understand</div>
        </div>
    </div>
</div>
""", unsafe_allow_html=True)

# Tools section header
st.markdown("""
<div class="tools-header">
    <h2 class="tools-main-title">🛠️ Our Financial Tools Suite</h2>
    <p class="tools-subtitle">Comprehensive tools to manage every aspect of your financial journey</p>
</div>
""", unsafe_allow_html=True)

st.markdown("---")

# Tools section with anchor IDs
tools = [
    {
        "id": "sip-calculator",
        "name": "SIP Calculator",
        "desc": "Master Systematic Investment Planning with advanced projections and wealth growth analysis for mutual funds and equity investments.",
        "link": "https://financialreach.streamlit.app/"
    },
    {
        "id": "credit-score",
        "name": "Credit Score Estimator", 
        "desc": "AI-Powered Credit Analysis using CIBIL-compatible algorithms with accurate score estimates and improvement strategies.",
        "link": "https://creditscores.streamlit.app/"
    },
    {
        "id": "tax-calculator",
        "name": "Tax Calculator",
        "desc": "Smart Tax Optimization for India's tax regime with liability calculations and deduction comparisons.",
        "link": "https://taxreturncalc.streamlit.app/"
    },
    {
        "id": "emi-calculator",
        "name": "EMI Calculator",
        "desc": "Complete Loan Planning Suite with EMI calculations, amortization schedules and prepayment analysis.",
        "link": "https://emicalculatorsj.streamlit.app/"
    },
    {
        "id": "expense-tracker",
        "name": "Expense Tracker",
        "desc": "Intelligent Expense Management with AI-powered categorization and smart budgeting insights.",
        "link": "https://expensetrac.streamlit.app/"
    },
    {
        "id": "retirement-planner",
        "name": "Retirement Planner",
        "desc": "Strategic Retirement Planning with inflation-adjusted calculations and corpus estimation tools.",
        "link": "https://retirementtrack.streamlit.app/"
    },
    {
        "id": "stock-market",
        "name": "Stock Market checker",
        "desc": "Check realtime stock prices of your favourite stocks with advanced analytics and visualization tools.",
        "link": "https://demo-stockpeers.streamlit.app/?ref=streamlit-io-gallery-favorites&stocks=AAPL%2CMSFT%2CGOOGL%2CNVDA%2CAMZN%2CTSLA%2CMETA"
    }
]

st.markdown('<div class="tools-grid">', unsafe_allow_html=True)
for tool in tools:
    st.markdown(
        f"""
        <div class="tool-card" id="{tool["id"]}">
            <h4 class="tool-title">{tool["name"]}</h4>
            <p class="tool-desc">{tool["desc"]}</p>
            <a href="{tool["link"]}" target="_blank" class="tool-button">
                Launch Tool →
            </a>
        </div>
        """,
        unsafe_allow_html=True
    )
st.markdown('</div>', unsafe_allow_html=True)

# Interactive Financial Dashboard Section
st.markdown("""
<div class="tools-header">
    <h2 class="tools-main-title">📊 Interactive Financial Dashboard</h2>
    <p class="tools-subtitle">Real-time financial insights and analytics at your fingertips</p>
</div>
""", unsafe_allow_html=True)

# Create some sample financial data
np.random.seed(42)
dates = pd.date_range(start='2023-01-01', end='2023-12-31', freq='D')
stock_prices = 100 + np.cumsum(np.random.randn(len(dates)) * 0.5)
investment_values = 10000 + np.cumsum(np.random.randn(len(dates)) * 100)

# Create a DataFrame
df = pd.DataFrame({
    'Date': dates,
    'Stock Price': stock_prices,
    'Investment Value': investment_values
})

# Create columns for the dashboard
col1, col2, col3 = st.columns(3)

with col1:
    st.markdown("""
    <div style="background: linear-gradient(135deg, #4F46E5, #8B5CF6); padding: 20px; border-radius: 15px; color: white; text-align: center;">
        <h3>Portfolio Value</h3>
        <h2>₹1,24,567</h2>
        <p>+12.3% this month</p>
    </div>
    """, unsafe_allow_html=True)

with col2:
    st.markdown("""
    <div style="background: linear-gradient(135deg, #10B981, #059669); padding: 20px; border-radius: 15px; color: white; text-align: center;">
        <h3>Monthly Savings</h3>
        <h2>₹23,450</h2>
        <p>15% of income</p>
    </div>
    """, unsafe_allow_html=True)

with col3:
    st.markdown("""
    <div style="background: linear-gradient(135deg, #F59E0B, #D97706); padding: 20px; border-radius: 15px; color: white; text-align: center;">
        <h3>Investment Growth</h3>
        <h2>18.7%</h2>
        <p>Annualized return</p>
    </div>
    """, unsafe_allow_html=True)

# Create charts
fig1 = px.line(df, x='Date', y='Stock Price', title='Stock Performance')
fig1.update_layout(
    plot_bgcolor='rgba(0,0,0,0)',
    paper_bgcolor='rgba(0,0,0,0)',
    font_color='white' if st.session_state.dark_mode else 'black'
)

fig2 = px.line(df, x='Date', y='Investment Value', title='Investment Growth')
fig2.update_layout(
    plot_bgcolor='rgba(0,0,0,0)',
    paper_bgcolor='rgba(0,0,0,0)',
    font_color='white' if st.session_state.dark_mode else 'black'
)

chart_col1, chart_col2 = st.columns(2)
with chart_col1:
    st.plotly_chart(fig1, use_container_width=True)

with chart_col2:
    st.plotly_chart(fig2, use_container_width=True)

# Professional showcase section with images
st.markdown(f"""
<div class="showcase-section">
    <h2 class="showcase-title">Trusted by Financial Professionals</h2>
    <p class="showcase-subtitle">See how our tools compare to industry-leading financial platforms</p>
    <div class="showcase-grid">
        <div class="showcase-item">
            <img src="{dashboard_image_url}" alt="Modern Financial Dashboard" />
            <p class="showcase-caption">Advanced Analytics Dashboard - Real-time portfolio tracking and performance analysis</p>
        </div>
        <div class="showcase-item">
            <img src="{analytics_image_url}" alt="Investment Portfolio Interface" />
            <p class="showcase-caption">Investment Portfolio Management - Professional-grade tools for wealth management</p>
        </div>
        <div class="showcase-item">
            <img src="{calculator_image_url}" alt="Financial Calculator Interface" />
            <p class="showcase-caption">Professional Calculator Interface - Precision tools for complex financial calculations</p>
        </div>
    </div>
</div>
""", unsafe_allow_html=True)

st.markdown("---")

# Enhanced info section
st.markdown("""
<div class="info-section">
    <strong>Completely Free Forever</strong><br>
    <em>Powered by cutting-edge fintech algorithms trusted by leading financial institutions</em>
</div>
""", unsafe_allow_html=True)
