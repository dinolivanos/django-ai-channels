from enum import StrEnum

from django import template

register = template.Library()


class RunningMode(StrEnum):
    IMAGE = "IMAGE"
    VIDEO = "VIDEO"


classifier_models = {
    "EfficientNet-Lite0_int8" :   "https://storage.googleapis.com/mediapipe-models/image_classifier/efficientnet_lite0/int8/latest/efficientnet_lite0.tflite",
    "EfficientNet-Lite0_float32": "https://storage.googleapis.com/mediapipe-models/image_classifier/efficientnet_lite0/float32/latest/efficientnet_lite0.tflite",
    "EfficientNet-Lite2_int8" :   "https://storage.googleapis.com/mediapipe-models/image_classifier/efficientnet_lite2/int8/latest/efficientnet_lite2.tflite",
    "EfficientNet-Lite2_float32": "https://storage.googleapis.com/mediapipe-models/image_classifier/efficientnet_lite2/float32/latest/efficientnet_lite2.tflite",
}

@register.inclusion_tag("aichannels/mp_video_classifier.html", takes_context=True)
def video_classifier(
        context,
        video_id: str,
        websocket_path: str,
        model_ready_callback: str = 'undefined',
        model_name: str = "EfficientNet-Lite0_int8",
        running_mode: RunningMode = RunningMode.IMAGE,
        locale: str = "en",
        max_results=-1,
        score_threshold="undefined",
        allow_list=None,
        deny_list=None,
):
    return {
        "host": context['request'].get_host(),
        "videoId": video_id,
        "websocketPath": websocket_path,
        "modelReadyCallback": model_ready_callback,
        "modelUrl": classifier_models[model_name],
        "runningMode": running_mode,
        "locale": locale,
        "maxResults": max_results,
        "scoreThreshold": score_threshold,
        "allowList": allow_list,
        "denyList": deny_list,
    }


object_detection_models = {
    "EfficientDet-Lite0_int8":      "https://storage.googleapis.com/mediapipe-models/object_detector/efficientdet_lite0/int8/latest/efficientdet_lite0.tflite",
    "EfficientDet-Lite0_float16":  "https://storage.googleapis.com/mediapipe-models/object_detector/efficientdet_lite0/float16/latest/efficientdet_lite0.tflite",
    "EfficientDet-Lite0_float32" : "https://storage.googleapis.com/mediapipe-models/object_detector/efficientdet_lite0/float32/latest/efficientdet_lite0.tflite",
    "EfficientDet-Lite2_int8":      "https://storage.googleapis.com/mediapipe-models/object_detector/efficientdet_lite2/int8/latest/efficientdet_lite2.tflite",
    "EfficientDet-Lite2_float16":  "https://storage.googleapis.com/mediapipe-models/object_detector/efficientdet_lite2/float16/latest/efficientdet_lite2.tflite",
    "EfficientDet-Lite2_float32" : "https://storage.googleapis.com/mediapipe-models/object_detector/efficientdet_lite2/float32/latest/efficientdet_lite2.tflite",
    "SSDMobileNet-V2_int8":         "https://storage.googleapis.com/mediapipe-models/object_detector/ssd_mobilenet_v2/float16/latest/ssd_mobilenet_v2.tflite",
    "SSDMobileNet-V2_int32":        "https://storage.googleapis.com/mediapipe-models/object_detector/ssd_mobilenet_v2/float32/latest/ssd_mobilenet_v2.tflite",


}

@register.inclusion_tag("aichannels/mp_video_object_detector.html", takes_context=True)
def video_object_detector(
        context,
        video_id: str,
        websocket_path: str,
        model_ready_callback: str = 'undefined',
        model_name: str = "EfficientDet-Lite0_int8",
        running_mode: RunningMode = RunningMode.IMAGE,
        locale: str = "en",
        max_results=-1,
        score_threshold="undefined",
        allow_list=None,
        deny_list=None,
):
    return {
        "host": context['request'].get_host(),
        "videoId": video_id,
        "websocketPath": websocket_path,
        "modelReadyCallback": model_ready_callback,
        "modelUrl": object_detection_models[model_name],
        "runningMode": running_mode,
        "locale": locale,
        "maxResults": max_results,
        "scoreThreshold": score_threshold,
        "allowList": allow_list,
        "denyList": deny_list,
    }
