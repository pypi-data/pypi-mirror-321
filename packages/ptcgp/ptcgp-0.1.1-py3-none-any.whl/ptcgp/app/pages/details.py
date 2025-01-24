__all__ = ("layout",)

import dash
import dash_mantine_components as dmc

from ptcgp import parser

dash.register_page(__name__, path_template="/card/<card_str>")


def layout(card_str: str | None = None, **kwargs):
    if not card_str:
        return dmc.Text("No card selected.")
    exp_name, card_id = card_str.split("_", maxsplit=1)
    card = parser.parse_card_by_id(exp_name, card_id)
    details_stack = dmc.Stack([
        dmc.Title(card.name),
    ])
    return dmc.Group([
        dmc.Image(src=card.image, alt=card.name, fit="scale-down", h=500),
        details_stack,
    ])
