## Car-And-Pedestrian-prediction
It is detecting cars and pedestrians simultaneously in real-time. It uses only Computer vision.

****How OpenCV trains the car & pedestrian detector?****

It trains the data by Supervised Learning. Like, which are cars and which are not is already given by us.

****How this code works:-****

1st we are taking a pre-trained dataset of cars and pedestrians, which has a ton of car images and pedestrian images to the algorithms.

Then we are making each frame (if it’s a video)/ the image in B&W (Grey Scale)

After that, we will use the algorithm to detect the cars and pedestrians’ coordinates.

And lastly, we are drawing rectangles on the basis of the coordinates.

****So, what is Haar Cascade?****

It is an Object Detection Algorithm used to identify objects in an image or a real-time video. It was proposed by Paul Viola and Michael Jones in their paper, “Rapid Object Detection using a Boosted Cascade of Simple Features” in 2001.

The algorithm uses different types of features/detections... like edge detection, line detection, etc.
