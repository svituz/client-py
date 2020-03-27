#
#  CodeSystems.py
#  client-py
#
#  Generated from FHIR {{ info.version }}
#  {{ info.year }}, SMART Health IT.
#
#  THIS HAS BEEN ADAPTED FROM Swift Enums WITHOUT EVER BEING IMPLEMENTED IN
#  Python, FOR DEMONSTRATION PURPOSES ONLY.
#
{%- if system.generate_enum %}

class {{system.name}}(object):
    """ {{ system.definition.description|wordwrap(width=120, wrapstring="\n") }}
    URL: {{ system.url }}
    {%- if system.definition.valueSet %}
    ValueSet: {{ system.definition.valueSet }}
    {%- endif %}
    """
    {%- for code in system.codes %}
    # {{ code.definition|wordwrap(width=112, wrapstring="\n	/// ") }}
    {{code.name}} = "{{ code.code }}"
    {%- endfor %}
{%- endif %}
