import streamlit as st
from datetime import datetime
import pandas as pd
import os

#MEMORY
agent_memory = []

CSV_FILE = "decision_log.csv"

#DECISION ENGINE
def decision_engine(user_input):
    user_input = user_input.lower()

    if "low sales" in user_input:
        return {
            "category": "Sales",
            "decision": "Sales performance issue detected",
            "confidence": 85,
            "recommendations": [
                "Improve marketing strategy",
                "Offer discounts or promotions",
                "Analyze customer preferences"
            ]
        }

    elif "high cost" in user_input:
        return {
            "category": "Cost Management",
            "decision": "Cost optimization required",
            "confidence": 80,
            "recommendations": [
                "Reduce unnecessary expenses",
                "Optimize supply chain",
                "Automate manual operations"
            ]
        }

    elif "customer" in user_input:
        return {
            "category": "Customer Experience",
            "decision": "Customer satisfaction issue detected",
            "confidence": 90,
            "recommendations": [
                "Improve customer service",
                "Collect customer feedback",
                "Introduce loyalty programs"
            ]
        }

    elif "profit" in user_input:
        return {
            "category": "Profitability",
            "decision": "Profitability analysis required",
            "confidence": 75,
            "recommendations": [
                "Increase operational efficiency",
                "Review pricing strategy",
                "Expand high-margin products"
            ]
        }

    else:
        return {
            "category": "General Business",
            "decision": "General business analysis required",
            "confidence": 65,
            "recommendations": [
                "Collect more business data",
                "Review KPIs",
                "Consult domain experts"
            ]
        }

#STREAMLIT UI
st.set_page_config(page_title="AI Decision Support System", layout="centered")

st.title("🤖 AI-Based Decision Support System")
st.write("An Agentic AI system that analyzes business problems and provides intelligent recommendations")

user_problem = st.text_area("🧑 Enter your business problem")

if st.button("Get Recommendation"):
    if user_problem.strip():
        result = decision_engine(user_problem)

        timestamp = datetime.now().strftime("%d-%m-%Y %H:%M:%S")

        #display_output
        st.subheader("🧠 AI Agent Analysis")
        st.success(result["decision"])

        st.write(f"**📂 Category:** {result['category']}")
        st.write(f"**📊 Confidence Score:** {result['confidence']}%")
        st.write(f"**🕒 Timestamp:** {timestamp}")

        st.subheader("⚙️ Recommended Actions")
        for rec in result["recommendations"]:
            st.write("•", rec)

        #store in memory
        record = {
            "Timestamp": timestamp,
            "Problem": user_problem,
            "Category": result["category"],
            "Decision": result["decision"],
            "Confidence": result["confidence"]
        }

        agent_memory.append(record)

        #save to CSV
        df = pd.DataFrame(agent_memory)
        df.to_csv(CSV_FILE, index=False)

        st.info("✅ Decision stored in agent memory and saved to CSV")

    else:
        st.warning("Please enter a business problem")

#MEMORY VIEW
if st.checkbox("📌 Show Agent Memory"):
    if agent_memory:
        st.subheader("Agent Decision History")
        st.dataframe(pd.DataFrame(agent_memory))
    else:
        st.write("No decisions recorded yet.")

#CSV DOWNLOAD
if os.path.exists(CSV_FILE):
    with open(CSV_FILE, "rb") as file:
        st.download_button(
            label="⬇ Download Decision Log (CSV)",
            data=file,
            file_name="decision_log.csv",
            mime="text/csv"
        )
