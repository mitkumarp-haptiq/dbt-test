{% macro age_from_dob(date_of_birth, reference_date=none) %}
  {#-
    Integer age in completed years from date_of_birth to reference_date.
    When reference_date is omitted, uses the warehouse current date.

    Usage:
      select {{ age_from_dob('birth_date') }} as age from {{ ref('users') }}
      select {{ age_from_dob('birth_date', "'2024-01-01'") }} as age_at_snapshot from users
  -#}
  {{ return(adapter.dispatch('age_from_dob', 'test')(date_of_birth, reference_date)) }}
{% endmacro %}

{% macro postgres__age_from_dob(date_of_birth, reference_date) %}
  {% if reference_date is none %}
    (extract(year from age(current_date, ({{ date_of_birth }})::date))::integer)
  {% else %}
    (extract(year from age(({{ reference_date }})::date, ({{ date_of_birth }})::date))::integer)
  {% endif %}
{% endmacro %}

{% macro default__age_from_dob(date_of_birth, reference_date) %}
  {{ postgres__age_from_dob(date_of_birth, reference_date) }}
{% endmacro %}
