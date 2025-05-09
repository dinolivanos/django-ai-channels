from unittest import TestCase

from django.template import Context, Template


class TestMediapipeTags(TestCase):
    @classmethod
    def setup_class(cls):
        pass

    def test_video_classifier_initialize_parameters(self):
        template_string = (
            '{% load mediapipe %} '
            '{% video_classifier video_id="vv" websocket_url="ws" %}'
        )
        # fmt: on
        out = Template(template_string).render(Context())
        # print(out)
        # White space is important below
        expected = """    model = initializeModel(
      'https://storage.googleapis.com/mediapipe-models/image_classifier/efficientnet_lite0/int8/latest/efficientnet_lite0.tflite',
      "VIDEO",
      -1,
      undefined
    );
"""
        self.assertIn(expected, out)