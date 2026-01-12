"""Unit tests for the ConvertTask class in the iloveimg module.

These tests verify correct behavior, parameter validation, and GIF animation options
for image conversion tasks using ConvertTask.
"""

import pytest

from iloveimg.convert_task import OUTPUT_FORMAT_OPTIONS, ConvertTask

from .base_test import AbstractUnitTaskTest


# pylint: disable=protected-access
class TestConvertTask(AbstractUnitTaskTest):
    """Unit tests for the ConvertTask class."""

    _task_class = ConvertTask
    _task_tool = "convertimage"

    def test_initialization_sets_default_values(self, my_task):
        """
        Ensure ConvertTask is initialized with default values.
        Checks that the default output format is 'jpg' and the tool is set to
            'convertimage'.
        """
        assert (
            OUTPUT_FORMAT_OPTIONS
            == my_task._EXTENSION_MAP.keys()
            == {"jpg", "png", "gif", "gif_animation"}
        )
        assert my_task._DEFAULT_PAYLOAD == {
            "convert_to": "jpg",
            "gif_time": 50,
            "gif_loop": True,
        }
        assert my_task.convert_to == "jpg"
        assert my_task.gif_time is None
        assert my_task.gif_loop is None

    @pytest.mark.parametrize("fmt", ["jpg", "png", "gif", "gif_animation"])
    def test_convert_to_valid_formats(self, my_task, fmt):
        """
        Test setting valid output formats for convert_to property, including
            gif_animation.
        """
        my_task.convert_to = fmt
        assert my_task.convert_to == fmt

    @pytest.mark.parametrize("invalid_fmt", ["pdf", "bmp", "", None, 123])
    def test_convert_to_invalid_formats(self, my_task, invalid_fmt):
        """
        Test setting invalid output formats raises ValueError.
        """
        with pytest.raises(ValueError):
            my_task.convert_to = invalid_fmt

    def test_gif_time_setter_and_getter_valid(self, my_task):
        """
        Test gif_time setter and getter with valid values when convert_to is
            'gif_animation'.
        """
        my_task.convert_to = "gif_animation"
        my_task.gif_time = 100
        assert my_task.gif_time == 100
        my_task.gif_loop = True
        assert my_task.gif_loop is True

    @pytest.mark.parametrize("invalid_time", [0, -10, "50", None, 1.5])
    def test_gif_time_invalid_values(self, my_task, invalid_time):
        """
        Test gif_time setter raises ValueError for invalid values or wrong
            convert_to.
        """
        my_task.convert_to = "gif_animation"
        with pytest.raises(ValueError):
            my_task.gif_time = invalid_time

    def test_gif_time_setter_wrong_convert_to(self, my_task):
        """
        Test gif_time setter raises ValueError if convert_to is not 'gif_animation'.
        """
        my_task.convert_to = "jpg"
        with pytest.raises(ValueError):
            my_task.gif_time = 50

    def test_gif_loop_setter_and_getter_valid(self, my_task):
        """
        Test gif_loop setter and getter with valid values when convert_to is
           'gif_animation'.
        """
        my_task.convert_to = "gif_animation"
        my_task.gif_loop = False
        assert my_task.gif_loop is False
        my_task.gif_loop = True
        assert my_task.gif_loop is True

    @pytest.mark.parametrize("invalid_loop", [1, 0, "True", None, [], {}])
    def test_gif_loop_invalid_values(self, my_task, invalid_loop):
        """
        Test gif_loop setter raises ValueError for invalid values or wrong convert_to.
        """
        my_task.convert_to = "gif_animation"
        with pytest.raises(ValueError):
            my_task.gif_loop = invalid_loop

    def test_gif_loop_setter_wrong_convert_to(self, my_task):
        """
        Test gif_loop setter raises ValueError if convert_to is not 'gif_animation'.
        """
        my_task.convert_to = "png"
        with pytest.raises(ValueError):
            my_task.gif_loop = True

    @pytest.mark.parametrize("convert_to", ("png", "jpg", "gif"))
    def test_to_payload_excludes_gif_options_when_not_gif_animation(
        self, my_task, convert_to
    ):
        """
        Test _to_payload excludes gif_time and gif_loop when convert_to is not
            'gif_animation'.
        """
        my_task.convert_to = convert_to
        params = my_task._to_payload()
        assert "gif_time" not in params
        assert "gif_loop" not in params

    def test_to_payload_includes_gif_options_when_gif_animation(self, my_task):
        """
        Test _to_payload includes gif_time and gif_loop when convert_to is
            'gif_animation'.
        """
        my_task.convert_to = "gif_animation"
        my_task.gif_time = 75
        my_task.gif_loop = False
        params = my_task._to_payload()
        assert params["convert_to"] == "gif_animation"
        assert params["gif_time"] == 75
        assert params["gif_loop"] is False

    @pytest.mark.parametrize(
        "convert_to,extensions",
        [
            ("jpg", ["png", "gif", "tif", "psd", "svg", "webp", "heic", "raw"]),
            ("png", ["jpg"]),
            ("gif", ["jpg"]),
            ("gif_animation", ["gif"]),
        ],
    )
    def test_validate_body_accepts_valid_extensions(
        self, my_task, convert_to, extensions
    ):
        """
        Test that _validate_body accepts valid extensions for the selected
            convert_to format.
        """
        my_task.convert_to = convert_to
        body = {
            "data": {
                "files": [
                    {"filename": f"sample.{extension}"} for extension in extensions
                ]
            }
        }
        assert my_task.validate_body(body)

    @pytest.mark.parametrize(
        "convert_to",
        ["jpg", "png", "gif", "gif_animation"],
    )
    def test_validate_body_raises_for_invalid_extension(self, my_task, convert_to):
        """
        Test that _validate_body raises ValueError when a file has an invalid extension
        for the selected convert_to format.
        """
        my_task.convert_to = convert_to
        payload = {"files": [{"filename": "sample1.abc"}]}
        with pytest.raises(ValueError):
            my_task._validate_payload(payload)
