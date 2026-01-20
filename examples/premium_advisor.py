"""
Premium Advisor Agent
---------------------
This example demonstrates the "Gatekeeper" capability of Bindu.
This agent is configured with an strict execution cost. The Bindu middleware
will intercept all requests and return a 402 Payment Required response 
unless a valid payment proof is provided.

It demonstrates:
1. Configuring `execution_cost` in bindufy
2. The X402 payment flow (Payment Required -> Invoice -> Service)
3. Using the `pay_to_address` for settlement
"""

from bindu.penguin.bindufy import bindufy
import logging

# Logic that runs ONLY after payment is verified
def handler(messages: list[dict[str, str]]) -> list[dict[str, str]]:
    """
    This handler provides premium market insights.
    It is protected by the X402 paywall.
    """
    user_input = messages[-1].get("content", "")
    
    # Premium response logic
    advice = (
        "🔮 **Premium Market Insight** 🔮\n\n"
        "Based on our proprietary deep-chain analysis:\n"
        "- **Accumulate**: Assets with high developer activity.\n"
        "- **Avoid**: Projects with anonymous founders and no audit.\n"
        "- **Strategy**: Dollar-Cost Average (DCA) is your best friend in this volatility."
    )
    
    return [{"role": "assistant", "content": advice}]

# Agent Configuration
config = {
    "author": "premium.advisor@example.com",
    "name": "Oracle_of_Value",
    "description": "I provide high-value market insights. Payment required upfront.",
    
    # The 'execution_cost' block enables the X402 Middleware
    "execution_cost": {
        "amount": "0.01",           # The cost of one interaction
        "token": "USDC",            # The currency
        "network": "base-sepolia",    # The network (Base Testnet)
        "pay_to_address": "0x742d35Cc6634C0532925a3b844Bc454e4438f44e" # Dummy ETH Address
    },
    
    # Standard deployment config
    "deployment": {
        "url": "http://localhost:3773", 
        "expose": True
    },
    
    # Use memory storage for this example
    "storage": {"type": "memory"},
    "scheduler": {"type": "memory"},
    
    # Optional: Enable debug logging to see the middleware in action
    "debug_mode": True
}

if __name__ == "__main__":
    # Start the agent server
    print("🔒 Starting Premium Advisor Agent...")
    print(f"💰 Cost: {config['execution_cost']['amount']} {config['execution_cost']['token']}")
    print("🚀 URL: http://localhost:3773")
    bindufy(config, handler)
