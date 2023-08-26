# Road_Sign_bbox_Detection
Predict bounding box around a Road sign in a given image and also predict the type of road sign.



- **Dataset:** [https://www.kaggle.com/andrewmvd/road-sign-detection](https://jovian.com/outlink?url=https%3A%2F%2Fwww.kaggle.com%2Fandrewmvd%2Froad-sign-detection)
  	- contains **877** images of **4 distinct classes** for the objective of **road sign detection**.
  	- Bounding box annotations are provided in the PASCAL VOC format
  	- Classes:  1) Trafic Light; 2) Stop; 3) Speedlimit;  4) Crosswalk.


- **To train the model:** \
	-> run `python train.py` \
	or \
	-> comand line: `yolo task=detect mode=train model=yolov8n.pt imgsz={640} data={Name_of_yaml.yaml} epochs={EPOCHS} batch={BATCH_SIZE} name={Name_of_result_folder}`

- **To evaluate the model:** \
	-> comand line: `yolo task=detect mode=val model=runs/detect/{Name_of_result_folder}/weights/best.pt name=yolov8n_eval data={Name_of_yaml.yaml}`

- **Inference on validation set:**
	-> `yolo task=detect mode=predict model=runs/detect/{Name_of_result_folder}/weights/best.pt source={Img_folder_path} imgsz=1280 name={Name_of_result_folder} hide_labels=True`
