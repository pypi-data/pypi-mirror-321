from pathlib import Path

import numpy as np
from sox import Transformer as SoxTransformer

from sonusai.mixture.datatypes import AudioStatsMetrics
from sonusai.mixture.datatypes import AudioT


def _convert_str_with_factors_to_int(x: str) -> int:
    if "k" in x:
        return int(1000 * float(x.replace("k", "")))
    if "M" in x:
        return int(1000000 * float(x.replace("M", "")))
    return int(x)


def calc_audio_stats(audio: AudioT, win_len: float | None = None) -> AudioStatsMetrics:
    from sonusai.mixture import SAMPLE_RATE

    args = ["stats"]
    if win_len is not None:
        args.extend(["-w", str(win_len)])

    tfm = Transformer()

    _, _, out = tfm.build(
        input_array=audio,
        sample_rate_in=SAMPLE_RATE,
        output_filepath="-n",
        extra_args=args,
        return_output=True,
    )

    if out is None:
        raise SystemError("Call to sox failed")

    stats = {}
    lines = out.split("\n")
    for line in lines:
        split_line = line.split()
        if len(split_line) == 0:
            continue
        value = split_line[-1]
        key = " ".join(split_line[:-1])
        stats[key] = value

    return AudioStatsMetrics(
        dco=float(stats["DC offset"]),
        min=float(stats["Min level"]),
        max=float(stats["Max level"]),
        pkdb=float(stats["Pk lev dB"]),
        lrms=float(stats["RMS lev dB"]),
        pkr=float(stats["RMS Pk dB"]),
        tr=float(stats["RMS Tr dB"]),
        cr=float(stats["Crest factor"]),
        fl=float(stats["Flat factor"]),
        pkc=_convert_str_with_factors_to_int(stats["Pk count"]),
    )


class Transformer(SoxTransformer):
    """Override certain sox.Transformer methods"""

    def build(  # pyright: ignore [reportIncompatibleMethodOverride]
        self,
        input_filepath: str | Path | None = None,
        output_filepath: str | Path | None = None,
        input_array: np.ndarray | None = None,
        sample_rate_in: float | None = None,
        extra_args: list[str] | None = None,
        return_output: bool = False,
    ) -> tuple[bool, str | None, str | None]:
        """Given an input file or array, creates an output_file on disk by
        executing the current set of commands. This function returns True on
        success. If return_output is True, this function returns a triple of
        (status, out, err), giving the success state, along with stdout and
        stderr returned by sox.

        Parameters
        ----------
        input_filepath : str or None
            Either path to input audio file or None for array input.
        output_filepath : str
            Path to desired output file. If a file already exists at
            the given path, the file will be overwritten.
            If '-n', no file is created.
        input_array : np.ndarray or None
            An np.ndarray of an waveform with shape (n_samples, n_channels).
            sample_rate_in must also be provided.
            If None, input_filepath must be specified.
        sample_rate_in : int
            Sample rate of input_array.
            This argument is ignored if input_array is None.
        extra_args : list or None, default=None
            If a list is given, these additional arguments are passed to SoX
            at the end of the list of effects.
            Don't use this argument unless you know exactly what you're doing!
        return_output : bool, default=False
            If True, returns the status and information sent to stderr and
            stdout as a tuple (status, stdout, stderr).
            If output_filepath is None, return_output=True by default.
            If False, returns True on success.

        Returns
        -------
        status : bool
            True on success.
        out : str (optional)
            This is not returned unless return_output is True.
            When returned, captures the stdout produced by sox.
        err : str (optional)
            This is not returned unless return_output is True.
            When returned, captures the stderr produced by sox.

        Examples
        --------
        > import numpy as np
        > import sox
        > tfm = sox.Transformer()
        > sample_rate = 44100
        > y = np.sin(2 * np.pi * 440.0 * np.arange(sample_rate * 1.0) / sample_rate)

        file in, file out - basic usage

        > status = tfm.build('path/to/input.wav', 'path/to/output.mp3')

        file in, file out - equivalent usage

        > status = tfm.build(
                input_filepath='path/to/input.wav',
                output_filepath='path/to/output.mp3'
            )

        array in, file out

        > status = tfm.build(
                input_array=y, sample_rate_in=sample_rate,
                output_filepath='path/to/output.mp3'
            )

        """
        from sox import file_info
        from sox.core import SoxError
        from sox.core import sox
        from sox.log import logger

        input_format, input_filepath = self._parse_inputs(input_filepath, input_array, sample_rate_in)

        if output_filepath is None:
            raise ValueError("output_filepath is not specified!")

        # set output parameters
        if input_filepath == output_filepath:
            raise ValueError("input_filepath must be different from output_filepath.")
        file_info.validate_output_file(output_filepath)

        args = []
        args.extend(self.globals)
        args.extend(self._input_format_args(input_format))
        args.append(input_filepath)
        args.extend(self._output_format_args(self.output_format))
        args.append(output_filepath)
        args.extend(self.effects)

        if extra_args is not None:
            if not isinstance(extra_args, list):
                raise ValueError("extra_args must be a list.")
            args.extend(extra_args)

        status, out, err = sox(args, input_array, True)
        if status != 0:
            raise SoxError(f"Stdout: {out}\nStderr: {err}")

        logger.info("Created %s with effects: %s", output_filepath, " ".join(self.effects_log))

        if return_output:
            return status, out, err  # pyright: ignore [reportReturnType]

        return True, None, None

    def build_array(  # pyright: ignore [reportIncompatibleMethodOverride]
        self,
        input_filepath: str | Path | None = None,
        input_array: np.ndarray | None = None,
        sample_rate_in: int | None = None,
        extra_args: list[str] | None = None,
    ) -> np.ndarray:
        """Given an input file or array, returns the output as a numpy array
        by executing the current set of commands. By default, the array will
        have the same sample rate as the input file unless otherwise specified
        using set_output_format. Functions such as channels and convert
        will be ignored!

        The SonusAI override does not generate a warning for rate transforms.

        Parameters
        ----------
        input_filepath : str, Path or None
            Either path to input audio file or None.
        input_array : np.ndarray or None
            A np.ndarray of a waveform with shape (n_samples, n_channels).
            If this argument is passed, sample_rate_in must also be provided.
            If None, input_filepath must be specified.
        sample_rate_in : int
            Sample rate of input_array.
            This argument is ignored if input_array is None.
        extra_args : list or None, default=None
            If a list is given, these additional arguments are passed to SoX
            at the end of the list of effects.
            Don't use this argument unless you know exactly what you're doing!

        Returns
        -------
        output_array : np.ndarray
            Output audio as a numpy array

        Examples
        --------

        > import numpy as np
        > import sox
        > tfm = sox.Transformer()
        > sample_rate = 44100
        > y = np.sin(2 * np.pi * 440.0 * np.arange(sample_rate * 1.0) / sample_rate)

        file in, array out

        > output_array = tfm.build(input_filepath='path/to/input.wav')

        array in, array out

        > output_array = tfm.build(input_array=y, sample_rate_in=sample_rate)

        specifying the output sample rate

        > tfm.set_output_format(rate=8000)
        > output_array = tfm.build(input_array=y, sample_rate_in=sample_rate)

        if an effect changes the number of channels, you must explicitly
        specify the number of output channels

        > tfm.remix(remix_dictionary={1: [1], 2: [1], 3: [1]})
        > tfm.set_output_format(channels=3)
        > output_array = tfm.build(input_array=y, sample_rate_in=sample_rate)


        """
        from sox.core import SoxError
        from sox.core import sox
        from sox.log import logger
        from sox.transform import ENCODINGS_MAPPING

        input_format, input_filepath = self._parse_inputs(input_filepath, input_array, sample_rate_in)

        # check if any of the below commands are part of the effects chain
        ignored_commands = ["channels", "convert"]
        if set(ignored_commands) & set(self.effects_log):
            logger.warning(
                "When outputting to an array, channels and convert "
                + "effects may be ignored. Use set_output_format() to "
                + "specify output formats."
            )

        output_filepath = "-"

        if input_format.get("file_type") is None:
            encoding_out = np.int16
        else:
            encoding_out = next(k for k, v in ENCODINGS_MAPPING.items() if input_format["file_type"] == v)

        n_bits = np.dtype(encoding_out).itemsize * 8

        output_format = {
            "file_type": "raw",
            "rate": sample_rate_in,
            "bits": n_bits,
            "channels": input_format["channels"],
            "encoding": None,
            "comments": None,
            "append_comments": True,
        }

        if self.output_format.get("rate") is not None:
            output_format["rate"] = self.output_format["rate"]

        if self.output_format.get("channels") is not None:
            output_format["channels"] = self.output_format["channels"]

        if self.output_format.get("bits") is not None:
            n_bits = self.output_format["bits"]
            output_format["bits"] = n_bits

        match n_bits:
            case 8:
                encoding_out = np.int8  # type: ignore[assignment]
            case 16:
                encoding_out = np.int16
            case 32:
                encoding_out = np.float32  # type: ignore[assignment]
            case 64:
                encoding_out = np.float64  # type: ignore[assignment]
            case _:
                raise ValueError(f"invalid n_bits {n_bits}")

        args = []
        args.extend(self.globals)
        args.extend(self._input_format_args(input_format))
        args.append(input_filepath)
        args.extend(self._output_format_args(output_format))
        args.append(output_filepath)
        args.extend(self.effects)

        if extra_args is not None:
            if not isinstance(extra_args, list):
                raise ValueError("extra_args must be a list.")
            args.extend(extra_args)

        status, out, err = sox(args, input_array, False)
        if status != 0:
            raise SoxError(f"Stdout: {out}\nStderr: {err}")

        out = np.frombuffer(out, dtype=encoding_out)  # pyright: ignore [reportArgumentType, reportCallIssue]
        if output_format["channels"] > 1:
            out = out.reshape(
                (output_format["channels"], int(len(out) / output_format["channels"])),
                order="F",
            ).T
        logger.info("Created array with effects: %s", " ".join(self.effects_log))

        return out
