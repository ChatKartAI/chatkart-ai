from states import ConversationState

class StateMachine:
    def transition(self,context, intent):
        state = context.get("state",ConversationState.START)
        if(state == ConversationState.START):
            return ConversationState.BROWSING
        
        if state == ConversationState.BROWSING:
            if intent == "view_product":
                return ConversationState.VIEWING_PRODUCT
            if intent == "checkout":
                return ConversationState.CHECKOUT                
        
        if state == ConversationState.VIEWING_PRODUCT:
            if intent == "add_to_cart":
                return ConversationState.CART
            if intent == "search":
                return ConversationState.BROWSING
        
        if state == ConversationState.CART:
            if intent == "checkout":
                return ConversationState.CHECKOUT
        return state