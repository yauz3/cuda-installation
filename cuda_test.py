from tensorflow.python.client import device_lib
import tensorflow as tf
import os
os.environ['TF_CPP_MIN_LOG_LEVEL'] = '2'
print(tf.config.list_physical_devices('GPU'))


print("Num GPUs Available: ", len(tf.config.list_physical_devices('GPU')))


import tensorflow as tf
print(tf.__version__)
#import coremltools as ct
import os
print(tf.test.gpu_device_name())

os.environ['TF_CPP_MIN_LOG_LEVEL'] = '2'
gpu_devices = tf.config.experimental.list_physical_devices('GPU')
for device in gpu_devices:
    a=tf.config.experimental.set_memory_growth(device, True)
    print(a)
print("Num GPUs Available: ", len(tf.config.list_physical_devices('GPU')))
from tensorflow.python.client import device_lib
print(device_lib.list_local_devices())
import tensorflow as tf
if tf.test.gpu_device_name():
    print('Default GPU Device: {}'.format(tf.test.gpu_device_name()))
else:
    print("Please install GPU version of TF")
import tensorflow as tf
print(tf.config.list_physical_devices('GPU') )
assert tf.test.is_gpu_available()
assert tf.test.is_built_with_cuda()


import tensorflow as tf
if tf.test.gpu_device_name():
    print('Default GPU Device:{}'.format(tf.test.gpu_device_name()))
else:
   print("Please install GPU version of TF")


print("Num GPUs Available: ", len(tf.config.list_physical_devices('GPU')))
import tensorflow as tf

assert tf.test.is_gpu_available()
assert tf.test.is_built_with_cuda()
print("burası")