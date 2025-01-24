from sonusai.mixture.datatypes import AudioT
from sonusai.mixture.datatypes import Augmentation
from sonusai.mixture.datatypes import AugmentationEffects
from sonusai.mixture.datatypes import AugmentationRule
from sonusai.mixture.datatypes import ImpulseResponseData
from sonusai.mixture.datatypes import OptionalNumberStr
from sonusai.mixture.mixdb import MixtureDatabase


def get_augmentation_rules(rules: list[dict] | dict, num_ir: int = 0) -> list[AugmentationRule]:
    """Generate augmentation rules from list of input rules

    :param rules: Dictionary of augmentation config rule[s]
    :param num_ir: Number of impulse responses in config
    :return: List of augmentation rules
    """
    from sonusai.utils import dataclass_from_dict

    from .datatypes import AugmentationRule

    processed_rules: list[dict] = []
    if not isinstance(rules, list):
        rules = [rules]

    for rule in rules:
        rule = _parse_ir(rule, num_ir)
        processed_rules = _expand_rules(expanded_rules=processed_rules, rule=rule)

    return [dataclass_from_dict(AugmentationRule, processed_rule) for processed_rule in processed_rules]  # pyright: ignore [reportReturnType]


def _expand_rules(expanded_rules: list[dict], rule: dict) -> list[dict]:
    """Expand rules

    :param expanded_rules: Working list of expanded rules
    :param rule: Rule to process
    :return: List of expanded rules
    """
    from copy import deepcopy

    from sonusai.utils import convert_string_to_number

    from .constants import VALID_AUGMENTATIONS
    from .eq_rule_is_valid import eq_rule_is_valid

    if "pre" not in rule:
        raise ValueError("Rule must have 'pre' key")

    if "post" not in rule:
        rule["post"] = {}

    for key in rule:
        if key not in ("pre", "post", "mixup"):
            raise ValueError(f"Invalid augmentation key: {key}")

        if key in ("pre", "post"):
            for k, v in list(rule[key].items()):
                if v is None:
                    del rule[key][k]

    # replace old 'eq' rule with new 'eq1' rule to allow both for backward compatibility
    for key in rule:
        rule[key] = {"eq1" if k == "eq" else k: v for k, v in rule[key].items()}

    for key in ("pre", "post"):
        for k in rule[key]:
            if k not in VALID_AUGMENTATIONS:
                nice_list = "\n".join([f"  {item}" for item in VALID_AUGMENTATIONS])
                raise ValueError(f"Invalid augmentation: {k}.\nValid augmentations are:\n{nice_list}")

            if k in ["eq1", "eq2", "eq3"]:
                if not eq_rule_is_valid(rule[key][k]):
                    raise ValueError(f"Invalid augmentation value for {k}: {rule[key][k]}")

                if all(isinstance(el, list) or (isinstance(el, str) and el == "none") for el in rule[key][k]):
                    # Expand multiple rules
                    for value in rule[key][k]:
                        expanded_rule = deepcopy(rule)
                        if isinstance(value, str) and value == "none":
                            expanded_rule[key][k] = None
                        else:
                            expanded_rule[key][k] = deepcopy(value)
                        _expand_rules(expanded_rules, expanded_rule)
                    return expanded_rules

            else:
                if isinstance(rule[key][k], list):
                    for value in rule[key][k]:
                        if isinstance(value, list):
                            raise TypeError(f"Invalid augmentation value for {k}: {rule[key][k]}")
                        expanded_rule = deepcopy(rule)
                        expanded_rule[key][k] = deepcopy(value)
                        _expand_rules(expanded_rules, expanded_rule)
                    return expanded_rules
                else:
                    rule[key][k] = convert_string_to_number(rule[key][k])
                    if not (
                        isinstance(rule[key][k], float | int)
                        or rule[key][k].startswith("rand")
                        or rule[key][k] == "none"
                    ):
                        raise ValueError(f"Invalid augmentation value for {k}: {rule[key][k]}")

    expanded_rules.append(rule)
    return expanded_rules


def _generate_none_rule(rule: dict) -> dict:
    """Generate a new rule from a rule that contains 'none' directives

    :param rule: Rule
    :return: New rule
    """
    from copy import deepcopy

    out_rule = deepcopy(rule)
    for key in out_rule:
        if out_rule[key] == "none":
            out_rule[key] = None

    return out_rule


def _generate_random_rule(rule: dict, num_ir: int = 0) -> dict:
    """Generate a new rule from a rule that contains 'rand' directives

    :param rule: Rule
    :param num_ir: Number of impulse responses in config
    :return: Randomized rule
    """
    from copy import deepcopy
    from random import randint

    out_rule = deepcopy(rule)
    for key in ("pre", "post"):
        for k in out_rule[key]:
            if k == "ir" and out_rule[key][k] == "rand":
                # IR is special case
                if num_ir == 0:
                    out_rule[key][k] = None
                else:
                    out_rule[key][k] = randint(0, num_ir - 1)  # noqa: S311
            else:
                out_rule[key][k] = evaluate_random_rule(str(out_rule[key][k]))

            # convert EQ values from strings to numbers
            if k in ("eq1", "eq2", "eq3"):
                for n in range(3):
                    if isinstance(out_rule[key][k][n], str):
                        out_rule[key][k][n] = eval(out_rule[key][k][n])  # noqa: S307

    return out_rule


def _rule_has_rand(rule: dict) -> bool:
    """Determine if any keys in the given rule contain 'rand'

    :param rule: Rule
    :return: True if rule contains 'rand'
    """
    return any("rand" in str(rule[key][k]) for key in rule for k in rule[key])


def estimate_augmented_length_from_length(length: int, tempo: OptionalNumberStr = None, frame_length: int = 1) -> int:
    """Estimate the length of audio after augmentation

    :param length: Number of samples in audio
    :param tempo: Tempo rule
    :param frame_length: Pad resulting audio to be a multiple of this
    :return: Estimated length of augmented audio
    """
    import numpy as np

    if tempo is not None:
        length = int(np.round(length / float(tempo)))

    length = _get_padded_length(length, frame_length)

    return length


def get_mixups(augmentations: list[AugmentationRule]) -> list[int]:
    """Get a list of mixup values used

    :param augmentations: List of augmentations
    :return: List of mixup values used
    """
    return sorted({augmentation.mixup for augmentation in augmentations})


def get_augmentation_indices_for_mixup(augmentations: list[AugmentationRule], mixup: int) -> list[int]:
    """Get a list of augmentation indices for a given mixup value

    :param augmentations: List of augmentations
    :param mixup: Mixup value of interest
    :return: List of augmentation indices
    """
    indices = []
    for idx, augmentation in enumerate(augmentations):
        if mixup == augmentation.mixup:
            indices.append(idx)

    return indices


def pad_audio_to_frame(audio: AudioT, frame_length: int = 1) -> AudioT:
    """Pad audio to be a multiple of frame length

    :param audio: Audio
    :param frame_length: Pad resulting audio to be a multiple of this
    :return: Padded audio
    """
    return pad_audio_to_length(audio, _get_padded_length(len(audio), frame_length))


def _get_padded_length(length: int, frame_length: int) -> int:
    """Get the number of pad samples needed

    :param length: Length of audio
    :param frame_length: Desired length will be a multiple of this
    :return: Padded length
    """
    mod = int(length % frame_length)
    pad_length = frame_length - mod if mod else 0
    return length + pad_length


def pad_audio_to_length(audio: AudioT, length: int) -> AudioT:
    """Pad audio to given length

    :param audio: Audio
    :param length: Length of output
    :return: Padded audio
    """
    import numpy as np

    return np.pad(array=audio, pad_width=(0, length - len(audio)))


def apply_gain(audio: AudioT, gain: float) -> AudioT:
    """Apply gain to audio

    :param audio: Audio
    :param gain: Amount of gain
    :return: Adjusted audio
    """
    return audio * gain


def evaluate_random_rule(rule: str) -> str | float:
    """Evaluate 'rand' directive

    :param rule: Rule
    :return: Resolved value
    """
    import re
    from random import uniform

    from .constants import RAND_PATTERN

    def rand_repl(m):
        return f"{uniform(float(m.group(1)), float(m.group(4))):.2f}"  # noqa: S311

    return eval(re.sub(RAND_PATTERN, rand_repl, rule))  # noqa: S307


def _parse_ir(rule: dict, num_ir: int) -> dict:
    from .helpers import generic_ids_to_list

    def _resolve_str(rule_in: str) -> str | list[int]:
        if rule_in in ["rand", "none"]:
            return rule_in

        rule_out = generic_ids_to_list(num_ir, rule_in)
        if not all(ro in range(num_ir) for ro in rule_out):
            raise ValueError(f"Invalid ir entry of {rule_in}")
        return rule_out

    def _process(rule_in: dict) -> dict:
        if "ir" not in rule_in:
            return rule_in

        ir = rule_in["ir"]

        if ir is None:
            return rule_in

        if isinstance(ir, str):
            rule_in["ir"] = _resolve_str(ir)
            return rule_in

        if isinstance(ir, list):
            rule_in["ir"] = []
            for item in ir:
                result = _resolve_str(item)
                if isinstance(result, str):
                    rule_in["ir"].append(_resolve_str(item))
                else:
                    rule_in["ir"] += _resolve_str(item)

            return rule_in

        if isinstance(ir, int):
            if ir not in range(num_ir):
                raise ValueError(f"Invalid ir of {ir}")
            return rule_in

        raise ValueError(f"Invalid ir of {ir}")

    for key in rule:
        if key in ("pre", "post"):
            rule[key] = _process(rule[key])

    return rule


def apply_augmentation(
    mixdb: MixtureDatabase,
    audio: AudioT,
    augmentation: AugmentationEffects,
    frame_length: int = 1,
) -> AudioT:
    """Apply augmentations to audio data using torchaudio.sox_effects

    :param mixdb: Mixture database
    :param audio: Audio
    :param augmentation: Augmentation
    :param frame_length: Pad resulting audio to be a multiple of this
    :return: Augmented audio
    """
    import numpy as np
    import torch
    import torchaudio

    from .audio import read_ir
    from .constants import SAMPLE_RATE

    effects: list[list[str]] = []

    # TODO: Always normalize and remove normalize from list of available augmentations
    # Normalize to globally set level (should this be a global config parameter, or hard-coded into the script?)
    # TODO: Support all sox effects supported by torchaudio (torchaudio.sox_effects.effect_names())
    if augmentation.normalize is not None:
        effects.append(["norm", str(augmentation.normalize)])

    if augmentation.gain is not None:
        effects.append(["gain", str(augmentation.gain)])

    if augmentation.pitch is not None:
        effects.append(["pitch", str(augmentation.pitch)])
        effects.append(["rate", str(SAMPLE_RATE)])

    if augmentation.tempo is not None:
        effects.append(["tempo", "-s", str(augmentation.tempo)])

    if augmentation.eq1 is not None:
        effects.append(["equalizer", *[str(item) for item in augmentation.eq1]])

    if augmentation.eq2 is not None:
        effects.append(["equalizer", *[str(item) for item in augmentation.eq2]])

    if augmentation.eq3 is not None:
        effects.append(["equalizer", *[str(item) for item in augmentation.eq3]])

    if augmentation.lpf is not None:
        effects.append(["lowpass", "-2", str(augmentation.lpf), "0.707"])

    if effects:
        if audio.ndim == 1:
            audio = np.reshape(audio, (1, audio.shape[0]))
        out = torch.tensor(audio)

        try:
            out, _ = torchaudio.sox_effects.apply_effects_tensor(out, sample_rate=SAMPLE_RATE, effects=effects)
        except Exception as e:
            raise RuntimeError(f"Error applying {augmentation}: {e}") from e

        audio_out = np.squeeze(np.array(out))
    else:
        audio_out = audio

    if augmentation.ir is not None:
        audio_out = apply_impulse_response(
            audio=audio_out,
            ir=read_ir(
                name=mixdb.impulse_response_file(augmentation.ir),  # pyright: ignore [reportArgumentType]
                delay=mixdb.impulse_response_delay(augmentation.ir),  # pyright: ignore [reportArgumentType]
                use_cache=mixdb.use_cache,
            ),
        )

    # make sure length is multiple of frame_length
    return pad_audio_to_frame(audio=audio_out, frame_length=frame_length)


def apply_impulse_response(audio: AudioT, ir: ImpulseResponseData) -> AudioT:
    """Apply impulse response to audio data using scipy

    :param audio: Audio
    :param ir: Impulse response data
    :return: Augmented audio
    """
    import numpy as np
    from librosa import resample
    from scipy.signal import fftconvolve

    from .constants import SAMPLE_RATE

    # Early exit if no ir or if all audio is zero
    if ir is None or not audio.any():
        return audio

    # Convert audio to IR sample rate
    audio_in = resample(audio, orig_sr=SAMPLE_RATE, target_sr=ir.sample_rate, res_type="soxr_hq")
    max_in = np.max(np.abs(audio_in))

    # Apply IR
    audio_out = fftconvolve(audio_in, ir.data, mode="full")

    # Delay compensation
    audio_out = audio_out[ir.delay :]

    # Convert back to global sample rate
    audio_out = resample(audio_out, orig_sr=ir.sample_rate, target_sr=SAMPLE_RATE, res_type="soxr_hq")

    # Trim to length
    audio_out = audio_out[: len(audio)]
    max_out = np.max(np.abs(audio_out))

    compensation_gain = max_in / max_out

    return audio_out * compensation_gain


def augmentation_from_rule(rule: AugmentationRule, num_ir: int) -> Augmentation:
    from sonusai.utils import dataclass_from_dict

    processed_rule = rule.to_dict()
    del processed_rule["mixup"]
    processed_rule = _generate_none_rule(processed_rule)
    if _rule_has_rand(processed_rule):
        processed_rule = _generate_random_rule(processed_rule, num_ir)

    return dataclass_from_dict(Augmentation, processed_rule)  # pyright: ignore [reportReturnType]
