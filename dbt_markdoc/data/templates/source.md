# [`{{ name }}`]({{ path }})

{{ description }}

## Source Info

**Name**: `{{ source_name }}`

**Description**: {{ source_description or "Not provided" }}

**Database**: `{{ database | upper }}`

**Schema**: `{{ schema_ | upper }}`

## Columns

{{ "No column metadata provided" if not columns -}}

{% for col in columns -%}

* `{{ col.name }}` : *`{{ col.date_type }}`*

    {{ col.description }}

{% endfor %}
