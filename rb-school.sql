/*
 Navicat Premium Data Transfer

 Source Server         : S1ow-开发库
 Source Server Type    : MySQL
 Source Server Version : 50728
 Source Host           : 127.0.0.1:33006
 Source Schema         : rb-school

 Target Server Type    : MySQL
 Target Server Version : 50728
 File Encoding         : 65001

 Date: 15/10/2020 10:21:14
*/

SET NAMES utf8mb4;
SET FOREIGN_KEY_CHECKS = 0;

-- ----------------------------
-- Table structure for rb_course
-- ----------------------------
DROP TABLE IF EXISTS `rb_course`;
CREATE TABLE `rb_course` (
  `id` int(11) NOT NULL AUTO_INCREMENT COMMENT '主键',
  `school_id` int(11) NOT NULL COMMENT '学校id',
  `course_name` varchar(64) COLLATE utf8mb4_bin DEFAULT NULL COMMENT '课程名称',
  `goal` varchar(16) COLLATE utf8mb4_bin DEFAULT NULL COMMENT '目的',
  `during_lean` varchar(64) COLLATE utf8mb4_bin DEFAULT NULL COMMENT '学习期间',
  `class_time` varchar(8) COLLATE utf8mb4_bin DEFAULT NULL COMMENT '上课时间',
  `class_week` int(2) DEFAULT NULL COMMENT '教课周数',
  `into_time` varchar(8) COLLATE utf8mb4_bin DEFAULT NULL COMMENT '入学时间',
  `kaohe_fee` varchar(16) COLLATE utf8mb4_bin DEFAULT NULL COMMENT '考核费',
  `ruxuejin` varchar(16) COLLATE utf8mb4_bin DEFAULT NULL COMMENT '入学金',
  `xue_fee` varchar(16) COLLATE utf8mb4_bin DEFAULT NULL COMMENT '学费',
  `other_fee` varchar(16) COLLATE utf8mb4_bin DEFAULT NULL COMMENT '其他',
  `total_fee` varchar(16) COLLATE utf8mb4_bin DEFAULT NULL COMMENT '合计',
  PRIMARY KEY (`id`)
) ENGINE=InnoDB AUTO_INCREMENT=1462 DEFAULT CHARSET=utf8mb4 COLLATE=utf8mb4_bin;

-- ----------------------------
-- Table structure for rb_enter_count
-- ----------------------------
DROP TABLE IF EXISTS `rb_enter_count`;
CREATE TABLE `rb_enter_count` (
  `id` int(11) NOT NULL AUTO_INCREMENT COMMENT '主键',
  `school_id` int(4) DEFAULT NULL COMMENT '学校id',
  `college_count` int(2) DEFAULT NULL COMMENT '大学院',
  `school_count` int(2) DEFAULT NULL COMMENT '大学',
  `junior_count` int(2) DEFAULT NULL COMMENT '短期大学',
  `higher_count` int(2) DEFAULT NULL COMMENT '高等专门学校',
  `specialize_count` int(2) DEFAULT NULL COMMENT '专修学校\n（专门课程）',
  `various_count` int(2) DEFAULT NULL COMMENT '各种学校',
  `other_count` int(2) DEFAULT NULL COMMENT '其他',
  PRIMARY KEY (`id`)
) ENGINE=InnoDB AUTO_INCREMENT=401 DEFAULT CHARSET=utf8mb4 COLLATE=utf8mb4_bin COMMENT='升学人数表';

-- ----------------------------
-- Table structure for rb_exam
-- ----------------------------
DROP TABLE IF EXISTS `rb_exam`;
CREATE TABLE `rb_exam` (
  `id` int(11) NOT NULL AUTO_INCREMENT COMMENT '主键id',
  `school_id` int(4) DEFAULT NULL COMMENT '学校id',
  `language1` varchar(255) COLLATE utf8mb4_bin DEFAULT NULL COMMENT '语言',
  `exam_count1` int(4) DEFAULT NULL COMMENT '应考者',
  `score219_count1` int(4) DEFAULT NULL COMMENT '得分219分\n以上者',
  `score100_count1` int(4) DEFAULT NULL COMMENT '得分100分\n以上者',
  `language2` varchar(255) COLLATE utf8mb4_bin DEFAULT NULL COMMENT '语言',
  `exam_count2` int(4) DEFAULT NULL COMMENT '应考者',
  `score219_count2` int(4) DEFAULT NULL COMMENT '得分219分\n以上者',
  `score100_count2` int(4) DEFAULT NULL COMMENT '得分100分\n以上者',
  PRIMARY KEY (`id`)
) ENGINE=InnoDB AUTO_INCREMENT=1207 DEFAULT CHARSET=utf8mb4 COLLATE=utf8mb4_bin;

-- ----------------------------
-- Table structure for rb_level_info
-- ----------------------------
DROP TABLE IF EXISTS `rb_level_info`;
CREATE TABLE `rb_level_info` (
  `id` int(11) NOT NULL AUTO_INCREMENT COMMENT '主键',
  `school_id` int(4) DEFAULT NULL COMMENT '学校id',
  `level_name` varchar(255) COLLATE utf8mb4_bin DEFAULT NULL COMMENT '等级名称',
  `exam_count` int(4) DEFAULT NULL COMMENT '应试人数',
  `qualified_count` int(4) DEFAULT NULL COMMENT '合格人数',
  PRIMARY KEY (`id`)
) ENGINE=InnoDB AUTO_INCREMENT=2030 DEFAULT CHARSET=utf8mb4 COLLATE=utf8mb4_bin COMMENT='日语等级表';

-- ----------------------------
-- Table structure for rb_school
-- ----------------------------
DROP TABLE IF EXISTS `rb_school`;
CREATE TABLE `rb_school` (
  `id` int(11) NOT NULL COMMENT '主键',
  `code` varchar(32) COLLATE utf8mb4_bin DEFAULT NULL COMMENT '号码',
  `name` varchar(255) COLLATE utf8mb4_bin DEFAULT NULL COMMENT '学校名称',
  `introduce` varchar(255) COLLATE utf8mb4_bin DEFAULT NULL COMMENT '学校简介',
  `zip_code` varchar(16) COLLATE utf8mb4_bin DEFAULT NULL COMMENT '邮编',
  `address` varchar(255) COLLATE utf8mb4_bin DEFAULT NULL COMMENT '地址',
  `telephone` varchar(32) COLLATE utf8mb4_bin DEFAULT NULL COMMENT '电话',
  `fax` varchar(255) COLLATE utf8mb4_bin DEFAULT NULL COMMENT '传真',
  `website` varchar(255) COLLATE utf8mb4_bin DEFAULT NULL COMMENT '网址',
  `e_mail` varchar(255) COLLATE utf8mb4_bin DEFAULT NULL COMMENT 'E-Mail',
  `way` varchar(255) COLLATE utf8mb4_bin DEFAULT NULL COMMENT '最近地铁路线',
  `type` varchar(32) COLLATE utf8mb4_bin DEFAULT NULL COMMENT '创立人类别',
  `representative` varchar(32) COLLATE utf8mb4_bin DEFAULT NULL COMMENT '代表人',
  `principal` varchar(32) COLLATE utf8mb4_bin DEFAULT NULL COMMENT '校长',
  `classify` varchar(32) COLLATE utf8mb4_bin DEFAULT NULL COMMENT '归类',
  `tech_start_time` varchar(32) COLLATE utf8mb4_bin DEFAULT NULL COMMENT '日语教育开始时间',
  `cognizance_time` varchar(48) COLLATE utf8mb4_bin DEFAULT NULL COMMENT '认定期间',
  `teacher_count` varchar(32) COLLATE utf8mb4_bin DEFAULT NULL COMMENT '教员人数',
  `count` varchar(32) COLLATE utf8mb4_bin DEFAULT NULL COMMENT '名额',
  `dormitory` varchar(255) COLLATE utf8mb4_bin DEFAULT NULL COMMENT '学生宿舍',
  `gre` varchar(255) COLLATE utf8mb4_bin DEFAULT NULL COMMENT '入学资格',
  `enter_method` varchar(255) COLLATE utf8mb4_bin DEFAULT NULL COMMENT '入学考核方法',
  `now_count` varchar(255) COLLATE utf8mb4_bin DEFAULT NULL COMMENT '在学人数',
  PRIMARY KEY (`id`)
) ENGINE=InnoDB DEFAULT CHARSET=utf8mb4 COLLATE=utf8mb4_bin;

-- ----------------------------
-- Table structure for rb_student_count
-- ----------------------------
DROP TABLE IF EXISTS `rb_student_count`;
CREATE TABLE `rb_student_count` (
  `id` int(11) NOT NULL AUTO_INCREMENT COMMENT 'id',
  `school_id` int(11) NOT NULL COMMENT '学校id',
  `country_name` varchar(255) COLLATE utf8mb4_bin DEFAULT NULL COMMENT '国家名称',
  `count` int(11) DEFAULT NULL COMMENT '人数',
  PRIMARY KEY (`id`)
) ENGINE=InnoDB AUTO_INCREMENT=12007 DEFAULT CHARSET=utf8mb4 COLLATE=utf8mb4_bin;

-- ----------------------------
-- Table structure for rb_tese
-- ----------------------------
DROP TABLE IF EXISTS `rb_tese`;
CREATE TABLE `rb_tese` (
  `id` int(11) NOT NULL AUTO_INCREMENT COMMENT '主键id',
  `school_id` int(4) DEFAULT NULL COMMENT '学校id',
  `description` varchar(255) COLLATE utf8mb4_bin DEFAULT NULL COMMENT '特色',
  PRIMARY KEY (`id`)
) ENGINE=InnoDB AUTO_INCREMENT=1198 DEFAULT CHARSET=utf8mb4 COLLATE=utf8mb4_bin COMMENT='教育特色表';

SET FOREIGN_KEY_CHECKS = 1;
