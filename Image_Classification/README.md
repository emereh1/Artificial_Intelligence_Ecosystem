# AI Image Processing and Classification Project

This project is designed to give you hands-on experience working with an image classifier and enhancing your programming skills using AI assistance. The project has two parts, each focused on different aspects of image classification and processing. By the end, you'll have explored fundamental concepts like Grad-CAM, image classification, and creative image filtering.

Final Report – Image Classification and Filter Project
Name: Emere Hoehne
Project: Image Classification & Creative Filters
GitHub Repo: https://github.com/emereh1/Artificial_Intelligence_Ecosystem/tree/main/Image_Classification
Alternative Location: In ReadMe project file
________________________________________
Part 1: Base Classifier and Grad-CAM Analysis
Classifier Overview:
If you have Python experience, compare its explanation with your own understanding. (Base Classifier)

For this project, I think ChatGPT explained it well as a pre-trained MobileNetV2 model as the base classifier. The program takes an image path from the user, processes the image, and predicts the top-3 labels with confidence scores. The program continues until the user types “exit.” For my chosen image, Reptile.jpg, the predictions were:
•	common_iguana: 0.60
•	green_lizard: 0.14
•	agama: 0.03
The classifier correctly identified the iguana but with moderate confidence This was an image of a common iguana, which it is an image of an iguana with a nice back drop.

AI Summary of Grad Cam
Grad-CAM (Gradient-weighted Class Activation Mapping) is a technique that highlights which parts of an image a CNN focuses on for a specific class prediction. It works by:
1.	Forward pass: Feed the image through the CNN to get class scores.
2.	Gradient computation: Calculate the gradient of the target class score with respect to the last convolutional layer’s feature maps.
3.	Weighting: Average the gradients spatially to get importance weights for each feature map.
4.	Heatmap creation: Combine the weighted feature maps and apply ReLU to highlight positive contributions.
5.	Upsampling: Resize the heatmap to the input image size and overlay it.
The resulting heatmap shows which areas of the image were most important for the model’s prediction, helping with interpretability and trust in CNNs.
Grad-CAM Observations:
I integrated Grad-CAM to visualize which areas of the image the model focused on. Interestingly, the heatmap highlighted more of the background than the iguana itself. This explains the classifier’s 60% confidence in identifying the iguana. The experiment illustrated that background elements and occlusions can significantly influence predictions, emphasizing the importance of interpretability tools like Grad-CAM in understanding CNN behavior.
Reflection on Python and AI Assistance:
Working with Python and AI explanations was helpful. ChatGPT provided clear explanations of how the classifier and Grad-CAM work, which matched my understanding. The AI helped me comprehend the workflow from image preprocessing to prediction and visualization, making the project easier to execute and analyze.
________________________________________
Part 2: Custom Image Filters
(Basic Filter)
Yes, it makes sense summarized as This script takes an image from the user, resizes it, applies a Gaussian blur, and saves the result with a modified filename. It also handles errors and loops until the user types "exit".
My Filter
I created two filters the first I believe went horribly trying to make a cool filter that places a baseball cap, gold chain, and sun glasses on the object in the photo, however there were issues with the background for each accessory as well as the placement. I then made a neon sort of cyberpunk like filter that changed the gradient and saturation which worked a bit better.
Filter Development:
I experimented with two artistic filters:
1.	Accessory Filter: Attempted to add a baseball cap, gold chain, and sunglasses to the object. Placement issues and background integration made this less successful.
2.	Neon/Cyberpunk Filter: Applied gradient and saturation adjustments to create a neon, futuristic effect. This filter worked well, producing a visually striking and cohesive image.
Effect on Images:
The neon filter enhanced colors and visual appeal, giving the image a cyberpunk aesthetic. The accessory filter was conceptually fun but revealed challenges in overlaying objects accurately on images, especially with complex backgrounds.
Reflection on AI Assistance:
AI guidance was valuable in understanding image processing and modifying filters. It suggested methods for resizing, color adjustments, and looping through images, which helped me iterate quickly. The collaboration highlighted how AI can accelerate experimentation and learning, while still requiring human judgment for creative decisions.
________________________________________
Summary:
This project provided hands-on experience with image classification, Grad-CAM interpretability, and creative filtering in Python. I gained insight into how CNNs can be influenced by background features, how heatmaps reveal model focus, and how image processing techniques can be creatively applied. The experience also reinforced the value of AI assistance in explaining code, implementing features, and iterating on artistic