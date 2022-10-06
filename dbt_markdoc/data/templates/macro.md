# [`{{ name }}`]({{ path }})

{{ description or "No description provided" -}}

{% if arguments -%}

## Arguments

{% for arg in arguments -%}

* `{{ arg.name }}` : *`{{ arg.type }}`*{{ "(default: *`" ~ arg.default ~ "`*)" if arg.default is defined }}

    {{ arg.description }}

{% endfor -%}

{% if usage_info -%}

## Usage

{{ usage_info }}

{% endif -%}
{% endif -%}
