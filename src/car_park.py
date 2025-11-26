class CarPark:
    def __init__(self, id, message, is_on):
        self.id = id
        self.message = message
        self.is_on = is_on or []

    def __str__(self):
        return f"Welcome to {self.location} car park"
