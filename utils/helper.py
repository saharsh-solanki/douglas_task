import os
from datetime import datetime
import pandas as pd


def save_to_excel(promo, brand, product_type, for_whom, gift, product_count):
    # Save result to an Excel file
    data_folder = "test_data/output_data"
    os.makedirs(data_folder, exist_ok=True)

    filename = f"{data_folder}/{promo}_{datetime.now().strftime('%Y-%m-%d_%H-%M-%S')}.xlsx"
    df = pd.DataFrame([
        {"Brand": brand, "Product Type": product_type, "For Whom": for_whom, "Gift": gift, "Count": product_count}
    ])
    df.to_excel(filename, index=False)
    print(f"Results saved to {filename}")

