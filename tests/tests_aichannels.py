from django.test import TestCase
from django.template import Context, Template, TemplateSyntaxError
from aichannels import templatetags


class TestAichannels(TestCase):
    @classmethod
    def setup_class(cls):
        pass

    def test_aichannels_template_coco_ssd_js(self):
        templatetags.aichannels.coco_ssd_js

        # must pass element_id
        with self.assertRaises(TemplateSyntaxError):
            Template("{% load aichannels%} {% coco_ssd_js %}").render(Context())

        # fmt: off
        template_string = (
            '{% load aichannels %} '
            '{% coco_ssd_js element_id="xx" %}'
        )
        # fmt: on
        out = Template(template_string).render(Context())
        self.assertNotIn("only generate this if loadedCB given", out)

        # fmt: off
        template_string = (
            '{% load aichannels %} '
            '{% coco_ssd_js element_id="xx" model_loaded_callback="cb"%}'
        )
        # fmt: on
        out = Template(template_string).render(Context())
        self.assertIn("only generate this if loadedCB given", out)
        self.assertIn("(model) => cb()", out)

        # fmt: off
        template_string = (
            '{% load aichannels %} '
            '{% coco_ssd_js element_id="xx" prediction_callback="cb" %}'
        )
        # fmt: on
        out = Template(template_string).render(Context())
        self.assertIn('(model) => attach_model("xx", cb)', out)

    @classmethod
    def teardown_class(cls):
        pass
