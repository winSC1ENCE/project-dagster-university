import json
import dagster as dg
from dagster_dbt import DagsterDbtTranslator, DbtCliResource, dbt_assets
from dagster_and_dbt.defs.partitions import daily_partition
from dagster_and_dbt.defs.project import dbt_project

INCREMENTAL_SELECTOR = "config.materialized:incremental"


class CustomizedDagsterDbtTranslator(DagsterDbtTranslator):
    def get_asset_key(self, dbt_resource_props):
        resource_type = dbt_resource_props["resource_type"]
        name = dbt_resource_props["name"]
        if resource_type == "source":
            return dg.AssetKey(f"taxi_{name}")
        else:
            return super().get_asset_key(dbt_resource_props)

# This asset is configured to run all dbt models except those that are incremental
# It uses a custom DagsterDbtTranslator to handle asset keys for sources
# and other models
# It will run models that are materialized as table or view
# It excludes models that are materialized as incremental
@dbt_assets(
    manifest=dbt_project.manifest_path,
    dagster_dbt_translator=CustomizedDagsterDbtTranslator(),
    exclude=INCREMENTAL_SELECTOR,
)
def dbt_analytics(context: dg.AssetExecutionContext, dbt: DbtCliResource):
    yield from dbt.cli(["build"], context=context).stream()


# This asset is configured to run only on incremental models
# It uses a custom DagsterDbtTranslator to handle asset keys
# and partitions for incremental models
# It is partitioned by day using the daily_partition defined in the project
# It will only run models that are materialized as incremental 
@dbt_assets(
    manifest=dbt_project.manifest_path,
    dagster_dbt_translator=CustomizedDagsterDbtTranslator(),
    select=INCREMENTAL_SELECTOR,
    partitions_def=daily_partition,
)
def incremental_dbt_models(context: dg.AssetExecutionContext, dbt: DbtCliResource):
    time_window = context.partition_time_window
    dbt_vars = {
        "min_date": time_window.start.strftime('%Y-%m-%d'),
        "max_date": time_window.end.strftime('%Y-%m-%d')
    }

    yield from dbt.cli(
        ["build", "--vars", json.dumps(dbt_vars)], context=context
    ).stream()