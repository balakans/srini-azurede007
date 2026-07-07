"""
Handles appending query logs safely to a CSV file.
"""

import pandas as pd
import os
from datetime import datetime

LOG_FILE = "qa_log.csv"

def log_question(question):
    """Appends the user's question and timestamp to a local CSV log."""
    log_data = pd.DataFrame([{
        "question": question,
        "timestamp": datetime.now().strftime("%Y-%m-%d %H:%M:%S")
    }])

    # Write to CSV in append mode. Write header only if file doesn't exist.
    log_data.to_csv(
        LOG_FILE,
        mode='a',
        header=not os.path.exists(LOG_FILE),
        index=False
    )