import importlib.util
import pathlib
import typing


def _friendly_pillow_import_error() -> None:
    if importlib.util.find_spec("PIL") is None:
        message = "Unable to find the PIL module. Please install it with `pip install pillow`."
        raise ModuleNotFoundError(message)


def _check_max_shape_in_pixels(shape_in_pixels: tuple[int, int]) -> None:
    max_shape_in_pixels = 256

    shapes_over_limit = (axis > max_shape_in_pixels for axis in shape_in_pixels)
    if any(shapes_over_limit):
        message = f"Maximum shape in pixels is {max_shape_in_pixels}; {shape_in_pixels} was specified."
        raise ValueError(message)


def _resample_and_save(
    image_file_path: pathlib.Path,
    output_file_path: pathlib.Path,
    shape_in_pixels: tuple[int, int],
    output_format: typing.Literal["ICO", "PNG", "XBM"],
) -> None:
    import PIL.Image

    source_image = PIL.Image.open(fp=image_file_path)

    match output_format:
        case "XBM":
            image = source_image.convert("1").resize(size=shape_in_pixels, resample=PIL.Image.Resampling.LANCZOS)
        case _:
            image = source_image.resize(size=shape_in_pixels, resample=PIL.Image.Resampling.LANCZOS)

    image.save(fp=output_file_path, format=output_format)


def convert_image_file_to_ico_icon(
    image_file_path: pathlib.Path | str,
    shape_in_pixels: tuple[int, int] = (64, 64),
) -> None:
    """
    Convert a standard image file (.jpg, .png, etc.) to a .ico file.

    The new file is written adjacent to the original source file.

    These are used by Windows and Mac to display the icons on executable programs.
    """
    image_file_path = pathlib.Path(image_file_path)

    _friendly_pillow_import_error()
    _check_max_shape_in_pixels(shape_in_pixels=shape_in_pixels)

    ico_image_file_path = image_file_path.parent / f"{image_file_path.stem}.ico"
    _resample_and_save(
        image_file_path=image_file_path,
        output_file_path=ico_image_file_path,
        shape_in_pixels=shape_in_pixels,
        output_format="ICO",
    )


def convert_image_file_to_png_icon(
    image_file_path: pathlib.Path | str,
    shape_in_pixels: tuple[int, int] = (64, 64),
) -> None:
    """
    Convert a standard image file (.jpg, .png, etc.) to a reduced .png file appropriate for use as a Linux desktop icon.

    The new file is written adjacent to the original source file.
    """
    image_file_path = pathlib.Path(image_file_path)

    _friendly_pillow_import_error()
    _check_max_shape_in_pixels(shape_in_pixels=shape_in_pixels)

    ico_image_file_path = image_file_path.parent / f"{image_file_path.stem}.png"
    _resample_and_save(
        image_file_path=image_file_path,
        output_file_path=ico_image_file_path,
        shape_in_pixels=shape_in_pixels,
        output_format="PNG",
    )


def convert_image_file_to_xbm_icon(
    image_file_path: pathlib.Path | str,
    shape_in_pixels: tuple[int, int] = (64, 64),
) -> None:
    """
    Convert a standard image file (.jpg, .png, etc.) to a .xbm file.

    The new file is written adjacent to the original source file.

    These are the Linux equivalent of .ico files in some capacities.
    """
    image_file_path = pathlib.Path(image_file_path)

    _friendly_pillow_import_error()
    _check_max_shape_in_pixels(shape_in_pixels=shape_in_pixels)  # Technically not required for XBM, but still good idea

    xbm_image_file_path = image_file_path.parent / f"{image_file_path.stem}.xbm"
    _resample_and_save(
        image_file_path=image_file_path,
        output_file_path=xbm_image_file_path,
        shape_in_pixels=shape_in_pixels,
        output_format="XBM",
    )
