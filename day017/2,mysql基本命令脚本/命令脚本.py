'''
命令脚本
'''
'''
一，基本命令
1，启动服务：
    说明：以管理员身份运行cmd
    格式：net start <服务名称>
    示例：net start mysql80
2，停止服务
    说明：以管理员身份运行cmd
    格式：net stop <服务名称>
    示例：net stop mysql80
3，连接数据
    格式：mysql -u 用户名 -p
    示例：mysql -u root -p
    输入密码(安装时设置的密码 tracy)
4，退出登录（断开连接）
    quit或exit
5，查看版本(连接后可以执行)
    示例：select version();
    我现在的版本是8.0.16
6，显示当前时间(连接后执行)
    示例：select now();
7，远程连接
    格式：mysql -h ip地址 -u 用户名 -p
    输入对方密码
    1130 是拒绝远程连接

二，数据库操作
1，创建数据库
    格式：create database <数据库名> charset=utf8;
    示例：create database tracy charset=utf8;
2，删除数据库
    格式：drop database <数据库名>;
    示例：drop database tracy;
3，切换数据库
    格式：use <数据库名>;
    示例：use tracy；
4，查看当前选择的数据库；(先切换到数据库上)
    格式：select database();
    示例：select database();

三，表操作
1，查看当前数据中所有表
    格式：show tables;
2，创建表
    格式：create table 表名(列及类型)
    示例：create table student(id int auto_increment primary key，name varchar(20) not null,age int not null,gengder bit default 1,address varchar(20),isDelete bit default 0);
    说明：  auto_increment表明自增长
            primary key 主键
            not null 不为空
3，删除表
    格式：drop table 表名;
    示例：drop table student;
4，查看表结构
    格式：desc 表名；
    示例：desc student；
5，查看建表语句
    格式：show create table 表名;
    示例：show create table car;
6，重命名表
   格式：rename table 原表名 to 新表名;
   示例：rename table car to newcar;
7，修改表结构
    格式：alter table 表名 add|change|drop 列名  类型;
    示例：alter table newcar add isDelete bit default 0
四，数据操作
1，增
    a,全列插入
        格式：insert into 表名 value(...)
        说明：主键列是自动增长，但是在全列插入时需要占位，通常使用0，插入成功以后以实际数据为准。
        示例：insert into student value(0,"tom",19,1," ",0);

    b,缺省插入
        格式：insert into 表名(列1，列2,...) values(值1,值2,...);
        示例：insert into student(name,age,address) values("BMW",8,"上海");
    c,同时插入多条数据
        格式：insert into 表名 values(...),(...),...
        示例：insert into 表名 values(0,"BMW",19,"南京",0),(0,"chevrolet",9,"天津",0),(0,"linkco",4,"广州",0);
2，删
    格式：delete from 表名 where 条件;
    示例：delete from car where id=2;
    注意：没有条件是全部删除，慎用。git 远程仓库
3，改
    格式：update 表名 set 列1=值1，列2=值2，...where 条件;
    示例：update student set age=16 where id=7;
    注意：没有条件全部列都修改，慎用
4，查
    说明：查询表中的全部数据
    格式：select * from 表名;
    示例：select * from student;


五，查(重要)
    1，基本语法
        格式：select * from 表名
        说明：
            a，from关键字后面是表名，表示数据来源于这张表
            b，selelct后边写表中的列名，如果是*表示在结果集中显示表中的所有列。
            c，在select后面的列名部分，可以使用as为列名起别名，这个别名显示在结果集中。
            d，如果要查询多个列，之间使用逗号分隔。
            select * from car;
            select name,age from car;
    2，消除重复行
        在select后面列前面使用distinct可以消除重复的行
        示例：
            select gender from student;
            select distinct gender from student;

    3，条件查询
        a，语法
            select * from 表名 where 条件
        b，比较运算符
            等于：=
            大于：>
            小于: <
            大于等于: >=
            小于等于: <=
            不等于: !=或<>
            需求：查询id值大于8的所有数据
            示例：select * from car where id>8;
        c，逻辑运算符
            and     并且
            or      或者
            not     非
            需求：查询id值大于7的女同学
            示例：select * from car where id>7 and gender=0;
        d，模糊查询
            like %  表示任意多个任意字符
            _  表示一个任意字符
            需求：查询姓习的同学
            示例：select * from student where name like 'tian%';
            系列
            insert into car values(0,"BMW_7系",35,"天津",0),(0,"BMW_X6",21,"南京",0);
        e，范围查询
            in               表示在一个非连续的范围内
            between...and... 表示在一个连续的范围内

            需求：查询标号为8,10,12的学生
            示例：select * from student where id in(8,10,12);
            需求：查询编号为6到8的学生
            示例：select * from car where id between 6 and 8;

        f，空判断
            注意：null与""是不同
            判断空：is null
            判断非空：is not null

            需求：查询没有地址的同学
            示例：select * from student where address is null;
        g，优先级
            小括号，not 比较运算符，逻辑运算符
            and 比 or 优先级高，入股偶同事出现并希望先选or，需要结合            ()来使用。

    4，聚合
        为了快速得到统计数据，提供了五个聚合函数
        a,count(*)   表示计算总行数，括号中可以写*和列名
        b,max(列)    表示求此列的最大值
        c,min(列)    表示求此列的最小值
        d,sum(列）   表示求此列的和
        e,avg(列)    表示求此列的平均值

        需求：查询学生总数
        示例：select count(*) from student;
        需求：查询女生的编号最大值
        示例：select max(id) from student where gender=0;
        需求：查询女生编号的最小值
        示例：select min(id) from student where gender=0;
        需求：查询所有学生的年龄和
        示例：select sum(age) from student;
        需求：求所有学生的年龄平均值
        示例：select avg(age) from student;

    5，分组
        按照字段分组，表示此字段相同的数据会被放到一个集合
        分组后，只能查询出相同的数据列，对于有差异的数据列无法显示在结果集中。
        可以对分组后的数据进行统计，做集合运算
        语法：select 列1，列2，聚合... from 表名 group by 列1，列2，列3，.
         需求：查询男女生总数
         示例：select gender from student group by gender;

         分组后的数据筛选：select 列1，列2，聚合... from 表名 group by gender having  gender;
         示例：select gender，count(*) from student group be gender having gender
         where与having的区别：
         where 是对 from 后面指定的表进行筛选。属于对原始数据的筛选
         having是对group by的结果进行筛选。


    6，排序
        语法：select * from 表名 order by 列1 asc|desc,列2, asc|desc,..
        说明：
            a,将数据按照列1进行排序，如果某些列1的值相同，则按照列2进行排序
            b,默认按照从小到大的顺序排序
            c,asc升序
            d,desc降序

            需求：将没有被删除的数据按年龄排序
            示例：select * from student where isDelete=0 order by age;

    7，分页
        语法：select * from 表名 limit start,count;
        说明：start索引从0开始
        示例：select * from student limit 0,3;
                select * from student where gender=1 limit 0,3;

六，关联
    一对多：class table：id(主键)，name
            student table：id(主键)，name，classid(外键)
    建表语句：
    1，create table class(id int auto_increment primary key,name varchar(20) not null,stuNum int not null);
    2,create table students(id int auto)increment primary key,name varchar(20) not null,gender bit default 1,classid int not null,foreign key(calssid) references class(id);

    插入一些数据：
    insert into class values(0,"python01",55),(0,"python02",50),(0,"python03",45),(0,"python04",60);
    insert into students values(0,"tom",1,1);
    insert into students values(0,"lilei",1,10),
    insert into students values(0,"kobe",1,2),(0,"tracy",1,1)

    select students.name,class.name from class right join students on class.id=students.classid;

    分类：
    1，表A inner join 表B
    表示表A与表B匹配的行会出现在结果集中。
    2，表A left join 表B
    表A与表B匹配度行会出现在结果集中，外加表A中独有的数据，未对应的数据使用null填充
    3，表A right join 表B
    表A与表B匹配度行会出现在结果集中，外加表A中独有的数据，未对应的数据使用null填充

'''