__all__ = ("layout",)

import dash
import dash_mantine_components as dmc

from ... import parser

dash.register_page(__name__, path_template="/card/<card_str>")


def layout(card_str: str, **kwargs):
    exp_name, card_id = card_str.split("_", maxsplit=1)
    card = parser.parse_card_by_id(exp_name, card_id)
    return dmc.Image(src=card.image)
