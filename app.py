import streamlit as st
import pandas as pd
import seaborn as sns
import matplotlib.pyplot as plt

# Page configuration
st.set_page_config(
    page_title="Exam Practice Time Optimization",
    page_icon="📊",
    layout="wide",
    initial_sidebar_state="expanded",
)

# Title and description
st.title("📊 Exam Practice Time Optimization Dashboard")
st.markdown("""
Optimize student performance by analyzing practice durations and scores.  
Upload your dataset to explore insights and recommendations.  
**Developed by Pankaj Devikar**
""")

# Sidebar for file upload
st.sidebar.header("Upload Dataset")
uploaded_file = st.sidebar.file_uploader("Upload your dataset (CSV)", type=["csv"])

# Load dataset
if uploaded_file is not None:
    df = pd.read_csv(uploaded_file)
    st.sidebar.success("File uploaded successfully!")
    
    # Show dataset preview in expandable section
    with st.expander("📋 Dataset Preview", expanded=False):
        st.dataframe(df.head())

    # Check for required columns
    required_columns = ["Student Name", "Topic", "Practice Duration (Minutes)", "Performance Score"]
    if all(column in df.columns for column in required_columns):
        # Layout with tabs
        tab1, tab2, tab3 = st.tabs(["📊 Visualizations", "📈 Recommendations", "📑 Summary"])

        # Tab 1: Visualizations
        with tab1:
            st.subheader("Visualizations")

            # Practice Duration Distribution
            st.write("### Distribution of Practice Durations")
            fig1, ax1 = plt.subplots(figsize=(10, 6))
            sns.histplot(df["Practice Duration (Minutes)"], bins=20, kde=True, color="blue", ax=ax1)
            ax1.set_title("Distribution of Practice Durations")
            ax1.set_xlabel("Practice Duration (Minutes)")
            ax1.set_ylabel("Frequency")
            st.pyplot(fig1)

            # Performance Score by Topic
            st.write("### Performance Score by Topic")
            fig2, ax2 = plt.subplots(figsize=(10, 6))
            sns.boxplot(x="Topic", y="Performance Score", data=df, palette="coolwarm", ax=ax2)
            ax2.set_title("Performance Score Distribution by Topic")
            ax2.set_xlabel("Topic")
            ax2.set_ylabel("Performance Score")
            st.pyplot(fig2)

        # Tab 2: Recommendations
        with tab2:
            st.subheader("Recommendations")
            optimal_durations = df.groupby("Topic")["Practice Duration (Minutes)"].median()
            st.write("### Recommended Practice Durations by Topic")
            st.bar_chart(optimal_durations)
            st.write("""
            The chart above shows the median practice duration for each topic.  
            Focus on achieving these durations for optimal performance.
            """)

        # Tab 3: Summary
        with tab3:
            st.subheader("Summary")
            st.markdown("""
            - Analyze the practice durations and their impact on performance.
            - Use the recommendations tab to focus efforts on specific topics.
            - Optimize practice schedules for maximum effectiveness.
            """)
    else:
        st.error(f"Dataset must include the following columns: {', '.join(required_columns)}")
else:
    st.info("Awaiting CSV file upload. Please upload a file to proceed.")

# Footer
st.sidebar.markdown("**Developed by Pankaj Devikar**")
