import re
import time
import requests
from mysql import MySQL
from bs4 import BeautifulSoup

# 打开数据库连接
mysql = MySQL()

# 获取html信息
def get_html( url ):
    strhtml = requests.get(url)
    return BeautifulSoup(strhtml.text,'lxml')

# 根据数据标签获取text值，必须为单数组
# 特殊字符\u3000、\xa0、\n、\t
def get_text_local( soup, selector ):
    arr = soup.select(selector)
    # print(arr)
    for item in arr:
        str = item.get_text()
        str = str.replace("\n", "", 10)
        str = str.replace("\t", "", 10)
        str = str.replace("\xa0", "", 10)
        str = str.replace("\u3000", "", 10)
        str = str.replace("■号码：", "", 10)
        str = str.replace("■最近车站到校路线", "", 1)
        return str

def str_to_date(publish_Time): 
    try:
        array = time.strptime(publish_Time, u"%Y年%m月%d日")
        publishTime = time.strftime("%Y-%m-%d", array)
    except Exception as e:
        publishTime = ""
    # print(publishTime)
    return publishTime


# 学校的基础信息
def get_baseInfo( soup, id ): 
    # print(f'开始爬取基本信息：id={id}')
    school = {}
    school.setdefault('id', id)
    school.setdefault('code', get_text_local( soup,'.floL'))
    school.setdefault('name', get_text_local( soup,'#mainPad > h2'))
    if(school['name'] != '' and school['name'] != 'ゲスト'):
        school.setdefault('introduce', get_text_local( soup,'#mainPad > p.bsp10.center'))
        school.setdefault('zip_code', get_text_local( soup,'.lsp20'))
        school.setdefault('address', get_text_local( soup,'.lsp10'))
        school.setdefault('telephone', get_text_local( soup,'#mainPad > table:nth-child(4) > tr:nth-child(1) > td > table > tr:nth-child(2) > td:nth-child(2)'))
        school.setdefault('fax', get_text_local( soup,'#mainPad > table:nth-child(4) > tr:nth-child(1) > td > table > tr:nth-child(3) > td:nth-child(2)'))
        school.setdefault('website', get_text_local( soup,'#mainPad > table:nth-child(4) > tr:nth-child(1) > td > table > tr:nth-child(4) > td:nth-child(2) > a'))
        school.setdefault('e_mail', get_text_local( soup,'#mainPad > table:nth-child(4) > tr:nth-child(1) > td > table > tr:nth-child(5) > td:nth-child(2)'))
        school.setdefault('way', get_text_local( soup,'#mainPad > table:nth-child(4) > tr:nth-child(1) > td > table > tr:nth-child(2) > td:nth-child(3)'))
        school.setdefault('type', get_text_local( soup,'#mainPad > table:nth-child(4) > tr:nth-child(2) > td > table > tr:nth-child(2) > td:nth-child(2)'))
        school.setdefault('representative', get_text_local( soup,'#mainPad > table:nth-child(4) > tr:nth-child(2) > td > table > tr:nth-child(3) > td:nth-child(2)'))
        school.setdefault('principal', get_text_local( soup,'#mainPad > table:nth-child(4) > tr:nth-child(2) > td > table > tr:nth-child(4) > td:nth-child(2)'))
        school.setdefault('classify', get_text_local( soup,'#mainPad > table:nth-child(4) > tr:nth-child(2) > td > table > tr:nth-child(5) > td:nth-child(4)'))
        
        strDate = get_text_local( soup,'#mainPad > table:nth-child(4) > tr:nth-child(2) > td > table > tr:nth-child(1) > td:nth-child(4)')
        school.setdefault('tech_start_time', str_to_date(strDate))
        
        school.setdefault('cognizance_time', get_text_local( soup,'#mainPad > table:nth-child(4) > tr:nth-child(2) > td > table > tr:nth-child(2) > td:nth-child(4)'))
        school.setdefault('teacher_count', get_text_local( soup,'#mainPad > table:nth-child(4) > tr:nth-child(2) > td > table > tr:nth-child(3) > td:nth-child(4)'))
        
        count_text = get_text_local( soup,'#mainPad > table:nth-child(4) > tr:nth-child(2) > td > table > tr:nth-child(4) > td:nth-child(4)')
        count = re.findall(r'\d+', count_text)[0]
        school.setdefault('count', count)

        school.setdefault('dormitory', get_text_local( soup,'#mainPad > table:nth-child(4) > tr:nth-child(2) > td > table > tr:nth-child(5) > td:nth-child(4)'))
        school.setdefault('gre', get_text_local( soup,'#mainPad > table:nth-child(4) > tr:nth-child(3) > td > table > tr:nth-child(1) > td:nth-child(2)'))
        school.setdefault('enter_method', get_text_local( soup,'#mainPad > table:nth-child(4) > tr:nth-child(3) > td > table > tr:nth-child(2) > td:nth-child(2)'))
        
        other_count = get_text_local( soup, '#mainPad > table:nth-child(7) > tr:nth-child(4) > td')
        if(other_count == ''):
            other_count = 0
        now_count_text = get_text_local( soup, '#mainPad > table:nth-child(7) > tr:nth-child(3) > td:nth-child(10)')
        now_count = int(re.findall(r'\d+', now_count_text)[0]) + int(other_count)
        school.setdefault('now_count', now_count)
        # print(school)
        # mysql.insert('rb_school', school)
        # print(f'爬取基本信息完成，id={id}。')
        return school
    else:    
        print(f'爬取：{id}号学校失败。原因：学校不存在。')
        return {}
        
# 各国学生人数信息的爬取
def get_country( soup, id ):
    # print(f"开始爬取的学生人数信息：id={id}。")
    clist = []
    arr = soup.select('#mainPad > table:nth-child(7) > tr > td.center')
    
    for item in arr:
        str = item.get_text()
        name = re.findall(r'\D+', str)[0]
        count = re.findall(r'\d+', str)[0]
        name = name.replace("\n", "", 10)
        name = name.replace("\t", "", 10)
        if(name != '合计'):
            clist.append((id, name, count))
    # mysql.batch_insert_student_count(clist)
    # print(f"爬取学生人数信息完成，id={id}。")
    return clist

# 爬取课程信息
def get_course( soup, id ):
    courseList = []
    tr_arr = soup.select('#mainPad > table:nth-child(10) > tr')
    for tr in tr_arr:
        tds = tr.find_all('td')
        course = [id]
        for td in tds:
            text = td.get_text()
            text = text.replace("\n", "", 10)
            text = text.replace("\t", "", 10)
            text = text.replace("\xa0", "", 10)
            course.append(text)

        if(len(course) > 3 and course[5] != ''):
            courseList.append(tuple(course))
    
    # print(courseList)
    return courseList

def get_level_info(soup, id):
    level_list = []

    level_name_td = soup.select('#mainPad > table.tableStyle03 > tr:nth-child(1)')[0].find_all('th')
    exam_count_td = soup.select('#mainPad > table.tableStyle03 > tr:nth-child(2)')[0].find_all('td')
    qualified_count_td = soup.select('#mainPad > table.tableStyle03 > tr:nth-child(3)')[0].find_all('td')
    # print(level_name_td)
    for num in range(1, 6):
        level_name = level_name_td[num].get_text()
        exam_count = exam_count_td[num - 1].get_text()
        qualified_count = qualified_count_td[num - 1].get_text()
        level_list.append((id, level_name, exam_count, qualified_count))
    # print(level_list)
    return level_list

def get_exam_info(soup, id):
    exam_list = []

    exam_tds = soup.select('#mainPad > table:nth-child(16) > tr:nth-child(5)')[0].find_all('td')

    exam_list.append(( id, '日语', exam_tds[0].get_text(), exam_tds[1].get_text(), 0, '日语', exam_tds[6].get_text(), exam_tds[7].get_text(), 0 ))
    exam_list.append(( id, '文科', exam_tds[2].get_text(), 0, exam_tds[3].get_text(), '文科', exam_tds[8].get_text(), 0, exam_tds[9].get_text() ))
    exam_list.append(( id, '理科', exam_tds[4].get_text(), 0, exam_tds[5].get_text(), '理科', exam_tds[10].get_text(), 0, exam_tds[11].get_text()) )

    return exam_list

def get_enter_count(soup, id):
    enter_list = []

    enter_tds = soup.select('#mainPad > table:nth-child(19) > tr:nth-child(2)')[0].find_all('td')

    enters = [id]
    for td in enter_tds:
        text = td.get_text()
        text = text.replace("\n", "", 10)
        text = text.replace("\t", "", 10)
        text = text.replace("\xa0", "", 10)
        if(text != ''):
            enters.append(text)
    
    enter_list.append(tuple(enters))
    # print(enter_list)
    return enter_list

def get_tese(soup, id):
    tese_list = []

    tese_trs = soup.select('#mainPad > table:nth-child(22)')[0].find_all('tr')

    for tr in tese_trs:
        tese = [id]
        td = tr.find_all('td')[0]
        text = td.get_text()
        text = text.replace("\n", "", 10)
        text = text.replace("\t", "", 10)
        text = text.replace("\xa0", "", 10)
        tese.append(text)
        tese_list.append(tuple(tese))
    # print(tese_list)
    return tese_list

def run(id):
    print(f'开始爬取：{id}号学校...')
    url = f'https://www.nisshinkyo.org/search/college.php?lng=3&id={id}'
    soup = get_html(url)

    baseInfo = get_baseInfo(soup, id)
    if 'id' in baseInfo :
        # 获取各国学生人数信息
        clist  = get_country(soup, id)
        courseList =  get_course(soup, id)

        levelList = get_level_info(soup, id)

        examList = get_exam_info(soup, id)

        enterList = get_enter_count(soup, id)

        teseList = get_tese(soup, id)

        # 批量插入或更新基本信息
        mysql.insert('rb_school', baseInfo)

        # 批量插入或更新各国学生信息
        mysql.batch_insert_student_count(clist, id)

        # 批量插入或更新课程信息
        mysql.batch_insert_course_info(courseList, id)

        # 批量插入或更新等级信息
        mysql.batch_insert_level_info(levelList, id)

        # 批量插入或更新考试信息
        mysql.batch_insert_exam_info(examList, id)

        # 批量插入或更新升学信息
        mysql.batch_insert_enter_info(enterList, id)

        # 批量插入或更新教育特色信息
        mysql.batch_insert_tese_info(teseList, id)

        print(f'成功爬取：{id}号学校。')
    
if __name__ == '__main__':

    ids = mysql.getAllSchool()
    # print(schoolList)
    for id in ids:
        run(id[0])