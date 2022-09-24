import org.apache.spark.sql.SparkSession
object NarrowANDWide {

  def main(args:Array[String]):Unit={

    val spark = SparkSession.builder().master("local[*]").appName("narrow&wide").getOrCreate()
    var data_path="Z:\\SparkProgrammingInScala-master\\01-HelloSpark\\src\\test\\scala\\us_500.csv"
    //val data=spark.read.option("header",true).csv(data_path)
    val data =spark.read.csv(data_path)
    val data1=spark.read.option("header",true).csv(data_path)

    data.show(5)
    data1.show(5)
    val a=data1.filter("state=='LA'") ///this is narrow transformation
    a.show(5)
    a.rdd.getNumPartitions

    val b=data1.select("state").distinct()//this is wide transformation

    b.count()
    b.show()
    b.rdd.getNumPartitions
    


  }

}
