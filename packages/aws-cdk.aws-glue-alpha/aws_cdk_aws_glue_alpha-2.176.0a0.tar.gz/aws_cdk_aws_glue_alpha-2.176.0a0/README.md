# AWS Glue Construct Library

<!--BEGIN STABILITY BANNER-->---


![cdk-constructs: Experimental](https://img.shields.io/badge/cdk--constructs-experimental-important.svg?style=for-the-badge)

> The APIs of higher level constructs in this module are experimental and under active development.
> They are subject to non-backward compatible changes or removal in any future version. These are
> not subject to the [Semantic Versioning](https://semver.org/) model and breaking changes will be
> announced in the release notes. This means that while you may use them, you may need to update
> your source code when upgrading to a newer version of this package.

---
<!--END STABILITY BANNER-->

This module is part of the [AWS Cloud Development Kit](https://github.com/aws/aws-cdk) project.

## Job

A `Job` encapsulates a script that connects to data sources, processes them, and then writes output to a data target.

There are 3 types of jobs supported by AWS Glue: Spark ETL, Spark Streaming, and Python Shell jobs.

The `glue.JobExecutable` allows you to specify the type of job, the language to use and the code assets required by the job.

`glue.Code` allows you to refer to the different code assets required by the job, either from an existing S3 location or from a local file path.

`glue.ExecutionClass` allows you to specify `FLEX` or `STANDARD`. `FLEX` is appropriate for non-urgent jobs such as pre-production jobs, testing, and one-time data loads.

### Spark Jobs

These jobs run in an Apache Spark environment managed by AWS Glue.

#### ETL Jobs

An ETL job processes data in batches using Apache Spark.

```python
# bucket: s3.Bucket

glue.Job(self, "ScalaSparkEtlJob",
    executable=glue.JobExecutable.scala_etl(
        glue_version=glue.GlueVersion.V5_0,
        script=glue.Code.from_bucket(bucket, "src/com/example/HelloWorld.scala"),
        class_name="com.example.HelloWorld",
        extra_jars=[glue.Code.from_bucket(bucket, "jars/HelloWorld.jar")]
    ),
    worker_type=glue.WorkerType.G_8X,
    description="an example Scala ETL job"
)
```

#### Streaming Jobs

A Streaming job is similar to an ETL job, except that it performs ETL on data streams. It uses the Apache Spark Structured Streaming framework. Some Spark job features are not available to streaming ETL jobs.

```python
glue.Job(self, "PythonSparkStreamingJob",
    executable=glue.JobExecutable.python_streaming(
        glue_version=glue.GlueVersion.V5_0,
        python_version=glue.PythonVersion.THREE,
        script=glue.Code.from_asset(path.join(__dirname, "job-script", "hello_world.py"))
    ),
    description="an example Python Streaming job"
)
```

### Python Shell Jobs

A Python shell job runs Python scripts as a shell and supports a Python version that depends on the AWS Glue version you are using.
This can be used to schedule and run tasks that don't require an Apache Spark environment. Currently, three flavors are supported:

* PythonVersion.TWO (2.7; EOL)
* PythonVersion.THREE (3.6)
* PythonVersion.THREE_NINE (3.9)

```python
# bucket: s3.Bucket

glue.Job(self, "PythonShellJob",
    executable=glue.JobExecutable.python_shell(
        glue_version=glue.GlueVersion.V1_0,
        python_version=glue.PythonVersion.THREE,
        script=glue.Code.from_bucket(bucket, "script.py")
    ),
    description="an example Python Shell job"
)
```

### Ray Jobs

These jobs run in a Ray environment managed by AWS Glue.

```python
glue.Job(self, "RayJob",
    executable=glue.JobExecutable.python_ray(
        glue_version=glue.GlueVersion.V5_0,
        python_version=glue.PythonVersion.THREE_NINE,
        runtime=glue.Runtime.RAY_TWO_FOUR,
        script=glue.Code.from_asset(path.join(__dirname, "job-script", "hello_world.py"))
    ),
    worker_type=glue.WorkerType.Z_2X,
    worker_count=2,
    description="an example Ray job"
)
```

### Enable Spark UI

Enable Spark UI setting the `sparkUI` property.

```python
glue.Job(self, "EnableSparkUI",
    job_name="EtlJobWithSparkUIPrefix",
    spark_uI=glue.SparkUIProps(
        enabled=True
    ),
    executable=glue.JobExecutable.python_etl(
        glue_version=glue.GlueVersion.V3_0,
        python_version=glue.PythonVersion.THREE,
        script=glue.Code.from_asset(path.join(__dirname, "job-script", "hello_world.py"))
    )
)
```

The `sparkUI` property also allows the specification of an s3 bucket and a bucket prefix.

See [documentation](https://docs.aws.amazon.com/glue/latest/dg/add-job.html) for more information on adding jobs in Glue.

### Enable Job Run Queuing

AWS Glue job queuing monitors your account level quotas and limits. If quotas or limits are insufficient to start a Glue job run, AWS Glue will automatically queue the job and wait for limits to free up. Once limits become available, AWS Glue will retry the job run. Glue jobs will queue for limits like max concurrent job runs per account, max concurrent Data Processing Units (DPU), and resource unavailable due to IP address exhaustion in Amazon Virtual Private Cloud (Amazon VPC).

Enable job run queuing by setting the `jobRunQueuingEnabled` property to `true`.

```python
glue.Job(self, "EnableRunQueuing",
    job_name="EtlJobWithRunQueuing",
    executable=glue.JobExecutable.python_etl(
        glue_version=glue.GlueVersion.V5_0,
        python_version=glue.PythonVersion.THREE,
        script=glue.Code.from_asset(path.join(__dirname, "job-script", "hello_world.py"))
    ),
    job_run_queuing_enabled=True
)
```

## Connection

A `Connection` allows Glue jobs, crawlers and development endpoints to access certain types of data stores. For example, to create a network connection to connect to a data source within a VPC:

```python
# security_group: ec2.SecurityGroup
# subnet: ec2.Subnet

glue.Connection(self, "MyConnection",
    type=glue.ConnectionType.NETWORK,
    # The security groups granting AWS Glue inbound access to the data source within the VPC
    security_groups=[security_group],
    # The VPC subnet which contains the data source
    subnet=subnet
)
```

For RDS `Connection` by JDBC, it is recommended to manage credentials using AWS Secrets Manager. To use Secret, specify `SECRET_ID` in `properties` like the following code. Note that in this case, the subnet must have a route to the AWS Secrets Manager VPC endpoint or to the AWS Secrets Manager endpoint through a NAT gateway.

```python
# security_group: ec2.SecurityGroup
# subnet: ec2.Subnet
# db: rds.DatabaseCluster

glue.Connection(self, "RdsConnection",
    type=glue.ConnectionType.JDBC,
    security_groups=[security_group],
    subnet=subnet,
    properties={
        "JDBC_CONNECTION_URL": f"jdbc:mysql://{db.clusterEndpoint.socketAddress}/databasename",
        "JDBC_ENFORCE_SSL": "false",
        "SECRET_ID": db.secret.secret_name
    }
)
```

If you need to use a connection type that doesn't exist as a static member on `ConnectionType`, you can instantiate a `ConnectionType` object, e.g: `new glue.ConnectionType('NEW_TYPE')`.

See [Adding a Connection to Your Data Store](https://docs.aws.amazon.com/glue/latest/dg/populate-add-connection.html) and [Connection Structure](https://docs.aws.amazon.com/glue/latest/dg/aws-glue-api-catalog-connections.html#aws-glue-api-catalog-connections-Connection) documentation for more information on the supported data stores and their configurations.

## SecurityConfiguration

A `SecurityConfiguration` is a set of security properties that can be used by AWS Glue to encrypt data at rest.

```python
glue.SecurityConfiguration(self, "MySecurityConfiguration",
    cloud_watch_encryption=glue.CloudWatchEncryption(
        mode=glue.CloudWatchEncryptionMode.KMS
    ),
    job_bookmarks_encryption=glue.JobBookmarksEncryption(
        mode=glue.JobBookmarksEncryptionMode.CLIENT_SIDE_KMS
    ),
    s3_encryption=glue.S3Encryption(
        mode=glue.S3EncryptionMode.KMS
    )
)
```

By default, a shared KMS key is created for use with the encryption configurations that require one. You can also supply your own key for each encryption config, for example, for CloudWatch encryption:

```python
# key: kms.Key

glue.SecurityConfiguration(self, "MySecurityConfiguration",
    cloud_watch_encryption=glue.CloudWatchEncryption(
        mode=glue.CloudWatchEncryptionMode.KMS,
        kms_key=key
    )
)
```

See [documentation](https://docs.aws.amazon.com/glue/latest/dg/encryption-security-configuration.html) for more info for Glue encrypting data written by Crawlers, Jobs, and Development Endpoints.

## Database

A `Database` is a logical grouping of `Tables` in the Glue Catalog.

```python
glue.Database(self, "MyDatabase",
    database_name="my_database",
    description="my_database_description"
)
```

## Table

A Glue table describes a table of data in S3: its structure (column names and types), location of data (S3 objects with a common prefix in a S3 bucket), and format for the files (Json, Avro, Parquet, etc.):

```python
# my_database: glue.Database

glue.S3Table(self, "MyTable",
    database=my_database,
    columns=[glue.Column(
        name="col1",
        type=glue.Schema.STRING
    ), glue.Column(
        name="col2",
        type=glue.Schema.array(glue.Schema.STRING),
        comment="col2 is an array of strings"
    )],
    data_format=glue.DataFormat.JSON
)
```

By default, a S3 bucket will be created to store the table's data but you can manually pass the `bucket` and `s3Prefix`:

```python
# my_bucket: s3.Bucket
# my_database: glue.Database

glue.S3Table(self, "MyTable",
    bucket=my_bucket,
    s3_prefix="my-table/",
    # ...
    database=my_database,
    columns=[glue.Column(
        name="col1",
        type=glue.Schema.STRING
    )],
    data_format=glue.DataFormat.JSON
)
```

Glue tables can be configured to contain user-defined properties, to describe the physical storage of table data, through the `storageParameters` property:

```python
# my_database: glue.Database

glue.S3Table(self, "MyTable",
    storage_parameters=[
        glue.StorageParameter.skip_header_line_count(1),
        glue.StorageParameter.compression_type(glue.CompressionType.GZIP),
        glue.StorageParameter.custom("separatorChar", ",")
    ],
    # ...
    database=my_database,
    columns=[glue.Column(
        name="col1",
        type=glue.Schema.STRING
    )],
    data_format=glue.DataFormat.JSON
)
```

Glue tables can also be configured to contain user-defined table properties through the [`parameters`](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-glue-table-tableinput.html#cfn-glue-table-tableinput-parameters) property:

```python
# my_database: glue.Database

glue.S3Table(self, "MyTable",
    parameters={
        "key1": "val1",
        "key2": "val2"
    },
    database=my_database,
    columns=[glue.Column(
        name="col1",
        type=glue.Schema.STRING
    )],
    data_format=glue.DataFormat.JSON
)
```

### Partition Keys

To improve query performance, a table can specify `partitionKeys` on which data is stored and queried separately. For example, you might partition a table by `year` and `month` to optimize queries based on a time window:

```python
# my_database: glue.Database

glue.S3Table(self, "MyTable",
    database=my_database,
    columns=[glue.Column(
        name="col1",
        type=glue.Schema.STRING
    )],
    partition_keys=[glue.Column(
        name="year",
        type=glue.Schema.SMALL_INT
    ), glue.Column(
        name="month",
        type=glue.Schema.SMALL_INT
    )],
    data_format=glue.DataFormat.JSON
)
```

### Partition Indexes

Another way to improve query performance is to specify partition indexes. If no partition indexes are
present on the table, AWS Glue loads all partitions of the table and filters the loaded partitions using
the query expression. The query takes more time to run as the number of partitions increase. With an
index, the query will try to fetch a subset of the partitions instead of loading all partitions of the
table.

The keys of a partition index must be a subset of the partition keys of the table. You can have a
maximum of 3 partition indexes per table. To specify a partition index, you can use the `partitionIndexes`
property:

```python
# my_database: glue.Database

glue.S3Table(self, "MyTable",
    database=my_database,
    columns=[glue.Column(
        name="col1",
        type=glue.Schema.STRING
    )],
    partition_keys=[glue.Column(
        name="year",
        type=glue.Schema.SMALL_INT
    ), glue.Column(
        name="month",
        type=glue.Schema.SMALL_INT
    )],
    partition_indexes=[glue.PartitionIndex(
        index_name="my-index",  # optional
        key_names=["year"]
    )],  # supply up to 3 indexes
    data_format=glue.DataFormat.JSON
)
```

Alternatively, you can call the `addPartitionIndex()` function on a table:

```python
# my_table: glue.Table

my_table.add_partition_index(
    index_name="my-index",
    key_names=["year"]
)
```

### Partition Filtering

If you have a table with a large number of partitions that grows over time, consider using AWS Glue partition indexing and filtering.

```python
# my_database: glue.Database

glue.S3Table(self, "MyTable",
    database=my_database,
    columns=[glue.Column(
        name="col1",
        type=glue.Schema.STRING
    )],
    partition_keys=[glue.Column(
        name="year",
        type=glue.Schema.SMALL_INT
    ), glue.Column(
        name="month",
        type=glue.Schema.SMALL_INT
    )],
    data_format=glue.DataFormat.JSON,
    enable_partition_filtering=True
)
```

### Glue Connections

Glue connections allow external data connections to third party databases and data warehouses. However, these connections can also be assigned to Glue Tables, allowing you to query external data sources using the Glue Data Catalog.

Whereas `S3Table` will point to (and if needed, create) a bucket to store the tables' data, `ExternalTable` will point to an existing table in a data source. For example, to create a table in Glue that points to a table in Redshift:

```python
# my_connection: glue.Connection
# my_database: glue.Database

glue.ExternalTable(self, "MyTable",
    connection=my_connection,
    external_data_location="default_db_public_example",  # A table in Redshift
    # ...
    database=my_database,
    columns=[glue.Column(
        name="col1",
        type=glue.Schema.STRING
    )],
    data_format=glue.DataFormat.JSON
)
```

## [Encryption](https://docs.aws.amazon.com/athena/latest/ug/encryption.html)

You can enable encryption on a Table's data:

* [S3Managed](https://docs.aws.amazon.com/AmazonS3/latest/dev/UsingServerSideEncryption.html) - (default) Server side encryption (`SSE-S3`) with an Amazon S3-managed key.

```python
# my_database: glue.Database

glue.S3Table(self, "MyTable",
    encryption=glue.TableEncryption.S3_MANAGED,
    # ...
    database=my_database,
    columns=[glue.Column(
        name="col1",
        type=glue.Schema.STRING
    )],
    data_format=glue.DataFormat.JSON
)
```

* [Kms](https://docs.aws.amazon.com/AmazonS3/latest/dev/UsingKMSEncryption.html) - Server-side encryption (`SSE-KMS`) with an AWS KMS Key managed by the account owner.

```python
# my_database: glue.Database

# KMS key is created automatically
glue.S3Table(self, "MyTable",
    encryption=glue.TableEncryption.KMS,
    # ...
    database=my_database,
    columns=[glue.Column(
        name="col1",
        type=glue.Schema.STRING
    )],
    data_format=glue.DataFormat.JSON
)

# with an explicit KMS key
glue.S3Table(self, "MyTable",
    encryption=glue.TableEncryption.KMS,
    encryption_key=kms.Key(self, "MyKey"),
    # ...
    database=my_database,
    columns=[glue.Column(
        name="col1",
        type=glue.Schema.STRING
    )],
    data_format=glue.DataFormat.JSON
)
```

* [KmsManaged](https://docs.aws.amazon.com/AmazonS3/latest/dev/UsingKMSEncryption.html) - Server-side encryption (`SSE-KMS`), like `Kms`, except with an AWS KMS Key managed by the AWS Key Management Service.

```python
# my_database: glue.Database

glue.S3Table(self, "MyTable",
    encryption=glue.TableEncryption.KMS_MANAGED,
    # ...
    database=my_database,
    columns=[glue.Column(
        name="col1",
        type=glue.Schema.STRING
    )],
    data_format=glue.DataFormat.JSON
)
```

* [ClientSideKms](https://docs.aws.amazon.com/AmazonS3/latest/dev/UsingClientSideEncryption.html#client-side-encryption-kms-managed-master-key-intro) - Client-side encryption (`CSE-KMS`) with an AWS KMS Key managed by the account owner.

```python
# my_database: glue.Database

# KMS key is created automatically
glue.S3Table(self, "MyTable",
    encryption=glue.TableEncryption.CLIENT_SIDE_KMS,
    # ...
    database=my_database,
    columns=[glue.Column(
        name="col1",
        type=glue.Schema.STRING
    )],
    data_format=glue.DataFormat.JSON
)

# with an explicit KMS key
glue.S3Table(self, "MyTable",
    encryption=glue.TableEncryption.CLIENT_SIDE_KMS,
    encryption_key=kms.Key(self, "MyKey"),
    # ...
    database=my_database,
    columns=[glue.Column(
        name="col1",
        type=glue.Schema.STRING
    )],
    data_format=glue.DataFormat.JSON
)
```

*Note: you cannot provide a `Bucket` when creating the `S3Table` if you wish to use server-side encryption (`KMS`, `KMS_MANAGED` or `S3_MANAGED`)*.

## Types

A table's schema is a collection of columns, each of which have a `name` and a `type`. Types are recursive structures, consisting of primitive and complex types:

```python
# my_database: glue.Database

glue.S3Table(self, "MyTable",
    columns=[glue.Column(
        name="primitive_column",
        type=glue.Schema.STRING
    ), glue.Column(
        name="array_column",
        type=glue.Schema.array(glue.Schema.INTEGER),
        comment="array<integer>"
    ), glue.Column(
        name="map_column",
        type=glue.Schema.map(glue.Schema.STRING, glue.Schema.TIMESTAMP),
        comment="map<string,string>"
    ), glue.Column(
        name="struct_column",
        type=glue.Schema.struct([
            name="nested_column",
            type=glue.Schema.DATE,
            comment="nested comment"
        ]),
        comment="struct<nested_column:date COMMENT 'nested comment'>"
    )],
    # ...
    database=my_database,
    data_format=glue.DataFormat.JSON
)
```

### Primitives

#### Numeric

| Name      	| Type     	| Comments                                                                                                          |
|-----------	|----------	|------------------------------------------------------------------------------------------------------------------	|
| FLOAT     	| Constant 	| A 32-bit single-precision floating point number                                                                   |
| INTEGER   	| Constant 	| A 32-bit signed value in two's complement format, with a minimum value of -2^31 and a maximum value of 2^31-1 	|
| DOUBLE    	| Constant 	| A 64-bit double-precision floating point number                                                                   |
| BIG_INT   	| Constant 	| A 64-bit signed INTEGER in two’s complement format, with a minimum value of -2^63 and a maximum value of 2^63 -1  |
| SMALL_INT 	| Constant 	| A 16-bit signed INTEGER in two’s complement format, with a minimum value of -2^15 and a maximum value of 2^15-1   |
| TINY_INT  	| Constant 	| A 8-bit signed INTEGER in two’s complement format, with a minimum value of -2^7 and a maximum value of 2^7-1      |

#### Date and time

| Name      	| Type     	| Comments                                                                                                                                                                	|
|-----------	|----------	|-------------------------------------------------------------------------------------------------------------------------------------------------------------------------	|
| DATE      	| Constant 	| A date in UNIX format, such as YYYY-MM-DD.                                                                                                                              	|
| TIMESTAMP 	| Constant 	| Date and time instant in the UNiX format, such as yyyy-mm-dd hh:mm:ss[.f...]. For example, TIMESTAMP '2008-09-15 03:04:05.324'. This format uses the session time zone. 	|

#### String

| Name                                       	| Type     	| Comments                                                                                                                                                                                          	|
|--------------------------------------------	|----------	|---------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------	|
| STRING                                     	| Constant 	| A string literal enclosed in single or double quotes                                                                                                                                              	|
| decimal(precision: number, scale?: number) 	| Function 	| `precision` is the total number of digits. `scale` (optional) is the number of digits in fractional part with a default of 0. For example, use these type definitions: decimal(11,5), decimal(15) 	|
| char(length: number)                       	| Function 	| Fixed length character data, with a specified length between 1 and 255, such as char(10)                                                                                                          	|
| varchar(length: number)                    	| Function 	| Variable length character data, with a specified length between 1 and 65535, such as varchar(10)                                                                                                  	|

#### Miscellaneous

| Name    	| Type     	| Comments                      	|
|---------	|----------	|-------------------------------	|
| BOOLEAN 	| Constant 	| Values are `true` and `false` 	|
| BINARY  	| Constant 	| Value is in binary            	|

### Complex

| Name                                	| Type     	| Comments                                                          	|
|-------------------------------------	|----------	|-------------------------------------------------------------------	|
| array(itemType: Type)               	| Function 	| An array of some other type                                       	|
| map(keyType: Type, valueType: Type) 	| Function 	| A map of some primitive key type to any value type                	|
| struct(collumns: Column[])          	| Function 	| Nested structure containing individually named and typed collumns 	|

## Data Quality Ruleset

A `DataQualityRuleset` specifies a data quality ruleset with DQDL rules applied to a specified AWS Glue table. For example, to create a data quality ruleset for a given table:

```python
glue.DataQualityRuleset(self, "MyDataQualityRuleset",
    client_token="client_token",
    description="description",
    ruleset_name="ruleset_name",
    ruleset_dqdl="ruleset_dqdl",
    tags={
        "key1": "value1",
        "key2": "value2"
    },
    target_table=glue.DataQualityTargetTable("database_name", "table_name")
)
```

For more information, see [AWS Glue Data Quality](https://docs.aws.amazon.com/glue/latest/dg/glue-data-quality.html).
