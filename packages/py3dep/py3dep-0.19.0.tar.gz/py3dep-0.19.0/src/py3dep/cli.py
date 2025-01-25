"""Command-line interface for Py3DEP."""

from __future__ import annotations

from pathlib import Path
from typing import TYPE_CHECKING, Literal, TypeVar, cast

import click
import geopandas as gpd
import pandas as pd

from py3dep import py3dep
from py3dep.exceptions import InputTypeError, MissingColumnError, MissingCRSError
from py3dep.py3dep import LAYERS

if TYPE_CHECKING:
    DFType = TypeVar("DFType", pd.DataFrame, gpd.GeoDataFrame)


def get_target_df(tdf: DFType, req_cols: list[str]) -> DFType:
    """Check if all required columns exists in the dataframe.

    It also re-orders the columns based on ``req_cols`` order.
    """
    missing = [c for c in req_cols if c not in tdf]
    if missing:
        raise MissingColumnError(missing)
    return tdf[req_cols]  # pyright: ignore[reportReturnType]


CONTEXT_SETTINGS = {"help_option_names": ["-h", "--help"]}

save_arg = click.option(
    "-s",
    "--save_dir",
    default="topo_3dep",
    type=click.Path(exists=False),
    help=" ".join(
        (
            "Path to a directory to save the requested files.",
            "Extension for the outputs is either `.nc` for geometry or `.csv` for coords.",
        )
    ),
)


@click.group(context_settings=CONTEXT_SETTINGS)
def cli() -> None:
    """Command-line interface for Py3DEP."""


@cli.command("coords", context_settings=CONTEXT_SETTINGS)
@click.argument("fpath", type=click.Path(exists=True))
@click.option(
    "-q",
    "--query_source",
    default="tep",
    type=click.Choice(["tnm", "tep"], case_sensitive=False),
    help="Source of the elevation data: The National Map (tnm) or 3DEP (tep).",
)
@save_arg
def coords(
    fpath: Path,
    query_source: Literal["tep", "tnm"] = "tep",
    save_dir: str | Path = "topo_3dep",
) -> None:
    """Retrieve topographic data for a list of coordinates.

    \b
    FPATH: Path to a csv file with two columns named ``lon`` and ``lat``.

    \b
    Examples:
        $ cat coords.csv
        lon,lat
        -122.2493328,37.8122894
        $ py3dep coords coords.csv -q tep -s topo_dir
    """  # noqa: D301
    fpath = Path(fpath)
    elev = get_target_df(pd.read_csv(fpath), ["lon", "lat"])

    count = "1 point" if len(elev) == 1 else f"{len(elev)} points"
    click.echo(f"Found coordinates of {count} in {fpath.resolve()}. Retrieving ... ")

    coords_list = list(elev.itertuples(index=False, name=None))
    coords_list = cast("list[tuple[float, float]]", coords_list)
    elev["elevation"] = py3dep.elevation_bycoords(coords_list, 4326, query_source)

    Path(save_dir).mkdir(parents=True, exist_ok=True)
    elev.astype("f4").to_csv(Path(save_dir, f"{fpath.stem}_elevation.csv"))
    click.echo("Done.")


@cli.command("geometry", context_settings=CONTEXT_SETTINGS)
@click.argument("fpath", type=click.Path(exists=True))
@click.option(
    "-l",
    "--layers",
    multiple=True,
    default=["DEM"],
    type=click.Choice(LAYERS, case_sensitive=True),
    help="Target topographic data layers",
)
@save_arg
def geometry(
    fpath: Path,
    layers: str | list[str] = "DEM",
    save_dir: str | Path = "topo_3dep",
) -> None:
    """Retrieve topographic data within geometries.

    \b
    FPATH: Path to a shapefile (.shp) or geopackage (.gpkg) file.
    This file must have three columns and contain a ``crs`` attribute:
        - ``id``: Feature identifiers that py3dep uses as the output netcdf/csv filenames.
        - ``res``: Target resolution in meters.
        - ``geometry``: A Polygon or MultiPloygon.

    \b
    Examples:
        $ py3dep geometry ny_geom.gpkg -l "Slope Map" -l DEM -s topo_dir
    """  # noqa: D301
    fpath = Path(fpath)
    if fpath.suffix not in (".shp", ".gpkg"):
        raise InputTypeError("file", ".shp or .gpkg")

    target_df = gpd.read_file(fpath)
    if target_df.crs is None:
        raise MissingCRSError
    crs = target_df.crs.to_string()

    target_df = get_target_df(target_df, ["id", "res", "geometry"])
    args_list = ((g, r, Path(save_dir, f"{i}.nc")) for i, r, g in target_df.itertuples(index=False))

    count = "1 geometry" if len(target_df) == 1 else f"{len(target_df)} geometries"
    click.echo(f"Found {count} in {fpath.resolve()}.")

    Path(save_dir).mkdir(parents=True, exist_ok=True)
    with click.progressbar(
        args_list, label="Getting topographic data from 3DEP", length=len(target_df)
    ) as bar:
        for geo, res, f in bar:
            py3dep.get_map(layers, geo, res, geo_crs=crs, crs=4326).to_netcdf(f)
    click.echo("Done.")
