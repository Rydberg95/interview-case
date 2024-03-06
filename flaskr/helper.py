import random
from uuid import uuid4


def generate_claim_id() -> str:
    # Generates a random claim id based on the uuid module
    return str(uuid4())


def generate_random_claim_cost() -> float:
    # Generates a random claim cost, in the range of 0 to 100 000
    return random.random() * 1e5
