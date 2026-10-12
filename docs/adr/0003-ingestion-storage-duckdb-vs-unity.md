# Ingestion Storage: Parquet + DuckDB vs. Parquet + Unity Catalog

## Title
Ingestion Storage: Parquet + DuckDB vs. Parquet + Unity Catalog

## Status
Proposed

## Context
We need to decide on the storage solution for our ingestion pipelines. We have two options: Parquet + DuckDB and Parquet + Unity Catalog.

## Decision
We will use Partitioned Parquet files on disk + DuckDB for local SQL querying (fast, zero-infrastructure, embedded) while maintaining catalog compatibility for future scaling.

## Consequences
This will allow us to have a lightweight, file-based querying system that is easy to set up and use. Partitioning the Parquet files will improve query performance and scalability.
