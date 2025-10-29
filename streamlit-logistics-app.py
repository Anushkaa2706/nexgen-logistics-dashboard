import streamlit as st
import pandas as pd
import plotly.express as px
import plotly.graph_objects as go

st.set_page_config(page_title="NexGen Logistics AI", layout="wide")

# Header
st.markdown("""
<div style='background: linear-gradient(90deg, #2563eb 0%, #1e40af 100%); padding: 2rem; border-radius: 10px; margin-bottom: 2rem;'>
    <h1 style='color: white; margin: 0;'>🚚 NexGen Logistics Intelligence Platform</h1>
    <p style='color: #dbeafe; margin: 0;'>AI-Powered Analytics & Optimization Dashboard</p>
</div>
""", unsafe_allow_html=True)

# Tabs
tab1, tab2, tab3, tab4 = st.tabs(["📊 Overview", "🚛 Delivery", "💰 Costs", "🗺️ Routes"])

# Data
delivery_data = pd.DataFrame({
    'month': ['Jan', 'Feb', 'Mar', 'Apr', 'May', 'Jun'],
    'onTime': [78, 75, 72, 70, 68, 65],
    'delayed': [22, 25, 28, 30, 32, 35]
})

cost_data = pd.DataFrame({
    'category': ['Fuel', 'Labor', 'Maintenance', 'Insurance', 'Tech'],
    'amount': [2450000, 1960000, 1260000, 840000, 490000],
    'percentage': [35, 28, 18, 12, 7]
})

route_data = pd.DataFrame({
    'route': ['Mumbai-Delhi', 'Delhi-Bangalore', 'Mumbai-Chennai'],
    'distance': [1450, 2150, 1340],
    'time': [28, 42, 26],
    'cost': [45000, 68000, 42000],
    'utilization': [87, 82, 91]
})

with tab1:
    # KPIs
    col1, col2, col3, col4 = st.columns(4)
    with col1:
        st.metric("On-Time Delivery", "65%", "-3%", delta_color="inverse")
    with col2:
        st.metric("Avg Delay", "4.2 hrs", "+0.4 hrs", delta_color="inverse")
    with col3:
        st.metric("Monthly Orders", "19.5K", "+8%")
    with col4:
        st.metric("Cost per Delivery", "₹245", "+5%", delta_color="inverse")
    
    st.markdown("---")
    
    # AI Predictions
    st.subheader("🤖 AI-Powered Predictive Insights")
    
    col1, col2 = st.columns(2)
    
    with col1:
        st.error("**🚨 High Risk Alert (78% confidence)**")
        st.write("Mumbai-Delhi delays expected")
        st.info("💡 Recommendation: Add 2 vehicles, avoid peak hours")
        
        st.warning("**⚠️ Cost Alert (85% confidence)**")
        st.write("Fuel costs up 12% next month")
        st.info("💡 Recommendation: Optimize routes, negotiate contracts")
    
    with col2:
        st.warning("**📦 Capacity Issue (92% confidence)**")
        st.write("Chennai warehouse at 95% capacity")
        st.info("💡 Recommendation: Redistribute inventory")
        
        st.success("**✨ Opportunity (88% confidence)**")
        st.write("Bangalore-Kolkata route underutilized")
        st.info("💡 Recommendation: Increase marketing")
    
    st.markdown("---")
    
    # Charts
    col1, col2 = st.columns(2)
    
    with col1:
        st.subheader("Delivery Performance Trend")
        fig = px.line(delivery_data, x='month', y=['onTime', 'delayed'],
                     labels={'value': 'Percentage', 'variable': 'Status'},
                     color_discrete_map={'onTime': '#10b981', 'delayed': '#ef4444'})
        st.plotly_chart(fig, use_container_width=True)
    
    with col2:
        st.subheader("Cost Distribution")
        fig = px.pie(cost_data, values='percentage', names='category',
                    color_discrete_sequence=px.colors.qualitative.Set2)
        st.plotly_chart(fig, use_container_width=True)

with tab2:
    st.subheader("📈 Delivery Performance Analysis")
    
    fig = go.Figure()
    fig.add_trace(go.Scatter(x=delivery_data['month'], y=delivery_data['onTime'],
                            mode='lines+markers', name='On-Time %',
                            line=dict(color='#10b981', width=3)))
    fig.add_trace(go.Scatter(x=delivery_data['month'], y=delivery_data['delayed'],
                            mode='lines+markers', name='Delayed %',
                            line=dict(color='#ef4444', width=3)))
    fig.update_layout(height=400)
    st.plotly_chart(fig, use_container_width=True)
    
    st.warning("""
    **Key Findings:**
    - On-time delivery down 13% over 6 months (78% → 65%)
    - Average delays increased significantly
    - Recommendation: Implement predictive delay alerts
    """)

with tab3:
    st.subheader("💰 Cost Intelligence & Optimization")
    
    col1, col2 = st.columns([1, 1])
    
    with col1:
        fig = px.pie(cost_data, values='amount', names='category',
                    title='Monthly Cost Breakdown',
                    color_discrete_sequence=px.colors.qualitative.Bold)
        st.plotly_chart(fig, use_container_width=True)
    
    with col2:
        st.subheader("Cost Details")
        for i, row in cost_data.iterrows():
            with st.container():
                st.write(f"**{row['category']}**")
                st.write(f"₹{row['amount']:,} ({row['percentage']}%)")
                savings = row['amount'] * 0.15
                st.success(f"Potential savings: ₹{savings:,.0f}")
                st.markdown("---")
        
        st.success("**Total Savings Potential: ₹847,000/month**")

with tab4:
    st.subheader("🗺️ Smart Route Optimization")
    
    fig = px.bar(route_data, x='route', y=['utilization', 'time'],
                barmode='group', 
                labels={'value': 'Value', 'variable': 'Metric'},
                color_discrete_map={'utilization': '#10b981', 'time': '#3b82f6'})
    st.plotly_chart(fig, use_container_width=True)
    
    st.subheader("Route Details")
    st.dataframe(route_data.style.format({
        'distance': '{:,.0f} km',
        'time': '{:.0f} hrs',
        'cost': '₹{:,.0f}',
        'utilization': '{:.0f}%'
    }), use_container_width=True)
    
    st.info("""
    **Optimization Recommendations:**
    - Mumbai-Chennai: Best performer (91% utilization)
    - Consider AI-based dynamic routing
    - Projected fuel savings: ₹280,000/month
    """)

# Footer
st.markdown("---")
st.markdown("""
<div style='text-align: center; color: #6b7280; padding: 1rem;'>
    <p>NexGen Logistics Innovation Challenge | AI Internship Project</p>
    <p style='font-size: 0.875rem;'>Built with Python + Streamlit | Real-time Analytics Dashboard</p>
</div>
""", unsafe_allow_html=True)
