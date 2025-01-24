"""
This file contains functions to convert labelme json files to
COCO format dataset.
Modified from
https://github.com/wkentaro/labelme/blob/master
/examples/instance_segmentation/labelme2coco.py
"""
import collections
import datetime
import glob
import json
import logging
import os
import os.path as osp
import sys
import uuid
import imgviz
import numpy as np
from pathlib import Path
import labelme
from annolid.gui.label_file import LabelFile

logger = logging.getLogger(__name__)

try:
    import pycocotools.mask
except ImportError:
    logger.warning(
        "Please install pycocotools:\n\n    pip install pycocotools\n")
    sys.exit(1)


def _create_dirs(dir_path):
    if not os.path.exists(dir_path):
        os.makedirs(dir_path)


def convert(input_annotated_dir,
            output_annotated_dir,
            labels_file='labels.txt',
            vis=False,
            save_mask=True,
            train_valid_split=0.7,
            radius_ratio=0.2
            ):

    assert os.path.isfile(
        labels_file), "Please provide the correct label file."

    assert os.path.exists(input_annotated_dir), "Please check the input dir."

    class_instance_counter = {}
    train_class_instance_counter = {}

    if not osp.exists(output_annotated_dir):
        os.makedirs(output_annotated_dir)
        os.makedirs(osp.join(output_annotated_dir,
                             'train',
                             "JPEGImages"))
        os.makedirs(osp.join(output_annotated_dir,
                             'valid',
                             "JPEGImages"))
    if vis:
        train_vis_dir = osp.join(output_annotated_dir,
                                 'train', 'Visualization')
        _create_dirs(train_vis_dir)
        valid_vis_dir = osp.join(output_annotated_dir,
                                 'valid', 'Visualization')
        _create_dirs(valid_vis_dir)

    if save_mask and vis:
        train_mask_dir = osp.join(output_annotated_dir, 'train', 'Masks')
        _create_dirs(train_mask_dir)
        valid_mask_dir = osp.join(output_annotated_dir, 'valid', 'Masks')
        _create_dirs(valid_mask_dir)

    logger.info(f"Creating dataset:  {output_annotated_dir}")
    training_examples_sofar = 0

    now = datetime.datetime.now()

    train_data = dict(
        info=dict(
            description=None,
            url=None,
            version=None,
            year=now.year,
            contributor=None,
            date_created=now.strftime("%Y-%m-%d %H:%M:%S.%f"),
        ),
        licenses=[dict(url=None, id=0, name=None,)],
        images=[
            # license, url, file_name, height, width, date_captured, id
        ],
        type="instances",
        annotations=[
            # segmentation, area, iscrowd, image_id, bbox, category_id, id
        ],
        categories=[
            # supercategory, id, name
        ],
    )
    valid_data = dict(
        info=dict(
            description=None,
            url=None,
            version=None,
            year=now.year,
            contributor=None,
            date_created=now.strftime("%Y-%m-%d %H:%M:%S.%f"),
        ),
        licenses=[dict(url=None, id=0, name=None,)],
        images=[
            # license, url, file_name, height, width, date_captured, id
        ],
        type="instances",
        annotations=[
            # segmentation, area, iscrowd, image_id, bbox, category_id, id
        ],
        categories=[
            # supercategory, id, name
        ],
    )

    class_name_to_id = {}
    with open(labels_file, 'r') as lf:
        for i, line in enumerate(lf.readlines()):
            class_id = i - 1  # starts with -1
            class_name = line.strip()
            if class_id == -1:
                assert class_name == "__ignore__"
                continue

            if class_name != '_background_':
                class_instance_counter[class_name] = 0
                train_class_instance_counter[class_name] = 0
            class_name_to_id[class_name] = class_id
            train_data["categories"].append(
                dict(supercategory=None, id=class_id, name=class_name,)
            )
            valid_data["categories"].append(
                dict(supercategory=None, id=class_id, name=class_name,)
            )

    train_out_ann_file = osp.join(output_annotated_dir, 'train',
                                  "annotations.json")
    valid_out_ann_file = osp.join(output_annotated_dir, 'valid',
                                  "annotations.json")
    label_files = glob.glob(osp.join(input_annotated_dir, "*.json"))
    # By default, only manually labeled frames have png files saved.
    label_files = [_lf for _lf in label_files if osp.exists(
        _lf.replace('.json', '.png'))]
    num_label_files = len(label_files)

    # Calculate training_percentage based on the train_valid_split parameter
    if train_valid_split > 1:
        if train_valid_split <= num_label_files:
            training_percentage = train_valid_split / num_label_files
        else:
            # If the provided train_valid_split is greater than the number of label files,
            # we assume a default split of 70% for training.
            training_percentage = 0.7
    else:
        # If train_valid_split is a fraction (<=1), it directly represents the training percentage.
        training_percentage = train_valid_split

    _angles = [0, 15, 30, 45, 60, 75, 90, 105, 120, 135, 150, 165,
               180, 195, 210, 225, 240, 255, 270, 285, 300, 315, 330, 345, 360]

    for image_id, filename in enumerate(label_files):
        progress = (image_id + 1) / num_label_files * 100
        yield int(progress), filename

        label_file = LabelFile(filename=filename)

        base = osp.splitext(osp.basename(filename))[0]
        train_out_img_file = osp.join(output_annotated_dir, 'train',
                                      "JPEGImages", base + ".jpg")
        valid_out_img_file = osp.join(output_annotated_dir, 'valid',
                                      "JPEGImages", base + ".jpg")

        if label_file.imageData is None or len(label_file.imageData) < 2:
            continue
        img = labelme.utils.img_data_to_arr(label_file.imageData)

        is_train = 0
        # for area
        masks = {}
        # for segmentation
        segmentations = collections.defaultdict(list)
        for shape in label_file.shapes:
            points = shape["points"]
            label = shape["label"]
            group_id = shape.get("group_id")

            if group_id is None:
                group_id = uuid.uuid1()

            instance = (label, group_id)

            shape_type = shape.get("shape_type", "polygon")

            if train_valid_split > 1:
                if training_examples_sofar < train_valid_split:
                    train_class_instance_counter[label] = train_class_instance_counter.get(
                        label, 0)
                    if train_class_instance_counter[label] == 0:
                        is_train = 1
                    elif train_class_instance_counter[label] <= (
                            train_valid_split / len(train_class_instance_counter)) + 1:
                        is_train = 1
                    # make sure very instances in the class is covered
                    # before random sampling
                    elif 0 not in train_class_instance_counter.values():
                        is_train = 1
                    else:
                        is_train = np.random.choice(
                            [0, 1], p=[1-training_percentage, training_percentage]
                        )

            elif train_valid_split < 1:
                is_train = np.random.choice(
                    [0, 1], p=[1-train_valid_split, train_valid_split])
            elif train_valid_split == 1:
                is_train = 1

            try:
                class_instance_counter[label] += 1
            except KeyError:
                class_instance_counter[label] = 1

            if is_train == 1:
                try:
                    train_class_instance_counter[label] += 1
                except KeyError:
                    train_class_instance_counter[label] = 1

            if shape_type == 'point':
                try:
                    min_dim = min(img.shape)
                    cx, cy = points[0]
                    radius = min_dim * radius_ratio + \
                        np.random.choice(np.arange(0, 1, 0.1))
                    xs = cx + (radius * np.cos(np.array(_angles) * np.pi/180))
                    ys = cy + (radius * np.sin(np.array(_angles) * np.pi/180))
                    points = np.asarray([list(p) for p in zip(xs, ys)])
                    shape_type = "polygon"
                except IndexError:
                    logger.warning(f"{filename} has a invalid point {points}.")
                    continue

            try:
                mask = labelme.utils.shape_to_mask(
                    img.shape[:2], points, shape_type
                )
            except:
                logger.warning("Polygon must have points more than 2")
                continue

            if instance in masks:
                masks[instance] = masks[instance] | mask
            else:
                masks[instance] = mask

            if shape_type == "rectangle":
                (x1, y1), (x2, y2) = points
                x1, x2 = sorted([x1, x2])
                y1, y2 = sorted([y1, y2])
                points = np.asarray([x1, y1, x2, y1, x2, y2, x1, y2])
                segmentations[instance].append(points.flatten().tolist())
            elif shape_type == "circle":
                (x1, y1), (x2, y2) = points
                radius = int(((x1-x2)**2 + (y1-y2)**2)**(1/2))
                xs = x1 + (radius * np.cos(np.array(_angles) * np.pi/180))
                ys = y1 + (radius * np.sin(np.array(_angles) * np.pi/180))
                points = np.asarray([list(p) for p in zip(xs, ys)])
                points = np.asarray(points).flatten().tolist()
                shape_type = "polygon"
                segmentations[instance].append(points)
            else:
                points = np.asarray(points).flatten().tolist()
                segmentations[instance].append(points)
        segmentations = dict(segmentations)

        for instance, mask in masks.items():
            cls_name, group_id = instance
            if cls_name not in class_name_to_id:
                continue
            cls_id = class_name_to_id[cls_name]

            mask = np.asfortranarray(mask.astype(np.uint8))
            mask = pycocotools.mask.encode(mask)
            area = float(pycocotools.mask.area(mask))
            bbox = pycocotools.mask.toBbox(mask).flatten().tolist()

            if is_train:
                train_data["annotations"].append(
                    dict(
                        id=len(train_data["annotations"]),
                        image_id=image_id,
                        category_id=cls_id,
                        segmentation=segmentations[instance],
                        area=area,
                        bbox=bbox,
                        iscrowd=0,
                    )
                )
            else:
                valid_data["annotations"].append(
                    dict(
                        id=len(valid_data["annotations"]),
                        image_id=image_id,
                        category_id=cls_id,
                        segmentation=segmentations[instance],
                        area=area,
                        bbox=bbox,
                        iscrowd=0,
                    )
                )

        if is_train == 1:
            training_examples_sofar += 1
            imgviz.io.imsave(train_out_img_file, img)
        else:
            imgviz.io.imsave(valid_out_img_file, img)

        if is_train == 1:
            train_data["images"].append(
                dict(
                    license=0,
                    url=None,
                    # handle windows backward slash issue
                    file_name=osp.relpath(train_out_img_file,
                                          osp.dirname(train_out_ann_file)
                                          ).replace("\\", '/'),
                    height=img.shape[0],
                    width=img.shape[1],
                    date_captured=None,
                    id=image_id,))
        else:
            valid_data["images"].append(
                dict(
                    license=0,
                    url=None,
                    file_name=osp.relpath(valid_out_img_file,
                                          osp.dirname(valid_out_ann_file)
                                          ).replace("\\", '/'),
                    height=img.shape[0],
                    width=img.shape[1],
                    date_captured=None,
                    id=image_id,))

        if save_mask and vis:
            lbl, _ = labelme.utils.shapes_to_label(
                img.shape, label_file.shapes, class_name_to_id)
            if is_train == 1:
                out_mask_file = osp.join(
                    train_mask_dir, base + '_mask.png')
            else:
                out_mask_file = osp.join(
                    valid_mask_dir, base + '_mask.png')
            labelme.utils.lblsave(out_mask_file, lbl)

        if vis:
            labels, captions, masks = zip(
                *[
                    (class_name_to_id[cnm], cnm, msk)
                    for (cnm, gid), msk in masks.items()
                    if cnm in class_name_to_id
                ]
            )
            viz = imgviz.instances2rgb(
                image=img,
                labels=labels,
                masks=masks,
                captions=captions,
                font_size=15,
                line_width=2,
            )
            if is_train:
                out_viz_file = osp.join(
                    output_annotated_dir, "train", "Visualization", base + ".jpg"
                )
            else:
                out_viz_file = osp.join(
                    output_annotated_dir, "valid", "Visualization", base + ".jpg"
                )
            imgviz.io.imsave(out_viz_file, viz)

    with open(train_out_ann_file, "w") as f:
        json.dump(train_data, f)
    with open(valid_out_ann_file, "w") as f:
        json.dump(valid_data, f)

    # create a data.yaml config file
    categories = []
    for c in train_data["categories"]:
        # exclude backgroud with id 0
        if not c['id'] == 0:
            categories.append(c['name'])

    data_yaml = Path(f"{output_annotated_dir}/data.yaml")
    names = list(categories)
    input_annotated_dir_name = os.path.basename(input_annotated_dir)
    output_annotated_dir_name = Path(os.path.basename(output_annotated_dir))
    # dataset folder is in same dir as the yolov5 folder
    with open(data_yaml, 'w') as dy:
        dy.write(f"DATASET:\n")
        dy.write(f"    name: '{input_annotated_dir_name}'\n")
        dy.write(
            f"""    train_info: '{output_annotated_dir_name /"train"/"annotations.json"}'\n""")
        dy.write(
            f"""    train_images: '{output_annotated_dir_name /"train"}'\n""")
        dy.write(
            f"""    valid_info: '{output_annotated_dir_name /"valid"/"annotations.json"}'\n""")
        dy.write(
            f"""    valid_images: '{output_annotated_dir_name /"valid"}'\n""")
        dy.write(f"    class_names: {names}\n")

        dy.write(f"YOLACT:\n")
        dy.write(f"    name: '{input_annotated_dir_name}'\n")
        dy.write(f"    dataset: 'dataset_{input_annotated_dir_name}_coco'\n")
        dy.write(f"    max_size: 512\n")
    logger.info('Done.')
    logger.info(f"All: {class_instance_counter}")
    logger.info(f"Training set:  {train_class_instance_counter}")
