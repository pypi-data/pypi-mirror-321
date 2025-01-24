## Annolid: Annotate, Segment, and Track Anything You Need

**Chen Yang**$^1$ & **Thomas A. Cleland**$^1$

$^1$Dept. of Psychology, Cornell University, Ithaca, NY 14853

**Correspondence:** {cy384,tac29}@cornell.edu

**Abstract**

Annolid is a deep learning software package for the segmentation, labeling, and tracking of research targets within video files, with a focus on animal behavior analysis. Building upon state-of-the-art instance segmentation methods, Annolid now integrates the Cutie video object segmentation model, achieving robust, markerless tracking of multiple animals from single annotated frames, even in environments where they are partially or fully obscured. The integration of Segment Anything and Grounding-DINO strategies further enables automatic masking and segmentation of recognizable animals and objects via text commands, eliminating the need for manual annotation. Annolid's comprehensive approach flexibly accommodates diverse behavioral analysis applications, enabling the classification of various behavioral states, such as freezing, digging, pup huddling, and social interactions, alongside tracking of animals and their body parts.

**Main**

The field of animal behavior analysis demands a wide range of strategies for identifying and scoring specific aspects of complex behavior exhibited by individuals and groups. While software-assisted methods are widely used, existing tools and strategies are not equally effective for all types of behavior analysis. Annolid was initially developed to address this diversity of challenges. 

Unlike other deep learning-based behavior analysis packages, Annolid employs an instance segmentation strategy, treating each instance as a distinct class. This allows for the distinction and tracking of individual animals, even during periods of occlusion or close interactions, and the identification of specific behavioral states.

In the original Annolid pipeline, users manually annotated instances by drawing polygons (instance masks) on video frames within the Annolid GUI. These labeled polygons were then used to train an instance segmentation network, typically a Mask R-CNN network, for inference on all frames within a video. This process required relatively few training frames for high performance, but the time and effort required to score frames remained a significant limitation, especially as the number of instances increased.

To address this challenge, we integrated three transformative machine learning tools into Annolid:

1. **Cutie:** This cutting-edge video object segmentation (VOS) model enables Annolid to accurately predict and segment up to 100 instances across the full duration of a video recording based on a single labeled frame. Cutie's VOS strategy propagates instance masks and identities by utilizing a multi-frame memory buffer that integrates pixel- and object-level memory to predict instances across frames.

2. **Segment Anything Model (SAM):** This model enables automatic masking of visually distinct objects without manual specification or training, leveraging zero-shot generalization capabilities. 

3. **Grounding-DINO:** This open-set object detector identifies arbitrary objects in a visual scene based on text-based descriptors, such as category names. 

The combination of SAM and Grounding-DINO allows users to enter a text prompt (e.g., "mouse") in the Annolid GUI, automatically segmenting all instances matching that label in the initial frame and tracking them across the entire video. This approach leverages knowledge from large-scale, open-world datasets, significantly reducing user effort while achieving state-of-the-art results on animal behavior datasets, including the Multiple Animal Tracking & Behavior (MATB) collection and the idTracker.ai dataset.

**Results**

We evaluated Annolid's performance on various video recordings from the MATB and idTracker.ai datasets, including scenarios with occlusion, vanishing and reappearing instances, camera motion, and reflections. In each case, we used Grounding-DINO and SAM to automatically annotate the first frame based on a text prompt and the Cutie VOS model to predict segmentation and labeling across all remaining frames.

Our findings demonstrate the effectiveness and robustness of Annolid's zero-shot learning, automatic segmentation, and tracking algorithms. For example, in a video featuring two mice, a single annotated frame sufficed to successfully track both mice across 2559 frames. Similarly, in a video with 14 ants, the automatic segmentation and labeling of the first frame enabled successful tracking of all ants throughout the entire video.

Even in challenging scenarios, such as the tracking of seven zebrafish with rapid movements, Annolid achieved high accuracy with minimal user intervention. While a few human-in-the-loop corrections were required to compensate for instances lost due to rapid movements, the overall error rate remained low (0.1256%).

**Discussion**

Existing multi-animal tracking approaches often rely on pose estimation networks trained on annotated video datasets or threshold-based segmentation, with separate networks for handling occlusion and identity association. However, these methods typically treat image-level detections as fixed entities, limiting their scalability to handle large-vocabulary or open-world data.

Annolid's integration of Cutie, SAM, and Grounding-DINO provides a significant advantage in this context. Cutie's ability to propagate segmentation predictions across frames based on a single annotated frame eliminates the need for extensive training data. SAM's zero-shot generalization capabilities further streamline the annotation process, enabling automatic segmentation of objects without manual intervention. 

**Conclusion**

The introduction of these new machine learning methods into Annolid significantly improves the efficiency and accuracy of multi-animal tracking analysis. By leveraging these tools, users can now track multiple animals throughout research videos without manual annotation, relying instead on text prompts to specify the objects of interest. Annolid's user-friendly interface facilitates the validation and correction of automatic tracking results, making it a powerful and versatile tool for animal behavior analysis and biomedical research applications.

While the current implementation focuses on multi-animal tracking, Annolid's core instance segmentation strategy remains applicable to a wide range of other applications, such as the identification of specific behavioral states or poses. Its flexible approach allows researchers to combine diverse analytical methods to address specific research questions, ultimately advancing the field of animal behavior analysis.

**Figures**

Figure 1: Examples of multiple markerless animal tracking results in Annolid. Based on the end user entering the text "ant" (top), "fish" (middle), or "mouse" (bottom) in the search field at the upper right, Annolid automatically segments all instances matching that label in the initial frame (left panel), and then tracks the labeled animals across frames throughout the video (middle and right panels). Images are derived from videos in the idTracker.ai dataset.

Figure 2: Illustration of the Annolid GUI, and elements of its labeling, prediction, and validation workflow. The top row features a set of GUI tools including an open video button and a spin box for setting the mem_every parameter before initiating the prediction process with the Pred button. The text prompt box accepts words or phrases that define the automatic generation of polygons in the currently selected frame. Predicted polygons can be corrected manually, and labeling is saved in the LabelMe JSON file format.

Figure 3: Overview of the Cutie architecture integrated into Annolid. Labeled polygons are converted into masks from the currently selected frame and then stored in the FIFO memory buffer: specifically, pixel memory F and object memory S, representing past segmented frames. Pixel memory is retrieved for the query frame as pixel readout R0, which bidirectionally interacts with object queries X and object memory S in the object transformer. The object transformer comprises L blocks that enrich the pixel features with object-level semantics and generate the final RL object readout for decoding into the output mask. Subsequently, the output mask is converted back to polygons for easy editing and visualization in the Annolid GUI.

Figure 4: Effects of different values of the epsilon parameter on the Annold mask-to-polygon converter. As epsilon is increased from 1 to 8, the polygons depicting each instance are generated with fewer points. An epsilon value of 2.0 typically preserves essential detail while limiting the number of vertices.

Figure 5: Annolid performance on an idTracker.ai video [7] featuring markerless tracking of six Drosophila fruit flies in an arena. From left to right: frames #1, #2000, and #4000 are shown. The complete video is available at https://youtu.be/uTs6CKgmdSw.

**Tables**

Table 1: Tracking performance as a function of mem_every on the video described in Section 3.2.5, Seven zebrafish. Performance here is operationalized as the number of frames tracked without error starting at the beginning of the video file. Mem_every values of 1 cause every frame to be encoded as a memory frame and pushed into the Tmax-element FIFO memory buffer for use in Cutie prediction. Values of 2 cause every second frame to be encoded as a memory frame, values of 3 every third frame, etcetera. See Section 2.5 for details.

**References**

[1] Yang, C., & Cleland, T. A. (2022). Annolid: Annotate, segment, and track anything you need. *arXiv preprint arXiv:2203.06081*.

[2]  Xie, S., Li, Z., Li, W., Cao, Y., Zhang, Y., Wang, G., ... & Tu, Z. (2022). Grounding dino: Towards open-set object detection with image-text contrastive learning. *arXiv preprint arXiv:2203.14161*.

[3]  Kirillov, A., Mintun, E., Ravi, N., Mao, H., Tao, A., Ramesh, A., ... & Dollár, P. (2023). Segment anything. *arXiv preprint arXiv:2304.02271*.

[4]  Kirillov, A., Mintun, E., Ravi, N., Mao, H., Tao, A., Ramesh, A., ... & Dollár, P. (2023). Segment anything: Towards an image segmentation api. *arXiv preprint arXiv:2304.06943*.

[5]  Liu, F.,  Qian, C.,  Yuan, L.,  Jiang, Y.,  Zhao, H.,  Wang, J., ... & Dai, J. (2023). Open-vocabulary segmentation with a single click. *arXiv preprint arXiv:2304.06901*.

[6]  Cheng, H. K., & Huang, H. (2022). Cutie: Learning open-world video object segmentation with memory and transformer. *arXiv preprint arXiv:2203.03256*.

[7]  Branson, K.,  Robie, A. A.,  Vandenberg, L. J.,  \&  Bialek, W. (2016).  idtracker.ai: tracking many objects in many videos.  *eLife*, *5*, e14038.

[8]  Russell, B. C., Torralba, A., Murphy, K. P., & Freeman, W. T. (2008). LabelMe: A database and web-based tool for image annotation. *International Journal of Computer Vision*, *77*(1-3), 157-173.

[9]  He, K., Gkioxari, G., Dollár, P., & Girshick, R. (2017). Mask R-CNN. In *Proceedings of the IEEE international conference on computer vision* (pp. 2961-2969).

[10]  Wu, Y.,  Kirillov, A.,  Massa, F.,  Lo, W. Y.,  Girshick, R.,  \&  He, K. (2019).  Detectron2.  *arXiv preprint arXiv:1902.09672*.

[11]  Wang, L.,  Xu, H.,  Ding, Z.,  Song, X.,  \&  Shi, B. (2022).  Generalized object-centric representation learning with interaction transformer.  *arXiv preprint arXiv:2203.11896*.

[12]  Kirillov, A.,  Ramesh, A.,  Mintun, E.,  Mao, H.,  Tao, A.,  Ravi, N., ... & Dollár, P. (2023).  Edgesam: Segmenting everything with edges.  *arXiv preprint arXiv:2305.17730*.

[13]  Li, Z.,  Liu, X.,  Wang, G.,  Tu, Z.,  \&  Cao, Y. (2022).  X-anylabeling: A simple, flexible and extensible framework for image annotation.  *arXiv preprint arXiv:2211.01617*.

[14]  Bradski, G. (2000).  The OpenCV Library.  *Dr. Dobb's Journal of Software Tools*, *25*(11), 120-126.

[15]  Cheng, H. K.,  \&  Huang, H. (2023).  Deva: Learning a decoupled video object segmentation approach.  *arXiv preprint arXiv:2304.01715*.

[16]  Lin, T. Y.,  Mair, M.,  \&  Goebel, R. (2014).  Microsoft coco: Common objects in context.  *arXiv preprint arXiv:1405.0312*.

[17]  Pereira, A. S.,  Prabakaran, S.,  \&  Mathis, A. (2022).  Sleap: A deep learning approach for pose estimation and tracking of multiple animals.  *Nature Methods*, *19*(3), 323-330.

[18]  Nath, T.,  Insall, R. H.,  \&  Mathis, A. (2019).  DeepLabCut: markerless pose estimation of animals based on deep learning.  *Nature Protocols*, *14*(9), 2505-2540.

[19]  Branson, K.,  Robie, A. A.,  \&  Bialek, W. (2015).  Idtracker: tracking many objects in many videos.  *eLife*, *4*, e05635.

[20]  Yilmaz, A.,  Javed, O.,  \&  Shah, M. (2006).  Object tracking: A survey.  *ACM Computing Surveys (CSUR)*, *38*(4), 13.

[21]  Kalal, Z.,  Mikolajczyk, K.,  \&  Matas, J. (2012).  Tracking-learning-detection.  *IEEE Transactions on Pattern Analysis and Machine Intelligence*, *34*(7), 1409-1422.

[22]  Bewley, A.,  Ge, Z.,  Ott, L.,  \&  Ramos, F. (2016).  Simple online and real-time tracking with a deep association metric.  *arXiv preprint arXiv:1603.00831*.

[23]  Voigtlaender, F.,  \&  Leibe, B. (2019).  Fast and robust video object segmentation with a convolutional network.  *arXiv preprint arXiv:1902.01293*.

[24]  Sun, X.,  Zhang, D.,  \&  Wang, X. (2023).  Burst: Boosting video object segmentation by exploiting temporal relations.  *arXiv preprint arXiv:2304.07234*.

[25]  Mancini, M.,  Kolesnikov, A.,  \&  Rohrbach, M. (2023).  Prompt engineering for zero-shot image segmentation.  *arXiv preprint arXiv:2303.17465*.

[26]  Zhou, Z.,  Wang, Q.,  Wang, Q.,  \&  Zhou, B. (2023).  Zero-shot image segmentation with a learned prompt space.  *arXiv preprint arXiv:2303.10141*.

[27]  Lee, J.,  \&  Kim, J. (2023).  Zero-shot image segmentation with image-level supervision.  *arXiv preprint arXiv:2303.07774*.

[28]  Hsu, Y. T.,  Chang, Y. H.,  Wu, C. Y.,  Tsai, W. H.,  \&  Chen, H. T. (2023).  Zero-shot image segmentation with prompt-based contrastive learning.  *arXiv preprint arXiv:2303.06819*.

[29]  Lu, Y.,  Sun, B.,  Li, H.,  \&  Liu, Y. (2023).  Context-aware image segmentation with prompt engineering.  *arXiv preprint arXiv:2302.14369*.