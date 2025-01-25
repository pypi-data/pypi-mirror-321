from jaix import Experiment, LOGGER_NAME
from jaix.experiment import ExperimentConfig
from ttex.config import ConfigFactory as CF
from ttex.log.handler import WandbHandler
from wandb.sdk import launch, AlertLevel
from importlib.metadata import version
from typing import Dict, Optional
import os
import wandb
from jaix.env.wrapper import LoggingWrapper, LoggingWrapperConfig
from ttex.log import get_logging_config
import sys
import logging
import argparse
import json

logger = logging.getLogger(LOGGER_NAME)


def wandb_logger(
    exp_config: ExperimentConfig,
    run: wandb.sdk.wandb_run.Run,
    wandb_logger_name: str = "jaix_wandb",
):
    """
    Add wandb logging to the experiment configuration
    Args:
        exp_config (ExperimentConfig): Experiment configuration
        run (wandb.sdk.wandb_run.Run): Wandb run
        wandb_logger_name (str, optional): Logger name for wandb. Defaults to "jaix_wandb".
    Returns:
        ExperimentConfig: Experiment configuration with wandb logging
    """
    # Adapt LoggingConfig
    if exp_config.logging_config.dict_config:
        logging_config = exp_config.logging_config.dict_config
    else:
        logging_config = get_logging_config(
            logger_name=LOGGER_NAME,
            disable_existing=exp_config.logging_config.disable_existing,
        )
    logging_config["loggers"][wandb_logger_name] = {
        "level": "INFO",
        "handlers": ["wandb_handler"],
    }
    logging_config["handlers"]["wandb_handler"] = {
        "()": WandbHandler,
        "wandb_run": run,
        "custom_metrics": {"env/step": ["env/*"], "restarts/step": ["restarts/*"]},
        "level": "INFO",
    }
    exp_config.logging_config.dict_config = logging_config

    wandb_log_wrapper = (
        LoggingWrapper,
        LoggingWrapperConfig(logger_name=wandb_logger_name),
    )

    if exp_config.env_config.env_wrappers:
        exp_config.env_config.env_wrappers.append(wandb_log_wrapper)
    else:
        exp_config.env_config.env_wrappers = [wandb_log_wrapper]
    return exp_config


def wandb_init(run_config: Dict, project: Optional[str] = None):
    """
    Initialize wandb run
    Args:
        run_config (Dict): Run configuration
        project (Optional[str], optional): Wandb project. Defaults to None.
    Returns:
        wandb.sdk.wandb_run.Run: Wandb run
    """
    # Config to log
    # jaix_version = version("tai_jaix")
    jaix_version = "0.1.0"  # TODO: Fix this
    config_override = {"repo": "jaix", "version": jaix_version}

    run_config.update(config_override)
    if not project:
        run = wandb.init(config=run_config)
    else:
        run = wandb.init(config=run_config, project=project)
    return run


def launch_jaix_experiment(
    run_config: Dict, project: Optional[str] = None, wandb: bool = True
):
    """
    Launch a jaix experiment from a run_config dictionary
    Args:
        run_config (Dict): Dictionary with the run configuration
        project (Optional[str], optional): Wandb project. Defaults to None.
        wandb (bool, optional): If True, will log to wandb. Defaults to True.
    Returns:
        data_dir (str): Path to the data directory
        exit_code (int): Exit code of the experiment
    """
    exp_config = CF.from_dict(run_config)
    if wandb:
        run = wandb_init(run_config, project)
        data_dir = run.dir
        exp_config = wandb_logger(exp_config, run)
        run.alert(
            "Experiment started", text="Experiment started", level=AlertLevel.INFO
        )
    else:
        data_dir = None

    try:
        Experiment.run(exp_config)
        exit_code = 0
    except Exception as e:
        logger.error(f"Experiment failed {e}", exc_info=True)
        exit_code = 1

    if wandb:
        if exit_code == 0:
            run.alert(
                "Experiment ended", text="Experiment ended", level=AlertLevel.INFO
            )
        else:
            run.alert(
                "Experiment failed",
                level=AlertLevel.ERROR,
                text="Experiment failed",
            )
        run.finish(exit_code=exit_code)

    return data_dir, exit_code


def parse_args():
    parser = argparse.ArgumentParser(description="Launch a jaix experiment")
    parser.add_argument(
        "--project",
        type=str,
        default=None,
        help="Wandb project to log to. If not provided, will not log to wandb",
    )
    parser.add_argument(
        "--config_file", type=str, help="Path to the configuration file"
    )
    return parser.parse_args()


if __name__ == "__main__":
    """
    This script is used to launch a jaix experiment from a wandb configuration
    """
    launch_arguments = {}
    if os.environ.get("WANDB_CONFIG", None):
        run_config = launch.load_wandb_config().as_dict()
        launch_arguments["run_config"] = run_config
        launch_arguments["wandb"] = True
    else:
        args = parse_args()
        # run_config = CF.from_file(args.config_file).as_dict()
        with open(args.config_file, "r") as f:
            run_config = json.load(f)
        launch_arguments["run_config"] = run_config
        if args.project:
            launch_arguments["project"] = args.project
            launch_arguments["wandb"] = True
        else:
            launch_arguments["wandb"] = False
    _, exit_code = launch_jaix_experiment(**launch_arguments)
    sys.exit(exit_code)
