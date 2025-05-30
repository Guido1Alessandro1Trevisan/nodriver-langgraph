# DO NOT EDIT THIS FILE!
#
# This file is generated from the CDP specification. If you need to make
# changes, edit the generator and regenerate all of the modules.
#
# CDP domain: HeadlessExperimental (experimental)

from __future__ import annotations

import typing
from dataclasses import dataclass

from deprecated.sphinx import deprecated  # type: ignore

from .util import T_JSON_DICT


@dataclass
class ScreenshotParams:
    """
    Encoding options for a screenshot.
    """

    #: Image compression format (defaults to png).
    format_: typing.Optional[str] = None

    #: Compression quality from range [0..100] (jpeg and webp only).
    quality: typing.Optional[int] = None

    #: Optimize image encoding for speed, not for resulting size (defaults to false)
    optimize_for_speed: typing.Optional[bool] = None

    def to_json(self) -> T_JSON_DICT:
        json: T_JSON_DICT = dict()
        if self.format_ is not None:
            json["format"] = self.format_
        if self.quality is not None:
            json["quality"] = self.quality
        if self.optimize_for_speed is not None:
            json["optimizeForSpeed"] = self.optimize_for_speed
        return json

    @classmethod
    def from_json(cls, json: T_JSON_DICT) -> ScreenshotParams:
        return cls(
            format_=(
                str(json["format"]) if json.get("format", None) is not None else None
            ),
            quality=(
                int(json["quality"]) if json.get("quality", None) is not None else None
            ),
            optimize_for_speed=(
                bool(json["optimizeForSpeed"])
                if json.get("optimizeForSpeed", None) is not None
                else None
            ),
        )


def begin_frame(
        frame_time_ticks: typing.Optional[float] = None,
        interval: typing.Optional[float] = None,
        no_display_updates: typing.Optional[bool] = None,
        screenshot: typing.Optional[ScreenshotParams] = None,
) -> typing.Generator[
    T_JSON_DICT, T_JSON_DICT, typing.Tuple[bool, typing.Optional[str]]
]:
    """
    Sends a BeginFrame to the target and returns when the frame was completed. Optionally captures a
    screenshot from the resulting frame. Requires that the target was created with enabled
    BeginFrameControl. Designed for use with --run-all-compositor-stages-before-draw, see also
    https://goo.gle/chrome-headless-rendering for more background.

    :param frame_time_ticks: *(Optional)* Timestamp of this BeginFrame in Renderer TimeTicks (milliseconds of uptime). If not set, the current time will be used.
    :param interval: *(Optional)* The interval between BeginFrames that is reported to the compositor, in milliseconds. Defaults to a 60 frames/second interval, i.e. about 16.666 milliseconds.
    :param no_display_updates: *(Optional)* Whether updates should not be committed and drawn onto the display. False by default. If true, only side effects of the BeginFrame will be run, such as layout and animations, but any visual updates may not be visible on the display or in screenshots.
    :param screenshot: *(Optional)* If set, a screenshot of the frame will be captured and returned in the response. Otherwise, no screenshot will be captured. Note that capturing a screenshot can fail, for example, during renderer initialization. In such a case, no screenshot data will be returned.
    :returns: A tuple with the following items:

        0. **hasDamage** - Whether the BeginFrame resulted in damage and, thus, a new frame was committed to the display. Reported for diagnostic uses, may be removed in the future.
        1. **screenshotData** - *(Optional)* Base64-encoded image data of the screenshot, if one was requested and successfully taken. (Encoded as a base64 string when passed over JSON)
    """
    params: T_JSON_DICT = dict()
    if frame_time_ticks is not None:
        params["frameTimeTicks"] = frame_time_ticks
    if interval is not None:
        params["interval"] = interval
    if no_display_updates is not None:
        params["noDisplayUpdates"] = no_display_updates
    if screenshot is not None:
        params["screenshot"] = screenshot.to_json()
    cmd_dict: T_JSON_DICT = {
        "method": "HeadlessExperimental.beginFrame",
        "params": params,
    }
    json = yield cmd_dict
    return (
        bool(json["hasDamage"]),
        (
            str(json["screenshotData"])
            if json.get("screenshotData", None) is not None
            else None
        ),
    )


@deprecated(version="1.3")
def disable() -> typing.Generator[T_JSON_DICT, T_JSON_DICT, None]:
    """
    Disables headless events for the target.

    .. deprecated:: 1.3
    """
    cmd_dict: T_JSON_DICT = {
        "method": "HeadlessExperimental.disable",
    }
    json = yield cmd_dict


@deprecated(version="1.3")
def enable() -> typing.Generator[T_JSON_DICT, T_JSON_DICT, None]:
    """
    Enables headless events for the target.

    .. deprecated:: 1.3
    """
    cmd_dict: T_JSON_DICT = {
        "method": "HeadlessExperimental.enable",
    }
    json = yield cmd_dict
