from django.forms.widgets import ChoiceWidget


class GameSelectMultiple(ChoiceWidget):
    """Create our own Game select widget.
    Parent should be CheckboxSelectMultiple,
    but template override wasn't working properly."""

    allow_multiple_selected = True
    input_type = 'checkbox'
    template_name = 'rent/game_select.html'
    option_template_name = 'rent/game_option.html'

    def use_required_attribute(self, initial):
        # Don't use the 'required' attribute because browser validation would
        # require all checkboxes to be checked instead of at least one.
        return False

    def value_omitted_from_data(self, data, files, name):
        # HTML checkboxes don't appear in POST data if not checked, so it's
        # never known if the value is actually omitted.
        return False

    def id_for_label(self, id_, index=None):
        """"
        Don't include for="field_0" in <label> because clicking such a label
        would toggle the first checkbox.
        """
        if index is None:
            return ''
        return super().id_for_label(id_, index)
