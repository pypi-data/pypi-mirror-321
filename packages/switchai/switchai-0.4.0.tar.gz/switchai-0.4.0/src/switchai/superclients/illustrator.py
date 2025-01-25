import json
from typing import List, Union

from PIL.Image import Image
from pydantic import BaseModel, Field
import xml.etree.ElementTree as ET

from .. import SwitchAI


class Color(BaseModel):
    value: str


class Vector(BaseModel):
    x: int
    y: int


class LinearGradient(BaseModel):
    colors: List[Color]
    id: str
    start_position: Vector
    end_position: Vector


class Line(BaseModel):
    starting_position: Vector
    ending_position: Vector
    stroke: Union[Color, LinearGradient]
    stroke_width: int


class Ellipse(BaseModel):
    radius: Vector
    position: Vector = Field(..., description="The position of the center of the ellipse.")
    color: Union[Color, LinearGradient]
    stroke: Union[Color, LinearGradient]
    stroke_width: int


class Rect(BaseModel):
    position: Vector = Field(..., description="The position of the top-left corner of the rectangle.")
    size: Vector
    color: Union[Color, LinearGradient]
    radii: Vector
    stroke: Union[Color, LinearGradient]
    stroke_width: int


class Illustration(BaseModel):
    canvas_size: Vector = Field(..., description="The size of the canvas where the logo is drawn.")
    shapes: List[Union[Ellipse, Rect, Line]]


def create_linear_gradient(gradient: LinearGradient):
    linear_gradient = ET.Element(
        "linearGradient",
        attrib={
            "id": gradient.id,
            "x1": str(gradient.start_position.x),
            "y1": str(gradient.start_position.y),
            "x2": str(gradient.end_position.x),
            "y2": str(gradient.end_position.y),
            "gradientUnits": "userSpaceOnUse",
        },
    )

    for i, color in enumerate(gradient.colors):
        stop = ET.Element(
            "stop",
            attrib={
                "offset": str(i / (len(gradient.colors) - 1)),
                "stop-color": color.value,
            },
        )

        linear_gradient.append(stop)

    return linear_gradient


def render_svg(illustration: Illustration):
    svg = f"""<svg width="{illustration.canvas_size.x}" height="{illustration.canvas_size.y}" xmlns="http://www.w3.org/2000/svg"><defs></defs></svg>"""

    root = ET.fromstring(svg)
    ET.register_namespace("", "http://www.w3.org/2000/svg")

    defs = root.find("{http://www.w3.org/2000/svg}defs")

    for shape in illustration.shapes:
        if isinstance(shape, Ellipse):
            circle = ET.Element(
                "ellipse",
                attrib={
                    "cx": str(shape.position.x),
                    "cy": str(shape.position.y),
                    "rx": str(shape.radius.x),
                    "ry": str(shape.radius.y),
                    "fill": add_fill_color(shape.color, defs),
                    "stroke": add_fill_color(shape.stroke, defs),
                    "stroke-width": str(shape.stroke_width),
                },
            )

            root.append(circle)
        elif isinstance(shape, Rect):
            rect = ET.Element(
                "rect",
                attrib={
                    "x": str(shape.position.x),
                    "y": str(shape.position.y),
                    "width": str(shape.size.x),
                    "height": str(shape.size.y),
                    "rx": str(shape.radii.x),
                    "ry": str(shape.radii.y),
                    "fill": add_fill_color(shape.color, defs),
                    "stroke": add_fill_color(shape.stroke, defs),
                    "stroke-width": str(shape.stroke_width),
                },
            )

            root.append(rect)

        elif isinstance(shape, Line):
            line = ET.Element(
                "line",
                attrib={
                    "x1": str(shape.starting_position.x),
                    "y1": str(shape.starting_position.y),
                    "x2": str(shape.ending_position.x),
                    "y2": str(shape.ending_position.y),
                    "stroke": add_fill_color(shape.stroke, defs),
                    "stroke-width": str(shape.stroke_width),
                },
            )

            root.append(line)

    return ET.tostring(root).decode()


def add_fill_color(fill, defs):
    if isinstance(fill, LinearGradient):
        linear_gradient = create_linear_gradient(fill)
        defs.append(linear_gradient)
        return f"url(#{fill.id})"
    elif isinstance(fill, Color):
        return fill.value


class Illustrator:
    """
    The Illustrator superclient generates illustrations based on text descriptions.

    Args:
        client: A chat SwitchAI client.
    """

    def __init__(self, client: SwitchAI):
        if client.model_category != "chat":
            raise ValueError("Illustrator requires a chat-based model.")

        self.client = client

    def generate_illustration(
        self,
        description: str,
        output_path: str,
        image_reference: Union[str, bytes, Image] = None,
        editor_mode: bool = False,
    ):
        """
        Generates an illustration based on the given description and saves it to the specified output path.

        Args:
            description: The description of the illustration.
            output_path: The path where the illustration will be saved. The file format should be SVG.
            image_reference: An image reference to be used to generate the illustration.
            editor_mode: If True, allows the user to interactively edit the illustration.
        """

        if not output_path.endswith(".svg"):
            raise ValueError("The output file format should be SVG.")

        messages = [
            {
                "role": "user",
                "content": [
                    {
                        "type": "text",
                        "text": description,
                    }
                ],
            }
        ]
        if image_reference:
            messages[0]["content"].append(
                {
                    "type": "image",
                    "image": image_reference,
                }
            )

        print("Generating initial illustration...")

        self._generate_and_save_illustration(messages, output_path)
        print(f"Illustration saved to {output_path}")

        if editor_mode:
            print("Entering editor mode.")

            while True:
                user_input = input("Enter your message (or type '/exit' to quit): ").strip()

                if user_input.lower() == "/exit":
                    print("Exiting editor mode.")
                    break

                messages.append({"role": "user", "content": user_input})
                try:
                    self._generate_and_save_illustration(messages, output_path)
                    print(f"Updated illustration saved to {output_path}")
                except RuntimeError as e:
                    print(f"Error: {e}")

    def _generate_and_save_illustration(self, messages, output_path: str) -> str:
        response = self.client.chat(messages=messages, response_format=Illustration)

        try:
            json_data = json.loads(response.choices[0].message.content)
            rendered_svg = render_svg(Illustration.model_validate(json_data))
        except (json.JSONDecodeError, AttributeError, ValueError) as e:
            raise RuntimeError("Failed to process the illustration response.") from e

        try:
            with open(output_path, "w") as f:
                f.write(rendered_svg)
        except IOError as e:
            raise RuntimeError(f"Failed to write to file: {output_path}") from e

        return rendered_svg
