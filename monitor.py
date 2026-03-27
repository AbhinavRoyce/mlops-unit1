import logging
import random

# Configure logging
logging.basicConfig(
    filename='model.log',
    level=logging.INFO,
    format='%(asctime)s - %(levelname)s - %(message)s'
)

# Dummy accuracy
accuracy = round(random.uniform(0.8, 1.0), 2)

print(f"Accuracy: {accuracy}")

# Log it
logging.info(f"Model accuracy: {accuracy}")

print("Log file created successfully")