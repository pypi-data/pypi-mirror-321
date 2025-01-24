from canproc.pipelines import canesm_pipeline
from canproc.pipelines import Pipeline
from canproc.pipelines.utils import parse_formula, AstParser
from canproc import register_module
from dask.dot import dot_graph
from canproc.runners import DaskRunner
from pathlib import Path
import pytest
import os


@pytest.mark.parametrize(
    "formula, vars, ops",
    [
        ("FSO", ["FSO"], []),
        ("FSO+FSR", ["FSO", "FSR"], ["+"]),
        ("FSO-FSR+OLR", ["FSO", "FSR", "OLR"], ["-", "+"]),
        ("FSO/FSR-OLR", ["FSO", "FSR", "OLR"], ["/", "-"]),
        ("FSO*FSR/OLR", ["FSO", "FSR", "OLR"], ["*", "/"]),
        (" FSO *FSR/ OLR+BALT - BEG", ["FSO", "FSR", "OLR", "BALT", "BEG"], ["*", "/", "+", "-"]),
        ("TCD > CDBC", ["TCD", "CDBC"], [">"]),
        ("TCD >= CDBC", ["TCD", "CDBC"], [">="]),
        ("TCD < CDBC", ["TCD", "CDBC"], ["<"]),
        ("TCD <= CDBC", ["TCD", "CDBC"], ["<="]),
    ],
    ids=[
        "single",
        "short",
        "add-sub",
        "div-sub",
        "mul-div",
        "whitespace",
        "greater than",
        "greater than equal",
        "less than",
        "less than equal",
    ],
)
def test_formula_parsing(formula: str, vars: list[str], ops: list[str]):
    test_vars, test_ops = parse_formula(formula)
    assert test_vars == vars
    assert test_ops == ops


@pytest.mark.parametrize(
    "filename, num_ops",
    [
        ("canesm_pipeline.yaml", 93),
        ("canesm_pipeline_v52.yaml", 8),
        ("test_duplicate_output.yaml", 8),
        ("test_masked_variable.yaml", 8),
        ("test_formula.yaml", 23),
        ("test_formula_compute_syntax.yaml", 22),
        ("test_multistage_computation.yaml", 9),
        ("test_compute_and_dag_in_stage.yaml", 10),
    ],
    ids=[
        "canesm 6 pipeline",
        "canesm 5 pipeline",
        "duplicate outputs",
        "masked variable",
        "formula",
        "formula compute syntax",
        "multistage computation",
        "both compute and dag",
    ],
)
def test_canesm_pipeline(filename: str, num_ops: int):
    """
    Test that the expected number of nodes are created.
    Note that this doesn't guarantee correctness and we should be testing
    node connections, but that is harder to check.
    """
    pipeline = Path(__file__).parent / "data" / "pipelines" / filename
    dag = canesm_pipeline(pipeline, input_dir="test")
    assert len(dag.dag) == num_ops
    # assert dag.id[0 : len(dag_id)] == dag_id

    # runner = DaskRunner()
    # dsk, output = runner.create_dag(dag)
    # dot_graph(dsk, f"{filename.split('.')[0]}.png", rankdir="TB", collapse_outputs=True)


def test_pipeline_with_custom_function():

    # defined in conftest.py
    import mymodule

    register_module(mymodule, "mymodule")

    pipeline = Path(__file__).parent / "data" / "pipelines" / "test_user_function.yaml"
    dag = canesm_pipeline(pipeline, input_dir="test")
    assert len(dag.dag) == 16


@pytest.mark.skip(reason="requires access to science")
def test_run_pipeline(client=None):

    import xarray as xr
    import time
    from dask.diagnostics import Profiler, ResourceProfiler, CacheProfiler, visualize
    from dask.distributed import performance_report

    # qsub -I -lselect=1:ncpus=1:mem=15gb -lplace=scatter -Wumask=022 -S/bin/bash -qdevelopment -lwalltime=06:00:00
    config = (
        Path(__file__).parent.parent
        / "src"
        / "canproc"
        / "templates"
        / "pipelines"
        / "canesm_pipeline.yaml"
    )
    config = r"/fs/site5/eccc/crd/ccrn/users/rlr001/software/canesm-processor/Emon.yaml"
    # config = r"/space/hall5/sitestore/eccc/crd/ccrn/users/rvs001/templates/canproc/canesm_pipeline_cmip6.yaml"
    # config = r"/space/hall5/sitestore/eccc/crd/ccrn/users/rvs001/store/canesm-processor/src/canproc/templates/pipelines/canesm_pipeline_rvs001.yaml"
    input_dir = r"/space/hall5/sitestore/eccc/crd/ccrn/users/rvs001/data/canamg_v51a1/2008_1.0x1.0_annual_sorted"
    # input_dir = r"/space/hall5/sitestore/eccc/crd/ccrn/users/rvs001/data/mc_jcl-dust-014_2003_m01_gem.001/1.0x1.0_annual_sorted"

    output_dir = r"/space/hall5/sitestore/eccc/crd/ccrn/users/rlr001/canproc/canamg_v51a1"

    print("creating pipeline...")
    pipeline = Pipeline(config, input_dir, output_dir)
    dag = pipeline.render()

    print("creating output directories...")
    for directory in pipeline.directories.values():
        os.makedirs(directory, exist_ok=True)

    start = time.time()
    print("running dag...")
    runner = DaskRunner(scheduler="processes")
    if client is not None:
        runner.scheduler = client.get
        # runner.run(dag)
        with performance_report(filename="profile_client.html"):
            output = runner.run(dag)
        end = time.time()
        print(f"processing took {end - start:3.4f} seconds")
        # client.profile(filename='profile_client.html')  # save to html file
    else:
        with Profiler() as prof, ResourceProfiler(dt=0.0001) as rprof, CacheProfiler() as cprof:
            output = runner.run(dag)
        end = time.time()
        print(f"processing took {end - start:3.4f} seconds")
        visualize([prof, rprof, cprof], filename="profile_processes.html")

    # ds = xr.open_dataset(
    #     r"/space/hall5/sitestore/eccc/crd/ccrn/users/rlr001/canproc/canamg_v51a1/diags/monthly/CI.nc"
    # )
    # print(f"sum of CI: {float(ds.CI.sum().values)}")
    print("SUCCESS!")


if __name__ == "__main__":
    # from dask.distributed import Client
    # client = Client(processes=True)

    from dask.distributed import LocalCluster, SubprocessCluster

    cluster = LocalCluster(processes=False)  # Fully-featured local Dask cluster
    # cluster = SubprocessCluster(n_workers=10, threads_per_worker=1)
    client = cluster.get_client()

    test_run_pipeline(client)
