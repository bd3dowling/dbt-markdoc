# [{{ name }}]({{ path }})

{{ description }}

## Source Info

Source Name: {{ source_name }}

Source Description: {{ source_description }}

Source Database: {{ source_database }}

Source Schema: {{ source_schema }}

## Columns

{{ 'No columns described' if not columns -}}

{% for col in columns -%}

* `{{ col.name }}` : *`{{ col.date_type }}`*

    {{ col.description }}

{% endfor -%}
