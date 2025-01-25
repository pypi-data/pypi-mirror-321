class VideoFrameTHelper:
    """
    Class to simplify and encapsulate the conversion
    between video and audio time frame moments 't' and
    frame indexes.
    """
    @staticmethod
    def get_video_frame_t_base(t: float, video_fps: float):
        """
        Turn the provided 't' video frame time moment to
        the real base one (the one who is the start of
        the frame time interval, plus a minimum quantity
        to avoid floating point number issues).
        """
        return round(t * video_fps) / video_fps + 0.000001

    @staticmethod
    def get_video_audio_frame_t_base(t: float, audio_fps: float):
        """
        Get the video audio frame 't' time moment base,
        which is the left (lower) limit of that 't' time
        moment.

        As a reminder, any 't' time moment goes from the
        lower limit (including it) to the upper limit 
        (not included). So, there is a time interval in 
        which any 't' time moment is included, which is
        defined by the range [lower_limit, upper_limit).

        For example, in a video with fps=30, any value
        between [0/30, 1/30) will be recognized as a 't'
        time moment for the frame index 0. As you can see,
        the 1/30 is not included, because it will be part
        of the next index, as it is its lower limit that
        is included.
        """
        return VideoFrameTHelper.get_video_frame_t_base(t, audio_fps)

    @staticmethod
    def get_video_frame_index_from_video_frame_t(t: float, video_fps: float):
        """
        Get the video frame index from the given video
        frame 't' time moment.
        """
        return int(VideoFrameTHelper.get_video_frame_t_base(t, video_fps) * video_fps)

    @staticmethod
    def get_video_audio_frame_index_from_video_audio_frame_t(t: float, audio_fps: float):
        """
        Get the video audio frame index from the given 
        video audio frame 't' time moment.
        """
        return VideoFrameTHelper.get_video_frame_index_from_video_frame_t(t, audio_fps)
    
    @staticmethod
    def get_video_frame_t_from_video_frame_index(index: float, video_fps: float):
        """
        Get the video frame 't' time moment from the
        given video frame index.
        """
        return index * (1 / video_fps) + 0.000001
    
    @staticmethod
    def get_video_audio_frame_t_from_video_audio_frame_index(index: float, audio_fps):
        return VideoFrameTHelper.get_video_frame_t_from_video_frame_index(index, audio_fps)
    
    @staticmethod
    def get_video_audio_tts_from_video_frame_t(t: float, video_fps: float, audio_fps: float):
        """
        Get all the audio time moments associated to
        the given 'video' 't' time moment, as an array.

        One video time moment 't' is associated with a lot
        of video audio time 't' time moments. The amount 
        of video audio frames per video frame is calculated
        with the divions of the audio fps by the video fps.

        The result is an array of 't' video audio time
        moments. Maybe you need to turn it into a numpy
        array before using it as audio 't' time moments.
        """
        from yta_general_utils.math.progression import Progression

        audio_frames_per_video_frame = int(audio_fps / video_fps)
        audio_frame_duration = 1 / audio_fps
        video_frame_duration = 1 / video_fps

        t = VideoFrameTHelper.get_video_frame_t_base(t, video_fps)

        return Progression(t, t + video_frame_duration - audio_frame_duration, audio_frames_per_video_frame).values

    @staticmethod
    def get_video_frame_t_from_video_audio_frame_t(t: float, video_fps: float):
        """
        Get the video frame 't' time moment associated with
        the given video audio 't' time moment.
        """
        video_frame_duration = 1 / video_fps

        # Convert audio t in video t
        t = t // video_frame_duration * video_frame_duration + 0.000001

        return VideoFrameTHelper.get_video_frame_t_base(t, video_fps)
    
    @staticmethod
    def get_video_frame_t_from_video_audio_frame_index(index: int, video_fps: float, audio_fps: float):
        """
        Get the video frame 't' time moment from the video
        audio frame index.
        """
        return VideoFrameTHelper.get_video_frame_t_from_video_audio_frame_t(
            VideoFrameTHelper.get_video_audio_frame_t_from_video_audio_frame_index(index, audio_fps),
            video_fps
        )
    
    @staticmethod
    def get_video_frame_index_from_video_audio_frame_index(index: int, video_fps: float, audio_fps: float):
        """
        Get the video frame index from the video audio frame
        index.
        """
        return VideoFrameTHelper.get_video_frame_index_from_video_frame_t(
            VideoFrameTHelper.get_video_frame_t_from_video_audio_frame_index(
                index,
                video_fps,
                audio_fps
            ),
            video_fps
        )
    
    @staticmethod
    def get_video_frame_index_from_video_audio_frame_t(t: int, video_fps: float):
        """
        Get the video frame index from the video audio frame
        't' time moment.
        """
        return VideoFrameTHelper.get_video_frame_index_from_video_frame_t(
            VideoFrameTHelper.get_video_frame_t_from_video_audio_frame_t(
                t,
                video_fps,
            )
        )
