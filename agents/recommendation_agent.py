from crewai import Agent
from services.llm_service import ask_llm
import json
from pathlib import Path
from config import settings


class RecommendationAgent(Agent):

    def __init__(self):
        super().__init__(
            role="Product Recommendation Specialist",
            goal="Recommend the best products based on customer requirements.",
            backstory="""
            You are an intelligent AI shopping assistant for an e-commerce platform.
            Your responsibility is to recommend products from the available product
            catalog based on the customer's needs.

            Always provide friendly, professional, and helpful responses.
            Never recommend products that are not available in the catalog.
            """
        )

    def handle(self, user_input, user_context=None):

        # Load product data
        data_path = (
            Path(__file__).resolve().parent.parent
            / "data"
            / "sample_data.json"
        )

        with open(data_path, "r") as file:
            products = json.load(file)["products"]

        # Convert product list into text for the LLM
        product_catalog = ""

        for product in products:
            product_catalog += (
                f"Product ID: {product['id']}\n"
                f"Product Name: {product['name']}\n"
                f"Category: {product['category']}\n\n"
            )

        system_prompt = f"""
You are an AI Product Recommendation Assistant for an e-commerce platform.

Available Products:

{product_catalog}

Instructions:

1. Recommend ONLY products from the above catalog.
2. Explain why the recommendation matches the customer's needs.
3. If multiple products match, recommend the best options.
4. If no product matches, politely inform the customer.
5. Never invent products that are not listed.
6. Keep responses professional and concise.

Customer Context:
{user_context}
"""

        response = ask_llm(
            system_prompt=system_prompt,
            user_query=user_input
        )

        return response
