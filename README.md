# OnnxInferenceLearn

<br>&ensp;&ensp;&ensp;&ensp;Moving into the Open-Source era, models are required on various devices. While doing this, the performance of single-machine is critical to improve models' performance and users' experience. <b>_Onnx_</b>(including <b>_Onnx Runtime_</b>) is one of the most famous _Inference Structures_ that both accelate the run time and reduce the memory consumption. </br>
&ensp;&ensp;&ensp;&ensp;However, <b>_onnxruntime-gpu_</b> hasn't supported the CUDA-11.7, available versions are shown as follow.</br>

|ONNX Runtime|CUDA|cuDNN|Notes|
|:---:|:---:|:---:|:---|
|1.13|11.6|8.2.4 (Linux) 8.5.0.96 (Windows)|libcudart 11.4.43 libcufft 10.5.2.100 libcurand 10.2.5.120 libcublasLt 11.6.5.2 libcublas 11.6.5.2 libcudnn 8.2.4|
|1.12 1.11|11.4|8.2.4 (Linux) 8.2.2.26 (Windows)|libcudart 11.4.43 libcufft 10.5.2.100 libcurand 10.2.5.120 libcublasLt 11.6.5.2 libcublas 11.6.5.2 libcudnn 8.2.4|
|1.10|11.4|8.2.4 (Linux) 8.2.2.26 (Windows)|libcudart 11.4.43 libcufft 10.5.2.100 libcurand 10.2.5.120 libcublasLt 11.6.1.51 libcublas 11.6.1.51 libcudnn 8.2.4|
|1.9|11.4|8.2.4 (Linux) 8.2.2.26 (Windows)|libcudart 11.4.43 libcufft 10.5.2.100 libcurand 10.2.5.120 libcublasLt 11.6.1.51 libcublas 11.6.1.51 libcudnn 8.2.4|
|1.8|11.0.3|8.0.4 (Linux) 8.0.2.39 (Windows)|libcudart 11.0.221 libcufft 10.2.1.245 libcurand 10.2.1.245 libcublasLt 11.2.0.252 libcublas 11.2.0.252 libcudnn 8.0.4|
|1.7|11.0.3|8.0.4 (Linux) 8.0.2.39 (Windows)|libcudart 11.0.221 libcufft 10.2.1.245 libcurand 10.2.1.245 libcublasLt 11.2.0.252 libcublas 11.2.0.252 libcudnn 8.0.4|
|1.5-1.6|10.2|8.0.3|CUDA 11 can be built from source|
|1.2-1.4|10.1|7.6.5|Requires cublas10-10.2.1.243; cublas 10.1.x will not work|
|1.0-1.1|10.0|7.6.4|CUDA versions from 9.1 up to 10.1, and cuDNN versions from 7.1 up to 7.4 should also work with Visual Studio 2017|

# Reference
[1] [https://blog.csdn.net/qq_33934427/article/details/124114195](https://blog.csdn.net/qq_33934427/article/details/124114195)</br>
[2] [https://pytorch.org/docs/master/onnx.html](https://pytorch.org/docs/master/onnx.html)</br>
[3] [https://onnxruntime.ai/docs/execution-providers/CUDA-ExecutionProvider.html](https://onnxruntime.ai/docs/execution-providers/CUDA-ExecutionProvider.html)</br>