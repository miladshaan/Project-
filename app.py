import streamlit as st
import pandas as pd
import plotly.express as px
import plotly.graph_objects as go
from datetime import datetime

# Page configuration
st.set_page_config(
    page_title="Strategic Partnership Analysis",
    page_icon="💼",
    layout="centered",
    initial_sidebar_state="collapsed"
)

# Custom CSS for styling
st.markdown("""
<style>
    .main-header {
        font-size: 2.5rem;
        color: #1f77b4;
        text-align: center;
        margin-bottom: 2rem;
    }
    .section-header {
        font-size: 1.8rem;
        color: #2c3e50;
        border-bottom: 2px solid #3498db;
        padding-bottom: 0.5rem;
        margin-top: 2rem;
    }
    .metric-box {
        background-color: #f8f9fa;
        padding: 1rem;
        border-radius: 10px;
        border-left: 4px solid #3498db;
        margin: 1rem 0;
    }
    .swot-box {
        padding: 1rem;
        border-radius: 10px;
        margin: 1rem 0;
    }
    .strength { background-color: #d4edda; border-left: 4px solid #28a745; }
    .weakness { background-color: #f8d7da; border-left: 4px solid #dc3545; }
    .opportunity { background-color: #d1ecf1; border-left: 4px solid #17a2b8; }
    .threat { background-color: #fff3cd; border-left: 4px solid #ffc107; }
    .final-message {
        background: linear-gradient(135deg, #667eea 0%, #764ba2 100%);
        padding: 3rem;
        border-radius: 15px;
        color: white;
        text-align: center;
    }
    .cover-section {
        background: linear-gradient(135deg, #2c3e50 0%, #3498db 100%);
        padding: 3rem;
        border-radius: 15px;
        color: white;
        text-align: center;
        margin: 2rem 0;
    }
</style>
""", unsafe_allow_html=True)

# Initialize session state for page navigation
if 'page' not in st.session_state:
    st.session_state.page = 'cover'

# Sample data for charts
def create_happiness_chart():
    data = {
        'Date': ['First Meet', 'First Date', 'First Trip', 'Today'],
        'Happiness': [30, 65, 85, 95]
    }
    df = pd.DataFrame(data)
    fig = px.line(df, x='Date', y='Happiness', title='Happiness Index Growth',
                  line_shape='spline', markers=True)
    fig.update_layout(yaxis_range=[0, 100])
    return fig

def create_relationship_metrics():
    metrics = {
        'Metric': ['Trust', 'Communication', 'Fun', 'Support', 'Love'],
        'Score': [90, 98, 97, 95, 100]
    }
    df = pd.DataFrame(metrics)
    fig = px.bar(df, x='Metric', y='Score', title='Relationship Metrics',
                 color='Score', color_continuous_scale='Viridis')
    fig.update_layout(yaxis_range=[0, 100])
    return fig

def create_investment_growth():
    # Updated: Start from August 2019 when you met
    dates = pd.date_range(start='2019-08-01', periods=18, freq='6M')  # Every 6 months from Aug 2019
    growth = [10, 25, 45, 65, 120, 180, 250, 350, 480, 620, 780, 950, 1150, 1350, 1600, 1850, 2100, 2400]
    
    df = pd.DataFrame({
        'Date': dates,
        'Value': growth
    })
    
    fig = px.area(df, x='Date', y='Value', 
                  title='Emotional Investment Growth Since We Met',
                  labels={'Value': 'Relationship Value Index'})
    fig.update_layout(xaxis_title='Timeline', yaxis_title='Relationship Value')
    return fig

# Cover Page
def show_cover():
    st.markdown("<div class='cover-section'>", unsafe_allow_html=True)
    st.markdown("<h1>CONFIDENTIAL</h1>", unsafe_allow_html=True)
    st.markdown("<h2>Strategic Partnership Analysis</h2>", unsafe_allow_html=True)
    st.markdown("<h3 style='color: #e74c3c;'>Milad & Hani</h3>", unsafe_allow_html=True)
    st.markdown("</div>", unsafe_allow_html=True)
    
    st.markdown("---")
    
    col1, col2, col3 = st.columns(3)
    with col1:
        st.info("**Date:** September 29, 2025")
        st.info("**Document ID:** MLD-HNI-073")
    with col2:
        st.warning("**Status:** PROPOSAL - FOR REVIEW")
        st.warning("**Classification:** Restricted")
    with col3:
        st.success("**Prepared for:** Hani")
        st.success("**Version:** 1.0")
    
    st.markdown("---")
    
    st.markdown("""
    <div class='metric-box'>
    <h3>📋 Project Overview</h3>
    <p>This confidential document presents a comprehensive analysis of the strategic partnership 
    between <strong>Milad</strong> and <strong>Hani</strong>. The analysis examines compatibility metrics, 
    growth potential, and long-term viability of this unique partnership opportunity.</p>
    </div>
    """, unsafe_allow_html=True)
    
    if st.button("🚀 Begin Analysis", type="primary", use_container_width=True):
        st.session_state.page = 'executive'

# Executive Summary Page
def show_executive_summary():
    st.markdown("<h1 class='section-header'>EXECUTIVE SUMMARY</h1>", unsafe_allow_html=True)
    
    st.markdown("""
    <div class='metric-box'>
    <h3>💡 Investment Opportunity Analysis</h3>
    <p>This proposal outlines the strategic partnership between <strong>Milad</strong> and <strong>Hani</strong>, 
    demonstrating exceptional compatibility and growth potential since our first meeting in August 2019. The analysis 
    confirms this partnership represents a unique opportunity for long-term emotional returns.</p>
    </div>
    """, unsafe_allow_html=True)
    
    # Key metrics
    col1, col2, col3 = st.columns(3)
    with col1:
        st.metric("Relationship Duration", "6+ Years", "100% Stability")
    with col2:
        st.metric("Emotional ROI", "Exceptional", "+∞% Growth")
    with col3:
        st.metric("Risk Assessment", "Minimal", "Diversified")
    
    st.plotly_chart(create_investment_growth(), use_container_width=True)
    
    st.markdown("""
    ### 📊 Key Findings:
    - **Synergistic Compatibility:** Unprecedented alignment of values and goals since 2019
    - **Sustainable Growth:** Consistent positive trajectory since initial engagement  
    - **Market Position:** Dominant share in respective emotional markets
    - **Future Outlook:** Excellent long-term prospects with minimal volatility
    - **Risk Management:** Proven resilience to external market pressures
    """)
    
    if st.button("📈 Continue to Market Analysis", use_container_width=True):
        st.session_state.page = 'market'

# Market Analysis Page
def show_market_analysis():
    st.markdown("<h1 class='section-header'>MARKET ANALYSIS</h1>", unsafe_allow_html=True)
    
    tab1, tab2, tab3 = st.tabs(["🎯 Target Market", "🏆 Competitive Landscape", "📈 Growth Potential"])
    
    with tab1:
        st.markdown("""
        <div class='metric-box'>
        <h3>Primary Market: Hani's Heart</h3>
        <p><strong>Target Market:</strong> Hani's Heart - 100% M.S. market share achieved</p>
        <p><strong>Market Size:</strong> Infinite capacity for love and happiness</p>
        <p><strong>Market Growth:</strong> Exponential since August 2019</p>
        <p><strong>Customer Loyalty:</strong> Absolute and unwavering</p>
        </div>
        """, unsafe_allow_html=True)
        
        # Create a market share chart
        data = {'Segment': ['Hani\'s Heart', 'Remaining Market'], 'Share': [100, 0]}
        df = pd.DataFrame(data)
        fig = px.pie(df, values='Share', names='Segment', 
                     title='Market Share Distribution',
                     color_discrete_sequence=['#3498db', '#ecf0f1'])
        st.plotly_chart(fig, use_container_width=True)
    
    with tab2:
        st.markdown("""
        <div class='metric-box'>
        <h3>Competitive Analysis</h3>
        <p><strong>Direct Competitors:</strong> None identified</p>
        <p><strong>Indirect Competitors:</strong> Work commitments, hobbies, social obligations</p>
        <p><strong>Competitive Advantage:** Irreplaceable emotional connection and compatibility</p>
        <p><strong>Barrier to Entry:</strong> Extremely high (requires unique compatibility metrics)</p>
        </div>
        """, unsafe_allow_html=True)
        
        st.success("✅ No viable competitive threats detected")
        st.success("✅ Sustainable competitive advantage confirmed")
        st.success("✅ Market entry barriers provide strong protection")
    
    with tab3:
        st.plotly_chart(create_happiness_chart(), use_container_width=True)
        st.markdown("""
        **📊 Growth Projections:**
        - **Short-term (1 year):** Continued happiness appreciation and deeper connection
        - **Medium-term (5 years):** Partnership formalization and shared life milestones  
        - **Long-term (Lifetime):** Sustainable joy, fulfillment, and legacy building
        - **Risk Factor:** Negligible - partnership has proven crisis-resistant
        """)
    
    if st.button("📊 View Performance Metrics", use_container_width=True):
        st.session_state.page = 'metrics'

# Metrics Page
def show_metrics():
    st.markdown("<h1 class='section-header'>KEY PERFORMANCE INDICATORS</h1>", unsafe_allow_html=True)
    
    st.plotly_chart(create_relationship_metrics(), use_container_width=True)
    
    # Key metrics in columns
    col1, col2, col3 = st.columns(3)
    with col1:
        st.metric("Happiness Index", "100%", "+5% vs target")
        st.metric("Trust Level", "98%", "Industry leading")
        st.metric("Conflict Resolution", "90%", "Efficient")
    with col2:
        st.metric("Communication", "92%", "Excellent")
        st.metric("Future Alignment", "96%", "Strong")
        st.metric("Adventure Score", "90%", "Growing")
    with col3:
        st.metric("Support System", "94%", "Reliable")
        st.metric("Fun Factor", "91%", "High")
        st.metric("Overall Score", "97%", "Exceptional")
    
    # Interactive metric
    st.markdown("---")
    st.subheader("🎚️ Relationship Health Score")
    health_score = st.slider("How would you rate our relationship health?", 80, 100, 94)
    
    if health_score >= 95:
        rating = "**Outstanding** 🌟"
    elif health_score >= 90:
        rating = "**Excellent** 💫"
    else:
        rating = "**Very Good** 👍"
    
    st.write(f"Current consensus score: {health_score}% - {rating}")
    
    st.markdown("""
    ### 📋 Performance Summary:
    - All key metrics exceed industry standards
    - Consistent performance across all categories
    - Positive trend in all measurable aspects
    - Strong foundation for future growth
    """)
    
    if st.button("🔍 SWOT Analysis", use_container_width=True):
        st.session_state.page = 'swot'

# SWOT Analysis Page
def show_swot():
    st.markdown("<h1 class='section-header'>SWOT ANALYSIS</h1>", unsafe_allow_html=True)
    
    st.markdown("""
    <div class='metric-box'>
    <h3>📋 Comprehensive Strategic Analysis</h3>
    <p>This SWOT analysis examines the internal strengths and weaknesses of the partnership, 
    along with external opportunities and threats that may impact future performance.</p>
    """, unsafe_allow_html=True)
    
    col1, col2 = st.columns(2)
    
    with col1:
        st.markdown("""
        <div class='swot-box strength'>
            <h3>💪 Strengths</h3>
            <ul>
                <li>Unmatched emotional connection and chemistry</li>
                <li>Excellent communication and conflict resolution</li>
                <li>Shared values, goals, and life vision</li>
                <li>Proven resilience during challenges</li>
                <li>Complementary personalities and skills</li>
                <li>Strong foundation of trust and respect</li>
            </ul>
        </div>
        """, unsafe_allow_html=True)
        
        st.markdown("""
        <div class='swot-box weakness'>
            <h3>⚠️ Weaknesses</h3>
            <ul>
                <li>Occasional over-investment in quality time</li>
                <li>High mutual emotional dependency</li>
                <li>Potential for reduced individual space</li>
                <li>Emotional vulnerability to external factors</li>
            </ul>
        </div>
        """, unsafe_allow_html=True)
    
    with col2:
        st.markdown("""
        <div class='swot-box opportunity'>
            <h3>🚀 Opportunities</h3>
            <ul>
                <li>Global expansion (travel together)</li>
                <li>Product development (future plans)</li>
                <li>Shared personal and professional growth</li>
                <li>Building a life legacy together</li>
                <li>Creating lasting memories and traditions</li>
                <li>Mentoring future generations</li>
            </ul>
        </div>
        """, unsafe_allow_html=True)
        
        st.markdown("""
        <div class='swot-box threat'>
            <h3>🛡️ Threats</h3>
            <ul>
                <li>None identified - business model is crisis-resistant</li>
            </ul>
        </div>
        """, unsafe_allow_html=True)
    
    st.markdown("""
    ### 🎯 Strategic Recommendations:
    - **Leverage Strengths:** Continue building on excellent communication and shared values
    - **Address Weaknesses:** Maintain healthy boundaries while nurturing connection
    - **Capture Opportunities:** Proactively plan shared experiences and growth
    - **Mitigate Threats:** Develop resilience strategies for external challenges
    """)
    
    if st.button("💌 Final Recommendation", use_container_width=True):
        st.session_state.page = 'final'

# Final Recommendation Page
def show_final():
    # Use Streamlit's native functions instead of complex HTML
    st.markdown("""
    <div class='final-message'>
        <h1 style='color: white; font-size: 2.5rem;'>FINAL RECOMMENDATION</h1>
    </div>
    """, unsafe_allow_html=True)
    
    st.markdown("### After comprehensive analysis of all qualitative and quantitative data...")
    
    st.success("## 🎯 STRONG BUY RECOMMENDATION")
    
    st.markdown("### **The most successful investment isn't in markets or companies - it's in us.**")
    
    st.markdown("""
    This wasn't a project. It's my way of showing you that what we have is the best ROI I could ever imagine. 
    Every metric points to one conclusion.
    """)
    
    # Birthday message section - using Streamlit native functions
    st.balloons()
    
    st.markdown("---")
    st.markdown("# 🎂 Happy Birthday, babe!")
    st.markdown("### I love you, and I choose us.")
    st.markdown("---")
    
    st.markdown("### With all my love,")
    st.markdown("# M.S.")
    
    if st.button("🔄 Start Over", use_container_width=True):
        st.session_state.page = 'cover'

# Main app logic
def main():
    # Add a simple header for navigation context
    if st.session_state.page != 'cover':
        col1, col2, col3 = st.columns([1, 2, 1])
        with col2:
            progress_text = {
                'executive': "Step 1/5: Executive Summary",
                'market': "Step 2/5: Market Analysis", 
                'metrics': "Step 3/5: Performance Metrics",
                'swot': "Step 4/5: SWOT Analysis",
                'final': "Step 5/5: Final Recommendation"
            }.get(st.session_state.page, "")
            
            if progress_text:
                st.info(f"📋 {progress_text}")
    
    # Show the appropriate page
    if st.session_state.page == 'cover':
        show_cover()
    elif st.session_state.page == 'executive':
        show_executive_summary()
    elif st.session_state.page == 'market':
        show_market_analysis()
    elif st.session_state.page == 'metrics':
        show_metrics()
    elif st.session_state.page == 'swot':
        show_swot()
    elif st.session_state.page == 'final':
        show_final()

if __name__ == "__main__":
    main()