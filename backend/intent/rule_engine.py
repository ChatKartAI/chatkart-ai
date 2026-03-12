class RuleBasedIntentDetector:
    def detect(self, message):
        message = message.lower()
        if any(word in message for word in ["show", "find", "search"]):
            return "search_products"
        if any(word in message for word in ["red", "blue", "cotton", "under"]):
            return "refine_search"
        if any(word in message for word in ["details", "more", "show product"]):
            return "view_product"
        if "add" in message and "cart" in message:
            return "add_to_cart"
        if any(word in message for word in ["buy", "checkout", "order"]):
            return "checkout"
        if any(word in message for word in ["hi","hello"]):
            return "greeting"
        return "fallback"
