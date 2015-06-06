def gen_concept_HTML(section_title, section_information):
    html_1 = '''
<div class="sections">
    <div class="headings">
	  <h1 id = "python">''' + section_title
    html_2 = '''</h1>
    </div>
    <div class="section-information">
       <p>''' + section_information
    html_3 = '''</p>
    </div>
</div>'''
    
    all_html = html_1 + html_2 + html_3
    return all_html

def my_title(section):
    start_location = section.find('TITLE:')
    end_location = section.find('INFORMATION:')
    title = section[start_location+7 : end_location-1]
    return title

def my_information(section):
    start_location = section.find('INFORMATION:')
    information = section[start_location+13 :]
    return information

def my_section_by_num(text, sec_num):
    total = 0
    while total < sec_num:
        total = total + 1
        next_section_start = text.find('TITLE:')
        next_section_end   = text.find('TITLE:', next_section_start + 1)
        if next_section_end >= 0:
            section = text[next_section_start:next_section_end]
        else:
            next_section_end = len(text)
            section = text[next_section_start:]
        text = text[next_section_end:]
    return section

Stage2_Notes = """TITLE: Control Flow & Loops: If and While / Debugging
INFORMATION: This lesson brought a lot of new information that will be used a lot during our time learning programming, not only in Python but in future languages and code itself! 
TITLE: Structured Data: Lists and For Loops / How to Solve Problems
INFORMATION: For the final two sections of Stage 2 we came across new data types and some tips to solving problems for the future"""

#Only went with the last 2 sections of Stage 2 as I write my information into my notes as Andy describes in the class. This was made to see if it works.

def generate_all_html(text):
    current_section = 1
    section = my_section_by_num(text, current_section)
    all_html = ''
    while section != '':
        title = my_title(section)
        information = my_information(section)
        my_html = gen_concept_HTML(title, information)
        all_html = all_html + my_html
        current_section = current_section + 1
        section = my_section_by_num(text, current_section)
    return all_html


print generate_all_html(Stage2_Notes)