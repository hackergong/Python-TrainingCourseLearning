'''
管理员模式下 mongod.exe  --dbpath=D:\mongoDB\data\db

命令指示符  mongo.exe

'''

'''
一，操作mongodb数据库
    1，创建数据库
        语法：use 数据库名
        说明：如果数据库不存在，则创建数据库，否则切换到指定的数据库
        注意：如果刚刚创建的数据库不在列表内，如果要显示它，我们需要向刚刚的创建的数据库中插入一些数据
        (db.student.insert({name:"tom",age:18,gender:1,address:"北京",isDelete:0}))
    2，删除数据库
        前提：使用当前数据库(use  数据库名）
        db.dropDatabase()
    3，查看所有数据库
        语法：show dbs
    4，查看当前正在使用的数据库
        a，db
        b，db.getName()
    5，断开连接
        exit
    6，查看命令api
        help

二，集合操作
    1，查看当前数据库下有哪些集合
        show collections
    2，创建集合
        a，
            语法：db.createCollection("集合名")
            示例：db.createCollection("class")
        b，
            语法：db.集合名.insert(document)
            示例：db.student.insert({name:"tom",age:18,gender:1,address:"北京",isDelete:0})
        区别：前者创建的是一个空的集合，后者创建一个空的集合并添加一个文档。

    3，删除当前数据库中的集合
        语法：db.集合.drop()
        示例：db.class.drop()


三，文档操作
    1，插入文档
        a，使用insert()方法插入文档
            语法：db.集合名.insert(document)
            插入一个：db.student.insert({name:"maymay",age:21,gender:0,address:"losangel",isDelete:0})
            语法：db.集合名.insert([document,document1,document2,document3])
            插入多个：db.student.insert([{name:"meimei",age:16,gender:0,address:"南京",isDelete:0},{name:"liuliu",age:17,gender:0,address:"天津",isDelete:0}])
        b，使用save()方法插入文档
            语法：db.集合名.save(文档)
            说明：如果不指定_id字段，save()方法类似于insert()方法。如果指定_id字段，则会更新_id字段的数据。
            示例1：db.student.save({name:"poi",age:12,gender:0,address:"广东",isDelete:0})
            #说明：前面加上_id可以更新_id的数据
            示例2：db.student.save({_id:ObjectId("5d36e7ee7057a018ec84e40f"),name:"poi",age:14,gender:0,address:"广东",isDelete:0})

    2，文档更新
        a，update()方法用于更新已存在的文档
        语法：
            db.集合名.update(
                <query>,
                <update>
                {
                    upset:<boolean>,
                    multi:<boolean>,
                    writeConcern:<document>
                }
                )
        参数说明：
            query:update的查询条件，类似于sql里update语句内where后面的内容
            update:update的对象和一些更新的操作符($set,$inc)等，$set直接更新，
            $inc在原有的基础上累加后更新。
            upset：可选，如果不存在update的记录，是否当新数据插入，true为插入，False为不插入。默认为False，
            multi：可选，mongodb默认是false，只更新找到的第一条记录，如果这个参数为true，就按照条件查找出来的数据全部更新
            writeConcern：可选，抛出异常的级别
        需求：将lilei的年龄更新为25
        db.student.update({name:"lilie"},{$set:{age:15}})  修改
        db.student.update({name:"lilie"},{$inc:{age:15}})  累加
        db.student.update({name:"poi"},{$set:{age:41}})
        db.student.update({name:"poi"},{$set:{age:21}},{multi:true}) 全改
                <query>,
                <update>
                {
                    upset:<boolean>,
                    multi:<boolean>,
                    writeConcern:<document>
                }
        b，save()方法通过传入的文档替换已有文档
            语法：
                db.集合名.save(
                    document,
                    {
                        writeConcern:<document>
                    }
                )
            参数说明
                document:文档数据
                writeConcern:可选，抛出异常的级别

    3，文档删除
        说明：在执行remove()函数前，先执行find()命令来判断执行的条件是否存在是一个良好习惯

        语法：
            db.集合名.remove(
                query,
                {
                    justOne:<boolean>
                    writeConcern:<document>
                }
            )
        参数说明：
            query：可选，删除的文档的条件
            justOne：可选，如果为true或1，则只删除一个文档
            writeConcern:可选，抛出异常的级别
        示例：test库
            db.student.remove({name:"tom"})
            db.student.remove({name:"poi"},{justOne:true})

    4，文档查询
        a，find()方法
            查询集合下，所有的文档(数据)
            语法：db.集合名.find()

        b，find()方法查询指定列
            语法：db.集合名.find(
                query,
                {
                    <key>:1,
                    <key>:1

                }
            )
            参数说明：
                query：查询条件
                key：要显示的字段，1表示显示

            示例：db.student.find({gender:1},{name:1,age:1})
                db.student.find({gender:0},{name:1,age:1})  #看所有性别为女的人年龄和名字不限

        c，pretty()方法以格式化的方式来显示文档
            示例：db.student.find().pretty()

        d，findOne()方法来查询匹配结果的第一条数据
            示例：db.student.findOne({gender:0})

    5，查询条件操作符
        作用：条件操作符用于比较两个表达式并从Mongodb集合中获取数据
        a，大于---$gt
            语法：db.集合名.find({<key>:{$gt:<value>}})
            示例：db.student.find({age:{$gt:20}})
        b，大于等于-$gte
            语法：db.集合名.find({<key>:{$gte:<value>}})
        c，小于-$lt
            语法：db.集合名.find({<key>:{$lt:<value>}})
        d，大于等于-$lte
            语法：db.集合名.find({<key>:{$lte:<value>}})
        e，大于等于 和  小于等于 ---$get  和  $lte
            语法：db.集合名.find({<key>:{$gte:<value>,$lte:<value>}})
        f，等于  -  :
            语法：db.集合名.find({<key>:<value>})
        g，使用_id进行查询
            语法：db.集合名.find({"_id":ObjectId("id值")})
            示例：db.student.find({"_id":ObjectId("5d36de827057a018ec84e40b")})
        h，查询某个结果集的数据条数
            db.student.find().count()
        i，查询某个字段的值当中是否包含另一个值
            语法：
            示例：db.student.find({name:/lili/})
        j，查询某个字段的值是否以另一个值开头
            db.student.find({name:/^li/})

    6，条件查询 and 和 or
        a，AND条件
            语法：db.集合名.find({条件1，条件2，....，条件n>})
            示例：db.student.find({gender:0,age:{$gt:16}})
        b，OR条件
            语法：
                db.集合名.find(
                    {
                        $or:[{条件1}，{条件2}，....{条件n}]
                    }
                )
            示例：db.student.find({$or:[{age:17},{age:{$gte:20}}]})

        c，AND和OR联合使用
            语法：db.集合名.find(
                        {
                            条件1，
                            条件2，
                            $or:[{条件1},{条件2}]
                        }
                    )

    7，limit,skip
    db.student.insert([{name:"hacker",age:12,gender:1,address:"dongbei",isDelete:0},{name:"ali",age:20,gender:0,address:"zhejiang",isDelete:0},{name:"tencent",age:26,gender:1,address:"shenzhen",isDelete:0}])
        a，limit():读取指定数量的数据记录
            示例：db.student.find().limit(3)
        b，skip():跳过指定数量的数据
            示例：db.student.find().skip(3)
        c，skip与limit联合使用
            通常用这种方式来实现分页功能
            分页越过前面的前五条，从服务器中越过五条再拿数据
            示例：db.student.find().skip(3).limit(3)

    8，排序
        语法：db.集合名.find().sort({<key>:1|-1})
        需求：对年龄排序
        示例：db.student.find9).sort({age:1})
        注意：1表示升序，-1表示降序

'''
