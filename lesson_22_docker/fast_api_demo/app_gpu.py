import torch
import time
print(torch.cuda.is_available())
print(torch.cuda.get_device_name(0))
time.sleep(100)  