from pyrlprob.problem import RLProblem
from pyrlprob.tests import *

from typing import *
import matplotlib.pyplot as plt
import yaml
import os
import matplotlib

from pyrlprob.utils.plots import plot_metric


def test_train_py(model: str="mlp",
        use_gpu: bool=False,
        res_dir: Optional[str]=None) -> None:
    """
    Test pyrlprob training functionalities in the Landing1D environment
        written in python.

    Args:
        model: mlp, lstm or gtrxl.
        use_gpu: use GPU for training?
        res_dir: path where results are saved. Current directory if not specified.
    """

    #Train
    _, _, _, _ = \
        test_landing_env_train(py_or_cpp="py",
                               model=model,
                               use_gpu=use_gpu,
                               res_dir=res_dir)


def test_train_cpp(res_dir: Optional[str]=None) -> None:
    """
    Test pyrlprob training functionalities in the Landing1D environment
        written in c++.

    Args:
        res_dir: path where results are saved. Current directory if not specified.
    """

    #Train
    _, _, _, _ = \
        test_landing_env_train(py_or_cpp="cpp",
                               res_dir=res_dir)


def test_train_eval_py(model: str="mlp",
                       use_gpu: bool=False,
                       res_dir: Optional[str]=None) -> None:
    """
    Test pyrlprob training, evaluation and post-processing functionalities 
        in the Landing1D environment written in python.

    Args:
        model: mlp, lstm or gtrxl.
        use_gpu: use GPU for training?
        res_dir: path where results are saved. Current directory if not specified.
    """

    #Train, evaluate, post-process
    test_landing_env_train_eval(py_or_cpp="py",
                               model=model,
                               use_gpu=use_gpu,
                               res_dir=res_dir)


def test_train_eval_cpp(res_dir: Optional[str]=None) -> None:
    """
    Test pyrlprob training, evaluation and post-processing functionalities 
        in the Landing1D environment written in c++.

    Args:
        res_dir: path where results are saved. Current directory if not specified.
    """

    #Train, evaluate, post-process
    test_landing_env_train_eval(py_or_cpp="cpp",
                               res_dir=res_dir)


def make_cpp_lib() -> None:
    """
    Create the dynamic library with the environments in c++.
    """

    __location__ = os.path.realpath(os.path.join(os.getcwd(), os.path.dirname(__file__)))
    os.system("make -f " + os.path.join(__location__, "Makefile"))

    return


def test_landing_env_train(py_or_cpp: str="py",
                           model: str="mlp",
                           use_gpu: bool=False,
                           res_dir: Optional[str]=None) -> Tuple[RLProblem, str, List[str], List[int]]:
    """
    Test pyrlprob training functionalities in the Landing1D environment.

    Args:
        py_or_cpp: python or cpp version of the environment?
        model: mlp, lstm or gtrxl.
        use_gpu: use GPU for training?
        res_dir: path where results are saved. Current directory if not specified.
    """

    #Config file
    __location__ = os.path.realpath(os.path.join(os.getcwd(), os.path.dirname(__file__)))
    if py_or_cpp == "py":
        if model == "mlp":
            if use_gpu:
                config = os.path.join(__location__, "landing1d_mlp_gpu_py.yaml")
            else:
                config = os.path.join(__location__, "landing1d_mlp_py.yaml")
        elif model == "lstm":
            config = os.path.join(__location__, "landing1d_lstm_py.yaml")
        elif model == "gtrxl":
            config = os.path.join(__location__, "landing1d_gtrxl_py.yaml")
        else:
            assert False, "Model not implemented."
    elif py_or_cpp == "cpp":
        if not any(fname.endswith('.so') for fname in os.listdir(__location__ + "/cpp_tests/")):
            assert False, "Run 'make_cpp_lib()' first to create the dynamic library, then launch again python."
        config = os.path.join(__location__, "landing1d_cpp.yaml")

    #Problem definition
    LandingProblem = RLProblem(config)

    #Training
    _, trainer_dir, exp_dirs, last_cps, _ = \
        LandingProblem.solve(res_dir, 
                             evaluate=False, 
                             postprocess=False,
                             debug=True)

    return LandingProblem, trainer_dir, exp_dirs, last_cps


def test_landing_env_train_eval(py_or_cpp: str="py",
                                model: str="mlp",
                                use_gpu: bool=False,
                                res_dir: Optional[str]=None) -> None:
    """
    Test pyrlprob training, evaluation and post-processing functionalities 
        in the Landing1D environment.

    Args:
        py_or_cpp: python or cpp version of the environment?
        model: mlp, lstm or gtrxl.
        use_gpu: use GPU for training?
        res_dir: path where results are saved. Current directory if not specified.
    """


    __location__ = os.path.realpath(os.path.join(os.getcwd(), os.path.dirname(__file__)))

    #Train
    LandingProblem, trainer_dir, exp_dirs, last_cps = \
        test_landing_env_train(py_or_cpp=py_or_cpp,
                               model=model,
                               use_gpu=use_gpu,
                               res_dir=res_dir)

    #Create new config file for model re-training
    load = {"load": {"trainer_dir": trainer_dir,
            "prev_exp_dirs": exp_dirs,
            "prev_last_cps": last_cps}}
    stop = {"stop": {"training_iteration": 2*last_cps[-1]}}
    config_new_dict = {**LandingProblem.input_config, **stop, **load}
    with open(os.path.join(__location__, "landing1d_load.yaml"), 'w') as outfile:
        yaml.dump(config_new_dict, outfile)
    
    #Training, evaluation and postprocessing of pre-trained model
    config_new = os.path.join(__location__, "landing1d_load.yaml")
    LandingProblemPretrained = RLProblem(config_new)
    _, trainer_dir, exp_dirs, last_cps, _ = \
        LandingProblemPretrained.solve(debug=False)

    # #Plot of metric trend
    # plt.style.use("seaborn")
    # plt.style.use("seaborn")
    # matplotlib.rc('font', size=20)
    # fig = plot_metric("episode_reward",
    #                   exp_dirs,
    #                   last_cps)
    # plt.xlabel('training iteration', fontsize=20)
    # plt.ylabel('episode reward', fontsize=20)
    # fig.savefig(trainer_dir + "episode_reward.png")


if __name__ == "__main__":
    import pytest
    import sys
    sys.exit(pytest.main(["-v", __file__]))