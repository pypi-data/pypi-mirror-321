"""Load aspire data into duckdb."""

from __future__ import annotations

import pathlib

import duckdb
import numpy as np
import pandas as pd
import typer


def main(file: pathlib.Path, db: pathlib.Path = pathlib.Path('aspire.duckdb')) -> None:
    df = _load_stata(file)
    transformed = _transform(df)
    with duckdb.connect(db) as con:
        _write_to_db(transformed, con)


def _load_stata(file: pathlib.Path) -> pd.DataFrame:
    return pd.read_stata(file)


def _write_to_db(df: pd.DataFrame, con: duckdb.DuckDBPyConnection) -> None:
    con.sql('CREATE OR REPLACE TABLE indicators AS SELECT * FROM df')


def _transform(df: pd.DataFrame) -> pd.DataFrame:
    # sub-topic 5 is subsumed by 6, which is the actual program
    # there are repeated values in 5/6 otherwise (all, and specifics)
    # ? to be confirmed
    filtered = df.drop(columns=['Sub_Topic5'])
    renamed = _rename_columns(filtered)
    return _remap_values(renamed)


def _rename_columns(df: pd.DataFrame) -> pd.DataFrame:
    renames = {
        'val': 'indicator_value',
        'Sub_Topic1': 'time_of_welfare_transfer',
        'Sub_Topic2': 'indicator_type_level_1',
        'Sub_Topic3': 'indicator_type_level_2',
        'Sub_Topic4': 'population_category',
        'Sub_Topic6': 'program_type',
    }
    return df.rename(columns=renames)


def _remap_values(df: pd.DataFrame) -> pd.DataFrame:
    # removing redundant prefix
    welfare = df['time_of_welfare_transfer'].str.replace(
        'Indicators estimated using ', ''
    )
    return df.assign(
        **{
            'time_of_welfare_transfer': welfare,
            'indicator_quintile': _extract_quintile(df['Indicator_Code']),
        }
    )


def _extract_quintile(indicator_code: pd.Series[str]) -> pd.Series[int]:
    parsed_from_code = indicator_code.str.extract(r'_q(\d)_', expand=False).astype(
        pd.Int8Dtype()
    )
    # `ep` represents `extreme_poor``
    is_lowest_quintile = np.where(
        indicator_code.str.contains(r'_ep_', regex=True), 1, pd.NA
    )
    # it could also be that the phrase 'extreme poor (<$2.15 a day)' indicates lowest quintile
    # but is not necessarily reliable, as there are some indicator groups without a quintile at all
    # best to leave those as null

    return parsed_from_code.fillna(pd.Series(is_lowest_quintile))


if __name__ == '__main__':
    typer.run(main)
