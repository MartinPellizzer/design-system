###############################
# ;tier 1
###############################
### ;color_brown
color_brand_brown_50 = '#efebe9'
color_brand_brown_100 = '#d7ccc8'
color_brand_brown_700 = '#5d4037'
color_brand_brown_900 = '#3e2723'
### ;color_gray
color_brand_white = '#ffffff'
color_brand_grey_50 = '#fafafa'
color_brand_grey_100 = '#f5f5f5'
color_brand_grey_200 = '#eeeeee'
color_brand_grey_300 = '#e0e0e0'
color_brand_grey_400 = '#bdbdbd'
color_brand_grey_500 = '#9e9e9e'
color_brand_grey_600 = '#757575'
color_brand_grey_700 = '#616161'
color_brand_grey_800 = '#424242'
color_brand_grey_900 = '#212121'
color_brand_black = '#000000'

###############################
# ;tier 2
###############################
### ;content
color_content_default = color_brand_grey_900
color_content_default_hover = color_brand_grey_600
color_content_subtle = color_brand_grey_600
color_content_knockout = color_brand_white
color_content_brand = color_brand_brown_900
color_content_brand_hover = color_brand_brown_700
color_content_disabled = color_brand_grey_500
### ;background
color_background_brand = color_brand_brown_50
### ;border
color_border_brand = color_brand_brown_900

###############################
# ;tier 3
###############################
### ;content
button_color_content_default = color_content_brand
### ;background
button_color_background_default = color_background_brand
### ;border
button_color_border_default = color_border_brand

css = []
glob_prefix = 'ds'
tier_prefix = 'theme'
css.append(':root {')
css.append(f'    --{glob_prefix}-{tier_prefix}-color-content-default: {color_content_default};')
css.append(f'    --{glob_prefix}-{tier_prefix}-color-content-default-hover: {color_content_default_hover};')
css.append(f'    --{glob_prefix}-{tier_prefix}-color-content-subtle: {color_content_subtle};')
css.append(f'    --{glob_prefix}-{tier_prefix}-color-content-knockout: {color_content_knockout};')
css.append(f'    --{glob_prefix}-{tier_prefix}-color-content-brand-hover: {color_content_brand_hover};')
css.append(f'    --{glob_prefix}-{tier_prefix}-color-content-brand: {color_content_brand};')
css.append(f'    --{glob_prefix}-{tier_prefix}-color-content-disabled: {color_content_disabled};')
css.append(f'    --{glob_prefix}-{tier_prefix}-button-color-content-default: {button_color_content_default};')
css.append(f'    --{glob_prefix}-{tier_prefix}-button-color-background-default: {button_color_background_default};')
css.append(f'    --{glob_prefix}-{tier_prefix}-button-color-border-default: {button_color_border_default};')
css.append('}\n')

css.append(f'''.ds-c-heading {{
    color: var(--{glob_prefix}-{tier_prefix}-color-content-brand);
}}\n''')
css.append(f'''.ds-c-paragraph {{
    color: var(--{glob_prefix}-{tier_prefix}-color-content-default);
}}\n''')
css.append(f'''.ds-c-button {{
    color: var(--{glob_prefix}-{tier_prefix}-button-color-content);
    background-color: var(--{glob_prefix}-{tier_prefix}-button-color-background);
    border: 1px solid var(--{glob_prefix}-{tier_prefix}-button-color-border);
    padding: 8px 16px;
    text-decoration-line: none;
}}\n''')

css_output = '\n'.join(css)
with open('style.css', 'w') as f: f.write(css_output)


###############################################################
# html
###############################################################

html_output = f'''
    <!DOCTYPE html>
    <html lang="en">
    <head>
        <meta charset="UTF-8">
        <meta name="viewport" content="width=device-width, initial-scale=1.0">
        <link rel="stylesheet" href="style.css">
        <title>Design System - Preview</title>
    </head>
    <body>
        <h1 class="ds-c-heading">Heading 1</h1>
        <p class="ds-c-paragraph">This is a short paragraph.</h1>
        <div>
            <a class="ds-c-button" href="#">Button 1</a>
        </div>
    </body>
    </html>
'''
with open('index.html', 'w') as f: f.write(html_output)
