# Road_Sign_bbox_Detection
Predict bounding box around a Road sign in a given image and also predict the type of road sign based on pretrained yolov8n.



- **Dataset:** [https://www.kaggle.com/andrewmvd/road-sign-detection](https://jovian.com/outlink?url=https%3A%2F%2Fwww.kaggle.com%2Fandrewmvd%2Froad-sign-detection)
  	- contains **877** images of **4 distinct classes** for the objective of **road sign detection**.
  	- Bounding box annotations are provided in the PASCAL VOC format
  	- Classes:  1) Trafic Light; 2) Stop; 3) Speedlimit;  4) Crosswalk.


- **To train the model:** \
	-> run `python train.py` \
	or \
	-> comand line: `yolo task=detect mode=train model=yolov8n.pt imgsz={640} data={Name_of_yaml.yaml} epochs={EPOCHS} batch={BATCH_SIZE} name={Name_of_result_folder}`

	-> the model is trained based on the pretrained weights: `yolov8n.pt`

	-> my training results is stored in: *'runs/detect/road_sign_yolov8_100e'*

	-> the best weight during the training is stored in: *'runs/detect/road_sign_yolov8_100e/weights/best.pt'*

- **To evaluate the model:** \
	-> comand line: `yolo task=detect mode=val model=runs/detect/{Name_of_result_folder}/weights/best.pt name=yolov8n_eval data={Name_of_yaml.yaml}`

	-> my evaluate results: *'runs/detect/yolov8n_eval'*

- **Inference on validation set:**
	-> `yolo task=detect mode=predict model=runs/detect/{Name_of_result_folder}/weights/best.pt source={Img_folder_path} imgsz=1280 name={Name_of_result_folder} hide_labels=True`

	-> my results of inference (predictions on every test images): *'runs/detect/yolov8_100e_infer'*


#### About files:
- `Road_Sign.ipynb`: -> Prepare the data for the yolov8n model to train
	- original data: 
		- images: "Data/images" -> .png files
		- labels: "Data/annotations" -> .xml files
	- split into training and testing datasets:
		- training: "Data/train" -> 80%
		- testing: "Data/test" -> 20%
		- the information of the bounding box is extracted from the .xml file and stored into .txt file, and is converted into yolo training format((x1,x2,y1,y2) -> (x,y,w,h))
	- also apply data augmentations on every images


- `road_sign_tolov8.yaml`:
	- Define the **path** of the training and testing dataset
	- set the **number of class**
	- set the **name** of each classes

- `predict.ipynb`:
	- random visualize some predictions made by my best training weights
	- make predictions on custom images and visualize them
		- the results of the predictions are stored in: *'runs/detect/predict'*


#### Citations
@software{yolov8_ultralytics,  author = {Glenn Jocher and Ayush Chaurasia and Jing Qiu},  title = {Ultralytics YOLOv8},  version = {8.0.0},  year = {2023},  url = {https://github.com/ultralytics/ultralytics},  orcid = {0000-0001-5950-6979, 0000-0002-7603-6750, 0000-0003-3783-7069},  license = {AGPL-3.0} }
