import cv2
import random


def create_bounding_box(detected_objects,np_img,output_image_path):
    label_colors = {}

    for obj in detected_objects:
        label = obj['label']
        confidence = obj['confidence']
        x_center, y_center, w, h = obj['coordinates']['x'], obj['coordinates']['y'], obj['coordinates']['width'], obj['coordinates']['height']
        
        x1 = int(x_center - w / 2)
        y1 = int(y_center - h / 2)
        x2 = int(x_center + w / 2)
        y2 = int(y_center + h / 2)
    
        if label not in label_colors:
            label_colors[label] = (random.randint(0, 255), random.randint(0, 255), random.randint(0, 255))
        color = label_colors[label]
        cv2.rectangle(np_img, (x1, y1), (x2, y2), color, 2)
        label_text = f"{label} ({confidence:.2f})"
        text_size = cv2.getTextSize(label_text, cv2.FONT_HERSHEY_SIMPLEX, 0.5, 1)[0]
        text_x, text_y = x1, y1 - 5
        
        cv2.rectangle(np_img, (text_x, text_y - text_size[1] - 2), (text_x + text_size[0], text_y + 2), color, -1)
        cv2.putText(np_img, label_text, (text_x, text_y), cv2.FONT_HERSHEY_SIMPLEX, 0.5, (255, 255, 255), 1)
    cv2.imwrite(output_image_path, np_img)
    return np_img