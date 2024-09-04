import os


def get_asset_path(relative_path: str = "") -> str:
    """
    Constructs the absolute path to a file
    or directory within the `assets` folder,
    relative to the directory where the script is located.

    Args:
        relative_path (str): The relative path within the `assets` directory. Defaults to an empty string, which will return the path to the `assets` directory itself.

    Returns:
        str: The absolute path to the specified file or directory within the `assets` folder.

    Raises:
        AssertionError: If the constructed path does not exist.
    """  # noqa: E501
    asset_path: str = os.path.join(
        os.path.dirname(__file__),
        "assets",
        relative_path
    )
    if not os.path.exists(asset_path):
        raise AssertionError(f"Path does not exist: {asset_path}")
    return asset_path
