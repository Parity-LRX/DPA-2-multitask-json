import torch
model_state= torch.load('DPA2_medium_28_10M_beta4.pt')
model_param = model_state['model']['_extra_state']['model_params']['shared_dict']
print(model_param)