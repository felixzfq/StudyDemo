
SET NAMES utf8mb4;
SET FOREIGN_KEY_CHECKS = 0;

-- ----------------------------
-- Table structure for t_gc
-- ----------------------------
DROP TABLE IF EXISTS `t_gc`;
CREATE TABLE `t_gc`  (
  `id` int(10) UNSIGNED NOT NULL AUTO_INCREMENT,
  `name` varchar(20) CHARACTER SET utf8 COLLATE utf8_general_ci NOT NULL,
  `type_id` int(10) UNSIGNED NOT NULL,
  `create_time` timestamp(0) NOT NULL DEFAULT CURRENT_TIMESTAMP(0),
  `update_time` timestamp(0) NOT NULL DEFAULT CURRENT_TIMESTAMP(0),
  `reserve` varchar(100) CHARACTER SET latin1 COLLATE latin1_swedish_ci NULL DEFAULT NULL,
  PRIMARY KEY (`id`) USING BTREE,
  UNIQUE INDEX `name`(`name`) USING BTREE
) ENGINE = InnoDB AUTO_INCREMENT = 109 CHARACTER SET = latin1 COLLATE = latin1_swedish_ci ROW_FORMAT = Compact;

-- ----------------------------
-- Records of t_gc
-- ----------------------------
INSERT INTO `t_gc` VALUES (22, '塑料瓶', 1, '2019-06-29 20:16:09', '2019-06-29 20:16:09', NULL);
INSERT INTO `t_gc` VALUES (23, '食品罐头', 1, '2019-06-29 20:16:10', '2019-06-29 20:16:10', NULL);
INSERT INTO `t_gc` VALUES (24, '玻璃瓶', 1, '2019-06-29 20:16:10', '2019-06-29 20:16:10', NULL);
INSERT INTO `t_gc` VALUES (25, '易拉罐', 1, '2019-06-29 20:16:11', '2019-06-29 20:16:11', NULL);
INSERT INTO `t_gc` VALUES (26, '报纸', 1, '2019-06-29 20:16:11', '2019-06-29 20:16:11', NULL);
INSERT INTO `t_gc` VALUES (27, '旧书包', 1, '2019-06-29 20:16:12', '2019-06-29 20:16:12', NULL);
INSERT INTO `t_gc` VALUES (28, '旧手提包', 1, '2019-06-29 20:16:12', '2019-06-29 20:16:12', NULL);
INSERT INTO `t_gc` VALUES (29, '旧鞋子', 1, '2019-06-29 20:16:12', '2019-06-29 20:16:12', NULL);
INSERT INTO `t_gc` VALUES (30, '牛奶盒', 1, '2019-06-29 20:16:13', '2019-06-29 20:16:13', NULL);
INSERT INTO `t_gc` VALUES (31, '旧塑料篮子', 1, '2019-06-29 20:16:13', '2019-06-29 20:16:13', NULL);
INSERT INTO `t_gc` VALUES (32, '旧玩偶', 1, '2019-06-29 20:16:14', '2019-06-29 20:16:14', NULL);
INSERT INTO `t_gc` VALUES (33, '玻璃壶', 1, '2019-06-29 20:16:14', '2019-06-29 20:16:14', NULL);
INSERT INTO `t_gc` VALUES (34, '旧铁锅', 1, '2019-06-29 20:16:15', '2019-06-29 20:16:15', NULL);
INSERT INTO `t_gc` VALUES (35, '垃圾桶', 1, '2019-06-29 20:16:15', '2019-06-29 20:16:15', NULL);
INSERT INTO `t_gc` VALUES (36, '塑料梳子', 1, '2019-06-29 20:16:16', '2019-06-29 20:16:16', NULL);
INSERT INTO `t_gc` VALUES (37, '旧帽子', 1, '2019-06-29 20:16:16', '2019-06-29 20:16:16', NULL);
INSERT INTO `t_gc` VALUES (38, '旧夹子', 1, '2019-06-29 20:16:17', '2019-06-29 20:16:17', NULL);
INSERT INTO `t_gc` VALUES (39, '废锁头', 1, '2019-06-29 20:16:17', '2019-06-29 20:16:17', NULL);
INSERT INTO `t_gc` VALUES (40, '篮球', 1, '2019-06-29 20:16:18', '2019-06-29 20:16:18', NULL);
INSERT INTO `t_gc` VALUES (41, '旧纸袋', 1, '2019-06-29 20:16:18', '2019-06-29 20:16:18', NULL);
INSERT INTO `t_gc` VALUES (42, '纸盒', 1, '2019-06-29 20:16:19', '2019-06-29 20:16:19', NULL);
INSERT INTO `t_gc` VALUES (43, '旧玩具', 1, '2019-06-29 20:16:19', '2019-06-29 20:16:19', NULL);
INSERT INTO `t_gc` VALUES (44, '木制梳子', 1, '2019-06-29 20:16:20', '2019-06-29 20:16:20', NULL);
INSERT INTO `t_gc` VALUES (45, '香水瓶', 1, '2019-06-29 20:16:20', '2019-06-29 20:16:20', NULL);
INSERT INTO `t_gc` VALUES (46, '煤气罐', 1, '2019-06-29 20:16:21', '2019-06-29 20:16:21', NULL);
INSERT INTO `t_gc` VALUES (47, '油漆桶', 2, '2019-06-29 20:22:17', '2019-06-29 20:22:17', NULL);
INSERT INTO `t_gc` VALUES (48, '电池', 2, '2019-06-29 20:22:17', '2019-06-29 20:22:17', NULL);
INSERT INTO `t_gc` VALUES (49, '油漆', 2, '2019-06-29 20:22:18', '2019-06-29 20:22:18', NULL);
INSERT INTO `t_gc` VALUES (50, '过期的胶囊药物', 2, '2019-06-29 20:22:18', '2019-06-29 20:22:18', NULL);
INSERT INTO `t_gc` VALUES (51, '含汞温度计', 2, '2019-06-29 20:22:19', '2019-06-29 20:22:19', NULL);
INSERT INTO `t_gc` VALUES (52, '过期药片', 2, '2019-06-29 20:22:19', '2019-06-29 20:22:19', NULL);
INSERT INTO `t_gc` VALUES (53, '荧光灯', 2, '2019-06-29 20:22:20', '2019-06-29 20:22:20', NULL);
INSERT INTO `t_gc` VALUES (54, '蓄电池', 2, '2019-06-29 20:22:20', '2019-06-29 20:22:20', NULL);
INSERT INTO `t_gc` VALUES (55, '杀虫剂', 2, '2019-06-29 20:22:21', '2019-06-29 20:22:21', NULL);
INSERT INTO `t_gc` VALUES (56, '菜叶', 3, '2019-06-29 20:22:27', '2019-06-29 20:22:27', NULL);
INSERT INTO `t_gc` VALUES (57, '橙皮', 3, '2019-06-29 20:22:28', '2019-06-29 20:22:28', NULL);
INSERT INTO `t_gc` VALUES (58, '葱', 3, '2019-06-29 20:22:28', '2019-06-29 20:22:28', NULL);
INSERT INTO `t_gc` VALUES (59, '饼干', 3, '2019-06-29 20:22:29', '2019-06-29 20:22:29', NULL);
INSERT INTO `t_gc` VALUES (60, '番茄酱', 3, '2019-06-29 20:22:29', '2019-06-29 20:22:29', NULL);
INSERT INTO `t_gc` VALUES (61, '蛋壳', 3, '2019-06-29 20:22:30', '2019-06-29 20:22:30', NULL);
INSERT INTO `t_gc` VALUES (62, '西瓜皮', 3, '2019-06-29 20:22:30', '2019-06-29 20:22:30', NULL);
INSERT INTO `t_gc` VALUES (63, '马铃薯', 3, '2019-06-29 20:22:31', '2019-06-29 20:22:31', NULL);
INSERT INTO `t_gc` VALUES (64, '鱼骨', 3, '2019-06-29 20:22:31', '2019-06-29 20:22:31', NULL);
INSERT INTO `t_gc` VALUES (65, '甘蔗', 3, '2019-06-29 20:22:32', '2019-06-29 20:22:32', NULL);
INSERT INTO `t_gc` VALUES (66, '玉米', 3, '2019-06-29 20:22:33', '2019-06-29 20:22:33', NULL);
INSERT INTO `t_gc` VALUES (67, '骨头（鸡鸭鹅）', 3, '2019-06-29 20:22:33', '2019-06-29 20:22:33', NULL);
INSERT INTO `t_gc` VALUES (68, '虾壳', 3, '2019-06-29 20:22:33', '2019-06-29 20:22:33', NULL);
INSERT INTO `t_gc` VALUES (69, '蛋糕', 3, '2019-06-29 20:22:34', '2019-06-29 20:22:34', NULL);
INSERT INTO `t_gc` VALUES (70, '面包', 3, '2019-06-29 20:22:34', '2019-06-29 20:22:34', NULL);
INSERT INTO `t_gc` VALUES (71, '草莓', 3, '2019-06-29 20:22:35', '2019-06-29 20:22:35', NULL);
INSERT INTO `t_gc` VALUES (72, '西红柿', 3, '2019-06-29 20:22:35', '2019-06-29 20:22:35', NULL);
INSERT INTO `t_gc` VALUES (73, '梨', 3, '2019-06-29 20:22:36', '2019-06-29 20:22:36', NULL);
INSERT INTO `t_gc` VALUES (74, '蟹壳', 3, '2019-06-29 20:22:37', '2019-06-29 20:22:37', NULL);
INSERT INTO `t_gc` VALUES (75, '香蕉皮', 3, '2019-06-29 20:22:37', '2019-06-29 20:22:37', NULL);
INSERT INTO `t_gc` VALUES (76, '辣椒', 3, '2019-06-29 20:22:38', '2019-06-29 20:22:38', NULL);
INSERT INTO `t_gc` VALUES (77, '巧克力', 3, '2019-06-29 20:22:38', '2019-06-29 20:22:38', NULL);
INSERT INTO `t_gc` VALUES (78, '茄子', 3, '2019-06-29 20:22:39', '2019-06-29 20:22:39', NULL);
INSERT INTO `t_gc` VALUES (79, '豌豆皮', 3, '2019-06-29 20:22:39', '2019-06-29 20:22:39', NULL);
INSERT INTO `t_gc` VALUES (80, '苹果', 3, '2019-06-29 20:22:40', '2019-06-29 20:22:40', NULL);
INSERT INTO `t_gc` VALUES (81, '盆栽树叶', 3, '2019-06-29 20:22:40', '2019-06-29 20:22:40', NULL);
INSERT INTO `t_gc` VALUES (82, '花生壳', 3, '2019-06-29 20:22:41', '2019-06-29 20:22:41', NULL);
INSERT INTO `t_gc` VALUES (83, '贝壳', 4, '2019-06-29 20:22:46', '2019-06-29 20:22:46', NULL);
INSERT INTO `t_gc` VALUES (84, '化妆棉', 4, '2019-06-29 20:22:47', '2019-06-29 20:22:47', NULL);
INSERT INTO `t_gc` VALUES (85, '海绵', 4, '2019-06-29 20:22:47', '2019-06-29 20:22:47', NULL);
INSERT INTO `t_gc` VALUES (86, '发胶', 4, '2019-06-29 20:22:48', '2019-06-29 20:22:48', NULL);
INSERT INTO `t_gc` VALUES (87, '卫生纸', 4, '2019-06-29 20:22:48', '2019-06-29 20:22:48', NULL);
INSERT INTO `t_gc` VALUES (88, '旧镜子', 4, '2019-06-29 20:22:49', '2019-06-29 20:22:49', NULL);
INSERT INTO `t_gc` VALUES (89, '桃核', 4, '2019-06-29 20:22:49', '2019-06-29 20:22:49', NULL);
INSERT INTO `t_gc` VALUES (90, '陶瓷碗', 4, '2019-06-29 20:22:50', '2019-06-29 20:22:50', NULL);
INSERT INTO `t_gc` VALUES (91, '一次性筷子', 4, '2019-06-29 20:22:50', '2019-06-29 20:22:50', NULL);
INSERT INTO `t_gc` VALUES (92, '西梅核', 4, '2019-06-29 20:22:51', '2019-06-29 20:22:51', NULL);
INSERT INTO `t_gc` VALUES (93, '坏的花盆', 4, '2019-06-29 20:22:51', '2019-06-29 20:22:51', NULL);
INSERT INTO `t_gc` VALUES (94, '脏污衣服', 4, '2019-06-29 20:22:52', '2019-06-29 20:22:52', NULL);
INSERT INTO `t_gc` VALUES (95, '烟蒂湿垃圾袋', 4, '2019-06-29 20:22:52', '2019-06-29 20:22:52', NULL);
INSERT INTO `t_gc` VALUES (96, '扫把', 4, '2019-06-29 20:22:53', '2019-06-29 20:22:53', NULL);
INSERT INTO `t_gc` VALUES (97, '牙刷', 4, '2019-06-29 20:22:53', '2019-06-29 20:22:53', NULL);
INSERT INTO `t_gc` VALUES (98, '过期化妆品', 4, '2019-06-29 20:22:54', '2019-06-29 20:22:54', NULL);
INSERT INTO `t_gc` VALUES (99, '牙膏皮', 4, '2019-06-29 20:22:54', '2019-06-29 20:22:54', NULL);
INSERT INTO `t_gc` VALUES (100, '水彩笔', 4, '2019-06-29 20:22:55', '2019-06-29 20:22:55', NULL);
INSERT INTO `t_gc` VALUES (101, '调色板', 4, '2019-06-29 20:22:55', '2019-06-29 20:22:55', NULL);
INSERT INTO `t_gc` VALUES (102, '打火机', 4, '2019-06-29 20:22:56', '2019-06-29 20:22:56', NULL);
INSERT INTO `t_gc` VALUES (103, '荧光棒', 4, '2019-06-29 20:22:56', '2019-06-29 20:22:56', NULL);
INSERT INTO `t_gc` VALUES (104, '医用手套', 4, '2019-06-29 20:22:57', '2019-06-29 20:22:57', NULL);
INSERT INTO `t_gc` VALUES (105, '医用纱布', 4, '2019-06-29 20:22:57', '2019-06-29 20:22:57', NULL);
INSERT INTO `t_gc` VALUES (106, '医用棉签', 4, '2019-06-29 20:22:58', '2019-06-29 20:22:58', NULL);
INSERT INTO `t_gc` VALUES (107, '创口贴', 4, '2019-06-29 20:22:58', '2019-06-29 20:22:58', NULL);
INSERT INTO `t_gc` VALUES (108, '注射器', 4, '2019-06-29 20:22:59', '2019-06-29 20:22:59', NULL);

-- ----------------------------
-- Table structure for t_put
-- ----------------------------
DROP TABLE IF EXISTS `t_put`;
CREATE TABLE `t_put`  (
  `id` int(10) UNSIGNED NOT NULL AUTO_INCREMENT,
  `guidance` varchar(50) CHARACTER SET utf8 COLLATE utf8_general_ci NOT NULL,
  `type_id` int(11) NOT NULL,
  PRIMARY KEY (`id`) USING BTREE
) ENGINE = InnoDB AUTO_INCREMENT = 13 CHARACTER SET = latin1 COLLATE = latin1_swedish_ci ROW_FORMAT = Compact;

-- ----------------------------
-- Records of t_put
-- ----------------------------
INSERT INTO `t_put` VALUES (1, '轻投轻放', 1);
INSERT INTO `t_put` VALUES (2, '清洁干燥，避免污染', 1);
INSERT INTO `t_put` VALUES (3, '废纸尽量平整', 1);
INSERT INTO `t_put` VALUES (4, '立体包装物请清空内容物，清洁后压扁投放', 1);
INSERT INTO `t_put` VALUES (5, '有尖锐边角的，应包裹后投放', 1);
INSERT INTO `t_put` VALUES (6, '投放时请注意轻投', 2);
INSERT INTO `t_put` VALUES (7, '易破损的请连带包装或包裹后轻放', 2);
INSERT INTO `t_put` VALUES (8, '如易挥发，请密封后投放', 2);
INSERT INTO `t_put` VALUES (9, '纯流质的食物垃圾，如牛奶等，应直接倒进下水口', 3);
INSERT INTO `t_put` VALUES (10, '有包装物的湿垃圾应将包装物去除后分类投放，包装物请投到对应的可回收物或干垃圾容器', 3);
INSERT INTO `t_put` VALUES (11, '尽量沥青水分', 4);
INSERT INTO `t_put` VALUES (12, '难以辨识类别的生活垃圾投入干垃圾容器内', 4);

-- ----------------------------
-- Table structure for t_type
-- ----------------------------
DROP TABLE IF EXISTS `t_type`;
CREATE TABLE `t_type`  (
  `id` int(10) UNSIGNED NOT NULL AUTO_INCREMENT,
  `type` varchar(20) CHARACTER SET utf8 COLLATE utf8_general_ci NOT NULL,
  `description` varchar(200) CHARACTER SET utf8 COLLATE utf8_general_ci NOT NULL,
  PRIMARY KEY (`id`) USING BTREE,
  UNIQUE INDEX `type`(`type`) USING BTREE
) ENGINE = InnoDB AUTO_INCREMENT = 5 CHARACTER SET = utf8 COLLATE = utf8_general_ci ROW_FORMAT = Compact;

-- ----------------------------
-- Records of t_type
-- ----------------------------
INSERT INTO `t_type` VALUES (1, '可回收物', '废纸张、废塑料、废玻璃制品、废金属、废织物等适宜回收，可循环利用的生活废弃物');
INSERT INTO `t_type` VALUES (2, '有害垃圾', '废电池、废灯管、废药品、废油漆及其容器等对人体健康或自然环境造成直接或者潜在危害的生活废弃物');
INSERT INTO `t_type` VALUES (3, '湿垃圾', '即易腐垃圾，是指食材废料、剩菜剩饭、过期食品、瓜皮果核、花卉绿植、中药药渣等生物质生活废弃物');
INSERT INTO `t_type` VALUES (4, '干垃圾', '即其它垃圾，是指可回收垃圾、有害垃圾、湿垃圾以外的其它生活废弃物');

SET FOREIGN_KEY_CHECKS = 1;
