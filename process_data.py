import os 
from tools import *

path_to_receipts = "./receipts"



for receipt_name in os.listdir(path_to_receipts):
	receipt_path = os.path.join(path_to_receipts, receipt_name)
	receipt_info = extract_infos_from_receipt(image_path=receipt_path)
	print(receipt_info)

# 	list_of_paths.append(receipt_path)

# print(list_of_paths)

