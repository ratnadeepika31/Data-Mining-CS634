### Transfer Learning for Custom Datasets in the Small-Data Regime for Basement

# Milestone 3: Annotation

## **Deep Extreme Cut: From Extreme Points to Object Segmentation**

DEXTR (Deep Extreme Cut) is a deep learning architecture that is designed to perform object segmentation in images. The architecture is based on the idea of "extreme points," which are the points in an image that are farthest away from the background. By identifying these extreme points and using them as the starting points for object segmentation, DEXTR is able to more accurately segment objects in images.

**![](https://lh6.googleusercontent.com/tcig1ZD6GH0imaEwYKfZbeBaTl0O1kdnBaEHtYsc8Qzn5CMGAi_poKhNtQDxk8R4Fu8Sg3x8ABQ28Ao5avU-IEMl7hn2ICrCvlNOhIMmS6ZyNZmRBfKIkeY0tRM87xPXsTrX-71Yr-yjQwvydCj-XK4yoRU-OEeAsS3mU7cCPTs2UmXtRAeBwMVVRZ3eHQ)**

The architecture of DEXTR consists of two main components: a feature extraction network and a decoder network. The feature extraction network is typically a pre-trained deep convolutional neural network (CNN), such as VGG-16 or ResNet-101, that is used to extract high-level features from the input image. The decoder network, on the other hand, is a fully-connected network that takes the output of the feature extraction network and generates a segmentation map for the input image.

  

## Feature Extraction:

  

A 4-channel input for the CNN is created in the DEXTR architecture by concatenating the heatmap with the RGB channels of the input image. A bounding box created from the extreme point annotations is used to crop this input. The bounding box is then relaxed by a few pixels to include context surrounding the object of interest. As a result of this preprocessing step, the input is an RGB crop that includes the object and its extreme points.

  

The ResNet-101 is used to extract the features. The fully connected layer and the last 2 max pooling layer are removed to get the required resolution(atrous convolution). After the ResNet, a pyramid scene based parsing module is designed to collect globally valuable features. The weights of the network are pre-defined using ImageNet to give better results. The output of the feature extraction part is the probability map. It represents the probability of each pixel belonging to an object.

  

  

CNN tries to minimize the given cost function. The given cost function is called the entropy loss function between the label and the prediction $\hat{y}_j$

  
  

$$\mathcal{L}=\sum_{j \in Y} w_{Y_j} C\left(y_j, \hat{y}_j\right), \quad j \in  1, \ldots,|Y|$$

  
  

## Decoder Network:

  

To generate the segmentation map, the decoder network first identifies the extreme points in the input image using a set of predefined rules. These points are then used as the starting points for a graph-based segmentation algorithm, which is used to generate the final segmentation map. This map is then refined using a set of post-processing steps, such as removing small objects and filling in gaps in the segmentation, to produce the final segmentation map for the input image.

  
  

## Interactive Segmentation:

  

Interactive segmentation is a method of segmenting objects in images that involves providing user input to guide the segmentation process. In the context of the Deep Extreme Cut architecture, interactive segmentation may be performed by providing the model with "extreme points" as input, which are the points in an image that are farthest away from the background. These points are used as the starting points for the DEXTR model to segment the objects in the image, allowing the user to guide the segmentation process by selecting the points that are most relevant to the task at hand.

  

  

The interactive segmentation can improve the accuracy and efficiency of object segmentation by allowing the user to provide guidance to the model, and can be a useful tool in situations where the objects of interest are not well-defined or are difficult to segment automatically.

  

## Conclusion

  

To conclude, the DEXTR architecture combines the strengths of both convolutional neural networks and graph-based methods to achieve state-of-the-art performance on a variety of object segmentation tasks. Due to this, there has been widespread adoption in the research community.


# Annotation Link
The dataset is uploaded on drive at this [Basement Data Set](https://drive.google.com/drive/folders/1bQI5NGNnWryRgPsNFFRrRT2tpAoFJZl2?usp=sharing)
