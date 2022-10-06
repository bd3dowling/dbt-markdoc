# [`{{ name }}`]({{ path }})

{{ description or "No description provided" }}

## Columns

{{ "No column metadata provided" if not columns }}

{%- for col in columns -%}

* `{{ col.name }}` : *`{{ col.data_type or "Unknown" }}`*

    {{ col.description }}

{% endfor %}

## Dependencies

{% if depends_on.models -%}

### Models

{% for model in depends_on.models -%}

* [`{{ model.name }}`]({{ model.path }})

{% endfor -%}

{% endif -%}

{% if depends_on.sources -%}

### Sources

{% for source in depends_on.sources -%}

* [`{{ source.name }}`]({{ source.path }})

{% endfor -%}

{% endif -%}

{% if depends_on.macros -%}

### Macros

{% for macro in depends_on.macros -%}

* [`{{ macro.name }}`]({{ macro.path }})

{% endfor -%}

{% endif -%}
