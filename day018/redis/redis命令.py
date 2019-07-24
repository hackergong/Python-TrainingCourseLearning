'''
port 6379
使用黑屏终端 执行 在redis安装目录下执行，redis-server.exe redis.windows.conf
再次启动一个终端redis-cli.exe
认证密码 auth 'tracy'

redis是键值对的集合
set name tracy  设置一个数据

redis-desktop-manager-08.8.384可视化工具
'''
'''
一，String
    概述：String是redis最基本的类型，最大能存储512MB的数据，String类型是二进制安全的，即可以存储任何数据，比如数字，图片，序列化对象等。
    1，设置
        a，设置键值
            set key value
            set a "tracy is a good man"
        b，设置键值及过期时间，以秒为单位
            setex key seconds value
            setex c 10 good
        c，设置多个键值
            mset key value [key value ...]
            mset c good
    2，获取
        a，根据键获取值，如果键不存在则返回None(null,0,nil)
            get key
        b，根据多个键获取多个值
            mget key [key ...]
            mget a
    3，运算
        要求：值是字符串类型的数字
        a，将key对应的值加1
            incr key
        b，将key对应的值减1
            decr key
        c，将key对应的值加整数
            incrby key intnum
        d，将key对应的值减整数
            decrby key intnum
    4，其它
        a，追加值
            append key value
        b，获取值长度
            strlen key


二，key
    1，查找键，参数支持正则
        keys pattern
        key *
    2，判断键是否存在，如果存在返回1，不存在返回0
        exists key
    3，查看键对应的value类型
        type key
    4，删除键及对应的值
        del key [key ,key...]
    5，设置过期时间以秒为单位
        expire key seconds
    6，查看有效时间，以秒为单位
        ttl key

三，hash
    概述：hash用于存储对象
        {
            name:"tom"
            age:18
        }
    1，设置
        a，设置单个值
            hset key field value
        b，设置多个值
            hmest key field value [field value ....]
    2，获取
        a，获取一个属性的值
            hget key field
        b，获取多个属性的值
            hmget key field [field,...]
        c，获取所有属性和值
            hgetall key
        d，获取所有属性
            hkeys key
        e，获取所有值
            hvals key
        f，返回包含属性的个数
            hlen key

    3，其他
        a，判断属性是否存在,存在返回1，不存在返回0
            hexists key field
        b，删除属性及值
            hdel key field [field...]
        c，返回值的字符串长度
            hstrlen key field

四，list
    概述：列表的元素类型为string，按照插入的顺序排序，在列表的头部或尾部添加元素
    1，设置
        a，在头部插入
            lpush key value [value...]
        b，在尾部插入
            rpush key value [value...]
        c，在一个元素的前|后插入新元素
            linsert key before|after pivot value
            linsert s1 agter 3 4
        d，设置指定索引的元素值
            lset key index value
            注意：index从0开始
            注意：索引值可以是负数，表示偏移量是从list的尾部开始，如-1表示最后一个元素
    2，获取
        a，移除并返回key对于的list的第一个元素
            lpop key
        b，移除并返回key对应的list的最后一个元素
            rpop key
        c，返回存储在key的列表中的指定范围的元素
            lrange key start end
            lrange s1 0 -1  整个列表
            注意：start end都是从0开始
            注意：偏移量可以是负数

    3，其他
        a，裁剪列表，改为原集合的子集
            ltrim key start end
            注意：start end都是从0开始
            注意：偏移量可以是负数
        b，返回存储在key里的list的长度
            llen key
        c，返回列表中索引对于的值
            lindex key index

五，set
    概述：无序集合，元素类型为string类型，元素具有唯一性，不重复
    1，设置
        a，添加元素
            sadd key member [member...]
    2，获取
        a，返回key集合中所有元素
            smembers key
        b，返回集合元素个数
            scard key

    3，其他
        a，求多个集合的交集
            sinter key [key...]
        b，求多个集合的差集
            sdiff key [key...]
        c，求多个集合的合集
            sunion key [key...]
        d，判断元素是否在集合中
            sismember key member
            member存在返回1，不存在返回0

六，zset
    概述：
    a，有序集合，元素类型为String，元素具有唯一性，不能重复。
    b，每个元素都会关联一个double类型的score(表示权重),通过权重的大小排序，元素的score可以相同

    1，设置
        a，添加
            zadd key score member [score member...]
            zadd z1 1 a 2 b
    2，获取
        a，返回指定范围内的元素
            zrange key start end
            zrange key 0 -1
        b，返回元素个数
            zcard z1
        c，返回有序集合key中，score在min和max之间的元素
            zcount key min max
            zcount z1 2 4
        d，返回有序集合key中，成员member的score值
            zscore key member
            zscore z1 c





























'''












