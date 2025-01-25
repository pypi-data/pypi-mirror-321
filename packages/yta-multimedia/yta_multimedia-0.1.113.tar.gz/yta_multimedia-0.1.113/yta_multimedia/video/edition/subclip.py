"""
All this file is currently in 'yta_multimedia' library
because I'm testing it, but the concepts contained in
this file don't belong to this library because they are
related to a VideoEditor concept, not to image or video
simple editing.

We need to handle, when working in building a whole video
project, videos as SubClips so we handle all attributes
and, if we subclip a SubClip instance, we .copy() the
previous attributes to the left, center and right clips
we obtain when subclipping. This would preserve previous
configurations and let us manage all the clips, so we
work on top of moviepy library in any change we process
and use moviepy only for basic and frame transformations.

TODO: These classes below will be moved in a near future
to its own project or to 'youtube_autonomous'.
"""
from yta_multimedia.video.parser import VideoParser
from yta_multimedia.image.edition.image_editor import ImageEditor
from yta_multimedia.video.edition.effect.moviepy.mask import ClipGenerator
from yta_multimedia.video.edition.settings import VOLUME_LIMIT, ZOOM_LIMIT, LAYERS_INDEXES_LIMIT, COLOR_TEMPERATURE_LIMIT, MAX_TIMELINE_LAYER_DURATION, BRIGHTNESS_LIMIT, CONTRAST_LIMIT, WHITE_BALANCE_LIMIT, SHARPNESS_LIMIT, SPEED_FACTOR_LIMIT
from yta_multimedia.video.edition.video_frame_t_helper import VideoFrameTHelper
from yta_general_utils.programming.parameter_validator import NumberValidator, PythonValidator
from yta_general_utils.programming.enum import YTAEnum as Enum
from moviepy.Clip import Clip
from moviepy import CompositeVideoClip, concatenate_videoclips
from typing import Union

import numpy as np


END_OF_CLIP = 999999
END_OF_TIMELINE = 120
"""
The limit of the timeline length. It is not possible
to generate a project which length is larger than 
this value.

TODO: This value could be very low in alpha and beta
versions for testing.
"""

# TODO: Move this decorator below to another place (?)
def unset_video_processed(func):
    """
    Decorator function that sets the '_video_processed'
    attribute to None to indicate that it has been
    modified and it must be processed again.
    """
    def wrapper(self, value):
        value = func(self, value)
        self._video_processed = None
        
        return value
    
    return wrapper


from yta_general_utils.math.rate_functions import mRateFunction
from yta_general_utils.math.progression import Progression


class SubClipAttributeModifier:
    """
    Class to encapsulate the possible ways to modify a 
    video attribute.

    This will be passed as an instance to a SubClip to 
    calculate the modification values array for each 
    frame and set those modifying values in the video
    instance to be lately applied to the video when
    processing it.

    This is a wrapper to simplify the way we interact
    with different object types valid to generate
    values.

    The only accepted values by now are:
    - Single value
    - SubClipSetting
    - Graphic
    """
    modifier: Union[any, 'SubClipSetting', 'Graphic'] = None

    @property
    def is_single_value(self) -> bool:
        """
        Return True if the modifier is just a single value.
        """
        return PythonValidator.is_number(self.modifier)

    def __init__(self, modifier: Union[any, 'SubClipSetting', 'Graphic']):
        # TODO: Change SubClipSetting name as its purpose is
        # now different and not to appropiate for this
        if (
            # TODO: Maybe we accept some non-numeric modifier
            # single values (?)
            not PythonValidator.is_number(modifier) and
            not PythonValidator.is_instance(modifier, 'SubClipSetting') and
            not PythonValidator.is_instance(modifier, 'Graphic')
        ):
            raise Exception('The provided "modifier" parameter is not a valid modifier.')
        
        self.modifier = modifier

    def get_values(self, n: float):
        """
        Obtain an array of 'n' values that will modify the
        attribute this instance is designed for. The 'n'
        value must be the number of frames.
        """
        # I don't like float 'fps' but it is possible, and I
        # should force any clip to be 30 or 60fps always
        if PythonValidator.is_number(self.modifier): return [self.modifier] * n
        if PythonValidator.is_instance(self.modifier, 'SubClipSetting'): return self.modifier.get_values(n)
        if PythonValidator.is_instance(self.modifier, 'Graphic'): return [self.modifier.get_xy_from_normalized_d(d)[1] for d in Progression(0, 1, n).values]

    def validate_values(self, n: float, limit: list[float, float]):
        """
        Validate that any of those 'values' is between the
        limit range. The 'n' parameter must be the number of
        frames in the video, and 'limit' a tuple of the lower
        and upper limit.

        This method must be called when a SubClipAttributeModifier
        instance is set in a SubClip because we know the number
        of frames and the limit for that specific attribute (it
        is being added to that attribute modifier) in that 
        moment.
        """
        if any(value < limit[0] or value > limit[1] for value in self.get_values(n)):
            raise Exception(f'One of the generated "values" is out of the limit [{limit[0]}, {limit[1]}]')

    def copy(self):
        return SubClipAttributeModifier(self.modifier.copy())


# TODO: Think again about this because now we have the
# SubClipAttributeModifier to be passed as the modifier
# and it accepts this SubClipSetting, that must be renamed
# for its new purpose
class SubClipSetting:
    """
    Class to represent a video setting to be able to handle
    dynamic setting values and not only simple values. This
    means we can make a video go from 0 contrast to 10 
    contrast increasing it smoothly (for example: 0, 2, 4,
    6, 8 and 10) and not only abruptly (from 0 in one frame
    to 10 in the next frame).
    """
    initial_value: float = None
    final_value: float = None
    rate_function: mRateFunction = None

    def __init__(self, initial_value: float, final_value: float, rate_function: mRateFunction = mRateFunction.LINEAR):
        # TODO: Maybe validate something? I don't know the
        # limits because each setting is different, but by
        # now I'm verifying the 'initial_value' and the
        # 'final_value' when using them on a SubClip
        self.initial_value = initial_value
        self.final_value = final_value
        self.rate_function = rate_function

    def get_values(self, steps: int):
        """
        Obtain an array with the values between the 'initial_value'
        and the 'final_value' according to the 'rate_function'.

        The 'steps' parameter must be the amount of frames in which
        we are planning to apply this setting so we are able to read
        the value for each frame according to its index.
        """
        # Same limits cannot be handled by the Progression class as
        # it is just an array of the same value repeated 'steps' 
        # times
        if self.initial_value == self.final_value:
            return [self.initial_value for _ in range(steps)]
        
        # TODO: Think a new way to avoid calculating the progression
        # again and again when asking for the same amount of 'steps'
        # and attributes are still the same
        return Progression(self.initial_value, self.final_value, steps, self.rate_function).values
    
    def copy(self):
        return SubClipSetting(
            self.initial_value,
            self.final_value,
            self.rate_function
        )


class SubClip:
    """
    Class to represent a subclip of a clip in which we
    can apply different modifications such as color
    temperature, zoom, movement, etc.

    This class represent the same as one of the subclips
    in any of your video editor apps.
    """
    # TODO: This, as the original video clip (moviepy),
    # maybe must be private to avoid using it directly
    video: Clip = None
    _video_processed: Clip = None
    """
    The video once it's been processed with all its
    attributes and effects.
    """
    # TODO: Add all needed attributes
    # Volume
    _volume: int = None

    # Attributes that can be modified
    _color_temperature: list[float] = None
    """
    A list of values for the color temperature modification
    in which each position is the modifier for each video
    frame.
    """
    _brightness: list[float] = None
    """
    A list of values for the brightness modification in
    which each position is the modifier for each video
    frame.
    """
    _contrast: list[float] = None
    """
    A list of values for the contrast modification in which
    each position is the modifier for each video frame.
    """
    _sharpness: list[float] = None
    """
    A list of values for the sharpness modification in which
    each position is the modifier for each video frame.
    """
    _white_balance: list[float] = None
    """
    A list of values for the white balance modification in
    which each position is the modifier for each video frame.
    """

    # Special modifiers
    # TODO: This is special because it affects to the video
    # duration. It has to be applied at the end
    _speed_factor: list[float] = None
    """
    A list of values for the speed modification in which the
    whole video duration is modified by these speed factor
    values, that are set for each video frame.

    TODO: Maybe I can have one single speed factor value 
    when I just need to apply the simple video effect, but
    an array of them when I need to modify it with a more
    complex algorithm.
    """

    # Color attributes
    # Zoom and movement
    _zoom: int = None
    
    x_movement: int = None
    y_movement: int = None
    rotation: int = None
    # Custom effects
    _effects: list['MEffect'] = None

    @staticmethod
    def init(video: Clip, start_time: Union[float, None] = 0, end_time: Union[float, None] = END_OF_CLIP):
        """
        This is the only method we need to use when instantiating
        a SubClip so we can obtain the left and right clip result
        of the subclipping process and also the new SubClip
        instance.

        This method returns a tuple with 3 elements, which are the
        left part of the subclipped video, the center part and the
        right part as SubClip instances. If no left or right part,
        they are return as None. So, the possibilities are (from
        left to right):

        - SubClip, SubClip, SubClip
        - SubClip, SubClip, None
        - None, SubClip, SubClip
        - None, SubClip, SubClip
        """
        video = VideoParser.to_moviepy(video)

        left_clip, center_clip, right_clip = subclip_video(video, start_time, end_time)

        return (
            SubClip(left_clip) if left_clip is not None else None,
            SubClip(center_clip),
            SubClip(right_clip) if right_clip is not None else None
        )

    def __init__(self, video: Clip):
        """
        DO NOT USE THIS METHOD DIRECTLY. Use static '.init()'
        method instead.

        The SubClip instantiating method has to be called only
        in the static 'init' method of this class so we are able
        to handle the rest of the clips (if existing) according
        to the subclipping process we do.
        """
        self.video = VideoParser.to_moviepy(video)
        self.volume = 100

    @property
    def video_processed(self):
        if not self._video_processed:
            self._video_processed = self._process()

        return self._video_processed

    @property
    def duration(self):
        """
        Shortcut to the actual duration of the video once
        it's been processed.
        """
        # TODO: Maybe this has to be the pre-processed
        #return self.video_processed.duration
        return self.video.duration
    
    @property
    def size(self):
        """
        Shortcut to the actual size of the video once
        it's been processed.
        """
        # TODO: Maybe this has to be the pre-processed
        return self.video_processed.size
    
    @property
    def fps(self):
        """
        Fps of the original video (the pre-processed one).
        """
        return self.video.fps
    
    @property
    def number_of_frames(self):
        """
        Number of frames of the original video (the 
        pre-processed one).

        Due to a bug with the moviepy reading way, this
        number cannot be the real number. Check the 
        MPVideo class that looks for the exact number.
        """
        # TODO: Maybe use MPVideo to ensure the video
        # has the real number of frames, and also 
        # subclip the video to the real duration based
        # on this. I have a method that does it by 
        # trying to get the last frames and catching
        # the warnings
        return int(self.duration * self.fps + 0.000001)
    
    @property
    def color_temperature(self):
        return self._color_temperature
    
    @color_temperature.setter
    def color_temperature(self, value: SubClipAttributeModifier):
        """
        Set the color temperature values by providing a 
        SubClipAttributeModifier that will set the values
        for the current SubClip.
        """
        _validate_is_video_attribute_modifier_instance(value)
        _validate_attribute_modifier(value, '_color_temperature', COLOR_TEMPERATURE_LIMIT, self.number_of_frames)

        self._color_temperature = value.get_values(self.number_of_frames)

    @property
    def brightness(self):
        return self._brightness
    
    @brightness.setter
    def brightness(self, value: SubClipAttributeModifier):
        _validate_is_video_attribute_modifier_instance(value)
        _validate_attribute_modifier(value, 'brightness', BRIGHTNESS_LIMIT, self.number_of_frames)

        self._brightness = value.get_values(self.number_of_frames)

    @property
    def contrast(self):
        return self._contrast
    
    @contrast.setter
    def contrast(self, value: SubClipAttributeModifier):
        _validate_is_video_attribute_modifier_instance(value)
        _validate_attribute_modifier(value, 'contrast', CONTRAST_LIMIT, self.number_of_frames)

        self._contrast = value.get_values(self.number_of_frames)

    @property
    def sharpness(self):
        return self._sharpness

    @sharpness.setter
    def sharpness(self, value: SubClipAttributeModifier):
        _validate_is_video_attribute_modifier_instance(value)
        _validate_attribute_modifier(value, 'sharpness', SHARPNESS_LIMIT, self.number_of_frames)

        self._sharpness = value.get_values(self.number_of_frames)

    @property
    def white_balance(self):
        return self._white_balance
    
    @white_balance.setter
    def white_balance(self, value: SubClipAttributeModifier):
        _validate_is_video_attribute_modifier_instance(value)
        _validate_attribute_modifier(value, 'white_balance', WHITE_BALANCE_LIMIT, self.number_of_frames)

        self._white_balance = value.get_values(self.number_of_frames)

    @property
    def speed_factor(self):
        return self._speed_factor
    
    @speed_factor.setter
    def speed_factor(self, value: SubClipAttributeModifier):
        _validate_is_video_attribute_modifier_instance(value)
        _validate_attribute_modifier(value, 'speed_factor', SPEED_FACTOR_LIMIT, self.number_of_frames)

        self._speed_factor = value.modifier if value.is_single_value else value.get_values(self.number_of_frames) 






    @property
    def zoom(self):
        return self._zoom
    
    @zoom.setter
    @unset_video_processed
    def zoom(self, value):
        _validate_zoom(value)
        
        self._zoom = int(value)

    @property
    def volume(self):
        return self._volume
    
    @volume.setter
    @unset_video_processed
    def volume(self, value):
        _validate_volume(value)
        
        self._volume = int(value)

    # Easy setters below, that are another way of setting
    # attributes values but just passing arguments. This
    # is interesting if you just need to apply a simple
    # and single value or an easy range
    def set_color_temperature(self, start: int, end: Union[int, None] = None, rate_function: mRateFunction = mRateFunction.LINEAR):
        """
        Set a new color temperature that will be modified frame by frame.

        If only 'start' is provided, the change will be the same in all
        frames, but if a different 'end' value is provided, the also given
        'rate_function' will be used to calculate the values in between
        those 'start' and 'end' limits to be applied in the corresponding
        frames.
        """
        self.color_temperature = SubClipAttributeModifier(
            SubClipSetting(
                start,
                start if end is None else end,
                mRateFunction.to_enum(rate_function)
            )
        )

    def set_brightness(self, start: int, end: Union[int, None] = None, rate_function: mRateFunction = mRateFunction.LINEAR):
        """
        Set a new brightness that will be modified frame by frame.
        
        If only 'start' is provided, the change will be the same in all
        frames, but if a different 'end' value is provided, the also given
        'rate_function' will be used to calculate the values in between
        those 'start' and 'end' limits to be applied in the corresponding
        frames.
        """
        self.brightness = SubClipAttributeModifier(
            SubClipSetting(
                start,
                start if end is None else end,
                mRateFunction.to_enum(rate_function)
            )
        )

    def set_contrast(self, start: int, end: Union[int, None] = None, rate_function: mRateFunction = mRateFunction.LINEAR):
        """
        Set a new contrast that will be modified frame by frame.
        
        If only 'start' is provided, the change will be the same in all
        frames, but if a different 'end' value is provided, the also given
        'rate_function' will be used to calculate the values in between
        those 'start' and 'end' limits to be applied in the corresponding
        frames.
        """
        self.contrast = SubClipAttributeModifier(
            SubClipSetting(
                start,
                start if end is None else end,
                mRateFunction.to_enum(rate_function)
            )
        )

    def set_sharpness(self, start: int, end: Union[int, None] = None, rate_function: mRateFunction = mRateFunction.LINEAR):
        """
        Set a new sharpness that will be modified frame by frame.
        
        If only 'start' is provided, the change will be the same in all
        frames, but if a different 'end' value is provided, the also given
        'rate_function' will be used to calculate the values in between
        those 'start' and 'end' limits to be applied in the corresponding
        frames.
        """
        self.sharpness = SubClipAttributeModifier(
            SubClipSetting(
                start,
                start if end is None else end,
                mRateFunction.to_enum(rate_function)
            )
        )

    def set_white_balance(self, start: int, end: Union[int, None] = None, rate_function: mRateFunction = mRateFunction.LINEAR):
        """
        Set a new white balance that will be modified frame by frame.
        
        If only 'start' is provided, the change will be the same in all
        frames, but if a different 'end' value is provided, the also given
        'rate_function' will be used to calculate the values in between
        those 'start' and 'end' limits to be applied in the corresponding
        frames.
        """
        self.white_balance = SubClipAttributeModifier(
            SubClipSetting(
                start,
                start if end is None else end,
                mRateFunction.to_enum(rate_function)
            )
        )

    def set_speed_factor(self, start: int, end: Union[int, None] = None, rate_function: mRateFunction = mRateFunction.LINEAR):
        """
        Set a new speed factor that will be modifier frame by frame.

        If only 'start' is provided, the change will be the same in all
        frames, but if a different 'end' value is provided, the also given
        'rate_function' will be used to calculate the values in between
        those 'start' and 'end' limits to be applied in the corresponding
        frames.
        """
        self.speed_factor = SubClipAttributeModifier(
            SubClipSetting(
                start,
                start if end is None else end,
                mRateFunction.to_enum(rate_function)
            )
        )

    
    
    def _apply_speed_factor(self, video):
        """
        Apply the speed factors to the video. This method 
        will use the 'time_transform' method and also will
        set a new duration with the 'with_duration' method.

        This method returns the new video modified.
        """
        if PythonValidator.is_number(self.speed_factor) or self.speed_factor is None:
            raise Exception(f'The "speed_factor" parameter is not valid for this method. It must be an array of {self.number_of_frames} elements.')

        def _get_video_frame_ts_applying_speed_factors(self: SubClip):
            """
            Get the final video frame 't' time moments according
            to the speed factors once they've been applied. These
            time moments must be accesed by the new final video 
            frame index to know which 't' time moment from the
            original video must be used.
            """
            if self.number_of_frames != len(self.speed_factor):
                raise Exception('The number of video frames and speed factors array must be the same.')
            
            final_video_frame_ts = []
            rest = 0
            current_frame_index = 0
            while current_frame_index < self.number_of_frames:
                current_speed_factor = self.speed_factor[current_frame_index]

                if current_speed_factor < 1:
                    # We need to repeat frames to slow it down
                    times_to_append = 1
                    current_rest = (1 / current_speed_factor) - 1
                    rest -= current_rest

                    if rest <= -1:
                        times_to_append += int(abs(rest))
                        rest += int(abs(rest))
                    
                    # We convert the current audio frame index to its 
                    # base 't' time moment so we can know which 't'
                    # time moment of the original video audio we will
                    # use for this frame index when rendering
                    final_video_frame_ts.extend([VideoFrameTHelper.get_video_frame_t_from_video_frame_index(current_frame_index, self.video.fps)])
                    
                elif current_speed_factor > 1:
                    # We need to skip frames to speed it up
                    final_video_frame_ts.append(VideoFrameTHelper.get_video_frame_t_from_video_frame_index(current_frame_index, self.video.fps))
                    current_rest = current_speed_factor - 1
                    rest += current_rest

                    if rest >= 1:
                        
                        current_frame_index += int(rest)
                        rest -= int(rest)

                current_frame_index += 1

            return final_video_frame_ts
    
        def _get_video_audio_frame_ts_applying_speed_factors(self: SubClip):
            """
            Get the final video audio frame 't' time moments
            according to the speed factors once they've been
            applied. These time moments must be accesed by the
            new final video audio frame index to know which 't'
            time moment from the original video must be used.
            """
            if self.number_of_frames != len(self.speed_factor):
                raise Exception('The number of video frames and speed factors array must be the same.')
            
            audio = self.video.audio
            total_video_audio_frames = int(audio.fps * audio.duration + 0.000001)
            final_video_audio_frame_ts = []
            rest = 0
            current_frame_index = 0
            while current_frame_index < total_video_audio_frames:
                current_speed_factor = self.speed_factor[VideoFrameTHelper.get_video_frame_index_from_video_audio_frame_index(current_frame_index, self.video.fps, audio.fps)]

                if current_speed_factor < 1:
                    # We need to repeat frames to slow it down
                    times_to_append = 1
                    current_rest = (1 / current_speed_factor) - 1
                    rest -= current_rest

                    if rest <= -1:
                        times_to_append += int(abs(rest))
                        rest += int(abs(rest))

                    # We need to repeat frames to slow it down
                    # We convert the current audio frame index to its 
                    # base 't' time moment so we can know which 't'
                    # time moment of the original video audio we will
                    # use for this frame index when rendering
                    final_video_audio_frame_ts.extend([VideoFrameTHelper.get_video_audio_frame_t_from_video_audio_frame_index(current_frame_index, audio.fps)] * times_to_append)
                    
                elif current_speed_factor > 1:
                    # We need to skip frames to speed it up
                    final_video_audio_frame_ts.append(VideoFrameTHelper.get_video_audio_frame_t_from_video_audio_frame_index(current_frame_index, audio.fps))
                    current_rest = current_speed_factor - 1
                    rest += current_rest

                    if rest >= 1:
                        current_frame_index += int(rest)
                        rest -= int(rest)

                current_frame_index += 1

            return final_video_audio_frame_ts

        final_video_frame_ts = _get_video_frame_ts_applying_speed_factors(self)
        final_audio_frame_ts = _get_video_audio_frame_ts_applying_speed_factors(self)

        def transform_t_with_both_frames(t, video_fps: float, audio_fps: float):
            if not PythonValidator.is_numpy_array(t):
                frame_index = VideoFrameTHelper.get_video_frame_index_from_video_frame_t(t, video_fps)
                if frame_index >= len(final_video_frame_ts):
                    print(f'Sorry, {frame_index} is out of bounds.')
                    frame_index = len(final_video_frame_ts) - 1

                return final_video_frame_ts[frame_index]
            else:
                tis = []
                for t_ in t:
                    frame_index = VideoFrameTHelper.get_video_audio_frame_index_from_video_audio_frame_t(t_, audio_fps)
                    if frame_index >= len(final_audio_frame_ts):
                        print(f'Sorry, {frame_index} is out of bounds.')
                        frame_index = len(final_audio_frame_ts) - 1

                    tis.append(frame_index)

                # I have to return an array that replaces the ts
                return np.array([final_audio_frame_ts[ti] for ti in tis])

        # TODO: What if video has no audio (?)
        video = video.time_transform(
            lambda t: transform_t_with_both_frames(t, self.video.fps, self.video.audio.fps), apply_to = ['mask', 'audio']
        )
        video = video.with_duration(len(final_video_frame_ts) * 1 / video.fps)

        return video

    def add_effect(self, effect: 'MEffect'):
        """
        Add the provided 'effect' instance to be applied on the clip.
        """
        if not PythonValidator.is_an_instance(effect) or not PythonValidator.is_subclass(effect, 'MEffect'):
            raise Exception('The provided "effect" parameter is not an instance of a MEffect subclass.')
        
        # TODO: Check that effect is valid (times are valid, there is
        # not another effect that makes it incompatible, etc.)
        self._effects.append(effect)

    def subclip(self, start: float, end: float):
        """
        This method will split the current SubClip instance
        into 3 different items, that will be new instances
        of SubClip class according to the 'start' and 'end'
        times provided.

        This method uses a copy of the current instance to
        not modify it but returning completely new (by
        using deepcopy). All settings and effects will be
        preserved as they were in the original instance for
        all of the new copies.

        This method will return 3 values: left part of the
        SubClip, center part and right part. Left and right
        part can be None.
        """
        # TODO: Validate
        if not NumberValidator.is_positive_number(start):
            raise Exception('The "start" parameter provided is not a valid and positive number (0 included).')
        
        if not NumberValidator.is_positive_number(end):
            raise Exception('The "end" parameter provided is not a valid and positive number (0 included).')
        
        if start >= end:
            raise Exception('The "start" parameter provided is greater or equal than the "end" parameter provided.')
        
        if end > self.duration:
            raise Exception(f'The "end" provided ({end}s) is longer than the current video duration ({self.duration}s).')

        # TODO: I need to calculate the frame index in which I'm
        # splitting the subclip to also subclip the arrays that
        # are inside the instance
        left = self.copy() if start not in (None, 0) else None
        center = self.copy()
        right = self.copy() if end is not None and end < self.duration else None

        def replace_attribute_values(instance: SubClip, start_index: Union[float, None], end_index: Union[float, None]):
            """
            Replaces the attribute values of the given 'instance' 
            considering the left, center and right videos that will
            be returned as result so each video can keep only their
            values.
            """
            def split_array(array: list, start_index: Union[float, None], end_index: Union[float, None]):
                # TODO: Validate 'start_index' and 'end_index' according
                # to 'array' size
                if start_index is not None and end_index is not None: return array[start_index:end_index]
                if start_index is not None: return array[start_index:]
                if end_index is not None: return array[:end_index]
                return array

            # TODO: Append here any new array of values per frame
            instance._color_temperature = split_array(instance._color_temperature, start_index, end_index) if instance._color_temperature is not None else None
            instance._brightness = split_array(instance._brightness, start_index, end_index) if instance._brightness is not None else None
            instance._contrast = split_array(instance._contrast, start_index, end_index) if instance._contrast is not None else None
            instance._sharpness = split_array(instance._sharpness, start_index, end_index) if instance._sharpness is not None else None
            instance._white_balance = split_array(instance._white_balance, start_index, end_index) if instance._white_balance is not None else None
            # TODO: '_speed_factor' is special and can be both a single
            # value or a list (or a None if no changes to apply)
            if PythonValidator.is_list(instance._speed_factor):
                instance._speed_factor = split_array(instance._speed_factor, start_index, end_index)
            else:
                instance._speed_factor = instance._speed_factor
            
            return instance

        last_index = 0
        # Left
        if left is not None:
            left.video = left.video.with_subclip(0, start)
            last_index = left.number_of_frames
            # Modify all the attributes per frame values
            replace_attribute_values(left, last_index, None)

        # Center
        center.video = center.video.with_subclip(start, end)
        # Modify all the attributes per frame values
        replace_attribute_values(center, last_index, last_index + center.number_of_frames)
        last_index = last_index + center.number_of_frames

        # Right
        if right is not None:
            right.video = right.video.with_subclip(start_time = end)
            # Modify all the attributes per frame values
            replace_attribute_values(right, None, last_index)

        return left, center, right
    
    def _process(self):
        """
        Process the video clip with the attributes set and 
        obtain a copy of the original video clip with those
        attributes and effects applied on it. This method
        uses a black (but transparent) background with the
        same video size to make sure everything works 
        properly.

        This method doesn't change the original clip, it
        applies the changes on a copy of the original one
        and returns that copy modified.
        """
        video = self.video.copy()

        from yta_multimedia.video import MPVideo

        # I use this class to ensure it fits the real number
        # of frames so we can modify it correctly
        video_handler = MPVideo(video)

        # TODO: The 3 customizable elements
        # This can be a factor or an absolute value, but I
        # recommend being a factor because it is easier
        resizes = [1 for _ in video_handler.frames_time_moments]
        rotations = [0 for _ in video_handler.frames_time_moments]
        # Position must be, at first, a center position, and then
        # transformed into upper left corner position to be 
        # positioned
        positions = [('center', 'center') for _ in video_handler.frames_time_moments]

        # Functions that need to be processed frame by frame
        def modify_video_frame_by_frame(get_frame, t):
            """
            Modificate anything related to pixel colors, distortion,
            etc. and not to position, rotation or frame size.
            """
            frame = get_frame(t)
            frame_index = video_handler.frame_time_to_frame_index(t, video.fps)

            frame = ImageEditor.modify_color_temperature(frame, self._color_temperature[frame_index]) if self._color_temperature is not None else frame
            frame = ImageEditor.modify_brightness(frame, self._brightness[frame_index]) if self._brightness is not None else frame
            frame = ImageEditor.modify_contrast(frame, self._contrast[frame_index]) if self._contrast is not None else frame
            frame = ImageEditor.modify_sharpness(frame, self._sharpness[frame_index]) if self._sharpness is not None else frame
            frame = ImageEditor.modify_white_balance(frame, self._white_balance[frame_index]) if self._white_balance is not None else frame

            return frame
        
        # Apply frame by frame video modifications
        video = video.transform(lambda get_frame, t: modify_video_frame_by_frame(get_frame, t))

        # Functions that can be processed in the whole clip
        # TODO: Careful. Some of these modification can be
        # done before the video positioning or resizing, so
        # the behaviour could be unexpected.
        size = video.size
        if self.zoom is not None:
            size = (self.zoom / 100 * size[0], self.zoom / 100 * size[1])
        
            video = video.resized(size)
            # This is to force the size to be 1920x1080 instead
            # of other bigger values, but thiss does not make 
            # the clip render faster
            # from moviepy.video.fx.Crop import Crop
            # video = Crop(x_center = video.size[0] / 2, y_center = video.size[1] / 2, width = 1920, height = 1080).apply(video)

        # Apply position, rotation and resize frame by frame
        video = video.resized(lambda t: resizes[video_handler.frame_time_to_frame_index(t, video_handler.fps)])
        video = video.with_position(lambda t: positions[video_handler.frame_time_to_frame_index(t, video_handler.fps)])
        # TODO: There is a Rotate Effect for rotating... so we could
        # use it instead of this (?)
        video = video.rotated(lambda t: rotations[video_handler.frame_time_to_frame_index(t, video_handler.fps)])

        # Functions that changes the audio
        if self.volume != 100:
            video = video.with_volume_scaled(self.volume / 100)

        # Edit speed with speed factors (carefully)
        if PythonValidator.is_number(self.speed_factor):
            from yta_multimedia.video.edition.effect.fit_duration_effect import FitDurationEffect
            video = FitDurationEffect().apply(video, self.duration / self.speed_factor)
        elif PythonValidator.is_list(self.speed_factor):
            video = self._apply_speed_factor(video)

        # TODO: This below is repeated in VideoEditor class as
        # '._overlay_video()'
        return CompositeVideoClip([
            ClipGenerator.get_default_background_video(duration = video.duration),
            video
        ])#.with_audio(VideoAudioCombinator(audio_mode).process_audio(background_video, video))
    
    def write_videofile(self, output_filename: str):
        """
        Writes the video once it is processed to the provided
        'output_filename'.
        """
        # TODO: Validate 'output_filename'

        self.video_processed.write_videofile(output_filename)
    
    def copy(self):
        # TODO: Complete this method to manually copy the instance
        # because 'deepcopy' is not working properly
        copy = SubClip(self.video.copy())

        # The only thing we need to preserve is the values that
        # modify each attribute. The modifier instance is only
        # passed to generate these values, so that generator is
        # only necessary once to generate those values
        copy._color_temperature = self._color_temperature.copy() if self._color_temperature is not None else None
        copy._brightness = self._brightness.copy() if self._brightness is not None else None
        copy._contrast = self._contrast.copy() if self._contrast is not None else None
        copy._sharpness = self._sharpness.copy() if self._sharpness is not None else None
        copy._white_balance = self._white_balance.copy() if self._white_balance is not None else None
        copy._speed_factor = self._speed_factor.copy() if self._speed_factor is not None else None

        return copy

class SubClipOnTimelineLayer:
    """
    Class to represent one of our SubClips but in
    the general project timeline and in a specific
    layer of it, with the start and end moment in
    that timeline, and also the layer in which it
    is placed.

    TODO: This is a concept in test phase. SubClip
    is a more definitive concept.
    """
    subclip: SubClip = None
    start_time: float = None
    """
    The start time on the general project timeline. Do 
    not confuse this term with the start time of a
    moviepy clip.
    """

    @property
    def video_processed(self):
        return self.subclip.video_processed

    @property
    def duration(self):
        """
        Shortcut to the actual duration of the video once
        it's been processed.
        """
        return self.subclip.duration
    
    @property
    def size(self):
        """
        Shortcut to the actual size of the video once it's
        been processed.
        """
        return self.subclip.size
    
    @property
    def end_time(self):
        """
        The end moment on the timeline, based on this
        instance 'start_time' and the real video 'duration'.
        """
        return self.start_time + self.duration

    def __init__(self, subclip: SubClip, start_time: float):
        if not PythonValidator.is_instance(subclip, SubClip):
            raise Exception('The provided "subclip" parameter is not a valid SubClip instance.')
        
        if not NumberValidator.is_number_between(start_time, 0, END_OF_TIMELINE):
            raise Exception(f'The provided "start_time" parameter is not a valid number between in the range (0, {END_OF_TIMELINE})')
        
        self.subclip = subclip
        self.start_time = start_time

    # def _process(self):
    #     return self.subclip._process()

class TimelineLayerType(Enum):
    """
    The type of a timeline layer, which will determine
    which kind of SubClips are accepted by the layer
    with this type.
    """
    VIDEO = 'video'
    """
    The type of layer that only accept video SubClips.
    """
    AUDIO = 'audio'
    """
    The type of layer that only accept audio SubClips.
    """
    # TODO: Probably add 'GreenscreenLayer',
    # 'AlphascreenLayer', 'TextLayer', 'SubtitleLayer',
    # and all needed in a future when this concept 
    # evolves properly

class TimelineLayer:
    index: int = None
    type: TimelineLayerType = None
    _subclips: list[SubClipOnTimelineLayer] = None

    @property
    def subclips(self):
        """
        The list of subclips in this timeline layer, ordered
        according to its 'start_time' from first to be displayed
        to last ones.
        """
        return sorted(self._subclips, key = lambda subclip: subclip.start_time)
    
    @property
    def duration(self):
        """
        The duration of this timeline layer, which is the
        'end_time' of the last displayed subclip, or 0 if no
        clips.
        """
        return self.subclips[-1].end_time if self.subclips else 0
    
    @property
    def all_clips(self):
        """
        The list of all clips needed to fulfill the timeline
        layer completely. This involves the actual subclips
        but also the needed black background clips to put in
        the gaps between the subclips.
        """
        all_subclips = []
        current_time_moment = 0
        # TODO: This 'timeline_duration' must be calculated
        # according to all timeline layers, so the longest
        # one is the one we need to assign here
        timeline_duration = self.subclips[-1].end_time

        for subclip in self.subclips:
            # We fulfill the gap if existing
            if subclip.start_time > current_time_moment:
                all_subclips.append(ClipGenerator.get_default_background_video(subclip.size, subclip.start_time - current_time_moment))
            
            # We add the existing subclip
            all_subclips.append(subclip.video_processed)
            
            current_time_moment = subclip.end_time
        
        # Check if gap at the end due to other longer layers
        if current_time_moment < timeline_duration:
            all_subclips.append(ClipGenerator.get_default_background_video(subclip.size, timeline_duration - current_time_moment))
        
        return all_subclips

    def __init__(self, index: int = 0, type: TimelineLayerType = TimelineLayerType.VIDEO):
        _validate_layer_index(index)
        type = TimelineLayerType.to_enum(type) if type is not None else TimelineLayerType.VIDEO

        self.index = index
        self.type = type
        self._subclips = []

    def add_subclip(self, subclip: SubClip, start_time: float):
        """
        Append the provided 'subclip' at the end of the list.

        TODO: Being in the end of the list doesn't mean being
        the last one displayed. By now I'm storing them just
        one after another and ordering them when trying to get
        them as a property. This will change in a near future
        to be more eficient.
        """
        if not PythonValidator.is_instance(subclip, SubClip):
            raise Exception('The provided "subclip" parameter is not a valid instance of the SubClip class.')
        
        if not NumberValidator.is_number_between(start_time, 0, MAX_TIMELINE_LAYER_DURATION):
            raise Exception('The provided "start_time" is not a valid value')

        # 
        # TODO: Check that the 'start_time' or the 'duration'
        # doesn't collide with another existing subclip. If
        # yes, choose what strategy to follow
        if any(subclip.start_time <= start_time <= subclip.end_time for subclip in self.subclips):
            raise Exception(f'There is one existing subclip at the {str(start_time)} time position.')

        self._subclips.append(SubClipOnTimelineLayer(subclip, start_time))

    def remove_subclip(self, index: int):
        """
        Delete the subclip in the provided 'index' position of
        the list (if existing), or raises an Exception if it
        doesn't exist or the list is empty.
        """
        # TODO: Maybe remove by passing the instance (?)
        if PythonValidator.is_empty_list(self._subclips):
            # TODO: Maybe I should not raise an Exception here...
            raise Exception('No subclips to remove.')
        
        if not NumberValidator.is_number_between(0, len(self._subclips)):
            raise Exception(f'The provided "index" is not a valid index (must be between [0, {str(len(self._subclips))}).')

        # TODO: Be very careful, I have a 'subclips' property which
        # returns the subclips ordered, but the raw '_subclips'
        # property is not ordered, so here the 'index' is potentially
        # wrong. Think how to handle this in a near future, please.
        del self._subclips[index]

    def build(self):
        """
        Concatenate all the timeline layer subclips (fulfilling the
        gaps with black transparent background clips) and return the
        concatenated clip.
        """
        # TODO: What if I have one non-transparent and transparent
        # clips in this timeline layer? They will be treated in a
        # similar way so it is not the expected behaviour...
        return concatenate_videoclips(self.all_clips)
    
class VideoProject:
    """
    Class representing a whole but single video project
    in which we have a timeline with different layers
    and clips on them.
    """
    timeline_layers: list[TimelineLayer] = None
    screen_size: tuple[int, int] = None
    """
    Dimensions of the final video that has to be
    exported.
    """

    def __init__(self, screen_size: tuple[int, int] = (1920, 1080)):
        self.timeline_layers = [
            TimelineLayer(0, TimelineLayerType.VIDEO),
            # TODO: I Simplify everything by now and I only
            # handle one video layer
            #TimelineLayer(0, TimelineLayerType.AUDIO)
        ]
        # TODO: Validate 'screen_size'
        self.screen_size = screen_size

    def get_layers(self, type: TimelineLayerType) -> list[TimelineLayer]:
        """
        Get the timeline layers of the provided 'type' sorted by
        index in ascending order.
        """
        type = TimelineLayerType.to_enum(type)

        return sorted(
            [layer for layer in self.timeline_layers if layer.type == type], 
            key = lambda layer: layer.index
        )
    
    def get_last_layer_index(self, type: TimelineLayerType) -> Union[int, None]:
        """
        Get the last index used for the layers of the given
        'type', that will be None if no layers of that type.
        """
        type = TimelineLayerType.to_enum(type)

        layers = self.get_layers(type)

        return layers[-1:].index if not PythonValidator.is_empty_list(layers) else None

    def add_layer(self, type: TimelineLayerType = TimelineLayerType.VIDEO) -> int:
        """
        Add a new layer of the provided 'type' and returns
        the index in which it has been placed.
        """
        type = TimelineLayerType.to_enum(type) if type is not None else TimelineLayerType.VIDEO

        layers = self.get_layers(type)
        index = len(layers) + 1 if layers else 0

        self.timeline_layers.append(TimelineLayer(index, type))

        return index
    
    def remove_layer(self, layer: TimelineLayer):
        if not PythonValidator.is_instance(layer, TimelineLayer):
            raise Exception('The provided "layer" is not an instance of the TimelineLayer class.')
        
        if layer not in self.timeline_layers:
            raise Exception('The provided "layer" does not exist in this project.')

        self.timeline_layers.remove(layer)

    def build(self):
        # TODO: Omg, cyclic import issue here again...
        from yta_multimedia.video.edition.duration import set_video_duration, ExtendVideoMode
        # TODO: Remove this code below when this is done 
        # individually by each layer. By now I'm forcing
        # all layers clips to have the same duration as
        # the longest layer clip has, but must be done
        # using a general and common 'max_duration'
        # property that is not calculated here.
        layers_clips = [
            layer.build()
            for layer in self.timeline_layers
        ]
        max_duration = max(layer_clip.duration for layer_clip in layers_clips)
        layers_clips = [
            set_video_duration(layer_clip, max_duration, extend_mode = ExtendVideoMode.BLACK_TRANSPARENT_BACKGROUND)
            for layer_clip in layers_clips
        ]

        return CompositeVideoClip(layers_clips)





def subclip_video(video: Clip, start_time: float, end_time: float) -> tuple[Union[Clip, None], Clip, Union[Clip, None]]:
    """
    Subclip the provided 'video' into 3 different subclips,
    according to the provided 'start_time' and 'end_time',
    and return them as a tuple of those 3 clips. First and
    third clip could be None.

    The first clip will be None when 'start_time' is 0, and 
    the third one when the 'end_time' is equal to the given
    'video' duration.
    """
    video = VideoParser.to_moviepy(video)

    left = None if (start_time == 0 or start_time == None) else video.with_subclip(0, start_time)
    center = video.with_subclip(start_time, end_time)
    right = None if (end_time is None or end_time >= video.duration) else video.with_subclip(start_time = end_time)

    return left, center, right



# TODO: This must be maybe moved to another file
# because it is mixed with the 'subclip_video'
# method...
def _validate_layer_index(layer_index: int):
    if not NumberValidator.is_number_between(layer_index, LAYERS_INDEXES_LIMIT[0], LAYERS_INDEXES_LIMIT[1]):
        raise Exception(f'The provided "layer_index" is not a valid layer, it must be an int value between [{LAYERS_INDEXES_LIMIT[0]}, {LAYERS_INDEXES_LIMIT[1]}].')
    
def _validate_is_video_attribute_modifier_instance(element: SubClipAttributeModifier):
    if not PythonValidator.is_instance(element, SubClipAttributeModifier):
        raise Exception('The provided "element" parameter is not a SubClipAttributeModifier instance.')
    
def _validate_zoom(zoom: int):
    if not NumberValidator.is_number_between(zoom, ZOOM_LIMIT[0], ZOOM_LIMIT[1]):
        raise Exception(f'The "zoom" parameter provided is not a number between [{ZOOM_LIMIT[0]}, {ZOOM_LIMIT[1]}].')
    
def _validate_setting(setting: SubClipSetting, name: str, range: tuple[float, float]):
    if not PythonValidator.is_instance(setting, SubClipSetting):
        raise Exception(f'The provided "{name}" is not a SubClipSetting instance.')
    
    if not NumberValidator.is_number_between(setting.initial_value, range[0], range[1]):
        raise Exception(f'The "{name}" parameter provided "initial_value" is not a number between [{range[0]}, {range[1]}].')
    
    if not NumberValidator.is_number_between(setting.final_value, range[0], range[1]):
        raise Exception(f'The "{name}" parameter provided "final_value" is not a number between [{range[0]}, {range[1]}].')

def _validate_attribute_modifier(attribute_modifier: SubClipAttributeModifier, name: str, limit_range: tuple[float, float], number_of_frames: int):
    """
    Validate the provided 'attribute_modifier' according to
    the given 'limit_range' in which all the values must fit.
    Also, if it is a Graphic instance, the 'number_of_frames'
    will be used to generate the values and check them.
    """
    if not PythonValidator.is_instance(attribute_modifier, SubClipAttributeModifier):
        raise Exception(f'The parameter "{name}" provided is not a SubClipAttributeModifier instance.')
    
    if PythonValidator.is_list(attribute_modifier.modifier):
        # TODO: Validate all values
        if any(not NumberValidator.is_number_between(value, limit_range[0], limit_range[1]) for value in attribute_modifier.modifier):
            raise Exception(f'The parameter "{name}" provided has at least one value out of the limits [{limit_range[0]}, {limit_range[1]}]')
    elif PythonValidator.is_instance(attribute_modifier.modifier, SubClipSetting):
        if not NumberValidator.is_number_between(attribute_modifier.modifier.initial_value, limit_range[0], limit_range[1]):
            raise Exception(f'The parameter "{name}" provided "initial_value" is not a number between [{limit_range[0]}, {limit_range[1]}].')
        
        if not NumberValidator.is_number_between(attribute_modifier.modifier.final_value, limit_range[0], limit_range[1]):
            raise Exception(f'The parameter "{name}" provided "final_value" is not a number between [{limit_range[0]}, {limit_range[1]}].')
    elif PythonValidator.is_instance(attribute_modifier.modifier, 'Graphic'):
        # TODO: This is very agressive, according to the way
        # we join the pairs of nodes we could get outliers
        # that are obviously out of the limit range. Some
        # easing functions have values below 0 and over 1.
        if any(not NumberValidator.is_number_between(value, limit_range[0], limit_range[1]) for value in attribute_modifier.get_values(number_of_frames)):
            raise Exception(f'The parameter "{name}" provided has at least one value out of the limits [{limit_range[0]}, {limit_range[1]}]')


def _validate_volume(volume: int):
    if not NumberValidator.is_number_between(volume, VOLUME_LIMIT[0], VOLUME_LIMIT[1]):
        raise Exception(f'The "volume" parameter provided is not a number between [{VOLUME_LIMIT[0]}, {VOLUME_LIMIT[1]}].')