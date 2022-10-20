# cuda-installation

https://stackoverflow.com/questions/66977227/could-not-load-dynamic-library-libcudnn-so-8-when-running-tensorflow-on-ubun <br />

wget https://developer.download.nvidia.com/compute/cuda/repos/ubuntu2004/x86_64/cuda-ubuntu2004.pin <br />
sudo mv cuda-ubuntu2004.pin /etc/apt/preferences.d/cuda-repository-pin-600 <br />
sudo apt-key adv --fetch-keys https://developer.download.nvidia.com/compute/cuda/repos/ubuntu2004/x86_64/${last_public_key}.pub <br />
sudo add-apt-repository "deb https://developer.download.nvidia.com/compute/cuda/repos/ubuntu2004/x86_64/ /" <br />
sudo apt-get update <br />
sudo apt-get install libcudnn8 <br />
sudo apt-get install libcudnn8-dev <br />


And if you want to install a specific version, the last 2 commands would be replaced with <br />

sudo apt-get install libcudnn8=${cudnn_version}-1+${cuda_version} <br />
sudo apt-get install libcudnn8-dev=${cudnn_version}-1+${cuda_version} <br />
