import torch
import torchvision
from torch.autograd import Variable

input_name = ['input']
output_name = ['output']
input = Variable(torch.randn(1, 3, 224, 224)).cuda()
model = torchvision.models.resnet50(pretrained=True).cuda()
dynamic_onnx = True
if dynamic_onnx:
    dynamic_axes = {
        'input': {0: "batch_size"},
        'output': {0: "batch_size"}
    }
    torch.onnx.export(model, input, 'resnet50_dynamic.onnx', input_names=input_name, output_names=output_name, dynamic_axes=dynamic_axes, verbose=True)
else:
    torch.onnx.export(model, input, 'resnet50.onnx', input_names=input_name, output_names=output_name, verbose=True)