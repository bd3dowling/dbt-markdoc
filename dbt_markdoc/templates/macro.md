# [{{ name }}]({{ path }})

{{ description }}

## Arguments

{% for arg in arguments -%}

* `{{ arg.name }}` : *`{{ arg.type }}`*{{ "(default: *`" ~ arg.default ~ "`*)" if arg.default is defined }}

    {{ arg.description }}

{% endfor -%}

{% if meta.usage -%}

## Usage

{{ meta.usage }}

{% endif %}
