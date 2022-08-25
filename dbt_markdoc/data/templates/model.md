# [{{ name }}]({{ path }})

{{ description }}

## Columns

{% for col in columns -%}

* `{{ col.name }}` : *`{{ col.date_type }}`*

    {{ col.description }}

{% endfor -%}

## Dependencies

### Models

{% for model in dependencies.models -%}

* `[{{ model.name }}]({{ model.path }})`

{% endfor -%}

### Sources

{% for source in dependencies.sources -%}

* `[{{ source.name }}]({{ source.path }})`

{% endfor -%}

### Macros

{% for macro in dependencies.macros -%}

* `[{{ macro.anme }}]({{ macro.path }})`

{% endfor -%}
