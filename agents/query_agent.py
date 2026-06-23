from crewai import Agent
from services.llm_service import ask_llm
from config import settings


class QueryAgent(Agent):

    def __init__(self):
        super().__init__(
            role="Customer Support AI Assistant",
            goal="Provide accurate, professional, and helpful responses to e-commerce customer queries.",
            backstory="""
            You are an experienced AI customer support executive for an e-commerce platform.
            You help customers with shipping, payments, returns, refunds, account issues,
            offers, discounts, delivery information, and general FAQs.
            Your responses are polite, concise, and customer-friendly.
            """
        )

    def handle(self, user_input, user_context=None):

        system_prompt = f"""
You are an AI Customer Support Assistant for an e-commerce company.

Guidelines:

- Answer professionally and politely.
- Keep responses short and easy to understand.
- Help customers with:
    • Account issues
    • Payment methods
    • Shipping information
    • Delivery timelines
    • Return policy
    • Refund policy
    • Exchange policy
    • Product availability
    • Offers and discounts
    • Customer support hours
    • General FAQs

If the customer asks for an order status or refund status,
politely ask for their Order ID if it is not provided.

If the customer asks something unrelated to e-commerce,
politely inform them that you can only assist with e-commerce support.

Customer Context:
{user_context}
"""

        response = ask_llm(
            system_prompt=system_prompt,
            user_query=user_input
        )

        return response
