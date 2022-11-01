def abs_path_from_project(relative_path: str):
    import mobile_utils
    from pathlib import Path

    return (
        Path(mobile_utils.__file__)
        .parent.parent.joinpath(relative_path)
        .absolute()
        .__str__()
    )
