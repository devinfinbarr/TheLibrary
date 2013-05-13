
from optparse import OptionParser
import os
import shutil
import time

from jinja2 import Environment, FileSystemLoader

this_path = os.path.abspath(os.path.dirname(__file__))
base_path = os.path.join(this_path, '..')
templates_path = os.path.join(base_path, './website')
catalog_path = os.path.join(base_path, './catalog')

def main():
    parser = OptionParser()
    parser.add_option('-u', '--upload', help='actually perform the upload to S3', action='store_true')
    options = parser.parse_args()[0]
    upload_website(options)

def upload_website(options):
    all_categories = []
    root_category = CatalogParser().parse_directory(catalog_path, all_categories, 0, '', '')
    build_path = build_web_pages(root_category, all_categories)
    if options.upload:
        upload_to_s3()
    
def build_web_pages(root_category, all_categories):
    build_path = base_path + '/build/latest'
    ticks = long(time.time())*1000
    if os.path.isdir(build_path):
        os.rename(build_path, base_path + '/build/website-%s' % (ticks))
    os.makedirs(build_path)
    shutil.copytree(templates_path + '/resources', build_path + '/resources')
    context = {
        'root_category': root_category,
        'all_categories': all_categories,
        'page_title': '1,200 Pages: Curated Reading Lists Covering Every Topic',
        'cache_buster': ticks,
        'category': Category(),
        }
    environment = Environment(loader=FileSystemLoader(templates_path))
    home_template = environment.get_template('home.html')
    html = home_template.render(context)
    f = open(build_path + '/index.html', 'w')
    f.write(html)
    f.close()
    page_template = environment.get_template('category-page.html')
    for category in all_categories:
        context['category'] = category
        context['page_title'] = category.title + ' | Best Books Reading List'
        out_path = build_path + category.url
        print "OUT PATH ", out_path
        folder = os.path.split(out_path)[0]
        if not os.path.isdir(folder):
            os.makedirs(folder)
        html = page_template.render(context)
        f = open(out_path, 'w')
        f.write(html)
        f.close()
    return build_path

def upload_to_s3():
    pass


class CatalogParser(object):
    def parse_directory(self, path, all_categories, level, parent_path, file_name):
        category = Category(level=level, parent_path=parent_path, directory_name=file_name)
        all_categories.append(category)
        index_path = path + '/index.txt'
        if os.path.isfile(index_path):
            f = open(index_path, 'r')
            text = f.read()
            f.close()
            self.parse_index_text(text, category)
        for file_name in os.listdir(path):
            full_path = path + '/' + file_name
            if os.path.isdir(full_path):
                category.children.append(self.parse_directory(full_path, all_categories, level + 1, category.path, file_name))
        return category                


    def parse_index_text(self, text, category):
        text = text.replace('\r', '')
        lines = text.split('\n')
        in_category_summary = False
        in_block_key = ''
        reading = None
        for i, line in enumerate(lines):
            if i == 0:
                title_line = lines[0]
                if ':' in title_line:
                    key, title = title_line.split(':', 1)
                else:
                    title = title_line
                category.title = title.strip()
            elif i == 1 and line.startswith('summary:'):
                in_category_summary = True
            elif in_category_summary:
                if line.startswith('end-summary'):
                    in_category_summary = False
                else:
                    category.summary += line
            elif line.startswith('*****'):
                reading = Reading()
                category.readings.append(reading)
            elif in_block_key:
                if line.startswith('end-%s' % in_block_key):
                    in_block_key = None
                else:
                    # append the line to the current value of the key we are processing
                    setattr(reading, in_block_key, getattr(reading, in_block_key, '') + '\n' + line)
            elif ':' in line:
                key, value = line.split(':', 1)
                value = value.strip()
                setattr(reading, key, value)
            elif line.startswith('-------'):
                reading = None
            else:
                continue
                

class Category(object):
    def __init__(self, title='', summary='', readings=None, children=None, level=0, parent_path='', directory_name=''):
        self.title = title
        self.summary = summary
        self.readings = readings or []
        self.children = children or []
        self.level = level
        self.path = parent_path + '/' + directory_name
        self.url = self.path + '.html'
        if not directory_name:
            self.path = ''
            self.url = '/root.html'
        
    @property
    def total_pages(self):
        total = 0
        for reading in self.readings:
            if str(reading.pages).isdigit():
                total += int(reading.pages)
        return total

    @property
    def total_percent_formatted(self):
        val = int(100 * self.total_pages / 1200.0)
        print "VAL ", val
        if val:
            return '%s%%' % val
        else:
            return '-'

class Reading(object):
    def __init__(
            self,
            title='',
            author='',
            publication_date='',
            selection='',
            free_link='',
            paid_link='',
            summary='',
            notes='',
            pages=0,
            ):
        self.title = title
        self.author = author
        self.publication_date = publication_date
        self.selection = selection
        self.free_link = free_link
        self.paid_link = paid_link
        self.summary = summary
        self.notes = notes
        self.pages = pages
        
    






if __name__ == "__main__":
    main()
