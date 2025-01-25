from pydantic import BaseModel


class Order(BaseModel):
    """
    Order class representing an order in the system.
    Attributes:
        OrderUniqueIdentifier (str): A unique identifier for the order.
        AppOrderID (int): The application-specific order ID.
        OrderStatus (str): The status of the order. Defaults to an empty string.
    Methods:
        __init__(OrderUniqueIdentifier: str, AppOrderID: int, OrderStatus: str = ""):
            Initializes a new instance of the Order class.
    """

    OrderUniqueIdentifier: str
    AppOrderID: int
    OrderStatus: str

    def __init__(
        self, OrderUniqueIdentifier: str, AppOrderID: int, OrderStatus: str = ""
    ):
        super().__init__(
            OrderUniqueIdentifier=OrderUniqueIdentifier,
            AppOrderID=AppOrderID,
            OrderStatus=OrderStatus,
        )
