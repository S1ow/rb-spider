from setting import MYSQL_PORT, MYSQL_USER, MYSQL_HOST, MYSQL_DATABASE, MYSQL_PASSWORD
import pymysql


class MySQL:
    def __init__(self, host=MYSQL_HOST, username=MYSQL_USER, password=MYSQL_PASSWORD, port=MYSQL_PORT,
                 database=MYSQL_DATABASE):
        """
        MySQL初始化
        :param host:
        :param username:
        :param password:
        :param port:
        :param database:
        """
        try:
            self.db = pymysql.connect(host, username, password, database, charset='utf8', port=port)
            self.cursor = self.db.cursor()
        except pymysql.MySQLError as e:
            print(e.args)

    def selectById(self, table, id):
        """
        查询数据，根据id
        :param table:
        :param id:
        :return:
        """
        sql_query = 'select * from %s where id = %s' % (table, id)
        try:
            self.cursor.execute(sql_query)
            res = self.cursor.fetchone()
            return res
        except expression as identifier:
            print(e.args)

    def getAllSchool(self):
        """
        查询所有学校
        """
        sql_query = 'select id from rb_school'
        try:
            self.cursor.execute(sql_query)
            res = self.cursor.fetchall()
            return res
        except expression as identifier:
            print(e.args)

    def insert(self, table, data):
        """
        插入数据

        :param table:
        :param data:
        :return:
        """
        keys = ', '.join(data.keys())
        values = ', '.join(['%s'] * len(data))
        sql_query = 'replace into %s (%s) values (%s)' % (table, keys, values)
        try:
            self.cursor.execute(sql_query, tuple(data.values()))
            self.db.commit()
        except pymysql.MySQLError as e:
            print(e.args)
            self.db.rollback()
    
    def update(self, table, data):
        '''
        更新数据
        :param table:
        :param data:
        :return:
        '''
        keys = ', '.join(data.keys())
        values = ', '.join(['%s'] * len(data))
        sql_query = 'update %s set (%s) = (%s) where id = %s' % (table, keys, values, data['id'])
        try:
            print(sql_query)
            self.cursor.execute(sql_query, tuple(data.values()))
            self.db.commit()
        except pymysql.MySQLError as e:
            print(e.args)
            self.db.rollback()

    def insertOrUpdate(self, table, data):
        res = self.selectById(table, data['id'])
        if(len(res) > 0):
            self.update(table, data)
        else:
            self.insert(table, data)

    # 批量保存各国学生人数信息
    def batch_insert_student_count(self, data, id):
        sql_del = 'DELETE from rb_student_count WHERE school_id = %s'
        sql_query = 'insert into rb_student_count \
            ( school_id, country_name, count ) \
            values \
            ( %s, %s, %s )'
        try:
            self.cursor.execute(sql_del, id)
            self.db.commit
            self.cursor.executemany(sql_query, data)
            self.db.commit()
        except pymysql.MySQLError as e:
            print(e.args)
            self.db.rollback()

    # 批量保存课程信息
    def batch_insert_course_info(self, data, id):
        sql_del = 'DELETE from rb_course WHERE school_id = %s'
        sql_query = 'insert into rb_course \
            ( school_id, course_name, goal, during_lean, class_time, class_week, into_time, kaohe_fee, ruxuejin, xue_fee, other_fee, total_fee) \
            values \
            ( %s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s )'
        try:
            self.cursor.execute(sql_del, id)
            self.db.commit
            self.cursor.executemany(sql_query, data)
            self.db.commit()
        except pymysql.MySQLError as e:
            print(e.args)
            self.db.rollback()

    # 批量保存日语等级要求信息
    def batch_insert_level_info(self, data, id):
        sql_del = 'DELETE from rb_level_info WHERE school_id = %s'
        sql_query = 'insert into rb_level_info \
            ( school_id, level_name, exam_count, qualified_count) \
            values \
            ( %s, %s, %s, %s )'
        try:
            self.cursor.execute(sql_del, id)
            self.db.commit
            self.cursor.executemany(sql_query, data)
            self.db.commit()
        except pymysql.MySQLError as e:
            print(e.args)
            self.db.rollback()

    # 批量保存考试信息
    def batch_insert_exam_info(self, data, id):
        sql_del = 'DELETE from rb_exam WHERE school_id = %s'
        sql_query = 'insert into rb_exam \
            ( school_id, language1, exam_count1, score219_count1, score100_count1, language2, exam_count2, score219_count2, score100_count2 ) \
            values \
            ( %s, %s, %s, %s, %s, %s, %s, %s, %s )'
        try:
            self.cursor.execute(sql_del, id)
            self.db.commit
            self.cursor.executemany(sql_query, data)
            self.db.commit()
        except pymysql.MySQLError as e:
            print(e.args)
            self.db.rollback()

    # 批量保存入学录取信息
    def batch_insert_enter_info(self, data, id):
        sql_del = 'DELETE from rb_enter_count WHERE school_id = %s'
        sql_query = 'insert into rb_enter_count \
            ( school_id, college_count, school_count, junior_count, higher_count, specialize_count, various_count, other_count ) \
            values \
            ( %s, %s, %s, %s, %s, %s, %s, %s )'
        try:
            self.cursor.execute(sql_del, id)
            self.db.commit
            self.cursor.executemany(sql_query, data)
            self.db.commit()
        except pymysql.MySQLError as e:
            print(e.args)
            self.db.rollback()

    # 批量保存教育特色信息
    def batch_insert_tese_info(self, data, id):
        sql_del = 'DELETE from rb_tese WHERE school_id = %s'
        sql_query = 'insert into rb_tese \
            ( school_id, description ) \
            values \
            ( %s, %s)'
        try:
            self.cursor.execute(sql_del, id)
            self.db.commit
            self.cursor.executemany(sql_query, data)
            self.db.commit()
        except pymysql.MySQLError as e:
            print(e.args)
            self.db.rollback()
