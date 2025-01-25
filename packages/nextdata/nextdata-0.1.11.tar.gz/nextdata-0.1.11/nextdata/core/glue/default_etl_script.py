from typing import Any
from pyspark.sql import functions as F
from nextdata.core.connections.spark import SparkManager
from nextdata.core.glue.connections.dsql import DSQLGlueJobArgs, generate_dsql_password
from nextdata.core.glue.glue_entrypoint import glue_job, GlueJobArgs
from nextdata.core.glue.connections.jdbc import JDBCGlueJobArgs
from pyspark.sql import DataFrame
import logging

logger = logging.getLogger(__name__)


@glue_job(JobArgsType=GlueJobArgs)
def main(
    spark_manager: SparkManager,
    job_args: GlueJobArgs,
):
    # Read source data into a Spark DataFrame

    base_query = f"SELECT * FROM {job_args.sql_table}"
    logger.info(f"Base query: {base_query}")
    connection_conf = None
    password = None
    if job_args.connection_type == "dsql":
        connection_args: dict[str, Any] = job_args.connection_properties
        connection_conf = DSQLGlueJobArgs(host=connection_args["host"])
        password = generate_dsql_password(connection_conf.host)
    elif job_args.connection_type == "jdbc":
        connection_conf = JDBCGlueJobArgs(**job_args.connection_properties)
        password = connection_conf.password
    else:
        raise ValueError(f"Unsupported connection type: {job_args.connection_type}")

    connection_options = dict(
        url=f"jdbc:{connection_conf.protocol}://{connection_conf.host}:{connection_conf.port}/{connection_conf.database}",
        dbtable=job_args.sql_table,
        user=connection_conf.username,
        password=password,
        ssl=True,
        sslmode="require",
        # driver="com.amazon.dsql.jdbc.Driver",
    )
    print(connection_options)
    source_df: DataFrame = spark_manager.spark.read.jdbc(
        url=connection_options["url"],
        table=connection_options["dbtable"],
        properties=connection_options,
    )
    logger.info(f"# of rows: {source_df.count()}")
    source_df.show()
    # Register the DataFrame as a temp view to use with Spark SQL
    source_df = source_df.withColumn("ds", F.current_date())

    spark_manager.write_to_table(
        table_name=job_args.sql_table,
        df=source_df,
        mode="overwrite" if job_args.is_full_load else "append",
    )


if __name__ == "__main__":
    main()
