import os
import numpy as np
import onnxruntime 

ort_session = onnxruntime.InferenceSession(
    # os.path.abspath(os.path.join(__file__, "..", "lib", "alexnet.onnx")), 
    "alexnet.onnx",
    # providers=['TensorrtExecutionProvider', 'CUDAExecutionProvider', 'CPUExecutionProvider']
    providers=['CPUExecutionProvider']
)
outputs = ort_session.run(
    None, 
    {'actual_input_1': np.random.randn(10, 3, 224, 224).astype(np.float32)}
)
print(outputs[0])