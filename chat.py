from agents.query_agent import QueryAgent
from agents.order_agent import OrderAgent
from agents.recommendation_agent import RecommendationAgent

query_agent = QueryAgent()
order_agent = OrderAgent()
recommendation_agent = RecommendationAgent()

print("=" * 60)
print("🤖 AI Customer Support Chatbot")
print("Type 'exit' to quit")
print("=" * 60)

while True:

    user_input = input("\nYou: ")

    if user_input.lower() == "exit":
        break

    if any(word in user_input.lower() for word in [
        "order",
        "track",
        "delivery",
        "refund",
        "return",
        "cancel"
    ]):

        response = order_agent.handle(user_input, {})

    elif any(word in user_input.lower() for word in [
        "recommend",
        "phone",
        "laptop",
        "headphone",
        "buy"
    ]):

        response = recommendation_agent.handle(user_input, {})

    else:

        response = query_agent.handle(user_input, {})

    print("\nAgent:", response)
