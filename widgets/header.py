from kivy.lang import Builder
from kivy.uix.floatlayout import FloatLayout
from kivy.animation import Animation
from kivy.properties import NumericProperty


Builder.load_file('widgets/kv/header.kv')


class Header(FloatLayout):

    """ Header animation
    """
    _language_label_opacity = NumericProperty(1)
    _direction_arrow_angle = NumericProperty(0)

    def __init__(self, *args, **kwargs):
        super(Header, self).__init__()
        self.register_event_type('on_language_choice')

    def on_language_choice(self, *args):
	    pass

    def on_language_button_click(self):
        self._animate_language_choice()
        self.dispatch('on_language_choice')

    def _animate_language_choice(self):
        angle = 360 if self._direction_arrow_angle == 0 else 0
        direction_anim = Animation(direction_arrow_angle=angle, duration=.7)
        label_disappearing_anim = Animation(language_label_opacity=0, duration=.5)
        label_disappearing_anim.bind(on_complete=self._change_labels_translation_direction)
        label_appearing_anim = Animation(language_label_opacity=1, duration=.2)
        anim = direction_anim
        anim &= label_disappearing_anim + label_appearing_anim
        anim.start(self)

    def _change_labels_translation_direction(self, *args):
        left_label = self.ids.left_language_label
        right_label = self.ids.right_language_label
        left_label.text, right_label.text = right_label.text, left_label.text

