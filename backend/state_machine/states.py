from enum import Enum

class ConversationState(Enum):
    START = "start"
    BROWSING = "browsing"
    VIEWING_PRODUCT= "viewing_product"
    CART = "cart"
    CHECKOUT = "checkout"

