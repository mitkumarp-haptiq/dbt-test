{% macro create_intermediate_users_table_if_not_exists() %}
  {%- set create_schema -%}
    create schema if not exists intermediate
  {%- endset -%}
  {% do run_query(create_schema) %}
  {%- set create_table -%}
    create table if not exists intermediate.users (
      name text,
      phone_number text,
      date_of_birth date
    )
  {%- endset -%}
  {% do run_query(create_table) %}
{% endmacro %}
