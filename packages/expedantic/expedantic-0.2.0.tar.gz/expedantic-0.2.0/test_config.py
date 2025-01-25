import inspect
import warnings
from argparse import ArgumentParser
from inspect import Parameter
from pathlib import Path
from typing import Any, Literal, Type, Annotated, Callable, TypeAlias


import numpy as np
import pydantic
import pydantic_yaml
from pydantic.functional_validators import (
    AfterValidator,
    PlainValidator,
    BeforeValidator,
)
from pydantic.functional_serializers import WrapSerializer

from expedantic import ConfigBase


EMPTY = Parameter.empty
POS_ONLY = Parameter.POSITIONAL_ONLY


def get_kwargs(cls: Type):
    signature = inspect.signature(cls)
    kw_args = {
        k: (
            v.annotation if v.annotation != EMPTY else Any,
            v.default if v.default != EMPTY else ...,
        )
        for k, v in signature.parameters.items()
        if v.kind != POS_ONLY
    }
    return kw_args


def is_np_dtype_str(s: str):
    try:
        dt = np.dtype(s)
    except TypeError:
        raise
    return str(dt)


Schedule: TypeAlias = Callable[[float], float]


class LinearSchedule:
    def __init__(
        self, start: float, end: float = 0.0, end_fraction: float = 1.0
    ) -> None:
        self.start = start
        self.end = end
        self.end_fraction = end_fraction
        self.ratio = (self.end - self.start) / self.end_fraction

    def __call__(self, progress_remaining: float) -> float:
        if (1 - progress_remaining) > self.end_fraction:
            return self.end
        else:
            return self.start + (1 - progress_remaining) * self.ratio

    def __repr__(self) -> str:
        if self.end == 0.0 and self.end_fraction == 1.0:
            return f"lin_{self.start}"
        else:
            return f"lin_{self.start}_{self.end}_{self.end_fraction}"


class ConstantSchedule:
    def __init__(self, value: float):
        self.value = value

    def __call__(self, _) -> float:
        return self.value

    def __repr__(self) -> str:
        return str(self.value)


def schedule_to_str(schedule: LinearSchedule | ConstantSchedule):
    return repr(schedule)


def get_schedule(s: str) -> Callable[[float], float]:
    try:
        value = float(s)
    except ValueError:
        pass
    else:
        return ConstantSchedule(value)

    if not s.startswith("lin_"):
        raise ValueError(f"Invalid schedule string {s}. It must starts with 'lin'.")

    s = s.replace("lin_", "")
    value = float(s)

    return LinearSchedule(value)


def flatten_uniques(nested: dict) -> dict[str, Any]:
    flattened: dict[str, Any] = {}
    for k, v in nested.items():
        if isinstance(v, dict):
            inner = flatten_uniques(v)
            duplicates = set(flattened.keys()) & set(inner.keys())
            if len(duplicates) > 0:
                warnings.warn(
                    f"[flatten_uniques] key{'s' if len(duplicates) > 1 else ''} {duplicates} are not unique; omitted."
                )
                for key in duplicates:
                    inner.pop(key)
                    flattened.pop(key)
            flattened.update(inner)
        else:
            flattened[k] = v

    return flattened


NPDtype = Annotated[str, AfterValidator(is_np_dtype_str)]

# MaybeSchedule = Annotated[Schedule | float, PlainValidator(get_schedule)]
MaybeSchedule = Annotated[
    Schedule | float, BeforeValidator(get_schedule), WrapSerializer(schedule_to_str)
]


SupportedEnv = Literal[
    "ClimberEasy-v0",
    "CoinrunEasy-v0",
    "BigfishEasy-v0",
    "MinerEasy-v0",
    "CaveflyerEasy-v0",
    "StarpilotEasy-v0",
    "JumperEasy-v0",
    "NinjaEasy-v0",
    "PlunderEasy-v0",
    "FruitbotEasy-v0",
    "LeaperEasy-v0",
    "HeistEasy-v0",
    "DodgeballEasy-v0",
    "BossfightEasy-v0",
    "MazeEasy-v0",
    "ChaserEasy-v0",
    "CartPole-v1",
    "Ant-v4",
    "HalfCheetah-v4",
    "Hopper-v4",
    "Humanoid-v4",
    "HumanoidStandup-v4",
    "InvertedDoublePendulum-v4",
    "Pusher-v4",
    "Reacher-v4",
    "Swimmer-v4",
    "Walker2d-v4",
    "MiniGrid-DoorKey-5x5-v0",
    "MiniGrid-DoorKey-6x6-v0",
    "MiniGrid-DoorKey-8x8-v0",
    "MiniGrid-DoorKey-16x16-v0",
    "MiniGrid-Empty-8x8-v0",
    "Breakout-v5",
    "MontezumaRevenge-v5",
    "FrozenLake8x8-v1",
    "Taxi-v3",
]


class PPOConfig(ConfigBase):
    learning_rate: float = 3e-4
    adam_eps: float = 1e-5
    n_steps: int = 2048
    n_envs: int
    batch_size: int = 64
    n_epochs: int = 10
    gamma: float = 0.99
    gae_lambda: float = 0.95
    clip_range: float = 0.2
    clip_range_vf: float | None = None
    normalize_advantage: bool = True
    ent_coef: float = 0.0
    vf_coef: float = 0.5
    max_grad_norm: float = 0.5
    use_sde: bool = False
    sde_sample_freq: int = 0
    tensorboard_log: str | None = None
    policy_kwargs: dict[str, Any] = {}
    use_kl_penalty: bool = False
    use_reverse_kl_penalty: bool = False
    kl_beta: float = 4.0


class PPGConfig(ConfigBase):
    n_iteration: int = 32
    e_policy: int = 1
    v_value: int = 1
    e_auxiliary: int = 6
    beta_clone: float = 1.0
    num_aux_rollouts: int = 4
    n_aux_grad_accum: int = 1
    adv_norm_fullbatch: bool = True
    num_minibatches: int = 8
    mode: Literal["detach", "single"] = "detach"
    ppg_target_kl: float | None = None
    alternative_value_regularisation: bool = False


class TRPOConfig(ConfigBase):
    cg_max_steps: int = 15
    cg_damping: float = 0.1
    line_search_shrinking_factor: float = 0.8
    line_search_max_iter: int = 10
    n_critic_updates: int = 10
    sub_sampling_factor: int = 1
    target_kl: float = 0.01
    trpo_reverse_kl: bool = True


class EAPOConfig(ConfigBase):
    use_entropy_advantage: bool = True
    augmented_reward: bool = False
    tau: float = 0.01
    c2: float = 0.5
    e_gamma: float | None = None
    e_lambda: float | None = None
    eta_policy: float = 1.0
    eta_aux: float = 0.1
    ea_coef: float = 1.0
    tau_on_entropy: bool = False
    no_popart_for_entropy: bool = False
    use_exact_entropy: bool = False
    use_combined_return: bool = False
    chemical_potential: float = 0.0
    apply_ratio: bool = False
    escort_transform: bool = False
    use_shared_entropy_net: bool = True
    et_p: float = 2.0
    auto_t: bool = False
    auto_t_lr: float = 5.0e-4
    auto_t_min: float = 0.005


class CPConfig(ConfigBase):
    n_step_lambda: float = 0.8
    n_step_vf_coef: float = 0.5
    n_step_v_net_arch: list[int] = [64, 64]
    average_reward: bool = False


class HPConfig(ConfigBase):
    h_lambda: float = 0.9
    ha_coef: float = 0.1
    hf_coef: float = 1.0


class ARConfig(ConfigBase):
    use_weighted_average: bool = True
    r_step_size: float = 0.001
    use_trace_for_weighted_average: bool = True
    use_advantage: bool = False
    state_dependent_rho: bool = False
    rho_lr: float | None = None


class TestDeep(ConfigBase):
    class Deeper(ConfigBase):
        class DEEP(ConfigBase):
            apple: bool = True

        orange: bool = False

    deeper: Deeper = Deeper()


class Config(ConfigBase):
    deeeeep: TestDeep = TestDeep()
    device: str = "auto"
    obs_dtype: NPDtype = "float32"
    seed: int | None = None
    num_exp: int = 5

    verbose: int = 1
    eval_verbose: int = 1
    progress_bar: bool = False

    env: SupportedEnv = "BigfishEasy-v0"
    algo: Literal[
        "PPO",
        "PPG",
        "SAC",
        "EAPO_PPO",
        "EAPO_PPG",
        "EAPO_TRPO",
        "EAPO_ARPPO",
        "CPPPO",
        "ARPPO",
        "HPPPO",
    ] = "EAPO_PPO"
    total_timesteps: int = 25_000_000

    # Algorithm Configs
    ppo_config: PPOConfig
    ppg_config: PPGConfig = PPGConfig()
    trpo_config: TRPOConfig = TRPOConfig()
    eapo_config: EAPOConfig = EAPOConfig()
    cp_config: CPConfig = CPConfig()
    hp_config: HPConfig = HPConfig()
    ar_config: ARConfig = ARConfig()

    pop_art: bool = False
    pop_art_beta: float = 3.0e-4
    handle_timeout: bool = False

    # Env
    norm_obs: bool = False
    norm_reward: bool = False
    norm_obs_clip_range: float = 10.0
    norm_rew_clip_range: float = 10.0
    procgen: bool = False
    procgen_train_num_levels: int = 200
    procgen_eval_num_levels: int = 0
    use_subproc_envs: bool = True
    minigrid: bool = False
    action_discretization: bool = False
    discretization_num_atomics: int = 7
    env_kwargs: dict[str, Any] = {}
    eval_env_kwargs: dict[str, Any] | None = None
    continuing_env: bool = False
    random_truncation: float = 0.0
    termination_cost: float = -1000.0
    absorbing_goal_state: bool = False

    # Evaluation
    n_eval_episodes: int = 100
    n_eval_envs: int = 32
    eval_freq: int = 1000
    eval_deterministic: bool = False
    prediction_temperatures: list[float] = []
    save_model: bool = False
    save_freq: int | None = None

    use_wandb: bool = False
    project: str = "EAPO"
    group: str | None = None
    entity: str | None = None

    def model_post_init(self, _context):
        super().model_post_init(_context)
        if self.group:
            flattened = flatten_uniques(self.model_dump())
            self.group = self.group.format_map(flattened)


def load_config(path: Path | str | None = None):
    path = path or "cfgs/default.yaml"
    return pydantic_yaml.parse_yaml_file_as(Config, path)


if __name__ == "__main__":
    parser = ArgumentParser()
    parser.add_argument("--generate_schema", action="store_true")
    args = parser.parse_args()

    if args.generate_schema:
        import json
        from pathlib import Path

        path = Path("schemas/config.json")
        path.parent.mkdir(exist_ok=True)
        json.dump(Config().model_json_schema(), path.open("w"))
        print("Schema generated at ", path)
    else:
        from pydantic_yaml import parse_yaml_file_as

        c = parse_yaml_file_as(Config, "config.yaml")
        print(c)
