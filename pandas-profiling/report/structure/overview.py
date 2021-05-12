from urllib.parse import quote

from pandas_profiling.model.messages import MessageType
from pandas_profiling.report.presentation.core import Container, Table, Warnings


def get_dataset_overview(summary):

    dataset_overview = Table(
        [
            {"name": idx, "value": var_sum["mean"], "fmt": "fmt_numeric"}
            for idx, var_sum in summary["variables"].items() if "mean" in var_sum
        ],
        name="Averages based on " + str(summary["table"]["n"]) + " shots",
    )

    return Container(
        [dataset_overview],
        anchor_id="dataset_overview",
        name="Overview",
        sequence_type="list",
    )


def get_dataset_reproduction(summary):
    version = summary["package"]["pandas_profiling_version"]
    config = quote(summary["package"]["pandas_profiling_config"])
    date_start = summary["analysis"]["date_start"]
    date_end = summary["analysis"]["date_end"]
    duration = summary["analysis"]["duration"]
    return Table(
        [
            {"name": "Analysis started", "value": date_start, "fmt": "fmt"},
            {"name": "Analysis finished", "value": date_end, "fmt": "fmt"},
            {"name": "Duration", "value": duration, "fmt": "fmt_timespan"},
            {
                "name": "Version",
                "value": f'<a href="https://github.com/pandas-profiling/pandas-profiling">pandas-profiling v{version}</a>',
                "fmt": "raw",
            },
            {
                "name": "Command line",
                "value": "<code>pandas_profiling --config_file config.yaml [YOUR_FILE.csv]</code>",
                "fmt": "raw",
            },
            {
                "name": "Download configuration",
                "value": f'<a download="config.yaml" href="data:text/plain;charset=utf-8,{config}">config.yaml</a>',
                "fmt": "raw",
            },
        ],
        name="Reproduction",
        anchor_id="reproduction",
    )


def get_dataset_warnings(warnings: list) -> Warnings:
    count = len(
        [
            warning
            for warning in warnings
            if warning.message_type != MessageType.REJECTED
        ]
    )
    return Warnings(warnings=warnings, name=f"Correlations ({count})", anchor_id="warnings")
