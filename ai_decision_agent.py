agent_memory = []

def ai_decision_agent():
    print("🤖 AI-Based Decision Support System")
    print("Type 'exit' to quit\n")

    while True:
        user_input = input("🧑 Enter your business issue: ").lower()

        if user_input == "exit":
            print("\n📌 Agent Memory Summary:")
            for i, memory in enumerate(agent_memory, 1):
                print(f"{i}. Problem: {memory['problem']} | Decision: {memory['decision']}")
            
            print("\nExiting Business Decision Support AI Agent. Goodbye!")
            break

        # Decision Logic
        if "low sales" in user_input:
            decision = "Sales performance issue detected"
            recommendation = (
                "- Improve marketing strategy\n"
                "- Offer discounts or promotions\n"
                "- Analyze customer preferences"
            )

        elif "high cost" in user_input:
            decision = "Cost optimization required"
            recommendation = (
                "- Reduce unnecessary expenses\n"
                "- Optimize supply chain\n"
                "- Automate manual operations"
            )

        elif "customer" in user_input:
            decision = "Customer satisfaction issue detected"
            recommendation = (
                "- Improve customer service\n"
                "- Collect customer feedback\n"
                "- Introduce loyalty programs"
            )

        elif "profit" in user_input:
            decision = "Profitability analysis required"
            recommendation = (
                "- Increase operational efficiency\n"
                "- Review pricing strategy\n"
                "- Expand high-margin products"
            )

        else:
            decision = "General business analysis required"
            recommendation = (
                "- Collect more business data\n"
                "- Review KPIs\n"
                "- Consult domain experts"
            )

        print("\n🧠 AI Agent Analysis:")
        print(decision)

        print("\n⚙️ Recommended Actions:")
        print(recommendation)

        agent_memory.append({
            "problem": user_input,
            "decision": decision
        })

        print("\n✅ Decision stored in agent memory")
        print("-" * 50)


# Run Agent
ai_decision_agent()
