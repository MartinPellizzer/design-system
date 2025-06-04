t1_colors = {
    'color': {
        'brand': {
            'brown': {
                '50': {
                    'value': '#efebe9',
                },
                '100': {
                    'value': '#d7ccc8',
                },
                '900': {
                    'value': '#3e2723',
                },
            },
            'grey': {
                '900': {
                    'value': '#212121',
                },
            },
        },
    },
}
tier_1_definitions = []


t2_colors = {
    'color': {
        'content': {
            'brand': {
                'value': t1_colors['color']['brand']['brown']['900']['value'],
            }
        },
        'background': {
            'brand': {
                'value': t1_colors['color']['brand']['brown']['50']['value'],
            }
        },
        'border': {
            'brand': {
                'value': t1_colors['color']['brand']['brown']['900']['value'],
            }
        },
    },
}
tier_2_usage = []


t3_buttons = {
    'button': {
        'color': {
            'content': {
                'value': t2_colors['color']['content']['brand']['value'],
            },
            'background': {
                'value': t2_colors['color']['background']['brand']['value'],
            },
            'border': {
                'value': t2_colors['color']['border']['brand']['value'],
            },
        },
    },
}
tier_3_component = []

### t1
for l1_key, l1_val in t1_colors.items():
    for l2_key, l2_val in t1_colors[l1_key].items():
        for l3_key, l3_val in t1_colors[l1_key][l2_key].items():
            for l4_key, l4_val in t1_colors[l1_key][l2_key][l3_key].items():
                for l5_key, l5_val in t1_colors[l1_key][l2_key][l3_key][l4_key].items():
                    css.append(f'    --{glob_prefix}-{l1_key}-{l2_key}-{l3_key}-{l4_key}: {l5_val};')
### t2
for l1_key, l1_val in t2_colors.items():
    for l2_key, l2_val in t2_colors[l1_key].items():
        for l3_key, l3_val in t2_colors[l1_key][l2_key].items():
            for l4_key, l4_val in t2_colors[l1_key][l2_key][l3_key].items():
                css.append(f'    --{glob_prefix}-{tier_prefix}-{l1_key}-{l2_key}-{l3_key}: {l4_val};')
### t3
for l1_key, l1_val in t3_buttons.items():
    for l2_key, l2_val in t3_buttons[l1_key].items():
        for l3_key, l3_val in t3_buttons[l1_key][l2_key].items():
            for l4_key, l4_val in t3_buttons[l1_key][l2_key][l3_key].items():
                css.append(f'    --{glob_prefix}-{tier_prefix}-{l1_key}-{l2_key}-{l3_key}: {l4_val};')

button_color_content = color_content_brand


typography = [
]

spacing = {
    '0': {
        'value': '0px',
    },
    '4': {
        'value': '4px',
    },
    '8': {
        'value': '8px',
    },
    '12': {
        'value': '12px',
    },
    '16': {
        'value': '16px',
    },
    '20': {
        'value': '20px',
    },
    '24': {
        'value': '24px',
    },
    '28': {
        'value': '28px',
    },
    '32': {
        'value': '32px',
    },
    '48': {
        'value': '48px',
    },
    '64': {
        'value': '64px',
    },
    '96': {
        'value': '96px',
    },
    '128': {
        'value': '128px',
    },
}

ds_t2_spacing_96 = spacing['96']

